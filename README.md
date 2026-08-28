# SmartMoneyAPI — machine-readable API contract

This repository is **one thing**: a generated, machine-readable contract for the
SmartMoneyAPI public data surface, kept in sync with the live API by a script in
this repo rather than by hand.

- **[`openapi.yaml`](openapi.yaml)** — OpenAPI 3.0.3, 207 operations. Point
  `openapi-generator`, Postman, an LLM agent, or your IDE at it.
- **[`api-reference.md`](api-reference.md)** — the same contract as prose, one
  section per endpoint, with parameters, response fields and a runnable `curl`.
- **[`examples/`](examples/)** — bash, Python and Node. Every field they read was
  observed on a real response, not illustrated.
- **[`tools/build_public_spec.py`](tools/build_public_spec.py)** — the generator.

## Why this repo exists

If you are wiring a bot, an agent, or a data pipeline to this API, you should not
have to scrape a docs page or trust a hand-typed field list. You want a file a
machine can read, that says exactly which endpoints exist, which need a key,
which tier unlocks each one, and what comes back.

The hand-maintained version of that file rotted. It carried 8 endpoints against
the live API's 263 paths, and it documented `/v1/alerts/conditions/{id}` — a
route that had been renamed and answered 404. So this repo no longer contains
anything written by hand. `openapi.yaml` and `api-reference.md` are both emitted
by `tools/build_public_spec.py`, and the script is committed here so anyone can
see the selection rule and re-run it.

## Last generated

| | |
|---|---|
| Generated | **2026-08-28** |
| Source | the live document the API serves at <https://smartmoneyapi.com/openapi.json> |
| Live spec | 263 paths |
| Published here | **207 paths / 207 operations** (149 keyless) |
| Response shapes measured against the running API | 131 operations |

## What is published, and what is not

An operation from the live document appears here **iff all three hold**:

1. **The method is `GET`.** This mirror is a read-only *data* contract. Nothing
   that mutates state — creating alert rules, registering webhooks, minting
   WebSocket tickets, posting analytics events — is published, so a client
   generated from this file cannot change anything in an account. One stated
   exception: the `/rpc/v1/*` JSON-RPC proxies are `POST` because JSON-RPC is a
   POST protocol, not because they change anything of ours.
2. **It carries `x-auth` and `x-tier`.** Upstream, those are derived from the
   gateway's own public-endpoint set and from the pricing manifest, not typed by
   hand — so the gating printed on each operation here is the gating the server
   actually enforces. An operation missing them is not published, because its
   access contract is unknown.
3. **Its namespace is not account-management or internal.** The withheld set —
   alerts, whale-alerts, webhooks, referrals, portfolio, preferences, watchlist,
   usage, telegram, assistant, purchases, socket tickets, contact/booking intake,
   internal research gates — is listed in the generator **with a reason for each
   entry**. Those routes exist and are documented for signed-in users at
   <https://smartmoneyapi.com/docs>; they are left out here because no
   integration calls them and publishing them only widens the surface people
   probe.

**Paid tiers are published.** You should be able to read the exact shape of what
a subscription returns before paying for it. `x-auth` on each operation says
whether a key is needed at all; `x-tier` names the plan that unlocks it.

## Where the response shapes come from — and their limits

The live document declares an empty `200` schema for most operations. Rather
than hand-write field lists (exactly the thing that rots), the generator **calls
every keyless, parameterless operation and records the field names and JSON
types it actually returned**. Those operations carry:

```yaml
x-response-measured: "2026-08-28"
x-response-note: "Field names and types below were recorded from one real
  response on 2026-08-28, not written by hand. A field absent from that response
  is absent here even if the endpoint can return it, and optional fields are not
  marked required. Treat this as a floor, not a closed set."
```

Only names and types are recorded — no values are copied out of any response.

**What is *not* measured, and is therefore weaker:** the 76 operations that need
a key or a required parameter carry whatever the live document declares, which
for some of them is nothing. Where you see an operation with no response fields
listed, that is an honest gap, not an empty response.

## Quickstart

Three of these need no key at all.

```bash
# How far back the deep archive goes. Keyless.
curl -s "https://api.smartmoneyapi.com/v1/history/coverage" | jq '.tables | keys'

# Executed forced liquidations bucketed by price x time. Keyless.
curl -s "https://api.smartmoneyapi.com/v1/liquidations/heatmap?symbol=BTC" | jq '{symbol, window_minutes, price_buckets}'

# Confirm a trade idea. Needs a key; the Free tier covers BTC, ETH and SOL.
curl -s -H "X-API-Key: sm_xxxxxxxxxxxx" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=BTC&direction=long" \
  | jq '{action, confidence, composite, size_mult}'
```

`/v1/confirm` returns an `action` your bot can branch on: `CONFIRM_FULL`,
`CONFIRM_REDUCED` and `CONFIRM_MINIMAL` mean take it at `size_mult` size;
`VETO_SKIP` means stand aside; **`NO_DATA_SKIP` means nothing was measured for
that symbol** — an explicit absence of coverage, not a weak or neutral read.
`composite` runs −1.0 → +1.0 and is a confluence read, **not** a win-rate.

## The deep archive is public and keyless

`/v1/history/<table>` federates the live database and the consolidated cold
archive into one newest-first response. Measured against
`/v1/history/coverage` on 2026-08-28: **115,706,185 rows across 9 tables**
(still accruing — re-read the endpoint for the current figure)
(`whale_positions`, `confirmations`, `signal_log`, `derivatives_agg`,
`whale_consensus`, `derivatives`, `onchain`, `signal_outcomes`,
`wallet_relationships`), oldest row **2026-03-18**. `sources` in every response
names each shard the answer came from, and `truncated` tells you whether you hit
the row cap.

A filter the archive cannot serve from an index is **rejected with `400` naming
the filters it can serve**, rather than dropped — a dropped filter would answer
a wider question than you asked and look like a valid result.

## Authentication

Send `X-API-Key: <key>` on every request. Never put a key in a URL. Create one at
<https://smartmoneyapi.com/dashboard>. Operations marked keyless answer without a
key at a reduced row cap and a per-IP throttle.

`429` is a quota or throttle rejection. `403` means your tier does not include
that operation or symbol.

## Regenerating this repo

```bash
pip install pyyaml
# rebuild from the live spec, measuring response shapes as it goes
python3 tools/build_public_spec.py --measure https://api.smartmoneyapi.com

# CI gate: rebuild in memory, exit non-zero if the committed files have drifted
python3 tools/build_public_spec.py --check --measure https://api.smartmoneyapi.com
```

`--check` compares against a fresh rebuild and exits non-zero if anything
structural has drifted — a route that appeared, vanished, or was renamed. Dates
are ignored, so it fires on real drift only. Run it in CI, so drift is caught
there instead of by a customer whose generated client 404s.

## Links

- Site: <https://smartmoneyapi.com>
- Interactive docs: <https://smartmoneyapi.com/docs>
- Live performance: <https://smartmoneyapi.com/performance>
- Pricing: <https://smartmoneyapi.com/pricing>
- Python SDK: <https://github.com/tashiardit/smartmoneyapi-python>

> Not financial advice. Crypto trading involves substantial risk, including loss
> of capital. Scores are a multi-factor confluence read; past signal accuracy
> does not guarantee future results.

## License

MIT — see [LICENSE](LICENSE).

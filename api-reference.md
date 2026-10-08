# SmartMoneyAPI — API reference

**Generated file — do not hand-edit.** Produced by `tools/build_public_spec.py` from the live OpenAPI document at <https://smartmoneyapi.com/openapi.json>, on 2026-10-08. It documents 249 of the 306 paths the live API routes; the selection rule is stated in [openapi.yaml](openapi.yaml) and implemented in [tools/build_public_spec.py](tools/build_public_spec.py).

Base URL: `https://api.smartmoneyapi.com`

Auth: send `X-API-Key: <key>` on every request. Operations marked **keyless** answer without one, at a reduced row cap and a per-IP throttle. Never put a key in a URL.

Errors: `429` is a quota or throttle rejection; `403` means your tier does not include that operation or symbol. Errors a browser can reach are returned as `503`, never `502`/`504`.

> Not financial advice. Scores are a multi-factor confluence read, not a guaranteed win-rate. Past signal accuracy does not guarantee future results.

## Contents

- [Account](#account) — 1 endpoint
- [COT](#cot) — 5 endpoints
- [Copy-trading](#copy-trading) — 9 endpoints
- [DEX](#dex) — 4 endpoints
- [DeFiLlama](#defillama) — 11 endpoints
- [Derivatives](#derivatives) — 11 endpoints
- [ETF](#etf) — 2 endpoints
- [Equities](#equities) — 24 endpoints
- [Historical](#historical) — 4 endpoints
- [History](#history) — 10 endpoints
- [Insiders](#insiders) — 1 endpoint
- [Integrations](#integrations) — 1 endpoint
- [Intelligence](#intelligence) — 6 endpoints
- [JSON-RPC](#json-rpc) — 6 endpoints
- [L2 order-book depth](#l2-order-book-depth) — 2 endpoints
- [L2 trade tape](#l2-trade-tape) — 2 endpoints
- [Liquidations](#liquidations) — 10 endpoints
- [Live chain](#live-chain) — 5 endpoints
- [Market](#market) — 11 endpoints
- [Meta](#meta) — 9 endpoints
- [News](#news) — 8 endpoints
- [Node](#node) — 13 endpoints
- [On-chain](#on-chain) — 10 endpoints
- [Options](#options) — 8 endpoints
- [Performance](#performance) — 3 endpoints
- [Reference](#reference) — 4 endpoints
- [Research](#research) — 4 endpoints
- [Screener](#screener) — 7 endpoints
- [Seasonality](#seasonality) — 6 endpoints
- [Signals](#signals) — 9 endpoints
- [Smart-money cohorts](#smart-money-cohorts) — 7 endpoints
- [Strategies](#strategies) — 6 endpoints
- [Technicals](#technicals) — 3 endpoints
- [Top traders](#top-traders) — 4 endpoints
- [Trading tools](#trading-tools) — 3 endpoints
- [Volume](#volume) — 5 endpoints
- [Whales](#whales) — 15 endpoints

## Account

### `GET /v1/symbols/available`

**Symbols available to you** — key required — Pro (15,000 calls/day)

The symbols the caller's tier may query (free tier is BTC/ETH/SOL).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/symbols/available"
```

## COT

### `GET /v1/cot/comparison`

**COT comparison** — keyless

COT positioning compared across the tracked contracts.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/comparison"
```

### `GET /v1/cot/history`

**COT history** — keyless

Historical COT positioning series.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `weeks` | query | no | Weeks of history. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/history"
```

### `GET /v1/cot/positioning`

**COT positioning** — keyless

CFTC Commitments of Traders categories for BTC, ETH, XAU or XAG with percentiles computed only from reports published by as_of. Disclosed positioning of a legally defined category, published Friday for the prior Tuesday. Source: CFTC Commitments of Traders. Public.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Market. One of: `BTC`, `ETH`, `XAU`, `XAG`. Default `BTC`. |
| `lookback_weeks` | query | no | Percentile window. One of: `52`, `156`. Default `156`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `availability_rule` | string |  |
| `available_ts` | integer |  |
| `basis` | string |  |
| `categories` | array |  |
| `caveats` | array |  |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `data_mode_counts` | object |  |
| `dataset_id` | string |  |
| `expected_obs` | integer |  |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `licence_class` | string |  |
| `lookback_weeks` | integer |  |
| `market` | object |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `methods` | object |  |
| `metric` | string |  |
| `n_obs` | integer |  |
| `note` | string |  |
| `released_ts` | integer |  |
| `report_as_of` | object |  |
| `report_date` | string |  |
| `report_family` | string |  |
| `report_name` | string |  |
| `rights` | object |  |
| `rows_excluded` | object |  |
| `scope` | string |  |
| `source` | string |  |
| `symbol` | string |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `validation` | object |  |
| `venue` | string |  |
| `versions` | object |  |
| `window` | object |  |
| `window_complete` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/positioning"
```

### `GET /v1/cot/summary`

**COT summary** — keyless

CFTC Commitments of Traders positioning summary.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/summary"
```

### `GET /v1/cot/trend`

**COT trend** — keyless

Trend in COT net positioning.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/trend"
```

## Copy-trading

### `GET /v1/copy-engine/history`

**Our copy-trading engine (experimental): order history (executed orders)** — key required — Pro (15,000 calls/day)

Executed orders of our own copy-trading accounts, newest first. pnl_status is known, unknown (realized_pnl is null: no stored exit) or not_applicable (opens and adds). Failed orders in the same window are not listed; failed_count counts them.

| Parameter | In | Required | Description |
|---|---|---|---|
| `wallet` | query | no | Source wallet address, exact match. |
| `symbol` | query | no | Base symbol, e.g. BTC. |
| `days` | query | no | Look-back window in days. Default `30`. |
| `limit` | query | no | Max rows returned. Default `100`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-engine/history"
```

### `GET /v1/copy-engine/leaderboard`

**Our copy-trading engine (experimental): source wallets, by our executed PnL** — key required — Pro (15,000 calls/day)

Source wallets our own copy-trading accounts copied, ranked by the realized PnL of OUR executed copies (closing orders with a stored exit price only; up to 50 rows). Not the source wallets' own record, not a ranking of skilled traders and not a signal. Failed orders enter no figure and are counted in failed_count; executed closing orders without a stored exit are counted in pnl_unknown. Every response carries scope "our copy-trading engine (experimental): executed orders of our own copy-trading accounts, not the source wallets' own trading record".

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-engine/leaderboard"
```

### `GET /v1/copy-engine/performance`

**Our copy-trading engine (experimental): daily PnL (executed orders)** — key required — Pro (15,000 calls/day)

One row per UTC calendar day in the last `days` days, today included, on which our own copy-trading accounts placed any order: PnL and trade counts from executed orders only, with executed_count, failed_count and pnl_unknown per day.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Calendar days back, today included. Default `30`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-engine/performance"
```

### `GET /v1/copy-engine/summary`

**Our copy-trading engine (experimental): totals (executed orders)** — key required — Pro (15,000 calls/day)

Totals over our own copy-trading accounts' executed orders: total_trades, wins, losses, win_rate and total_pnl over closing orders with a known PnL (before fees), plus executed_count, failed_count, pnl_unknown and last_executed_at. These are OUR engine's results, not any trader's.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-engine/summary"
```

### `GET /v1/copy-trading/overview`

**Copy-trading overview** — key required — Pro (15,000 calls/day)

Aggregate stats for the latest whale-position snapshot: active wallets, total positions, realized PnL, win rate.

Response fields:

| Field | Type | Description |
|---|---|---|
| `active_wallets` | integer |  |
| `performance` | object |  |
| `snapshot_ts` | integer |  |
| `total_positions` | integer |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-trading/overview"
```

### `GET /v1/copy-trading/performance`

**Copy-trading per-symbol performance** — key required — Pro (15,000 calls/day)

Per-symbol aggregate PnL across all tracked whale wallets in the latest snapshot.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-trading/performance"
```

### `GET /v1/copy-trading/positions`

**Whale positions** — key required — Pro (15,000 calls/day)

All whale positions in the latest snapshot, ordered by USD value.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max positions, capped at 1000. Default `200`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `positions` | array |  |
| `snapshot_ts` | integer |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-trading/positions"
```

### `GET /v1/copy-trading/shadow`

**Shadow book** — key required — Pro (15,000 calls/day)

The shadow (paper) copy-trading book. Published together with the measured verdict that the v3 overlay showed no durable out-of-sample edge and is not shipped as a product.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-trading/shadow"
```

### `GET /v1/copy-trading/wallets`

**Tracked whale wallets** — key required — Pro (15,000 calls/day)

Distinct whale wallets in the latest snapshot with position counts, total value and PnL.

Response fields:

| Field | Type | Description |
|---|---|---|
| `snapshot_ts` | integer |  |
| `wallets` | array |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/copy-trading/wallets"
```

## DEX

### `GET /v1/dex/pair`

**Pair details** — key required — withheld

Details for a single DEX pair.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | yes | Chain slug (e.g. ethereum, bsc). |
| `address` | query | yes | Pair contract address. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/dex/pair"
```

### `GET /v1/dex/search`

**Search DEX pairs** — key required — withheld

Search DexScreener pairs by name/symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `q` | query | yes | Search query. |
| `limit` | query | no | Max pairs. Default `20`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/dex/search"
```

### `GET /v1/dex/token`

**Token pairs** — key required — withheld

All DEX pairs for a token address.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | query | yes | Token contract address. |
| `limit` | query | no | Max pairs. Default `10`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/dex/token"
```

### `GET /v1/dex/trending`

**Trending DEX pairs** — key required — withheld

Trending pairs from DexScreener.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max pairs. Default `20`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/dex/trending"
```

## DeFiLlama

### `GET /v1/defillama/all`

**All DeFiLlama data** — key required — withheld

Every DeFiLlama dataset in one payload. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/all"
```

### `GET /v1/defillama/borrow-rates`

**Borrow rates** — key required — withheld

Lending-market borrow rates. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/borrow-rates"
```

### `GET /v1/defillama/bridges`

**Bridge volumes** — key required — withheld

Cross-chain bridge volume. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/bridges"
```

### `GET /v1/defillama/derivatives`

**Perp DEX volumes** — key required — withheld

Perpetual DEX volume rankings. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/derivatives"
```

### `GET /v1/defillama/fees`

**Protocol fees** — key required — withheld

Protocol fee and revenue rankings. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/fees"
```

### `GET /v1/defillama/hacks`

**Hacks** — key required — withheld

Logged protocol exploits and amounts lost. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/hacks"
```

### `GET /v1/defillama/momentum`

**Price momentum** — key required — withheld

Cross-token price momentum. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/momentum"
```

### `GET /v1/defillama/raises`

**Fundraises** — key required — withheld

Recent protocol fundraises. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/raises"
```

### `GET /v1/defillama/stablecoin-chains`

**Stablecoins by chain** — key required — withheld

Stablecoin supply broken down by chain. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/stablecoin-chains"
```

### `GET /v1/defillama/treasuries`

**Protocol treasuries** — key required — withheld

Protocol treasury holdings. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/treasuries"
```

### `GET /v1/defillama/unlocks`

**Token unlocks** — key required — withheld

Upcoming token unlock schedule. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/unlocks"
```

## Derivatives

### `GET /v1/coverage`

**Derivatives field coverage matrix** — keyless

How completely each tracked field (funding, open interest, long/short ratio, ...) is populated per venue over a lookback window, plus one symbol's per-venue/per-field detail when `?symbol=` is given. `venues_registry_only` names venues the instrument registry knows about but that never actually wrote a row in the window -- a registry entry is not evidence of collection. `listing_source` and `declaration` carry the metadata this matrix reasons from (what we believe is listed, and on what evidence) alongside `declaration_conflicts`, so a coverage gap can be told apart from a symbol that was never listed anywhere. `window_seconds` is clamped to [3600, 604800] (1h-7d); an out-of-range or unparsable value falls back to the clamped/default value rather than erroring. `?symbol=` other than alphanumeric/`_`/`-` is a 400 `bad_symbol`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `window_seconds` | query | no | Lookback window in seconds, clamped to [3600, 604800]. Default `86400`. |
| `symbol` | query | no | Restrict to one symbol's per-venue/per-field detail instead of the full matrix. Alphanumeric plus '_'/'-', max 24 chars. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `declaration` | object |  |
| `declaration_conflicts` | array |  |
| `fields` | array |  |
| `generated_at` | integer |  |
| `listing_source` | object |  |
| `not_claimed` | array |  |
| `per_field` | object | Per tracked field: distribution, buckets, per_venue counts, symbols_with_at_least_one_venue. Empty when status != ok. |
| `source_table` | string |  |
| `status` | string |  |
| `status_buckets` | object |  |
| `status_labels` | object |  |
| `symbol` | string |  |
| `symbols_observed` | integer |  |
| `venues` | object | Present only with ?symbol=: per-venue, per-field cell detail for that one symbol. |
| `venues_collected` | array |  |
| `venues_in_instrument_registry` | array |  |
| `venues_registry_only` | array |  |
| `window` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/coverage"
```

### `GET /v1/derivatives/detail`

**Derivatives detail** — key required — Pro (15,000 calls/day)

Full per-exchange derivatives detail for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/derivatives/detail"
```

### `GET /v1/derivatives/funding-arb`

**Funding arbitrage table** — keyless

Cross-exchange funding spreads ranked by annualised carry.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/funding-arb"
```

### `GET /v1/derivatives/funding-heatmap`

**Funding heatmap** — keyless

Funding-rate heatmap across exchanges. Anonymous callers get the first 10 heatmap rows.

Response fields:

| Field | Type | Description |
|---|---|---|
| `heatmap` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/funding-heatmap"
```

### `GET /v1/derivatives/heatmap`

**Derivatives heatmap** — key required — Trader (3,000 calls/day)

Funding heatmap (authenticated alias of /v1/derivatives/funding-heatmap).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/derivatives/heatmap"
```

### `GET /v1/derivatives/oi-rankings`

**Open-interest rankings** — keyless

Open-interest change rankings. Anonymous callers get a fixed 24h/top-10 view; authenticated callers can choose timeframe/limit.

| Parameter | In | Required | Description |
|---|---|---|---|
| `timeframe` | query | no | Ranking window (authenticated only). Default `24h`. |
| `limit` | query | no | Max rows, capped at 50 (authenticated only). Default `20`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/oi-rankings"
```

### `GET /v1/derivatives/provenance`

**Derivatives data provenance** — keyless

Which rows in the derivatives table were WATCHED live versus REPLAYED after the fact from a venue's own historical funding/price endpoint. Full scan of the derivatives_backfill table (~11s), served through a 30-minute cache. `backfilled` covers only the handful of symbols that were ever backfilled, NOT the whole tracked universe -- read `backfilled.instruments`/`backfilled.symbols`, never a symbol count multiplied by a venue count. Six of nine venues publish no historical open-interest endpoint, so an empty `rows_with_open_interest` for them is a venue limitation, not a gap in collection. If the shard has no derivatives_backfill table at all, `status` is `no_backfill_table` and every row in `derivatives` for this shard is observed (nothing was replayed).

Response fields:

| Field | Type | Description |
|---|---|---|
| `backfilled` | object |  |
| `not_claimed` | array |  |
| `observed` | object | Per-venue earliest/latest ts and row count for the live (non-backfilled) derivatives table in THIS shard -- the daemon rotates the database, so earliest_ts_in_this_shard is a floor on collection start, not when collection began. |
| `provenance_values_present` | array |  |
| `read_this_view` | string |  |
| `status` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/provenance"
```

### `GET /v1/derivatives/screener`

**Derivatives screener** — keyless

Cross-exchange derivatives screener (500+ symbols): funding, open interest, long/short ratio, signals. Anonymous callers get a fixed top-10 by OI (response carries public:true, limited:true); authenticated callers can sort/filter up to 200 rows.

BY-NAME LOOKUP REQUIRES A KEY. `?symbol=` (alias `?asset=`) is answered only for authenticated callers, and only for the symbols the caller's tier grants: the free tier's by-name list is published on every public operation as `x-free-tier-symbols`, and paid tiers cover every symbol. A keyless request that names a symbol gets 403 naming the free key as the fix; a keyed request naming a symbol outside the tier gets 403 with the included list. Keyless callers keep the top-10 preview by simply omitting `?symbol=` -- the preview is a RANKING, so a symbol you are entitled to may still be absent from it on any given day, which is why by-name exists.

An entitled symbol with no snapshot recorded yet returns an empty `symbols` array plus a `note`: that is absent data, not zero and not an exclusion.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Look one symbol up by name. Requires an API key; restricted to the tier's symbol list. Alias: asset. |
| `sort` | query | no | Sort field (authenticated only). Default `oi_usd`. |
| `dir` | query | no | Sort direction (authenticated only). One of: `asc`, `desc`. Default `desc`. |
| `limit` | query | no | Max rows, capped at 200 (authenticated only). Default `50`. |
| `min_oi` | query | no | Minimum open interest in USD (authenticated only). Default `0`. |
| `crowding` | query | no | Filter by crowding state (authenticated only). Legacy alias: signal. One of: `crowded_long`, `crowded_short`, `neutral`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/screener"
```

### `GET /v1/funding/clock`

**Measured funding-settlement clock** — keyless

Per-venue summary of the MEASURED funding-settlement interval, derived from each venue's own settlement timestamps (never from documentation): the newest gap, extended backwards while consecutive gaps agree. A median over full history is deliberately NOT used -- a venue that changed its clock mid-history (observed: Binance moved COTIUSDT from hourly to 4-hourly settlement) makes the median wrong for however long the new clock has been running. `venues_measured` only lists venues with a usable measurement; `venues_unmeasured` lists the rest, so a venue can never silently vanish from the coverage claim. `refuses_measurements_older_than_days` names the staleness bound past which a per-instrument measurement is refused rather than trusted.

Response fields:

| Field | Type | Description |
|---|---|---|
| `basis` | string |  |
| `how_measured` | string |  |
| `metadata_disagreements` | array |  |
| `not_claimed` | array |  |
| `refuses_measurements_older_than_days` | integer |  |
| `status` | string |  |
| `totals` | object |  |
| `venues` | object | Keyed by venue; each entry is the venue's raw coverage record plus measurement_age_days (derived from the measurement's own timestamp, so a stale sweep is visible in the payload). |
| `venues_measured` | array |  |
| `venues_unmeasured` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/funding/clock"
```

### `GET /v1/funding/normalised`

**Cross-venue funding on one clock** — keyless

One underlying's live funding rate on every venue we hold a rate for, put on a single annualised basis using each venue's MEASURED settlement clock (see /v1/funding/clock) instead of assuming every venue settles 8-hourly. Every venue that has a stored rate for this symbol lands in exactly one of three buckets so none can silently disappear from the average: `venues_contributing` (used in the mean), `venues_refused` (had a rate but the clock refused it, with a reason per venue), and `venues_unmapped` (no funding stored, or no single measured linear perpetual resolves for this base in the venue registry). `comparison` recomputes the same contributing rates assuming every venue is 8-hourly, so the size of the correction is checkable from the response alone (measured median across underlyings: 5.47 annualised percentage points). A symbol with no derivatives row in the last 2 hours returns `status: no_rows` rather than an empty average. `?symbol=` other than alphanumeric/`_`/`-` is a 400 `bad_symbol`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Alphanumeric plus '_'/'-', max 24 chars. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `base` | string |  |
| `basis` | string |  |
| `comparison` | object |  |
| `mean_annualised_pct` | number |  |
| `mean_rate_8h_equivalent` | number |  |
| `not_claimed` | array |  |
| `observed_ts` | integer |  |
| `per_venue` | object |  |
| `status` | string |  |
| `symbol` | string |  |
| `venues_contributing` | array |  |
| `venues_refused` | object |  |
| `venues_unmapped` | object |  |
| `venues_with_a_stored_rate` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/funding/normalised"
```

### `GET /v1/snapshot`

**Market snapshot** — key required — Trader (3,000 calls/day)

Full aggregated derivatives snapshot for a symbol (proxied to the aggregation daemon).

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/snapshot"
```

## ETF

### `GET /v1/etf/flows`

**ETF flows** — key required — withheld

Spot BTC/ETH ETF daily flows with per-fund breakdown (SoSoValue).

| Parameter | In | Required | Description |
|---|---|---|---|
| `asset` | query | no | ETF asset. One of: `BTC`, `ETH`. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/etf/flows"
```

### `GET /v1/etf/history`

**ETF flow history** — key required — withheld

Historical spot-ETF flow series.

| Parameter | In | Required | Description |
|---|---|---|---|
| `asset` | query | no | ETF asset. One of: `BTC`, `ETH`. Default `BTC`. |
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/etf/history"
```

## Equities

### `GET /v1/equity-flow`

**Equity flow stats** — keyless

Coverage and freshness of the free equity options-flow dataset.

Response fields:

| Field | Type | Description |
|---|---|---|
| `cycle_tickers_cap` | integer |  |
| `enabled` | boolean |  |
| `executor_workers` | integer |  |
| `expiries_per_ticker` | integer |  |
| `gex_snapshots` | integer |  |
| `last_gex_ts` | integer |  |
| `last_unusual_ts` | integer |  |
| `scan_interval_s` | integer |  |
| `tickers_with_unusual` | integer |  |
| `tracked_tickers` | integer |  |
| `unusual_options_rows` | integer |  |
| `yfinance_available` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/equity-flow"
```

### `GET /v1/equity-flow/dark-pool`

**Dark-pool prints** — key required — withheld

Off-exchange (dark-pool) prints for the tracked tickers.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/equity-flow/dark-pool"
```

### `GET /v1/equity-flow/gex`

**Equity gamma exposure** — key required — withheld

Dealer gamma exposure by strike for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | yes | Ticker symbol. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/equity-flow/gex"
```

### `GET /v1/equity-flow/stats`

**Equity flow stats** — keyless

Alias of /v1/equity-flow.

Response fields:

| Field | Type | Description |
|---|---|---|
| `cycle_tickers_cap` | integer |  |
| `enabled` | boolean |  |
| `executor_workers` | integer |  |
| `expiries_per_ticker` | integer |  |
| `gex_snapshots` | integer |  |
| `last_gex_ts` | integer |  |
| `last_unusual_ts` | integer |  |
| `scan_interval_s` | integer |  |
| `tickers_with_unusual` | integer |  |
| `tracked_tickers` | integer |  |
| `unusual_options_rows` | integer |  |
| `yfinance_available` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/equity-flow/stats"
```

### `GET /v1/equity-flow/unusual-activity`

**Unusual options activity** — key required — withheld

Unusual equity options prints ranked by a size/open-interest score.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `contract_type` | query | no | Contract type. One of: `call`, `put`. |
| `min_score` | query | no | Minimum unusualness score. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/equity-flow/unusual-activity"
```

### `GET /v1/flow/dark-pool`

**Dark-pool flow (paid feed)** — key required — Pro (15,000 calls/day)

Dark-pool prints from the paid Unusual Whales feed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/flow/dark-pool"
```

### `GET /v1/flow/gex`

**GEX (paid feed)** — key required — Pro (15,000 calls/day)

Gamma exposure from the paid Unusual Whales feed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Ticker symbol. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/flow/gex"
```

### `GET /v1/flow/status`

**Paid flow status** — keyless

Availability of the paid Unusual Whales flow feed.

Response fields:

| Field | Type | Description |
|---|---|---|
| `enabled` | boolean |  |
| `last_check` | — |  |
| `reason` | string |  |
| `source` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/flow/status"
```

### `GET /v1/flow/unusual`

**Unusual flow (paid feed)** — key required — Pro (15,000 calls/day)

Unusual options flow from the paid Unusual Whales feed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/flow/unusual"
```

### `GET /v1/stocks`

**Stock universe** — keyless

The tracked equity and tokenized-equity universe.

Response fields:

| Field | Type | Description |
|---|---|---|
| `meta` | object |  |
| `universe` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks"
```

### `GET /v1/stocks/activist-alerts`

**Activist alerts** — keyless

Recent activist (13D) filings.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `alerts` | array |  |
| `attribution` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/activist-alerts"
```

### `GET /v1/stocks/congress/{ticker}`

**Congressional trades** — key required — withheld

Disclosed congressional trades in one ticker, as filed, with the disclosure (PTR) link. Free public information, provided for public information and not investment advice: served to everyone with no key and the same rows on every plan. Coverage today is House of Representatives filings only: the feed holds no Senate filings and makes no claim about them. US law restricts commercial use of these reports (5 U.S.C. §13107(c)), so congress data is never an input to any score, ranking, signal or alert and is not part of any paid product. Every 200 carries `free: true`, a `source_note` and `source_links` to the official sources (the House Clerk PTR search and, for the Senate filings this feed does not hold, the Senate eFD). At most 200 rows are returned (`row_cap`) to every caller, newest first, and `truncated` says whether more rows matched. Published as disclosure data, not as a signal — the long-horizon study found no tradable edge.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/stocks/congress/{ticker}"
```

### `GET /v1/stocks/insider-clusters`

**Insider clusters** — keyless

Tickers with clustered insider buying or selling.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `attribution` | string |  |
| `clusters` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/insider-clusters"
```

### `GET /v1/stocks/insiders/{ticker}`

**Insider trades** — keyless

SEC Form 4 insider transactions for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |
| `days` | query | no | Look-back window in days. |
| `code` | query | no | Form 4 transaction code filter. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/insiders/{ticker}"
```

### `GET /v1/stocks/institutions/{ticker}`

**Institutional holders** — key required — withheld

Institutional holders and position changes for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/stocks/institutions/{ticker}"
```

### `GET /v1/stocks/new-listings`

**New listings** — keyless

Recently listed tokenized equities.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `new_listings` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/new-listings"
```

### `GET /v1/stocks/rankings`

**Equity rankings** — keyless

Tickers ranked by the tracked ownership and insider factors.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `rankings` | array |  |
| `withheld` | array |  |
| `withheld_sources` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/rankings"
```

### `GET /v1/stocks/short-interest/{ticker}`

**Short interest** — key required — withheld

Reported short interest for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/stocks/short-interest/{ticker}"
```

### `GET /v1/stocks/stats`

**Stock tracker stats** — keyless

Coverage and freshness of the equity tracker.

Response fields:

| Field | Type | Description |
|---|---|---|
| `analysed_count` | integer |  |
| `base_universe_size` | integer |  |
| `enabled` | boolean |  |
| `last_analysis_ts` | integer |  |
| `new_listings_7d` | integer |  |
| `tokenized_active_total` | integer |  |
| `tokenized_per_venue` | object |  |
| `universe_count` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/stats"
```

### `GET /v1/stocks/tokenized`

**Tokenized stocks** — keyless

Tokenized equities listed on the tracked venues.

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | no | Filter by venue. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `tokenized` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/tokenized"
```

### `GET /v1/stocks/universe`

**Stock universe** — keyless

Alias of /v1/stocks.

Response fields:

| Field | Type | Description |
|---|---|---|
| `meta` | object |  |
| `universe` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/universe"
```

### `GET /v1/stocks/whale-signals`

**Equity whale signals** — keyless

Cross-ticker aggregation of institutional and insider activity.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `signals` | array |  |
| `withheld` | array |  |
| `withheld_sources` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/whale-signals"
```

### `GET /v1/stocks/whales/{ticker}`

**Equity whales** — keyless

Large 13F/ownership positions in one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/whales/{ticker}"
```

### `GET /v1/stocks/{ticker}`

**Stock detail** — keyless

Detail for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/{ticker}"
```

## Historical

### `GET /v1/historical/funding`

**Funding-rate history** — keyless

Historical funding rates (Binance).

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Perpetual symbol. Default `BTCUSDT`. |
| `days` | query | no | Days of history. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `data` | array |  |
| `days` | integer |  |
| `symbol` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/historical/funding"
```

### `GET /v1/historical/long-short`

**Long/short ratio history** — keyless

Historical long/short account ratio (Binance).

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Perpetual symbol. Default `BTCUSDT`. |
| `days` | query | no | Days of history. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `data` | array |  |
| `days` | integer |  |
| `symbol` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/historical/long-short"
```

### `GET /v1/historical/market`

**Market OHLCV history** — key required — withheld

Historical market data by CoinGecko coin id.

| Parameter | In | Required | Description |
|---|---|---|---|
| `coin` | query | no | CoinGecko coin id. Default `bitcoin`. |
| `days` | query | no | Days of history. Default `30`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/historical/market"
```

### `GET /v1/historical/open-interest`

**Open-interest history** — keyless

Historical open interest (Binance).

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Perpetual symbol. Default `BTCUSDT`. |
| `days` | query | no | Days of history. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `data` | array |  |
| `days` | integer |  |
| `symbol` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/historical/open-interest"
```

## History

### `GET /v1/history/confirmations`

**Deep history: confirmations** — keyless

Federated newest-first read of the confirmations table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: confidence, direction, source, symbol. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `confidence` | query | no | Filter on confidence (exact match). |
| `direction` | query | no | Filter on direction (exact match). |
| `source` | query | no | Filter on source (exact match). |
| `symbol` | query | no | Filter on symbol (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/confirmations"
```

### `GET /v1/history/coverage`

**Deep-history coverage** — keyless

What history exists per table, before you query any of it: the live database range, the consolidated archive range, raw shards not yet consolidated, and which filter keys are index-served. Read this to draw an honest 'data from X to Y' instead of an empty chart. Both index states are reported so a null archive range can be told apart from an unreadable index. Public, keyless; throttled per IP.

Response fields:

| Field | Type | Description |
|---|---|---|
| `index_available` | boolean |  |
| `manifest_present` | boolean |  |
| `partition_cap` | integer |  |
| `query_budget_s` | number |  |
| `shard_index_available` | boolean |  |
| `source_budget_s` | number |  |
| `tables` | object |  |
| `unindexed_partitions` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/coverage"
```

### `GET /v1/history/derivatives`

**Deep history: derivatives** — keyless

Federated newest-first read of the derivatives table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: exchange, symbol. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `exchange` | query | no | Filter on exchange (exact match). |
| `symbol` | query | no | Filter on symbol (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/derivatives"
```

### `GET /v1/history/derivatives_agg`

**Deep history: derivatives_agg** — keyless

Federated newest-first read of the derivatives_agg table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: symbol. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `symbol` | query | no | Filter on symbol (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/derivatives_agg"
```

### `GET /v1/history/onchain`

**Deep history: onchain** — keyless

Federated newest-first read of the onchain table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: asset, metric. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `asset` | query | no | Filter on asset (exact match). |
| `metric` | query | no | Filter on metric (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/onchain"
```

### `GET /v1/history/signal_log`

**Deep history: signal_log** — keyless

Federated newest-first read of the signal_log table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: direction, signal_type, source, symbol. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `direction` | query | no | Filter on direction (exact match). |
| `signal_type` | query | no | Filter on signal_type (exact match). |
| `source` | query | no | Filter on source (exact match). |
| `symbol` | query | no | Filter on symbol (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/signal_log"
```

### `GET /v1/history/signal_outcomes`

**Deep history: signal_outcomes** — keyless

Federated newest-first read of the signal_outcomes table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: horizon. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `horizon` | query | no | Filter on horizon (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/signal_outcomes"
```

### `GET /v1/history/wallet_relationships`

**Deep history: wallet_relationships** — keyless

Federated newest-first read of the wallet_relationships table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: edge_type, wallet_a, wallet_b. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `edge_type` | query | no | Filter on edge_type (exact match). |
| `wallet_a` | query | no | Filter on wallet_a (exact match). |
| `wallet_b` | query | no | Filter on wallet_b (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/wallet_relationships"
```

### `GET /v1/history/whale_consensus`

**Deep history: whale_consensus** — keyless

Federated newest-first read of the whale_consensus table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: symbol. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `symbol` | query | no | Filter on symbol (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/whale_consensus"
```

### `GET /v1/history/whale_positions`

**Deep history: whale_positions** — keyless

Federated newest-first read of the whale_positions table across the live database and the consolidated cold archive, in one response. Public, keyless; throttled per IP. Filters accepted: direction, symbol, wallet. A filter that is neither index-served nor small enough to scan within budget is REJECTED with 400 naming the supported keys — it is never silently dropped, because dropping it would return rows that do not match the query the caller sees echoed back. GET /v1/history/coverage reports the index-served set per table.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | How far back the window starts, in days, when `from` is omitted (1-3650). Default `7`. |
| `from` | query | no | Window start, epoch seconds. Overrides `days`. |
| `to` | query | no | Window end, epoch seconds. Defaults to now. |
| `limit` | query | no | Max rows returned (1-5000). `truncated` says whether the cap was hit. Default `500`. |
| `direction` | query | no | Filter on direction (exact match). |
| `symbol` | query | no | Filter on symbol (exact match). |
| `wallet` | query | no | Filter on wallet (exact match). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | array |  |
| `index_available` | boolean |  |
| `limit` | integer |  |
| `live_starts_at` | integer |  |
| `live_state` | string |  |
| `partition_cap` | integer |  |
| `rows` | array |  |
| `shard_index_available` | boolean |  |
| `sources` | array |  |
| `table` | string |  |
| `took_ms` | number |  |
| `truncated` | boolean |  |
| `window` | object |  |
| `window_grain_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/history/whale_positions"
```

## Insiders

### `GET /v1/insiders/purchases`

**Insider open-market purchases** — key required — Trader (3,000 calls/day)

SEC Form 4 open-market purchases (code P) by officers and directors, classified opportunistic, routine or unclassified (Cohen, Malloy & Pomorski). Descriptive: the academic result has not been validated on our data. One row per filing (accession): its purchase lines summed, min_value applied to that sum. Source: SEC EDGAR. Lives under /v1/insiders, not /v1/stocks.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Lookback days. Default `30`. |
| `min_value` | query | no | Minimum purchase value USD. Default `100000`. |
| `cmp_class` | query | no | Classification filter. One of: `all`, `opportunistic`, `routine`, `unclassified`. Default `all`. |
| `limit` | query | no | Rows. Default `100`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `caveats` | array |  |
| `count` | integer |  |
| `coverage` | object |  |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `data_mode_counts` | object |  |
| `definition` | object |  |
| `filing_lag_days` | object |  |
| `filters` | object |  |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `rights` | object |  |
| `rows` | array |  |
| `scope` | string |  |
| `source` | string |  |
| `total_matching` | integer |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `validation` | object |  |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/insiders/purchases"
```

## Integrations

### `GET /v1/tradingview/setup`

**TradingView setup** — key required — Trader (3,000 calls/day)

The webhook URL and payload template to wire TradingView alerts into this account.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/tradingview/setup"
```

## Intelligence

### `GET /v1/analysis`

**AI market analysis** — key required — Pro (15,000 calls/day)

Latest AI-written market commentary over the aggregated data. Commentary only — it is not a prediction and carries no measured edge. It includes a `recommendation`, so the response carries `operator_position_disclosure` for its symbol, dated when served. `provider` says where it ran: `local` (the operator's own hardware) or `hosted` (a hosted model service); the exact model is named in `ai_backend`. It covers BTC, ETH and SOL only; any other symbol is refused with 400 `symbol_not_covered`, naming what is covered. A covered symbol with no reading yet answers 202 `not_cached` with an `engine` state (as under /v1/analysis/status) and a `message`; readings are generated when requested, and the first request may take up to a few minutes.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/analysis"
```

### `GET /v1/analysis/status`

**AI analysis status** — keyless

Freshness and availability of the AI analysis loop, with the public regime teaser: per symbol, `regime` and `regime_label` (an opinion on the asset, e.g. "Strong bullish trend"). `engine` is `ok`, `stale`, `warming` (just started, or generating now), `on_demand` (healthy and idle: readings are generated when requested, so an empty cache is normal until someone asks) or `unavailable` (a failed or paused run, a loop that is not reporting, or a cache that cannot be read; this route then answers HTTP 503). While no reading is cached, `message` says why. Every row carries `operator_position_disclosure`, dated when the response is served.

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | — |  |
| `cached_count` | integer |  |
| `engine` | string |  |
| `fresh_count` | integer |  |
| `full_analysis` | object |  |
| `message` | string |  |
| `note` | string |  |
| `requested_count` | integer |  |
| `stale_after_seconds` | integer |  |
| `symbols` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/analysis/status"
```

### `GET /v1/flows`

**Aggregate flow** — key required — Pro (15,000 calls/day)

Aggregated smart-money flow across the tracked venues.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/flows"
```

### `GET /v1/regimes/history`

**Regime history** — key required — Pro (15,000 calls/day)

Historical positioning-regime classification per symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/regimes/history"
```

### `GET /v1/sentiment`

**Sentiment snapshot** — key required — Trader (3,000 calls/day)

Aggregate sentiment across news, funding and positioning inputs.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/sentiment"
```

### `GET /v1/smart-money/flow`

**Smart-money flow** — key required — Trader (3,000 calls/day)

Directional whale flow per symbol with venue breakdown.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/flow"
```

## JSON-RPC

### `POST /rpc/v1/avax-c`

**Avalanche C-Chain JSON-RPC** — key required — rpc key (metered separately)

JSON-RPC proxy to the Avalanche C-Chain. rpc_ key required.

```bash
curl -X POST -H "X-API-Key: $SMARTMONEY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' \
  "https://api.smartmoneyapi.com/rpc/v1/avax-c"
```

### `POST /rpc/v1/avax-info`

**Avalanche info JSON-RPC** — key required — rpc key (metered separately)

JSON-RPC proxy to the Avalanche info API. rpc_ key required.

```bash
curl -X POST -H "X-API-Key: $SMARTMONEY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' \
  "https://api.smartmoneyapi.com/rpc/v1/avax-info"
```

### `POST /rpc/v1/avax-p`

**Avalanche P-Chain JSON-RPC** — key required — rpc key (metered separately)

JSON-RPC proxy to the Avalanche P-Chain. rpc_ key required.

```bash
curl -X POST -H "X-API-Key: $SMARTMONEY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' \
  "https://api.smartmoneyapi.com/rpc/v1/avax-p"
```

### `POST /rpc/v1/avax-x`

**Avalanche X-Chain JSON-RPC** — key required — rpc key (metered separately)

JSON-RPC proxy to the Avalanche X-Chain. rpc_ key required.

```bash
curl -X POST -H "X-API-Key: $SMARTMONEY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' \
  "https://api.smartmoneyapi.com/rpc/v1/avax-x"
```

### `POST /rpc/v1/bsc`

**BSC JSON-RPC** — key required — rpc key (metered separately)

JSON-RPC proxy to the self-hosted BSC full node. Authenticated with a dedicated rpc_ key, NOT the main API key, and metered separately from the plans.json call quotas.

```bash
curl -X POST -H "X-API-Key: $SMARTMONEY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' \
  "https://api.smartmoneyapi.com/rpc/v1/bsc"
```

### `GET /rpc/v1/health`

**RPC health** — keyless

Health of the resold BSC/Avalanche JSON-RPC endpoints. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `chains` | object |  |
| `plans` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/rpc/v1/health"
```

## L2 order-book depth

### `GET /v1/l2/depth`

**L2 order-book depth** — keyless

Raw order-book DEPTH updates for one venue over a bounded UTC hour window, read directly from the depth collector's store (never written to). Licence-gated by the SAME allow-list as the trade tape: a venue whose terms forbid redistribution is refused with **HTTP 403** naming the venue and the exact reason from `SOURCE_TERMS[venue].note`, and the refusal fires even when the store holds zero matching rows, so an empty result and a licence refusal can never be confused. **Collecting a venue never made it servable** -- ten venues are collected, and only the redistributable ones are served here; see GET /v1/l2/depth-venues. Rows carry the venue's OWN continuity evidence, and there are THREE different models: an update-id chain (`final_update_id` / `prev_final_update_id`, with `gap_count` in the coverage), a CRC32 BOOK-STATE checksum (`venue_checksum` / `checksum_verified`, kraken_spot -- which proves book state, NOT event delivery), and a periodic full SNAPSHOT with no continuity field at all (hyperliquid -- `gap_count` is null and MUST NOT be read as zero gaps). A row carries one model's evidence or the other's, never a blend. The window is capped at 2 hours per request (depth rows are heavier than trades) and `limit` defaults to 2,000, capped at 10,000; a cut is reported explicitly. An unreadable or unavailable store is **HTTP 503**, never 502/504.

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | yes | Venue id, e.g. binance_usdm. See GET /v1/l2/depth-venues for the full list. Required. |
| `symbol` | query | no | Restrict to one symbol (e.g. BTCUSDT). Omit to include every symbol the store collected in the window. |
| `start` | query | no | Window start, ISO-8601 UTC. Defaults to one hour before `end`. |
| `end` | query | no | Window end, ISO-8601 UTC, exclusive. Defaults to the current UTC hour. |
| `limit` | query | no | Max rows returned. Default 2,000, capped at 10,000. Default `2000`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `complete` | boolean |  |
| `coverage` | array |  |
| `dataset_version` | string |  |
| `hours_refused` | array |  |
| `limit` | integer |  |
| `row_count` | integer |  |
| `rows` | object | Depth rows: exchange_ts, local_recv_ts, venue, symbol, bid_prices, bid_sizes, ask_prices, ask_sizes, bid_levels, ask_levels, bid_levels_dropped, ask_levels_dropped, is_snapshot, source, and the continuity evidence for whichever model this venue uses (first/final/prev_update_id, or venue_checksum + checksum_verified, or neither). |
| `rows_available` | integer |  |
| `source_terms` | object | Keyed by venue served; each entry is that venue's SourceTerms. |
| `symbol` | string |  |
| `truncated` | boolean |  |
| `venue` | string |  |
| `window_covered_ms` | array |  |
| `window_requested_utc` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/l2/depth"
```

### `GET /v1/l2/depth-venues`

**L2 depth venue + continuity table** — keyless

Every venue the depth collector knows: whether it is cleared to reach a paying subscriber (the SAME licence answer as the trade tape, read from ops/l2_collector/dataset.py's SOURCE_TERMS), and WHICH CONTINUITY MODEL it proves itself with -- an update-id chain, a CRC32 book-state checksum, or a periodic snapshot that claims no continuity at all. Venues deliberately NOT collected are named with the specific unmeasured thing that blocks them, not a vague 'unsupported'.

Response fields:

| Field | Type | Description |
|---|---|---|
| `dataset_version` | string |  |
| `redistributable_venues` | array |  |
| `refused` | object | Venues not collected, each with the specific blocker. |
| `venues` | object | One entry per collected venue: venue, may_reach_subscriber, licence, origin, note, continuity model and the live evidence for it. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/l2/depth-venues"
```

## L2 trade tape

### `GET /v1/l2/trades`

**L2 trade tape** — keyless

Raw trade prints for one venue over a bounded UTC hour window, read directly from the collector's store (never written to). Only `venue=hyperliquid` returns rows today: every other venue's API terms forbid redistribution, and the request is refused with **HTTP 403** naming the venue and the exact licence reason (sourced from `SOURCE_TERMS[venue].note` -- see GET /v1/l2/venues for the full table). The refusal fires even when the store holds zero matching rows for that venue/window, so an empty result and a licence refusal can never be confused for one another. `start`/`end` are ISO-8601 UTC timestamps rounded down to the hour; the window is capped at 6 hours per request. `limit` caps the rows returned (default 5,000, capped at 20,000) -- `truncated`, `row_count` and `rows_available` in the response report a cut explicitly rather than silently. The response also carries the dataset's own coverage fields (`complete`, `hours_refused`, `window_covered_ms`, `dataset_version`, `source_terms`) so the limits of the extract travel with the data. An unreadable or unavailable store is **HTTP 503**, never 502/504.

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | yes | Venue id, e.g. hyperliquid. See GET /v1/l2/venues for the full list. Required. |
| `symbol` | query | no | Restrict to one symbol (e.g. BTC). Omit to include every symbol the store collected in the window. |
| `start` | query | no | Window start, ISO-8601 UTC (e.g. 2026-09-01T15:00:00Z). Defaults to one hour before `end`. |
| `end` | query | no | Window end, ISO-8601 UTC, exclusive. Defaults to the current UTC hour. |
| `limit` | query | no | Max rows returned. Default 5,000, capped at 20,000. Default `5000`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `complete` | boolean |  |
| `coverage` | array |  |
| `dataset_version` | string |  |
| `hours_refused` | array |  |
| `limit` | integer |  |
| `row_count` | integer |  |
| `rows` | object | Trade rows: exchange_ts, local_recv_ts, venue, symbol, side, price, size, tape (live/replay), source. |
| `rows_available` | integer |  |
| `source_terms` | object | Keyed by venue served; each entry is that venue's SourceTerms (origin, licence, may_reach_subscriber, note). |
| `symbol` | string |  |
| `truncated` | boolean |  |
| `venue` | string |  |
| `window_covered_ms` | array |  |
| `window_requested_utc` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/l2/trades"
```

### `GET /v1/l2/venues`

**L2 venue licence table** — keyless

Every venue this collector knows, whether it is cleared to reach a paying subscriber, and the reason for the rest -- read directly from ops/l2_collector/dataset.py's SOURCE_TERMS, the single place that answer is recorded (never a literal in the gateway).

Response fields:

| Field | Type | Description |
|---|---|---|
| `dataset_version` | string |  |
| `redistributable_venues` | array |  |
| `venues` | object | One entry per venue: venue, may_reach_subscriber, licence, origin, note. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/l2/venues"
```

## Liquidations

### `GET /v1/hl/frequently-liquidated`

**Frequently-liquidated HL wallets** — key required — Trader (3,000 calls/day)

Hyperliquid wallets ranked by liquidation frequency.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows, capped at 500. Default `100`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `frequently_liquidated` | array |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/hl/frequently-liquidated"
```

### `GET /v1/hl/liquidations`

**Hyperliquid whale liquidations** — key required — Trader (3,000 calls/day)

Recent liquidations of tracked Hyperliquid whale wallets, with summary.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows, capped at 500. Default `100`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `liquidations` | array |  |
| `summary` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/hl/liquidations"
```

### `GET /v1/hl/liquidations/summary`

**HL liquidation summary** — key required — Trader (3,000 calls/day)

Summary statistics for tracked Hyperliquid whale liquidations.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows, capped at 500. Default `100`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/hl/liquidations/summary"
```

### `GET /v1/liquidations`

**Liquidation levels (modelled) + realized tape** — key required — Trader (3,000 calls/day)

Two different things in one payload. (1) A MODELLED ladder of where leveraged positions would liquidate, built from measured open interest, an average leverage inferred from funding, and the liquidation prices of tracked Hyperliquid wallets. (2) `realized_heatmap` — what actually liquidated, from the live CEX tapes (Binance, OKX, Bybit, Bitget, BitMEX).

THE MODELLED LADDER IS NOT A SET OF OBSERVED CLUSTERS. Both band sides are placed at maintenance-margin/leverage from the same entry, so when neither side has a tracked wallet level in front of the bands the two nearest distances are EQUAL BY CONSTRUCTION. `nearest_symmetric: true` says so; `nearest_basis` names the source. Two equal percentages are one number restated, not two independent readings that agree.

NO PER-SIDE DOLLAR OPEN-INTEREST SPLIT IS INVENTED. `total_long_oi` and `total_short_oi` are null unless a venue actually reported a breakdown, and `oi_split_source` says which case you are in. For a perpetual, long and short notional are equal by identity, so a 50/50 bar is not an unmeasured quantity — it is a quantity that cannot differ. Directional skew is carried by `positioning`, which names the population behind every reading.

READ THE STATUS FIELDS. `bands_status`, `nearest_status`, `oi_split_source`, `positioning.status` and `whale_book.status` each separate "we measured this" from "we could not". A null distance, a null funding rate and a 'unknown' cascade_risk are absences, not zeros and not calm.

TIERS. Trader receives 26 of the 30 fields, listed per field below; the ladders are truncated to 5 levels per side (Pro: up to 10) and Pro additionally receives `nearest_status`, `nearest_excluded_modelled`, `nearest_exclusion_reason`, `realized_heatmap`. Anything a plan removed is named in `withheld` (`withheld_reason: "trader_plan"`), computed per response — so a short ladder does not report a boundary that removed nothing, and a missing key never has to stand in for both "not in your plan" and "the server had nothing".

NOTE: `nearest_status`, `nearest_excluded_modelled`, `nearest_exclusion_reason` qualify `nearest_long_liq_pct` / `nearest_short_liq_pct`, which Trader DOES receive, and are currently Pro-only. A Trader can still separate the two empty states — both distances null with a non-empty ladder means levels exist but none was eligible to set a headline; empty ladders mean nothing was on that side — but the count and the stated reason for refused levels are not on that plan.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `bands_status` | string | [Trader and Pro] Did the band model run? 'no_funding_measurement' means funding was never read, so nothing was modelled — a different question from `nearest_status`, and both are needed to write one honest sentence. |
| `cascade_risk` | string | [Trader and Pro] Bucket of the nearest reportable distance. 'unknown' means no distance was reportable at all — read it as absent, not as calm. |
| `current_price` | number | [Trader and Pro] Mark price every distance below is measured from. null when no usable price was readable — never 0. |
| `funding_rate` | number | [Trader and Pro] The only input to the inferred crowd leverage the bands are built from. null means never read, not zero. |
| `level_depth` | integer | [TRADER ONLY] Levels per side in this response (5). |
| `longs` | array | [Trader and Pro] Modelled long-liquidation ladder, nearest first. Each level carries liq_price, entry_px, leverage, dist_pct, source (whale_position \| oi_band) and size_measured. Trader receives the first 5 per side; Pro receives up to 10. The cut is taken from the FAR end, so the nearest level always matches the headline distance. |
| `nearest_basis` | string | [Trader and Pro] Where the headline distances came from: 'oi_band' (modelled ladder), 'whale' (a tracked position), or 'none'. |
| `nearest_excluded_modelled` | integer | [PRO/ENTERPRISE ONLY] How many drawn levels were refused as headline candidates because their liquidation price is modelled. Non-zero alongside nearest_status 'ok' is ordinary. |
| `nearest_exclusion_reason` | string | [PRO/ENTERPRISE ONLY] The caveat those refused levels carried. null when none were refused. |
| `nearest_long_liq_pct` | number | [Trader and Pro] Absolute percentage distance from `current_price` to the nearest long level eligible to set a headline. null when none was. |
| `nearest_short_liq_pct` | number | [Trader and Pro] Same on the short side. See `nearest_symmetric` before comparing the two. |
| `nearest_status` | string | [PRO/ENTERPRISE ONLY] Whether a distance was reportable. 'no_exchange_reported_levels' means levels exist and are drawn, but every candidate was modelled rather than exchange-reported and so was refused as a headline; 'no_levels' means there was nothing on that side at all. |
| `nearest_symmetric` | boolean | [Trader and Pro] true when BOTH nearest distances came from the open-interest band ladder. The bands place each side at maintenance-margin/leverage from the same entry, so the two percentages are then ONE number restated, not two located clusters. Do not read equality as agreement. |
| `oi_scope` | string | [Trader and Pro] What `total_oi` is a sum over. null whenever `total_oi` is null. |
| `oi_split_source` | string | [Trader and Pro] Why the per-side split is or is not present: 'measured' (a venue reported it), 'aggregate_only' (only the total was readable), 'unavailable' (nothing was). |
| `positioning` | object | [Trader and Pro] Directional skew, which unlike a dollar split IS measurable. Carries top_trader_long_share / top_trader_lsr with top_trader_scope, the account-headcount pair with its own scope, and `status` (ok \| unavailable \| unmeasured_default). 'unmeasured_default' means the upstream ratio was a default rather than a reading, and both shares are then null. |
| `price_age_s` | number | [Trader and Pro] Seconds between that price being observed and this payload being built. 0 for a live read. null when no price was readable — never 0, which would report an absent datum as a fresh one. |
| `price_source` | string | [Trader and Pro] Where `current_price` came from, in falling recency: 'binance_ticker' (live), 'last_known' (our own last good live read, bounded at 600 s), 'derivatives_snapshot' (median venue price from our newest collection cycle, bounded at 2700 s — derived from that feed's measured p99 of 28.8 min), or 'none' when no source answered and `current_price` is null. |
| `realized_by_side` | object | [TRADER ONLY] Trader's view of `realized_heatmap.by_side`. |
| `realized_heatmap` | object | [PRO/ENTERPRISE ONLY] The full realized tape for the last window: price x time matrices, per-price clusters, per-venue counts, totals and by_side. Present only when the stream has data for the symbol. |
| `realized_totals` | object | [TRADER ONLY] Trader's view of `realized_heatmap.totals` — notional and count of what actually liquidated. null when the tape had nothing. |
| `shorts` | array | [Trader and Pro] Modelled short-liquidation ladder, same shape and same truncation rule as `longs`. |
| `symbol` | string | [Trader and Pro] Base symbol this payload describes. |
| `total_long_oi` | number | [Trader and Pro] Long-side open interest in USD, and null unless a venue actually reported a per-side breakdown. The aggregate is NEVER halved into a 50/50 split — for a perpetual, long and short notional are equal by identity, so a dollar split is not a measurement. |
| `total_oi` | number | [Trader and Pro] Measured aggregate open interest in USD. The only open-interest number here that anything observed. |
| `total_short_oi` | number | [Trader and Pro] Short-side open interest in USD, under the same rule as `total_long_oi`. |
| `ts` | integer | [Trader and Pro] Unix timestamp the payload was built. |
| `whale_book` | object | [Trader and Pro] Summary of the tracked Hyperliquid book: status, scope, long_share, wallet counts, liq_price_source, as_of/age_s. No wallet identity. Trader's copy omits long_notional_usd, short_notional_usd. |
| `withheld` | array | [TRADER ONLY] Machine-readable list of what THIS response had removed by plan. Vocabulary: `level_detail_beyond_5`, `realized_heatmap.matrices`, `whale_book.long_notional_usd`, `whale_book.short_notional_usd`. Computed per response, so a symbol whose ladder was already short reports no boundary that removed nothing. |
| `withheld_reason` | string | [TRADER ONLY] Why those entries were removed. 'trader_plan' means the plan removed them; an absent field means nothing was removed. This is how a consumer tells 'your plan does not include this' apart from 'the server had nothing', which a missing key cannot express. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations"
```

### `GET /v1/liquidations/aftermath`

**Liquidation aftermath (live study)** — keyless

Conditional forward-return statistics after large liquidation minutes, computed over the RETAINED live tape. Descriptive statistics, explicitly not a directional signal: every horizon reports n, mean, median, positive fraction, a 95% CI, a permutation p-value and a plain-language verdict, so a result that is indistinguishable from baseline says so rather than being dressed up as an edge. `coverage` states the exact span and hours the statistics were computed over.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `coverage` | object |  |
| `data_posture` | string | Fixed disclaimer: descriptive conditional statistics, not a signal. |
| `event_definition` | string |  |
| `generated_at` | integer |  |
| `horizons` | object | Keyed by horizon ('+5m', '+15m', '+1h', ...), each holding long_liq / short_liq / all blocks with n, mean_pct, median_pct, pos_frac, std_pct, ci95_low_pct, ci95_high_pct, perm_p and verdict. |
| `n_events` | integer |  |
| `n_long_liq_events` | integer |  |
| `n_short_liq_events` | integer |  |
| `price_source` | string |  |
| `symbol` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/liquidations/aftermath"
```

### `GET /v1/liquidations/aftermath/historical`

**Liquidation aftermath (2-year OI-cascade proxy)** — keyless

The same aftermath question asked over two years of 4h open-interest and price history, because the live tape is only weeks deep. Takes no parameters: it serves one precomputed study for all symbols in the dataset. IMPORTANT — the events here are INFERRED from sharp OI drops coincident with price moves, not realized liquidations; `posture` says so in the payload and the two studies must not be pooled.

Response fields:

| Field | Type | Description |
|---|---|---|
| `dataset` | object |  |
| `event_definition` | string |  |
| `generated_at` | integer |  |
| `horizons` | array |  |
| `kind` | string |  |
| `n_events` | object |  |
| `per_symbol` | object |  |
| `posture` | string | States that events are an OI-cascade PROXY, not realized liquidations. |
| `span` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/liquidations/aftermath/historical"
```

### `GET /v1/liquidations/heatmap`

**Liquidation heatmap (realized)** — keyless

Price x time matrix of REAL executed forced liquidations, aggregated live from five public exchange WebSocket tapes (Binance, OKX, Bybit, Bitget, BitMEX) and persisted to a local archive. Nothing here is modelled or estimated: every cell is notional that actually liquidated at that price in that minute. Public, no key.

Windows up to 240 minutes are served from the in-process buffer (source='memory'); longer windows are read from the archive (source='archive') and additionally carry a `coverage` block.

READ `source` AND `coverage` BEFORE DRAWING A CONCLUSION. A flat, empty band in the matrix has two completely different meanings:
* the market was quiet (we were recording and nothing liquidated), or
* we were not recording at all (box down, feed down) — an absence of data, not an observation of zero.

`coverage.gaps` names the second case explicitly, and `coverage_note` summarises it in prose. `source='unavailable'` means the read itself failed, and the accompanying `note` says so — an empty payload with source='unavailable' must never be reported as 'no liquidations'.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `window_minutes` | query | no | Look-back window in minutes. Default 240 (4h). Clamped to 5-129600 (90 days); out-of-range and unparseable values fall back to the default rather than erroring. Windows <= the live buffer (240m) are served from memory; anything longer is read from the liquidation archive. Default `240`. |
| `price_buckets` | query | no | Number of price rows in the matrix. Default 50, clamped to 5-100. Default `50`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `by_side` | object |  |
| `clusters` | array | Price buckets ranked by liquidated notional — the practical output. |
| `coverage` | object | Recording coverage for the requested window. Only present when source == 'archive'. |
| `coverage_note` | string | Present only when coverage.gaps is non-empty: prose count and total hours of NOT-RECORDING inside this window. |
| `error` | string | Present when source == 'unavailable'. |
| `exchanges` | object | Event count per venue BACKING THIS RESPONSE. Read it instead of assuming all five tapes contributed — a venue missing here contributed nothing to this window. |
| `generated_at` | integer |  |
| `long_matrix` | array | Same grid, long liquidations only (longs force-sold). |
| `matrix` | array | price_buckets x time_buckets of liquidated notional (USD). Long + short combined. |
| `note` | string | Present only when totals.count == 0, and it says WHICH zero this is: a genuinely quiet window, or a failed read. |
| `price_bucket_size` | number |  |
| `price_buckets` | integer |  |
| `price_levels` | array | Row (price) axis, low to high. |
| `price_max` | number |  |
| `price_min` | number |  |
| `public` | boolean |  |
| `short_matrix` | array | Same grid, short liquidations only (shorts force-bought). |
| `source` | string | 'memory' = served from the live 4h buffer. 'archive' = read from the persisted liquidation history. 'unavailable' = the read FAILED (archive absent in this process, or the query errored); the payload is a well-formed empty structure and an `error` field explains the failure. Empty and broken are not the same state. |
| `symbol` | string |  |
| `time_bucket_minutes` | integer | Width of one matrix column, derived from the window. |
| `time_buckets` | array | Column (time) axis, epoch ms. |
| `totals` | object |  |
| `window_minutes` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/liquidations/heatmap"
```

### `GET /v1/liquidations/onchain`

**On-chain DeFi liquidations** — key required — Trader (3,000 calls/day)

Executed DeFi lending-protocol liquidations (AAVE, Venus, Benqi, etc.) watched directly from local BSC and Avalanche nodes, with per-chain/protocol summary. Pro additionally gets at-risk positions.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | no | Chain filter; omit for all. One of: `avax`, `bsc`. |
| `limit` | query | no | Max liquidations, capped at 500. Default `100`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `at_risk` | object |  |
| `chain` | string |  |
| `count` | integer |  |
| `liquidations` | array |  |
| `summary` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations/onchain"
```

### `GET /v1/liquidations/simulate`

**Liquidation cascade simulator** — keyless

Models what would be forced out if price moved by `move_pct` from here: triggered notional, per-exchange breakdown, cascade depth as a fraction of open interest, and the nearest long/short liquidation walls. MODELLED, not observed — `estimated: true` is in every response. It is built from tracked whale positions plus aggregate OI/leverage bands; no public data source exposes individual traders' real liquidation prices. For what actually liquidated, use /v1/liquidations/heatmap.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `move_pct` | query | no | Hypothetical price move in percent, signed (negative = down). Default -5. Clamped to -90..90. Default `-5`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `by_exchange` | object | Per-venue triggered notional: {venue: {long_usd, short_usd, total_usd}}. |
| `cascade_depth` | number |  |
| `cascade_risk` | string |  |
| `clusters` | array |  |
| `current_price` | number |  |
| `empty` | boolean | True when there was nothing to simulate (no positions/OI for this symbol). Distinct from ok=false, which is a failure. |
| `estimated` | boolean | Always true. This endpoint is a model. |
| `exchanges` | array | Venue names contributing to this simulation. |
| `methodology` | object | Every model assumption, surfaced in the payload. |
| `move_pct` | number |  |
| `nearest_long_wall` | object | Nearest modelled long liquidation wall, or null when none is derivable. |
| `nearest_short_wall` | object |  |
| `ok` | boolean |  |
| `realized_context` | object | REAL executed liquidations shown alongside the model for scale. Context only — it never makes the projection realized, and its own coverage span is stated so a short sample is not mistaken for a long one. |
| `symbol` | string |  |
| `target_price` | number |  |
| `total_oi_usd` | number |  |
| `triggered_count` | integer |  |
| `triggered_notional_usd` | number |  |
| `triggered_whale_usd` | number |  |
| `ts` | integer |  |
| `whale_positions_used` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/liquidations/simulate"
```

### `GET /v1/liquidations/symbols`

**Liquidation tape inventory** — keyless

Which symbols the liquidation archive actually holds, with per-symbol event count, first/last timestamp and total liquidated notional, plus the venue list.

This exists because /v1/liquidations/heatmap answers for ANY symbol string: a symbol that was never recorded returns the same well-formed empty grid as a symbol that was merely quiet. Check here first, and 'no rows for FOO' becomes a checkable fact instead of a guess.

source='unavailable' means the archive could not be read — an empty `symbols` list then means 'we could not look', not 'we hold nothing'.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max symbols returned, newest-busiest first. Default 500 (the gateway requests 2000), clamped to 1-2000. Default `500`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `error` | string | Present only when source == 'unavailable'. |
| `generated_at` | integer |  |
| `returned` | integer |  |
| `source` | string |  |
| `symbols` | array | Ordered by event count, descending. |
| `total_symbols` | integer | Symbols on the tape before the limit was applied. |
| `venues` | array | Distinct exchanges present in the archive. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/liquidations/symbols"
```

## Live chain

### `GET /v1/live-swaps/export`

**Export live swaps** — key required — Trader (3,000 calls/day)

CSV export of the live swap history. Authenticates with its own key check (X-API-Key header or ?key=) and is limited to 10 exports per account per rolling 24 hours.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/live-swaps/export"
```

### `GET /v1/live-swaps/recent`

**Recent DEX swaps** — keyless

First-paint snapshot of recent large DEX swaps. Website widgets call this once, then subscribe to the stream.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `events` | array |  |
| `public` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/live-swaps/recent"
```

### `GET /v1/live-swaps/status`

**Live-swap stream status** — keyless

Health and coverage of the live swap stream.

Response fields:

| Field | Type | Description |
|---|---|---|
| `active_subscribers` | integer |  |
| `archive` | object |  |
| `broadcast_min_usd` | number |  |
| `buffer_size` | integer |  |
| `dropped_below_threshold` | integer |  |
| `dropped_full_queue` | integer |  |
| `published_total` | integer |  |
| `subscribers_total_ever` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/live-swaps/status"
```

### `GET /v1/mempool/pending`

**Pending mempool swaps** — keyless

Pending large swaps observed in the local node mempool.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `chain` | string |  |
| `count` | integer |  |
| `events` | array |  |
| `public` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mempool/pending"
```

### `GET /v1/mempool/stats`

**Mempool statistics** — keyless

Mempool depth and gas statistics from the local nodes.

Response fields:

| Field | Type | Description |
|---|---|---|
| `bnb_price_usd` | number |  |
| `buffered` | integer |  |
| `chain` | string |  |
| `errors` | integer |  |
| `kept_total` | integer |  |
| `last_poll_ts` | integer |  |
| `min_bnb` | number |  |
| `pending_pool` | integer |  |
| `queued_pool` | integer |  |
| `seen_total` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mempool/stats"
```

## Market

### `GET /v1/market/altseason`

**Altcoin Season Index** — key required — withheld

Altcoin season index derived from top-coin performance vs BTC. Public.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/market/altseason"
```

### `GET /v1/market/basis`

**CME basis** — key required — withheld

CME futures basis vs spot. Public.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/market/basis"
```

### `GET /v1/market/candles`

**Recent OHLC candles** — keyless

Recent spot OHLC candles for a base symbol. Exists so the embeddable widgets can draw a price line without the reader's browser calling an exchange directly (the /embed/* CSP forbids it, and an embed must not leak the publisher's visitors to a third party). Public.

Returns 400 for a pair that is not listed upstream and 503 when the price cannot be read. It never returns an empty `candles` array: an empty series would be drawn as "no price here" rather than "unknown".

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `interval` | query | no | Candle interval. One of: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `1d`. Default `5m`. |
| `limit` | query | no | Number of candles returned, newest last. Default `68`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/candles"
```

### `GET /v1/market/dominance`

**BTC dominance** — key required — withheld

Bitcoin market-cap dominance. Public.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/market/dominance"
```

### `GET /v1/market/indices`

**All market indices** — keyless

All market indices in one response. Public.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/indices"
```

### `GET /v1/market/volatility`

**Volatility index** — keyless

Crypto volatility gauge (Deribit). Public.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/volatility"
```

### `GET /v1/mood`

**Market mood** — keyless

Composite market-mood reading built from funding, positioning and volatility inputs.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mood"
```

### `GET /v1/mood/history`

**Mood history** — keyless

Historical mood series for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `days` | query | no | Look-back window in days. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mood/history"
```

### `GET /v1/mood/overview`

**Mood overview** — keyless

Mood reading across the tracked symbol universe. Served from cache; returns a warming-up marker rather than recomputing inline.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mood/overview"
```

### `GET /v1/projection`

**Pattern projection** — keyless

Pattern-match projection from historical analogues: a bullish or bearish `direction` with its probabilities and a `signal_strength`. The response carries `operator_position_disclosure`, dated when served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_correlation` | number |  |
| `bear_path` | array |  |
| `bull_path` | array |  |
| `count_matches` | integer |  |
| `current_price` | number |  |
| `direction` | string |  |
| `historical_prices` | array |  |
| `horizon` | integer |  |
| `lookback` | integer |  |
| `matches` | array |  |
| `operator_position_disclosure` | object |  |
| `probability_bearish` | integer |  |
| `probability_bullish` | integer |  |
| `robustness` | integer |  |
| `signal_strength` | string |  |
| `symbol` | string |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/projection"
```

### `GET /v1/projection/screener`

**Projection screener** — keyless

Pattern projections across the symbol universe. Every row carries `operator_position_disclosure`, dated when the response is served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/projection/screener"
```

## Meta

### `GET /openapi.json`

**This OpenAPI document** — keyless

The machine-readable OpenAPI 3 description of this API. Served by the gateway and regenerated by ops/gen_openapi.py.

Response fields:

| Field | Type | Description |
|---|---|---|
| `components` | object |  |
| `info` | object |  |
| `openapi` | string |  |
| `paths` | object |  |
| `security` | array |  |
| `servers` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/openapi.json"
```

### `GET /v1/billing/regime`

**VAT regime in force** — keyless

The Italian VAT regime this business invoices under, read from `api_service/plans.json` — the single source of truth — and resolved for today. Public and keyless because peer systems (and anyone checking an invoice) must be able to read it without an account.

RESOLVE IT FOR THE INVOICE'S OWN DATE, NOT FOR 'NOW'. The regime is a property of the operation date (`DataDocumento`), so an invoice issued before a regime change keeps the regime that was in force when it was issued. `regime_today` is a convenience for the common case; it is not a licence to stamp today's regime onto a back-dated document.

`cache_s` is how long a caller may hold this before re-reading. An unreadable or malformed flag answers 503 rather than guessing a regime, so a peer keeps its last-good value instead of caching a fabricated one.

Response fields:

| Field | Type | Description |
|---|---|---|
| `VAT_REGIME` | string |  |
| `as_of` | string |  |
| `cache_s` | integer |  |
| `note` | string |  |
| `regime_today` | string |  |
| `schema_version` | integer |  |
| `source` | string |  |
| `vat` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/billing/regime"
```

### `GET /v1/exchange-health`

**Exchange health** — keyless

Per-exchange latency/error status from live probes (falls back to daemon health + recent data recency).

Response fields:

| Field | Type | Description |
|---|---|---|
| `exchanges` | object |  |
| `overall` | string |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/exchange-health"
```

### `GET /v1/health`

**Gateway health** — keyless

Simple gateway liveness check.

Response fields:

| Field | Type | Description |
|---|---|---|
| `ingestion` | object |  |
| `loop_stall` | object |  |
| `status` | string |  |
| `subsystems` | object |  |
| `subsystems_down` | array |  |
| `subsystems_warming` | array |  |
| `ts` | number |  |
| `warming` | boolean |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/health"
```

### `GET /v1/incidents`

**Incident log** — keyless

Recent operational incidents and degradations, as published on the public status page.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `incidents` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/incidents"
```

### `GET /v1/plans`

**Plan catalogue** — keyless

Public tier catalogue generated from plans.json: prices, daily call quotas, per-minute limits, allowed symbols and feature flags.

Response fields:

| Field | Type | Description |
|---|---|---|
| `annual_discount_bps` | integer |  |
| `currency` | string |  |
| `schema_version` | integer |  |
| `tiers` | object |  |
| `trial` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/plans"
```

### `GET /v1/stats`

**Site statistics** — keyless

Canonical public site stats: venue counts, tracked derivatives symbols, measured signal win-rates with sample sizes (in-sample labelled) and the accruing out-of-sample forward holdout. Cached.

TWO VENUE COUNTS, AND THEY ARE NOT INTERCHANGEABLE. `exchanges` counts the venues behind the DERIVATIVES data (currently 3) and is the number the copy 'derivatives across N exchanges' may use. `venues_total` counts the wider union including liquidation-only venues (currently 6) -- bitget, bitmex and okx stream liquidations but appear nowhere in the derivatives table, so publishing 6 as the derivatives venue count would be a claim we cannot support. `exchange_names` and `venue_names_all` are the corresponding name lists, so a consumer never has to guess which set a count refers to.

Every headline figure carries an entry in `basis` naming its source, window and what it counts. A field whose source is unavailable is OMITTED, never zeroed -- absence of a key means 'not measured', which is a different claim from a zero.

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_loss_pct` | number |  |
| `avg_win_pct` | number |  |
| `basis` | object |  |
| `chains` | integer |  |
| `confirm_excluded_episodes` | integer |  |
| `confirm_horizon` | string |  |
| `confirm_outcomes_n` | integer |  |
| `confirm_signals_dedup_rule` | string |  |
| `confirm_signals_n` | integer |  |
| `derivatives_symbols` | integer |  |
| `endpoints` | integer |  |
| `exchange_names` | array |  |
| `exchanges` | integer |  |
| `expectancy_pct` | number |  |
| `forward_holdout` | object |  |
| `high_expectancy_pct` | number |  |
| `high_n_forward` | integer |  |
| `high_pf` | number |  |
| `high_status` | string |  |
| `high_winrate` | number |  |
| `high_winrate_ci` | array |  |
| `high_winrate_forward` | number |  |
| `high_winrate_n` | integer |  |
| `high_winrate_publishable` | boolean |  |
| `high_winrate_withheld_reason` | string |  |
| `last_updated` | string |  |
| `medium_expectancy_pct` | number |  |
| `medium_pf` | number |  |
| `medium_winrate` | number |  |
| `medium_winrate_ci` | array |  |
| `medium_winrate_n` | integer |  |
| `medium_winrate_publishable` | boolean |  |
| `overall_accuracy` | number |  |
| `overall_accuracy_ci` | array |  |
| `overall_accuracy_forward` | number |  |
| `overall_accuracy_n` | integer |  |
| `overall_accuracy_publishable` | boolean |  |
| `overall_expectancy_pct` | number |  |
| `overall_n_forward` | integer |  |
| `overall_pf` | number |  |
| `payoff_horizon` | string |  |
| `profit_factor` | number |  |
| `refresh_cycle` | string |  |
| `refresh_cycle_s` | integer |  |
| `signal_count` | integer |  |
| `stats_source` | string |  |
| `tracked_symbols` | integer |  |
| `venue_names_all` | array |  |
| `venues_total` | integer |  |
| `whale_count` | integer |  |
| `whales_tracked_total` | integer |  |
| `winrate_basis` | string |  |
| `winrate_dedup_rule` | string |  |
| `winrate_excluded_episodes` | integer |  |
| `winrate_horizon` | string |  |
| `winrate_min_publish_n` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stats"
```

### `GET /v1/stats/calls`

**API calls served** — keyless

How many API calls we have served to callers who are NOT us. For the landing page, and public so the claim on it can be checked.

IT IS NOT THE TOTAL, AND THAT IS THE POINT. Measured over the week this was built: of 661,447 calls, 462,291 were our own daemon polling this gateway over loopback and 75,082 were the operator's own bots. A counter fed by the total would have been about 70% us, shown to visitors as evidence of demand. `excludes` names every category left out, including this endpoint itself -- the landing page polls it on a timer, and a number that grows by being looked at is not a measurement.

IT IS A FLOOR, AND IT PUBLISHES NO START DATE. The counter began from whatever the two request logs had not yet pruned, so it understates the true total by an unknown amount and covers no period we can name. It is a stored high-water mark rather than a COUNT(*), because the anonymous log is trimmed by age and by row count and a live scan would fall every time the pruner ran.

`calls` is null, with `state` naming the reason, whenever the number cannot be read -- including `warming` for a counter that has not yet run. Never measured and measured zero are different facts and neither is published as 0.

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | string |  |
| `calls` | integer |  |
| `counts` | string |  |
| `excludes` | array |  |
| `seed_is_a_floor` | boolean |  |
| `state` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stats/calls"
```

### `GET /v1/symbols`

**Tracked symbols** — keyless

All derivative symbols currently tracked by the aggregation daemon.

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `meta` | object |  |
| `symbols` | array |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/symbols"
```

## News

### `GET /v1/news/accuracy`

**News classifier accuracy** — keyless

Measured accuracy of the news impact classifier, published with its sample size.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/accuracy"
```

### `GET /v1/news/archive`

**News archive (paginated)** — keyless

The WHOLE retained news archive, not just the recent window that /v1/news/general serves. Cursor-paginated (keyset on ts+id, stable while new rows arrive at the head), date-rangeable and keyword-searchable. Unlike /v1/news/general this includes TRUMP_POLICY by default. Page size is capped server-side at 200. Every empty response carries a `status` (ok | no_match | before_coverage | after_coverage | no_records_yet) and an `empty_reason`, so a range that predates our records is distinguishable from a filter that matched nothing. The item array is under the key `events`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Page size, 1-200. Default `50`. |
| `cursor` | query | no | Opaque keyset cursor '<ts>_<id>' from `next_cursor` of the previous page. |
| `offset` | query | no | Alternative to cursor for random access. Default `0`. |
| `start` | query | no | Inclusive start, YYYY-MM-DD or unix seconds. |
| `end` | query | no | Exclusive end, YYYY-MM-DD or unix seconds. |
| `date` | query | no | Sugar for one whole UTC day, YYYY-MM-DD. |
| `category` | query | no | One of TRUMP_POLICY, WAR_GEOPOLITICAL, CRYPTO_REGULATORY, MARKET_SHOCK, FED_MONETARY, CRYPTO_GENERAL. |
| `source` | query | no | Publisher name, e.g. Reuters. |
| `q` | query | no | Keyword search over headline and summary; multiple terms are ANDed. |
| `include_trump` | query | no | Set 0 to exclude TRUMP_POLICY. Default 1. Default `1`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/archive"
```

### `GET /v1/news/coverage`

**News archive coverage** — keyless

What the archive actually contains: row count, oldest and newest timestamps and dates, span in days, and breakdowns by category and by source. Use it to render an honest coverage statement rather than implying records exist for dates we never retained.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/coverage"
```

### `GET /v1/news/fear-greed`

**Fear & Greed index** — keyless

Crypto Fear & Greed index (Alternative.me).

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/fear-greed"
```

### `GET /v1/news/general`

**General news** — keyless

General crypto/geopolitical news, keyword-classified into six categories (TRUMP_POLICY, WAR_GEOPOLITICAL, CRYPTO_REGULATORY, MARKET_SHOCK, FED_MONETARY, CRYPTO_GENERAL).

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max items. Default `30`. |
| `hours` | query | no | Lookback window in hours. Default `24`. |
| `category` | query | no | Filter by category name. |
| `include_trump` | query | no | Set 1 to stop excluding TRUMP_POLICY. The default (0) omits it; the response always declares what was withheld in `excluded_categories`. Default `0`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/general"
```

### `GET /v1/news/impact`

**News impact** — keyless

Current aggregated news impact state.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/impact"
```

### `GET /v1/news/treasury-yield`

**Treasury yields** — keyless

US Treasury yield levels used by the macro classifier.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/treasury-yield"
```

### `GET /v1/news/trump`

**Trump policy news** — keyless

Trump/policy-classified news items with impact levels.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max items. Default `20`. |
| `hours` | query | no | Lookback window in hours. Default `24`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/trump"
```

## Node

### `GET /v1/node/health`

**Node health** — keyless

Health of the self-hosted BSC and Avalanche full nodes backing the node-intelligence and JSON-RPC products.

Response fields:

| Field | Type | Description |
|---|---|---|
| `chains` | object |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/node/health"
```

### `GET /v1/node/{chain}/deployer/{address}`

**Deployer history** — key required — withheld

Deployment history for a contract deployer.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/deployer/{address}"
```

### `GET /v1/node/{chain}/honeypot/{address}`

**Honeypot check** — key required — per-feature node entitlement

Simulated buy/sell honeypot check for one token.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/honeypot/{address}"
```

### `GET /v1/node/{chain}/large-swaps`

**Large swaps** — key required — per-feature node entitlement

Large DEX swaps observed by the self-hosted node for the chain (bsc or avax). Entitlement and quota are enforced per chain and per feature by node_entitlements, independently of the API tier allowlist.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/large-swaps"
```

### `GET /v1/node/{chain}/liquidity-events`

**Liquidity events** — key required — per-feature node entitlement

Liquidity add/remove events. Indexer-backed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |
| `token` | query | no | Filter by token address. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/liquidity-events"
```

### `GET /v1/node/{chain}/new-pairs`

**New pairs** — key required — per-feature node entitlement

Newly created DEX pairs. Served by the on-chain indexer; returns 503 while the indexer is disabled on this deployment.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/new-pairs"
```

### `GET /v1/node/{chain}/pending-swaps`

**Pending swaps** — key required — per-feature node entitlement

Pending swaps in the node mempool. Indexer-backed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/pending-swaps"
```

### `GET /v1/node/{chain}/smart-money`

**Node smart money** — key required — per-feature node entitlement

Smart-money wallet activity from the node's own trace data.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/smart-money"
```

### `GET /v1/node/{chain}/snipers`

**Snipers** — key required — per-feature node entitlement

Wallets that sniped a launch. Indexer-backed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/snipers"
```

### `GET /v1/node/{chain}/token-risk/{address}`

**Token risk** — key required — per-feature node entitlement

Contract-level risk checks for one token.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/token-risk/{address}"
```

### `GET /v1/node/{chain}/token/{address}`

**Token profile** — key required — per-feature node entitlement

Node-derived profile for one token.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/token/{address}"
```

### `GET /v1/node/{chain}/top-holders/{address}`

**Top holders** — key required — withheld

Largest holders of one token.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/top-holders/{address}"
```

### `GET /v1/node/{chain}/wallet/{address}`

**Wallet profile** — key required — per-feature node entitlement

Node-derived profile for one wallet.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `chain` | path | yes | Node chain: bsc or avax. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/node/{chain}/wallet/{address}"
```

## On-chain

### `GET /v1/onchain/btc`

**BTC on-chain stats** — key required — withheld

Bitcoin network stats: hashrate, difficulty, mempool, transaction counts (Blockchain.com).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/btc"
```

### `GET /v1/onchain/dex`

**DEX volumes** — key required — withheld

Decentralised exchange volume rankings (DeFiLlama).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/dex"
```

### `GET /v1/onchain/gas`

**Ethereum gas** — keyless

Current Ethereum gas prices, derived from eth_feeHistory (base fee plus the 25th/50th/90th percentile priority tip over the last 20 blocks) against a public Ethereum RPC.

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/gas"
```

### `GET /v1/onchain/liquidations/coverage`

**On-chain liquidation coverage** — keyless

What we hold, per chain/protocol/source: event counts, the share that carries a USD price, and the time span. This is our own coverage FACT, never the events themselves, which is why it is public while the two event queries are not. `priced_pct` is published beside every count because a total taken over only the rows that happened to price is a different number from a total.

Response fields:

| Field | Type | Description |
|---|---|---|
| `meta` | object |  |
| `rows` | array |  |
| `totals` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/liquidations/coverage"
```

### `GET /v1/onchain/liquidations/history`

**On-chain liquidation events** — key required — Free (200 calls/day)

DeFi lending liquidation events (Aave V2/V3, Benqi, Venus, Compound forks and others) across arbitrum, base, bnb, ethereum, optimism, polygon and avalanche_c, newest first. Metered per plan: the window is clamped to your tier's history_days and the row count to its max_rows, and both limits plus `window_clamped_to_plan` ride in the response so a clamped answer is never mistaken for an empty one.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | no | Restrict to one chain, e.g. arbitrum, base, bnb, ethereum, optimism, polygon, avalanche_c. Omitted means every chain. |
| `protocol` | query | no | Restrict to one lending protocol, e.g. Aave, AaveV2, AaveV3, Benqi, Venus, CompoundFork. |
| `since` | query | no | Window start, unix seconds. Clamped to the history_days your plan allows; the response says so in window_clamped_to_plan. |
| `until` | query | no | Window end, unix seconds. |
| `min_usd` | query | no | Only events whose priced debt is at least this many USD. Unpriced events are never counted as zero — they are excluded and reported. |
| `limit` | query | no | Maximum rows. Clamped to the max_rows your plan allows. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `events_priced` | integer |  |
| `events_returned` | integer |  |
| `history_days_limit` | integer |  |
| `max_rows_limit` | integer |  |
| `meta` | object |  |
| `newest_ts` | integer |  |
| `oldest_ts` | integer |  |
| `priced_pct` | number |  |
| `rows` | array |  |
| `sources` | array |  |
| `tier` | string |  |
| `window_clamped_to_plan` | boolean |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/liquidations/history"
```

### `GET /v1/onchain/liquidations/top`

**Largest on-chain liquidations** — key required — Free (200 calls/day)

The largest PRICED liquidation events in a tier-metered window, by debt_usd descending. Events we could not price are EXCLUDED and counted in `unpriced_excluded` rather than ranked as zero.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | no | Restrict to one chain, e.g. arbitrum, base, bnb, ethereum, optimism, polygon, avalanche_c. Omitted means every chain. |
| `protocol` | query | no | Restrict to one lending protocol, e.g. Aave, AaveV2, AaveV3, Benqi, Venus, CompoundFork. |
| `since` | query | no | Window start, unix seconds. Clamped to the history_days your plan allows; the response says so in window_clamped_to_plan. |
| `until` | query | no | Window end, unix seconds. |
| `min_usd` | query | no | Only events whose priced debt is at least this many USD. Unpriced events are never counted as zero — they are excluded and reported. |
| `limit` | query | no | Maximum rows. Clamped to the max_rows your plan allows. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `events_scanned` | integer |  |
| `history_days_limit` | integer |  |
| `max_rows_limit` | integer |  |
| `meta` | object |  |
| `newest_ts` | integer |  |
| `priced_pct` | number |  |
| `rows` | array |  |
| `sources` | array |  |
| `tier` | string |  |
| `unpriced_excluded` | integer |  |
| `window_clamped_to_plan` | boolean |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/liquidations/top"
```

### `GET /v1/onchain/metrics`

**All on-chain metrics** — keyless

Aggregated on-chain metrics bundle (DeFiLlama TVL/stablecoins/DEX volumes, Blockchain.com BTC stats, Ethereum gas, CoinGecko global). Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `onchain` | object |  |
| `public` | boolean |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/metrics"
```

### `GET /v1/onchain/stablecoins`

**Stablecoin supply** — key required — withheld

Stablecoin circulating supply breakdown (DeFiLlama).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/stablecoins"
```

### `GET /v1/onchain/tvl`

**TVL by chain** — key required — withheld

DeFi total value locked per chain (DeFiLlama). Anonymous callers get the top 10 chains.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/tvl"
```

### `GET /v1/onchain/yields`

**DeFi yields** — key required — withheld

Top DeFi yield pools (DeFiLlama). Anonymous callers get the top 8 pools.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/onchain/yields"
```

## Options

### `GET /v1/options`

**Options index** — key required — withheld

Index of the available options endpoints.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options"
```

### `GET /v1/options/chain`

**Options chain summary** — key required — withheld

BTC/ETH options summary from Deribit: put/call ratio, max pain, open interest by strike, per-expiry breakdown.

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/chain"
```

### `GET /v1/options/gex`

**Gamma exposure** — key required — withheld

Dealer gamma-exposure profile by strike for BTC/ETH.

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/gex"
```

### `GET /v1/options/history`

**Options history** — key required — withheld

Historical options aggregates (put/call ratio, open interest).

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/history"
```

### `GET /v1/options/iv-surface`

**Implied-volatility surface (one book)** — key required — withheld

Per-instrument implied-volatility surface for one Deribit option book (BTC, ETH, or a USDC-linear book such as BTC_USDC, SOL_USDC, HYPE_USDC). Every `iv_pct` on a node is Deribit's own published mark IV, carried through unchanged; anything this endpoint derives itself (an interpolated ATM point, a fixed-moneyness skew point, the 25-delta risk reversal) is labelled `fitted: true` under its own key and never mixed into a measured field. The surface is SPARSE: `grid.rectangle_cells` (n_strikes x n_expiries) is not the number of quoted cells, and holes are listed per expiry rather than interpolated into the node set. `nodes` (the actual per-strike quotes) is included only with `?nodes=1` -- omitted by default because the full BTC node set is ~440KB against ~92KB without it on a keyless route. An unknown book or an upstream Deribit fetch failure both return 200 with `status` naming the failure (fetch_failed / unknown_book) rather than a 4xx/5xx, so a caller following `status` never has to special-case a non-2xx response; a genuine internal error (module failed to import) is a 503 with `error=capability_unavailable`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `book` | query | no | Deribit option book identifier (the part of an instrument name before the first '-'). BTC and ETH are coin-margined; each also lists a separate USDC-linear book (BTC_USDC, ETH_USDC, ...). See /v1/options/iv-surface/books for the full list. Default `BTC`. |
| `nodes` | query | no | Include the full per-strike/expiry node grid (call+put mark IV, quote_state, greeks). Accepts 1/true/yes; anything else is treated as 0. Default 0 (grid + term-structure + skew only, no nodes). Default `0`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/iv-surface"
```

### `GET /v1/options/iv-surface/books`

**Implied-volatility surface -- book list** — key required — withheld

Every Deribit option book currently listed, with headline surface numbers (grid fill, front-expiry ATM IV, leg counts) and no node payload -- the index to page against before calling /v1/options/iv-surface?book=<book>. BTC and ETH each list a coin-margined AND a USDC-linear book; those are two separate surfaces, not one book counted twice.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/iv-surface/books"
```

### `GET /v1/options/overview`

**Options overview (BTC + ETH)** — key required — withheld

Both BTC and ETH options summaries in one response.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/overview"
```

### `GET /v1/options/pcr`

**Put/call ratio** — key required — withheld

BTC options summary (put/call ratio focus). Same payload shape as /v1/options/chain with currency=BTC.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/pcr"
```

## Performance

### `GET /v1/performance`

**Signal accuracy stats** — keyless

Signal accuracy statistics across tracked symbols, merged with signal-tracker outcomes (recent_signals + whale_signals).

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Lookback window (1-3650). Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `by_confidence` | object |  |
| `by_symbol` | object |  |
| `excluded_signals` | integer |  |
| `licence_exclusion` | object |  |
| `min_resolved_sample` | integer |  |
| `overall_accuracy` | number |  |
| `overall_resolved` | integer |  |
| `period_days` | integer |  |
| `population` | object |  |
| `recent_signals` | array |  |
| `signal_counts` | object |  |
| `symbol_timeseries` | object |  |
| `total_signals` | integer |  |
| `veto_by_symbol` | object |  |
| `whale_signals` | object |  |
| `windows` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/performance"
```

### `GET /v1/performance/export`

**Performance export** — key required — Trader (3,000 calls/day)

CSV (or JSON, format=json) export of the tracked-signal performance log. Every row carries `operator_position_disclosure` as recorded when the signal was logged (`unavailable` for older rows); in CSV the object is one column of compact JSON.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/performance/export"
```

### `GET /v1/performance/track-record`

**Forward-test track record** — keyless

Forward-test equity curve and payoff stats for the smart_money_confirm engine. Live-generated (not a backtest), in-sample-tuned, pre-fee; carries the accruing out-of-sample forward_holdout and a disclaimer.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Lookback window (1-365). Default `30`. |
| `horizon` | query | no | Single-horizon view; omit for the blended 4-24h window. One of: `24h`, `48h`, `72h`. |
| `confidence` | query | no | Confidence-tier filter. One of: `HIGH`, `MEDIUM`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `basis` | string |  |
| `btc_overlay` | — |  |
| `confidence` | — |  |
| `cost_bases` | object |  |
| `cost_basis_note` | string |  |
| `curves` | array |  |
| `curves_gross` | array |  |
| `curves_net_fees` | array |  |
| `curves_net_fees_slip` | array |  |
| `dedup_effect` | object |  |
| `dedup_rule` | string |  |
| `disclaimer` | string |  |
| `excluded_episodes` | integer |  |
| `forward_holdout` | object |  |
| `horizon` | string |  |
| `is_full_span` | boolean |  |
| `licence_exclusion` | object |  |
| `min_publish_n` | integer |  |
| `n_signals` | integer |  |
| `population` | object |  |
| `scorer_frozen_ts` | integer |  |
| `sizing_note` | string |  |
| `summary` | object |  |
| `timestamps` | array |  |
| `window_days` | — |  |
| `window_end` | integer |  |
| `window_label` | string |  |
| `window_since_ts` | integer |  |
| `window_start` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/performance/track-record"
```

## Reference

### `GET /v1/symbols/universe`

**Symbol universe** — key required — Free (200 calls/day)

Every symbol currently listed across the tracked venues, resolved to a canonical asset from the base the VENUE declares in its own instrument metadata — the ticker string is never parsed. Delisted symbols are kept in history and never returned here. Free plans receive a sample.

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | no | Restrict to one venue key. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/symbols/universe"
```

### `GET /v1/symbols/universe/asset`

**One asset everywhere** — key required — Free (200 calls/day)

One canonical asset across every venue that lists it, with its scale variants (1000PEPE, KPEPE) LINKED but never merged — no venue publishes the multiplier as a field, so the link is derived and labelled as such.

| Parameter | In | Required | Description |
|---|---|---|---|
| `asset` | query | yes | Canonical asset id, e.g. BTC. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/symbols/universe/asset"
```

### `GET /v1/symbols/universe/coverage`

**Universe coverage** — key required — Trader (3,000 calls/day)

Per venue: what was requested, what was not, and whether absence is CONCLUSIVE. `absence_is_conclusive: false` means we never asked for that product line — our fetch gap, not a statement that the venue does not list the symbol.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/symbols/universe/coverage"
```

### `GET /v1/symbols/universe/venue`

**One venue's listings** — key required — Trader (3,000 calls/day)

One venue's live symbols, or — with `symbol` — the specific reason a symbol is absent from it (not listed / not requested / unknown because the last read failed).

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | yes | Venue key. |
| `symbol` | query | no | Ask why this symbol is absent instead of listing all. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/symbols/universe/venue"
```

## Research

### `GET /v1/research/coverage`

**Research capture coverage** — key required — Trader (3,000 calls/day)

Per-table coverage of the Hyperliquid research capture: time span, shards and status. A table with `status: empty` exists in the schema with no rows; that is different from a table we cannot read. Every response carries provenance including is_live_production_feed: false.

| Parameter | In | Required | Description |
|---|---|---|---|
| `counts` | query | no | Include row counts (slower). |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/research/coverage"
```

### `GET /v1/research/disk`

**Research storage report** — key required — Trader (3,000 calls/day)

Shard sizes, filesystem usage, retention policy and the (unexecuted) relocation plan. Paid plans only.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/research/disk"
```

### `GET /v1/research/query`

**Query the research capture** — key required — Trader (3,000 calls/day)

Read-only, bounded query over the research shards. Timestamps are epoch MILLISECONDS. Some tables have no timestamp-only index and therefore REFUSE an unfiltered range with 503 rather than running a multi-GB scan; truncation is always declared in the envelope.

| Parameter | In | Required | Description |
|---|---|---|---|
| `table` | query | yes | Table name. |
| `coin` | query | no | Filter by coin. |
| `wallet` | query | no | Filter by wallet. |
| `interval` | query | no | Kline interval. |
| `start_ms` | query | no | Start, epoch ms. |
| `end_ms` | query | no | End, epoch ms. |
| `order` | query | no | asc or desc. One of: `asc`, `desc`. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/research/query"
```

### `GET /v1/research/symbols`

**Research symbols** — key required — Trader (3,000 calls/day)

Distinct coins actually collected for a table. Free plans receive a sample.

| Parameter | In | Required | Description |
|---|---|---|---|
| `table` | query | no | Table name. Default `price_snapshots`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/research/symbols"
```

## Screener

### `GET /v1/rankings`

**Symbol rankings** — keyless

Composite symbol rankings with the methodology used to build them. Every row carries `operator_position_disclosure`, dated when the response is served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/rankings"
```

### `GET /v1/scanner/obs`

**Order-block scanner** — keyless

Order-block / imbalance scanner across the symbol universe.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/scanner/obs"
```

### `GET /v1/scanner/obs/extremes`

**Order-block extremes** — keyless

Most extreme order-block readings in the current scan.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/scanner/obs/extremes"
```

### `GET /v1/scanner/obs/symbol`

**Order-block detail** — keyless

Order-block scan detail for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/scanner/obs/symbol"
```

### `GET /v1/screener`

**Multi-factor screener** — keyless

Cross-symbol screener over derivatives, whale and technical factors, with a bullish/bearish classification per symbol. Every row carries `operator_position_disclosure`, dated when the response is served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/screener"
```

### `GET /v1/screener/rankings`

**Screener rankings** — keyless

Ranked screener output. Every row carries `operator_position_disclosure`, dated when the response is served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/screener/rankings"
```

### `GET /v1/screener/symbol`

**Screener detail** — keyless

Full screener factor breakdown for one symbol. Carries `operator_position_disclosure`, dated when served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/screener/symbol"
```

## Seasonality

### `GET /v1/seasonality`

**Seasonality summary** — keyless

Calendar-seasonality statistics for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality"
```

### `GET /v1/seasonality/dow`

**Day-of-week seasonality** — keyless

Day-of-week return distribution.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/dow"
```

### `GET /v1/seasonality/heatmap`

**Seasonality heatmap** — keyless

Month-by-year return heatmap.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/heatmap"
```

### `GET /v1/seasonality/overlay`

**Seasonality overlay** — keyless

Current year overlaid on the historical seasonal path.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/overlay"
```

### `GET /v1/seasonality/quarters`

**Quarterly seasonality** — keyless

Quarter-by-quarter return statistics.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/quarters"
```

### `GET /v1/seasonality/rankings`

**Seasonality rankings** — keyless

Symbols ranked by the current seasonal window.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/rankings"
```

## Signals

### `GET /v1/confirm`

**Smart-money confirmation** — key required — Free (200 calls/day)

Score a trade the caller is about to take. One request reads the aggregated Bybit/Binance/Hyperliquid derivatives, on-chain metrics and tracked whale positioning for the symbol, and returns a verdict with the full arithmetic behind it: per-component scores and weights (`factors`), every signed modifier (`adjustments`), which data families actually had data (`coverage`), and per-source provenance and staleness (`meta`). A component with no data contributes a neutral 0 and the other weights are not rescaled to cover for it; `coverage` says which data families had data, and a leg withheld for licence reasons is null in its score, has weight 0 and is named in `withheld_sources`. This is an aggregation and transparency endpoint: it does not predict price, and `confidence` is not a probability. Free tier: BTC, ETH, SOL, XAU, XAG; no added delay; these fields are stripped from the body: deriv_score, details, onchain_score, reasons, whale_score.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `direction` | query | no | Trade direction to confirm. One of: `long`, `short`. Default `long`. |
| `account_size` | query | no | Account size in USD for Kelly position sizing (Pro only). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `action` | string | The verdict. NO_DATA_SKIP is deliberately distinct from VETO_SKIP: it means nothing was measured, not that the data was negative. |
| `adjustments` | object | Every post-scoring modifier, signed. base_composite plus these gives composite, so a verdict is never a black box. |
| `ai_analysis` | object | LLM summary of the SAME numbers (regime, conflicts, risk factors) plus provider (`local` or `hosted`: where it ran), ai_backend and generation_time_ms. It has no extra information; if it disagrees with `composite`, `composite` is the machine-readable answer. |
| `base_composite` | number | Weighted factor sum BEFORE the `adjustments` are applied. Absent on the blacklist-VETO and NO_DATA branches. |
| `composite` | number | Final score for the requested direction after weighting and adjustments. Unitless: not a price target and not an expected return. |
| `confidence` | string | Bucketed composite. NOT a probability and NOT calibrated to any hit rate. |
| `coverage` | object | Which data families actually returned something. false means UNKNOWN — that component had no data and contributes a neutral 0; the other weights are not rescaled to cover for it. A leg withheld for licence reasons is null in its score, has weight 0 and is named in `withheld_sources`. |
| `decision` | string | Canonical coarse enum derived from confidence/action. ABSTAIN covers both LOW confidence and NO_DATA. Prefer this for branching. |
| `deriv_score` | number | Component score in [-1, +1], oriented to the requested direction: positive supports it. |
| `details` | object | Raw inputs behind each component (derivatives, onchain, whale, x_sentiment) so the score can be recomputed. Stripped on tiers whose plans.json strip_fields lists it. |
| `direction` | string | Echo of the direction that was scored. |
| `factors` | object | Per-component line items of the composite. Empty object {} on the NO_DATA branch. |
| `meta` | object | Proof-carrying provenance for the verdict. |
| `model_version` | string | Scoring model version. Scores are not comparable across a change of this value. |
| `multi_timeframe` | object | The same component scores re-weighted for short / medium / long horizons, each with composite, confidence, weights_used and timeframe_label. Horizons are tier-gated. A leg withheld for licence reasons (null score) has weight 0 in every horizon and the other weights are not rescaled to cover for it; while a leg is withheld a horizon reads HIGH only when the headline `confidence` is HIGH, otherwise MEDIUM at most. |
| `onchain_score` | number | Component score in [-1, +1], oriented to the requested direction: positive supports it. |
| `operator_position_disclosure` | object | Whether the operator's automated trading accounts hold a position in the asset (MiCA Art. 91(2)(c) conflict disclosure). A historical signal carries the value recorded when it was published; one with no record is 'unavailable'. Unavailable value: {"status": "unavailable", "side": null, "as_of": null, "source_age_s": null, "text": "Operator position data is unavailable right now; the operator's automated trading accounts may hold a position in this asset."}. |
| `personalized` | object | The caller's saved risk tolerance and base trade size turned into a suggested USD figure. Carries its own disclaimer field. Arithmetic on caller-supplied numbers, not advice. |
| `reasons` | array | One human-readable line per contributing observation and per non-zero adjustment. Stripped on tiers whose plans.json strip_fields lists it. |
| `size_mult` | number | Suggested fraction of the caller's normal position size for this confidence bucket, after a liquidation-distance reduction. Not risk management: it knows nothing about the caller's account. |
| `source` | string | Caller-supplied ?source= tag, echoed back. |
| `symbol` | string | Echo of the requested base symbol. |
| `ts` | integer | Unix second the verdict was computed. |
| `unsupported` | boolean | true only when the symbol is outside the tracked universe (no derivatives AND no whale data). Then action=NO_DATA_SKIP and every *_score is a zero meaning 'not measured'. |
| `weights` | object | The weight set actually used for this call. |
| `weights_mode` | string | Which weight set was selected, e.g. free, full, free_x, full_x. |
| `whale_score` | number | Component score in [-1, +1], oriented to the requested direction: positive supports it. |
| `x_score` | number | Always 0. The X/social sentiment input is switched off and its weight is renormalised to 0, so it cannot move the composite. Kept in the payload for client compatibility. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm"
```

### `GET /v1/disclosures/operator-positions`

**Operator position disclosure** — keyless

Whether the operator's automated trading accounts currently hold a position in each asset -- the conflict-of-interest disclosure MiCA Art. 91(2)(c) requires next to every published signal, served by the SAME provider as the `operator_position_disclosure` field on /v1/confirm, /v1/signals/recent, /v1/signals/{signal_id}/outcome, /v1/performance, /v1/performance/export, /v1/alerts/regime-flips, /v1/signals/capitulation (+ walkforward), /v1/shadow-gate/decisions, /v1/analysis, /v1/projection (+ screener), /v1/screener (+ rankings, symbol) and /v1/rankings. Read from the bots' own stored state, never from an exchange. `not_holding` is asserted only from position data at most 900 s old; stale, missing or unreadable data answers `unavailable`, whose text says the accounts MAY hold a position. Keys of `disclosures` are normalised base symbols (BTCUSDT -> BTC), in request order. 400 on a malformed `symbols`; 503 if the provider path fails.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbols` | query | yes | Comma-separated symbols, at most 50 (e.g. BTC,ETH,SOLUSDT). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `disclosures` | object |  |
| `generated_at` | string | UTC, YYYY-MM-DDTHH:MM:SSZ. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/disclosures/operator-positions"
```

### `GET /v1/signals/analytics/{view}`

**Signal analytics view** — keyless

Read-only aggregate views over the same signal log the published win-rate uses: edge, calibration, rolling, distribution, components, gates, confluence, leaderboard. All in-sample unless the view says otherwise.

| Parameter | In | Required | Description |
|---|---|---|---|
| `view` | path | yes | Analytics view name (edge, calibration, rolling, distribution, components, gates, confluence, leaderboard). |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/analytics/{view}"
```

### `GET /v1/signals/capitulation`

**Capitulation state** — keyless

Current capitulation reading per symbol from the liquidation and funding panel. Every `triggered[]` row carries `operator_position_disclosure`, dated when the response is served.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/capitulation"
```

### `GET /v1/signals/capitulation/backtest`

**Capitulation backtest** — keyless

In-sample backtest of the capitulation reading. Published with its own disclaimer: in-sample results are not evidence of forward edge.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/capitulation/backtest"
```

### `GET /v1/signals/capitulation/walkforward`

**Capitulation walk-forward** — keyless

Walk-forward (out-of-sample) evaluation of the capitulation reading. Every `trades[]` paper trade carries `operator_position_disclosure` as recorded when it was captured (`unavailable` for a backfill reconstruction or a trade captured before the field existed).

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/capitulation/walkforward"
```

### `GET /v1/signals/performance`

**Signal performance** — keyless

Aggregate outcome statistics for tracked signals (signal_tracker): hit rates per horizon.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Lookback window (1-365). Default `30`. |
| `type` | query | no | Filter by signal type (e.g. smart_money_confirm, regime_flip). |
| `symbol` | query | no | Filter by symbol. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `days` | integer |  |
| `excluded_signals` | integer |  |
| `horizons` | object |  |
| `licence_exclusion` | object |  |
| `signal_type` | — |  |
| `symbol` | — |  |
| `total_signals` | integer |  |
| `type_breakdown` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/performance"
```

### `GET /v1/signals/recent`

**Recent signals feed** — keyless

Recent published signals with optional resolved outcomes and live unrealized marks. Supports incremental delta polling via since_id and open_only; every response carries max_id as the next cursor.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max signals (1-2000). Default `50`. |
| `type` | query | no | Filter by signal type. |
| `outcomes` | query | no | Set to 1/true to include per-horizon outcomes. One of: `1`, `true`, `yes`. |
| `unrealized` | query | no | Set to 1/true to include live unrealized marks for open signals. One of: `1`, `true`, `yes`. |
| `open_only` | query | no | Set to 1/true to return only unresolved live-window signals. One of: `1`, `true`, `yes`. |
| `since_id` | query | no | Only signals newer than this id (delta polling cursor). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `max_id` | integer |  |
| `next_url` | string |  |
| `server_ts` | integer |  |
| `signals` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/recent"
```

### `GET /v1/signals/{signal_id}/outcome`

**Signal outcome** — keyless

The resolved 4h/12h/24h/72h outcome of one logged signal, with the `operator_position_disclosure` recorded when it was published.

| Parameter | In | Required | Description |
|---|---|---|---|
| `signal_id` | path | yes | Numeric signal id from /v1/signals/recent. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/{signal_id}/outcome"
```

## Smart-money cohorts

### `GET /v1/smart-money/activity`

**Wallet activity** — key required — Trader (3,000 calls/day)

What wallets did in an interval: open, add, reduce, close, flip, deposit, withdraw and transfers on Hyperliquid, or swap and transfer legs on bsc/avalanche read from our own node's scan (no cohorts; swap legs carry no direction because the ingest does not record one). bsc/avalanche answer 451 withheld_for_licence until the rights registry clears them; the shape is what they serve once cleared. A price move is never an activity event. The span is at most 7 days; the lookback is per plan (`features.sm_history_days`) and a clamp is reported in `lookback_clamped_by_tier`. `execution_context` separates observations from labelled estimates; on bsc/avalanche the honeypot probe is an estimate that does not execute the token's transfer hooks, and the Etherscan-derived contract source scan is withheld. No safety score, rating or recommendation is ever returned. Per-address cohort tags would list a cohort's members, so they are served only when membership is published; otherwise `cohorts` is null with `cohorts_state: "withheld"`, and a `cohort` filter answers 451 `withheld` with reason `member_lists`. An address on the privacy suppression list is never returned (on bsc/avalanche, neither as the wallet nor as the counterparty); if the list cannot be read the request answers 503.

| Parameter | In | Required | Description |
|---|---|---|---|
| `from` | query | no | Window start, unix seconds (default: to - 24h). |
| `to` | query | no | Window end, unix seconds (default: now). |
| `chain` | query | no | Venue. One of: `hyperliquid`, `bsc`, `avalanche`. Default `hyperliquid`. |
| `cohort` | query | no | Comma-separated cohort ids (hyperliquid only). Answers 451 `withheld` with reason `member_lists` unless membership is published. |
| `symbol` | query | no | Hyperliquid coin, matched case-insensitively (e.g. BTC, kPEPE). |
| `kind` | query | no | Comma-separated kinds. hyperliquid: open, add, reduce, close, flip, transfer_in, transfer_out, deposit, withdraw. bsc/avalanche: swap, transfer_in, transfer_out. |
| `min_usd` | query | no | Minimum notional USD. |
| `cursor` | query | no | `next_cursor` from the previous page (event_ts_seq). |
| `limit` | query | no | Events per page. Default `100`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `chain` | string |  |
| `cohort_labels` | object | cohort id -> label, for the cohorts the events carry (empty while tags are withheld) |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `events` | array |  |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `from` | integer |  |
| `from_requested` | integer |  |
| `history_days_limit` | integer |  |
| `licence_class` | string |  |
| `lookback_clamped_by_tier` | boolean |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `next_cursor` | string | null on the last page |
| `note` | string |  |
| `rights` | object |  |
| `scan` | object |  |
| `scope` | string |  |
| `to` | integer |  |
| `universe` | string |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/activity"
```

### `GET /v1/smart-money/activity/summary`

**Wallet activity summary** — key required — Trader (3,000 calls/day)

Per symbol: counts and USD of opens, adds, reduces, closes and flips, the price-neutral net_position_change_usd, and mark_to_market_change_usd reported beside it (never summed into it). The everyone rows are `all_observed`, which counts every wallet with an event (`cohort=all_observed` selects it), and `all_tracked`; they are served for any window. The row of a membership cohort is added only when cohort disclosure is enabled (see `disclosure_control`) and, under disclosure control, only for one complete UTC day (`window=1d`, or from/to on 00:00 UTC one day apart). A `cohort` filter other than `all_observed` answers 451 `withheld` with reason `member_lists` unless membership is published. USDC ledger transfers are listed by /activity, not summed here. Served on the hour grid; when `window` is not given it is `1d`, the last complete UTC day. Replaces the retired /flows design.

| Parameter | In | Required | Description |
|---|---|---|---|
| `window` | query | no | 1d = the last complete UTC day (the only window that carries membership-cohort cells under disclosure control); 1h/4h/24h/7d = the last 1, 4, 24 or 168 complete hours. One of: `1d`, `1h`, `4h`, `24h`, `7d`. Default `1d`. |
| `from` | query | no | Explicit start, a whole hour (multiple of 3600; with `to`, instead of window). The window is [from, to). |
| `to` | query | no | Explicit end, a whole hour, at least one hour after `from`; clamped to the last complete hour. |
| `cohort` | query | no | Comma-separated cohort ids from /v1/smart-money/cohorts. |
| `symbol` | query | no | Hyperliquid coin, matched case-insensitively (e.g. BTC, kPEPE). |
| `limit` | query | no | Symbols to return. Default `50`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `disclosure_control` | object | States the disclosure setting this response was served under. Present unless membership is published (where it is published the field is absent and the cells are exact). `mode` is `withheld`: only the everyone rows (`all_observed`, `all_tracked`) are served and no membership-cohort aggregate is (a week of controlled cells joined in one MILP was measured to rebuild the members). `mode` is `controlled` (an operator decision): membership-cohort cells are served under the disclosure control -- one UTC day, at least 10 distinct addresses inside a cell and 10 outside it in its row, per cell and per sub-aggregate; counts rounded to 5 and USD to 2 significant figures; a quantity that would decide one address's membership withheld; account-value tiers all or none. Not differential privacy. |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `from` | integer |  |
| `licence_class` | string |  |
| `lookback_clamped_by_tier` | boolean |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `method` | string |  |
| `note` | string |  |
| `rights` | object |  |
| `scope` | string |  |
| `symbols` | array |  |
| `to` | integer |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `venue` | string |  |
| `versions` | object |  |
| `window` | string | the window= asked for; null with from/to |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/activity/summary"
```

### `GET /v1/smart-money/cohorts`

**Smart-money cohorts** — keyless

Every cohort with its published rule, formation date, membership counts and validation status. Skill cohorts carry the label "past performers (unvalidated)" until their pre-registered out-of-sample study passes; size, vault and seed cohorts are labelled "descriptive". Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `cohorts` | array |  |
| `coverage` | object | The complete-sweep snapshot's own coverage, exactly as recorded; before the first snapshot {state: missing, missing_reason: no_snapshot}. |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `prereg_sha256` | string |  |
| `rights` | object |  |
| `scope` | string |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/smart-money/cohorts"
```

### `GET /v1/smart-money/positioning`

**Cohort positioning** — key required — Trader (3,000 calls/day)

What the tracked accounts hold on Hyperliquid perps, per symbol, from a complete sweep of the tracked accounts: long/short/net/gross USD, counts, observed addresses and an independent-participant estimate. The everyone row (`all_tracked`) is always served. The row of a membership cohort is added only when cohort disclosure is enabled (see `disclosure_control`); otherwise the response carries the everyone row alone, and a `cohort` filter naming a membership cohort that is not served returns no rows. Under disclosure control a membership cohort's cells come from the newest UTC-day snapshot (`cohort_snapshot_ts`) and are rounded, a cell or side under the floor is omitted or withheld (`withheld_fields`), and concentration and divergence are withheld; where membership is published the cells are exact. `include` adds concentration and divergence to the exact rows. Every cell that is served carries `state` (observed|missing|stale); a measured zero is observed 0, a missing value is null with a missing_reason. Descriptive, not a forecast.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Hyperliquid coin, matched case-insensitively (e.g. BTC, kPEPE). |
| `cohort` | query | no | Comma-separated cohort ids from /v1/smart-money/cohorts. |
| `include` | query | no | Comma-separated: concentration, divergence. |
| `min_gross_usd` | query | no | Keep symbols where a selected cohort holds at least this gross USD. Default `0`. |
| `limit` | query | no | Symbols to return. Default `50`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `cohort_snapshot_ts` | integer | the UTC-day snapshot the cohort cells come from |
| `coverage` | object | The complete-sweep snapshot's own coverage, exactly as recorded; before the first snapshot {state: missing, missing_reason: no_snapshot}. |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `disclosure_control` | object | States the disclosure setting this response was served under. Present unless membership is published (where it is published the field is absent and the cells are exact). `mode` is `withheld`: only the everyone rows (`all_observed`, `all_tracked`) are served and no membership-cohort aggregate is (a week of controlled cells joined in one MILP was measured to rebuild the members). `mode` is `controlled` (an operator decision): membership-cohort cells are served under the disclosure control -- one UTC day, at least 10 distinct addresses inside a cell and 10 outside it in its row, per cell and per sub-aggregate; counts rounded to 5 and USD to 2 significant figures; a quantity that would decide one address's membership withheld; account-value tiers all or none. Not differential privacy. |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `rights` | object |  |
| `scope` | string |  |
| `snapshot_ts` | integer |  |
| `symbols` | array |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `validation_by_cohort` | object |  |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/positioning"
```

### `GET /v1/smart-money/positioning/history`

**Cohort positioning history** — key required — Trader (3,000 calls/day)

Stored 4-hourly positioning points for one symbol and one cohort. Depth is per plan (`features.sm_history_days` in /v1/plans). A request deeper than the plan allows is clamped and says so in `truncated_by_tier`. The everyone cohort (`all_tracked`) is served as stored. A membership cohort is served only when cohort disclosure is enabled (see `disclosure_control`): one disclosure-controlled point per UTC day, and a side whose change since the last served point would decide one address's membership is withheld. Otherwise the request answers 451 `withheld` with reason `cohort_aggregates`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | yes | Hyperliquid coin (required). |
| `cohort` | query | yes | One cohort id (required). A membership cohort answers 451 `withheld` unless cohort disclosure is enabled. |
| `days` | query | no | Days of history, clamped to the plan. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `cohort_id` | string |  |
| `cohort_label` | string |  |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `days` | integer |  |
| `days_requested` | integer |  |
| `disclosure_control` | object | States the disclosure setting this response was served under. Present unless membership is published (where it is published the field is absent and the cells are exact). `mode` is `withheld`: only the everyone rows (`all_observed`, `all_tracked`) are served and no membership-cohort aggregate is (a week of controlled cells joined in one MILP was measured to rebuild the members). `mode` is `controlled` (an operator decision): membership-cohort cells are served under the disclosure control -- one UTC day, at least 10 distinct addresses inside a cell and 10 outside it in its row, per cell and per sub-aggregate; counts rounded to 5 and USD to 2 significant figures; a quantity that would decide one address's membership withheld; account-value tiers all or none. Not differential privacy. |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `history_days_limit` | integer |  |
| `history_start_ts` | integer |  |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `points` | array |  |
| `rights` | object |  |
| `scope` | string |  |
| `symbol` | string |  |
| `truncated_by_tier` | boolean |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `validation` | object | The cohort's validation object. |
| `venue` | string |  |
| `versions` | object |  |
| `window_start_ts` | integer |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/positioning/history"
```

### `GET /v1/smart-money/quality/{address}`

**Wallet quality profile** — key required — Trader (3,000 calls/day)

The wallet's own record: accounting, risk, evidence and specialization reconstructed from its own Hyperliquid fills, funding and ledger updates, labelled "performance on the observed venue" (spot, other perp dexes and other venues are not observed). No display names or off-chain identity. An address on the privacy suppression list returns only {address, status: "suppressed"}. Its cohort memberships and the rank inputs behind them (`cohorts`, `cohort_history`, `selection_inputs.rule_scores`) are served only when membership is published; otherwise they are withheld: null, with `cohorts_state: "withheld"`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Hyperliquid account address (0x + 40 hex). |
| `as_of` | query | no | An instant (unix seconds, not in the future): the profile from the formation in effect then (the newest at or before it), named in as_of_formation_ts; default the latest. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `accounting` | object |  |
| `address` | string |  |
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `as_of_formation_ts` | integer |  |
| `basis` | string |  |
| `cohort_history` | array | null while member tags are withheld |
| `cohorts` | array | null while member tags are withheld |
| `cohorts_missing_reason` | string |  |
| `cohorts_state` | string | present when cohorts is withheld |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `evidence` | object |  |
| `evidence_grade` | string |  |
| `exclusion_reason` | string |  |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `independence` | object |  |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `rights` | object |  |
| `risk` | object |  |
| `scope` | string |  |
| `selection_inputs` | object | rank inputs; rule_scores null while member tags are withheld |
| `specialization` | object |  |
| `status` | string |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-money/quality/{address}"
```

### `GET /v1/smart-money/validation`

**Cohort validation ledger** — keyless

The pre-registration (sha256, frozen date) and every study window, aggregate and decision, failures included. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer | When the response was assembled -- never the data time (see `updated`, `freshness`). |
| `basis` | string |  |
| `cohort_status` | object |  |
| `data_mode` | string | live or backfilled; null where no capture backs the body (e.g. /validation, which is derived, before its first run). |
| `freshness` | object | Computed when the response is SERVED, not when it was cached: a last-good copy older than stale_after_s reads `stale`. |
| `licence_class` | string |  |
| `meta` | object | Read from `freshness` alone: no measured source timestamp -> state unknown, stale true. |
| `note` | string |  |
| `prereg` | object |  |
| `published_failures` | array |  |
| `rights` | object |  |
| `scope` | string |  |
| `studies` | array |  |
| `updated` | integer | The datum time (freshness.source_timestamp); absent when nothing measured dates the body. |
| `venue` | string |  |
| `versions` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/smart-money/validation"
```

## Strategies

### `GET /v1/strategies/active`

**Active strategy positions** — keyless

Currently open positions for a strategy account.

| Parameter | In | Required | Description |
|---|---|---|---|
| `account` | query | no | Strategy account id (1-10). Defaults to 1; out-of-range values fall back to 1. Default `1`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `positions` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/active"
```

### `GET /v1/strategies/equity`

**Strategy equity curve** — keyless

Chronological equity curve for a strategy account. Each point carries equity, pnl, cumulative_pnl and drawdown_pct (chart-ready); deposit/withdrawal adjustments appear as separate points.

| Parameter | In | Required | Description |
|---|---|---|---|
| `account` | query | no | Strategy account id (1-10). Defaults to 1; out-of-range values fall back to 1. Default `1`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `account` | integer |  |
| `current_equity` | number |  |
| `curve` | array |  |
| `initial_equity` | number |  |
| `max_drawdown_percent` | number |  |
| `total_adjustments` | number |  |
| `total_pnl_usdt` | number |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/equity"
```

### `GET /v1/strategies/signals`

**Strategy signal-filter stats** — keyless

Signal-type statistics across strategy accounts: per-reason counts, wins/losses, win rate, average pnl.

Response fields:

| Field | Type | Description |
|---|---|---|
| `signal_types` | object |  |
| `total_signals` | integer |  |
| `unique_signal_types` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/signals"
```

### `GET /v1/strategies/stats`

**Strategy statistics** — keyless

Aggregate performance for a strategy account: win rate, profit factor, max drawdown (portfolio + per-trade), equity, per-exit-reason and per-direction breakdowns.

| Parameter | In | Required | Description |
|---|---|---|---|
| `account` | query | no | Strategy account id (1-10). Defaults to 1; out-of-range values fall back to 1. Default `1`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `account` | integer |  |
| `current_equity` | number |  |
| `max_drawdown_portfolio` | number |  |
| `profit_factor` | number |  |
| `total_pnl_usdt` | number |  |
| `total_trades` | integer |  |
| `win_rate` | number |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/stats"
```

### `GET /v1/strategies/symbols`

**Per-symbol strategy stats** — keyless

Per-symbol performance breakdown for a strategy account.

| Parameter | In | Required | Description |
|---|---|---|---|
| `account` | query | no | Strategy account id (1-10). Defaults to 1; out-of-range values fall back to 1. Default `1`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/symbols"
```

### `GET /v1/strategies/trades`

**Strategy trades** — keyless

Closed trades for a live strategy account (newest first).

| Parameter | In | Required | Description |
|---|---|---|---|
| `account` | query | no | Strategy account id (1-10). Defaults to 1; out-of-range values fall back to 1. Default `1`. |
| `limit` | query | no | Max trades, capped at 500. Default `100`. |
| `offset` | query | no | Pagination offset. Default `0`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/strategies/trades"
```

## Technicals

### `GET /v1/ta/history`

**Technical history** — key required — Pro (15,000 calls/day)

Historical indicator series for one symbol/interval.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `interval` | query | no | Candle interval. Default `1h`. |
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/ta/history"
```

### `GET /v1/ta/screener`

**Technical screener** — keyless

Technical-indicator screener across the symbol universe.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/ta/screener"
```

### `GET /v1/ta/technicals`

**Technical indicators** — keyless

Indicator set (moving averages, RSI, MACD, ATR) for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/ta/technicals"
```

## Top traders

### `GET /v1/top-traders/history`

**One top trader's closed episodes in a window** — key required — Pro (15,000 calls/day)

The closed position episodes behind a trader's win rate in one window, newest first: coin, side, open and close time, size, entry and exit VWAP, Hyperliquid closedPnl, fees, net PnL and the outcome, with `counted` false and `excluded_reason` for episodes left out of the rate. Read from the episodes the fills job stored with the counts; nothing is listed for a window not proven observed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `wallet` | query | yes | The trader's address (0x + 40 hex). |
| `window` | query | no | Window. One of: `day`, `week`, `month`, `allTime`. Default `month`. |
| `limit` | query | no | Max episodes returned. Default `100`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/history"
```

### `GET /v1/top-traders/leaderboard`

**Hyperliquid leaderboard, with each trader's own win rate** — key required — Pro (15,000 calls/day)

The top N accounts of Hyperliquid's leaderboard for one window (day, week, month or allTime), ranked by that window's PnL. Each row carries `hl_leaderboard`: pnl, roi and vlm for all four windows plus account_value, exactly as Hyperliquid publishes them in its daily snapshot, with provenance in `snapshot` (source URL, our fetch time, Hyperliquid's Last-Modified time of the file, as_of, sha256). It also carries `win_rate_stats`: closed-episode wins / closed episodes reconstructed from the trader's own fills, net of fees, funding not included, with n, the window, coverage and the excluded episodes by reason; `state` partial_coverage (and no number, with `partial_reason`) when not all of the window's fills were observed: coverage is proven, never assumed, by requiring the notional of the held fills to reach Hyperliquid's own published vlm for the window (`volume_check`), and it fails for an account whose older fills Hyperliquid no longer serves, for older history the job skipped, or for fills Hyperliquid omitted. It also carries `closing_order_share` (version tt-closeshare-2), a second figure from the same fills, labelled "share of closing orders in profit — an order is counted once however many fills it executed; this is not a per-trade win rate": of the trader's closing orders in the window (an order with at least one fill that reduces or closes a position; the unit is an order, not a fill, and one order can execute as thousands of fills), how many have closedPnl minus fee, summed over their closing fills, above 0, as a count of orders (the sample size), a share and a notional-weighted share, net of the fees of the closing fills only and not the opening fee, funding not included; the fill counts are secondary. It is not the strict win rate: a position closed by three orders counts three times, and the partial closes of a position that is still open count too. It is served only where the same volume proof holds (otherwise `state` partial_coverage and no number, with the same `partial_reason`, or `fills_missing_order_id` when a closing fill has no order id); a proven window with no closing order is `no_closing_orders` with null shares, never 0%; a snapshot processed before the metric existed, or under a different version of it, is `not_computed`. Hyperliquid's own anomalies are flagged, not repaired (`hl_leaderboard_anomalies`). Vaults are labelled `is_vault`. Addresses on our privacy suppression list are omitted (`omitted_privacy`). Descriptive past performance on one venue: not a forecast, not a ranking of skill, not a recommendation or signal.

| Parameter | In | Required | Description |
|---|---|---|---|
| `window` | query | no | Which leaderboard window ranks the rows. One of: `day`, `week`, `month`, `allTime`. Default `month`. |
| `limit` | query | no | Rows returned (capped at the job's top N, default 25). Default `100`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/leaderboard"
```

### `GET /v1/top-traders/performance`

**One top trader: leaderboard figures and win rates, all windows** — key required — Pro (15,000 calls/day)

For one address in the top N of any window of the served snapshot: its rank per window, Hyperliquid's published pnl/roi/vlm for day, week, month and allTime, a `win_rate_stats` block per window from its own fills, and a `closing_order_share` block per window: the "share of closing orders in profit — an order is counted once however many fills it executed; this is not a per-trade win rate" (version tt-closeshare-2; the unit is an order, not a fill, and one order can execute as thousands of fills), a different figure from the strict win rate with its own counts and states. An address outside the top N gets status not_in_top_traders and no figures; a suppressed address gets status suppressed.

| Parameter | In | Required | Description |
|---|---|---|---|
| `wallet` | query | yes | The trader's address (0x + 40 hex). |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/performance"
```

### `GET /v1/top-traders/summary`

**Top-traders snapshot, job coverage and definitions** — key required — Pro (15,000 calls/day)

The served leaderboard snapshot and its provenance, the state of the fills job that computes the win rates (targets, computed, pending, failed, the share of the single-IP Hyperliquid budget it uses), the count of win-rate states per window (`win_rate_states`), the count of `closing_order_share` states per window (`closing_order_states`), and the full definitions of the leaderboard fields, of the win rate and of the share of closing orders in profit (`closing_order_share_definition`).

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/summary"
```

## Trading tools

### `GET /v1/funding-arb`

**Funding arbitrage scanner** — key required — Trader (3,000 calls/day)

Cross-exchange funding-rate arbitrage opportunities. Trader tier: top-1 opportunity without spread history; Pro tier: full list.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Filter opportunities by symbol. |
| `min_spread` | query | no | Minimum funding spread. Default `0.01`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `min_spread_filter` | number |  |
| `opportunities` | array |  |
| `scanned_symbols` | integer |  |
| `ts` | number |  |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/funding-arb"
```

### `GET /v1/kelly`

**Kelly position sizing** — key required — Pro (15,000 calls/day)

Kelly-criterion position sizing from the published (in-sample) hit rate and payoff. Sizing arithmetic, not a forecast.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/kelly"
```

### `GET /v1/smart-stop`

**Smart stop levels** — key required — Trader (3,000 calls/day)

A stop price WITH the basis it was derived from. `stop_basis` records whether the recommendation came from a modelled liquidation cluster or from nothing but the caller's own `risk_pct` with no cluster read at all — two stops that look identical on the wire and mean completely different things. Read it before sizing anything.

The cluster it may be aware of is the MODELLED ladder from /v1/liquidations, not an observed order book, and it carries that endpoint's caveats.

TIERS. Trader receives 16 of the 22 fields, tagged per field below. Pro additionally receives `stops`, `stop_detail`, `avoid_zones`, `take_profit_suggestions`, `take_profit_basis`, `error`. Trader alone receives `recommended_stop`, `recommended_stop_detail`, `withheld`, `withheld_reason` — `recommended_stop` is the single stop lifted out of the Pro `stops` dict, and `recommended_stop_detail` is its slice of `stop_detail`. Whatever a plan removed is named per response in `withheld` (`withheld_reason: "trader_plan"`), and the qualifier fields for the stop that IS returned are never removed.

Every type below was resolved from the expression that fills the field; where none could be, the property carries no `type` and says so, rather than a plausible guess a generated client would enforce.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `direction` | query | no | Position direction. One of: `long`, `short`. Default `long`. |
| `entry_price` | query | no | Entry price; omit to use current price. |
| `risk_pct` | query | no | Risk percentage of account. Default `2.0`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `avoid_zones` | array | [PRO/ENTERPRISE ONLY] The liquidation clusters the stops were placed around. |
| `current_price` | number | [Trader and Pro] The daemon mark at computation time, or null when it could not be read. It is never the entry price wearing the mark's name. |
| `direction` | string | [Trader and Pro] Position direction the stop was placed for: long or short. |
| `entry_price` | number | [Trader and Pro] The entry the stop distance is measured from. null when none was supplied and no daemon price was readable — read `entry_price_source` before treating it as the caller's own number. |
| `entry_price_source` | string | [Trader and Pro] Where `entry_price` came from: 'caller' (you supplied it), 'daemon_snapshot' (inferred from the mark), or 'none'. |
| `error` | string | [PRO/ENTERPRISE ONLY] Set only on the degraded response where no entry price could be determined at all. NOTE: the Trader reshape does not forward it, so on that plan the same condition is readable from `stop_basis.unavailable_reason` instead. |
| `liq_cascade_risk` | — | [Trader and Pro] The estimator's cascade bucket for this symbol, or its word for an absence. It is not smoothed into a reassuring value when unknown. NO JSON TYPE IS PUBLISHED for this field: no type could be derived from the source expression that fills it, and a guessed type in a schema that clients generate against is worse than a missing one. Unstated is not permissive — treat the shape as unverified. |
| `price_reference` | number | [Trader and Pro] The price the liquidation model was actually run against. |
| `price_reference_source` | string | [Trader and Pro] 'daemon_snapshot' when the mark was readable, 'caller_entry_price' when it was not and your entry stood in for it. The second case is a stop measured against your own input, not against the market. |
| `recommended_stop` | number | [TRADER ONLY] The one stop price on this plan. null when no stop could be placed. Read `stop_basis.status` before sizing: an identical number means completely different things depending on it. |
| `recommended_stop_detail` | object | [TRADER ONLY] Provenance of THIS stop only: which cluster informed it, how far away it is, or the note saying no cluster did. The other labels' detail is in `stop_detail`. |
| `risk_pct_reference` | object | [Trader and Pro] The risk_pct arithmetic, LABELLED as arithmetic, offered only when no cluster informed the stops. null otherwise. It is not a recommendation. |
| `risk_pct_requested` | number | [Trader and Pro] The risk_pct the request asked for, echoed back. |
| `stop_basis` | object | [Trader and Pro] Whether the stop came from a measured liquidation cluster, from the caller's own risk_pct with no cluster read, or from nothing at all. Carries status, explanation, unavailable_reason, liquidation_data ('read' vs 'unavailable'), liquidation_error, bands_status and the level/cluster counts. This is the field to branch on. |
| `stop_detail` | object | [PRO/ENTERPRISE ONLY] Per-label provenance for all three stops, same shape as `recommended_stop_detail`. |
| `stops` | object | [PRO/ENTERPRISE ONLY] The full tight / recommended / wide dict. All three are null when `stop_basis.status` reports the analysis could not be performed. |
| `symbol` | string | [Trader and Pro] Base symbol this stop was computed for. |
| `take_profit_basis` | string | [PRO/ENTERPRISE ONLY] What the take-profit ladder was measured against, or null when there was nothing to measure. An all-null ladder with no basis would leave you guessing between 'no stop' and 'no TP model'. |
| `take_profit_suggestions` | object | [PRO/ENTERPRISE ONLY] Reward/risk ladder keyed by label. Every value is null unless the recommended stop came from a measured cluster — there is no measured risk to build a ladder on otherwise, and the ratios would only re-express your own risk_pct. |
| `ts` | integer | [Trader and Pro] Unix timestamp the stop was computed. |
| `withheld` | array | [TRADER ONLY] Machine-readable list of what THIS response had removed by plan. Vocabulary: `avoid_zones`, `stops.tight_and_wide`, `take_profit_suggestions`. Computed per response, so a response the model left empty anyway reports no boundary. |
| `withheld_reason` | string | [TRADER ONLY] Why those entries were removed. 'trader_plan' means the plan removed them; an absent field means nothing was. This is how a consumer separates 'not in your plan' from 'the server had nothing', which a missing key cannot express. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/smart-stop"
```

## Volume

### `GET /v1/volume`

**Volume series** — keyless

Per-venue traded volume series on the same timeframe grid as the liquidation heatmap, over the permanently retained archive. Series values are NULLABLE: null means the venue was not measured for that bar, 0 means it was measured and nothing traded. They are not interchangeable and gaps must not be plotted as zero. The response carries a coverage block naming which venues were absent and why.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `timeframe` | query | no | Bar size. Alias: tf. One of: `5m`, `15m`, `30m`, `1h`, `4h`, `1d`. Default `1h`. |
| `window_minutes` | query | no | Lookback in minutes, snapped to the timeframe grid. Alias: window. Defaults to 200 bars; a window asking for more than 1500 points is rejected with 400 rather than silently truncated. |
| `exchanges` | query | no | Comma-separated venues (binance, okx, bybit, bitget, bitmex). Alias: exchange. Omit for all. An unknown venue is a 400, never a silently wider query. |
| `to_ts` | query | no | End of the window as a unix timestamp (default now). Alias: to. Snapped to the timeframe grid. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `coverage` | object |  |
| `series` | object |  |
| `symbol` | string |  |
| `timeframe` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/volume"
```

### `GET /v1/volume/aggregate`

**Aggregate volume series** — keyless

Volume summed across the selected venues, on the same grid as /v1/volume. Series values are NULLABLE: null means the venue was not measured for that bar, 0 means it was measured and nothing traded. They are not interchangeable and gaps must not be plotted as zero. The response carries a coverage block naming which venues were absent and why.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `timeframe` | query | no | Bar size. Alias: tf. One of: `5m`, `15m`, `30m`, `1h`, `4h`, `1d`. Default `1h`. |
| `window_minutes` | query | no | Lookback in minutes, snapped to the timeframe grid. Alias: window. Defaults to 200 bars; a window asking for more than 1500 points is rejected with 400 rather than silently truncated. |
| `exchanges` | query | no | Comma-separated venues (binance, okx, bybit, bitget, bitmex). Alias: exchange. Omit for all. An unknown venue is a 400, never a silently wider query. |
| `to_ts` | query | no | End of the window as a unix timestamp (default now). Alias: to. Snapped to the timeframe grid. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `coverage` | object |  |
| `series` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/volume/aggregate"
```

### `GET /v1/volume/exchange`

**Single-venue volume series** — keyless

Volume series for exactly one venue. `exchange` is REQUIRED and must name a single venue (binance, okx, bybit, bitget, bitmex); naming none or several is a 400, because quietly widening it would return a different query than the one asked for. Series values are NULLABLE: null means the venue was not measured for that bar, 0 means it was measured and nothing traded. They are not interchangeable and gaps must not be plotted as zero. The response carries a coverage block naming which venues were absent and why.

| Parameter | In | Required | Description |
|---|---|---|---|
| `exchange` | query | yes | Exactly one venue (binance, okx, bybit, bitget, bitmex). One of: `binance`, `okx`, `bybit`, `bitget`, `bitmex`. |
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `timeframe` | query | no | Bar size. Alias: tf. One of: `5m`, `15m`, `30m`, `1h`, `4h`, `1d`. Default `1h`. |
| `window_minutes` | query | no | Lookback in minutes, snapped to the timeframe grid. Alias: window. Defaults to 200 bars; a window asking for more than 1500 points is rejected with 400 rather than silently truncated. |
| `to_ts` | query | no | End of the window as a unix timestamp (default now). Alias: to. Snapped to the timeframe grid. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `exchange` | string |  |
| `series` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/volume/exchange"
```

### `GET /v1/volume/health`

**Volume collector health** — keyless

Collector liveness per venue: last bar written, lag, and whether the archive is currently being appended to. Use this to tell an outage apart from a quiet market before drawing conclusions from a flat series.

Response fields:

| Field | Type | Description |
|---|---|---|
| `status` | string |  |
| `venues` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/volume/health"
```

### `GET /v1/volume/symbols`

**Symbols held in the volume archive** — keyless

Every symbol the volume archive actually holds bars for. An empty series from /v1/volume plus a symbol listed here means the window is empty; a symbol absent here was never collected. A 503 from this endpoint is a READ FAILURE and must not be read as 'no volume recorded'.

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `symbols` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/volume/symbols"
```

## Whales

### `GET /v1/wallet/{address}/positions`

**Wallet positions** — keyless

Open positions for one wallet. Public even for authenticated callers — there is no separate gated handler for this path.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/wallet/{address}/positions"
```

### `GET /v1/wallet/{addr}/profile`

**Whale wallet profile** — keyless

Cross-venue profile for a tracked Hyperliquid whale, built from live position snapshots: current open positions, unrealized-PnL / exposure / position-count time series, an OPEN/CLOSE/FLIP activity timeline (diffed from consecutive snapshots), decoded HL-leaderboard label, and an open-book summary. pnl is HL's own unrealized mark-to-market; value_usd is open notional. Realized P&L per round-trip is unavailable (only open snapshots are seen) and is returned as null. Valid-but-untracked address returns tracked=false; invalid address returns ok=false, error=invalid_address (HTTP 400).

| Parameter | In | Required | Description |
|---|---|---|---|
| `addr` | path | yes | Wallet address. |
| `days` | query | no | Look-back window for series & timeline. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | integer |  |
| `error` | string | Present when ok=false (e.g. invalid_address). |
| `first_seen_ts` | integer |  |
| `hyperliquid` | object |  |
| `latest_snapshot_ts` | integer |  |
| `note` | string | Present when tracked=false. |
| `ok` | boolean |  |
| `tracked` | boolean |  |
| `wallet` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/wallet/{addr}/profile"
```

### `GET /v1/wallets/relationships/stats`

**Wallet-graph statistics** — keyless

Size and density of the wallet co-positioning graph.

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_jaccard` | number |  |
| `computed_at` | integer |  |
| `edges` | integer |  |
| `max_jaccard` | number |  |
| `unique_wallets` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/wallets/relationships/stats"
```

### `GET /v1/wallets/{address}/relationships`

**Wallet relationships** — keyless

Edges in the wallet co-positioning graph for one address (Jaccard similarity over 14 days of positions, rebuilt every 6h).

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |
| `limit` | query | no | Max rows returned. |
| `min_jaccard` | query | no | Minimum Jaccard similarity. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/wallets/{address}/relationships"
```

### `GET /v1/wallets/{address}/scorecard`

**Wallet scorecard** — keyless

Historical scorecard for one whale wallet.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | path | yes | Wallet or contract address. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/wallets/{address}/scorecard"
```

### `GET /v1/whale-consensus`

**Whale consensus** — keyless

Aggregated directional bias per symbol from Hyperliquid whale positions (long/short counts + volume), exchange derivatives (funding rate, long/short ratio) and 24h on-chain whale net flow.

Response fields:

| Field | Type | Description |
|---|---|---|
| `chain_flows` | object |  |
| `consensus` | array |  |
| `count` | integer |  |
| `meta` | object |  |
| `updated` | integer |  |
| `whale_wallets_in_window` | integer |  |
| `whale_window_s` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whale-consensus"
```

### `GET /v1/whale-events`

**Whale events (authenticated)** — key required — Trader (3,000 calls/day)

Full whale-event feed with per-event PnL, leverage and margin detail. Trader gets an aggregate summary only (ignores limit/before_ts/before_id); Pro/Enterprise get this keyset-paginated feed, capped at `limit` events per response with NO exception (including when many events share one `ts`, which is the normal case here, not an edge one). Each response adds `has_more`, `next_before_ts` and `next_before_id` (the ts/id of the last event returned, null once nothing older is left) alongside `limit` and `window_hours`. `count` is the number of events in THIS response, not in the whole window. To page, request with no cursor, then keep requesting with before_ts AND before_id set to the previous response's next_before_ts/next_before_id together while has_more is true. before_ts and before_id must be given TOGETHER or NOT AT ALL -- either one alone -> 400 (a ts-only cursor can skip the untraversed rest of a tie group; an id-only one is meaningless).

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max events per page (Pro/Enterprise feed only). Clamped 1-5000; non-integer -> 400. Default `500`. |
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `before_ts` | query | no | Keyset pagination cursor (Pro/Enterprise feed only). Must be given together with before_id, or not at all -- alone, -> 400. Returns events strictly before the exact (ts, id) pair. Unix-seconds, range 0-10^12; non-integer or out of range -> 400. Pass the previous response's next_before_ts. |
| `before_id` | query | no | Keyset pagination cursor (Pro/Enterprise feed only). Must be given together with before_ts, or not at all -- alone, -> 400. The id of a specific whale_events row. Range 0-2^62; non-integer or out of range -> 400. Pass the previous response's next_before_id. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/whale-events"
```

### `GET /v1/whale-health`

**Whale portfolio health** — keyless

Margin/health readings for the tracked whale wallets.

| Parameter | In | Required | Description |
|---|---|---|---|
| `wallets` | query | no | Comma-separated wallet addresses. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whale-health"
```

### `GET /v1/whales/addresses`

**Tracked whale addresses** — key required — Trader (3,000 calls/day)

The auto-discovered whale wallet universe with discovery metadata.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/whales/addresses"
```

### `GET /v1/whales/crowding`

**Whale crowding & positioning context** — keyless

Combined whale positioning across Hyperliquid + GMX v2 + Jupiter Perps per symbol: gross/net notional, directional skew, wallet & venue counts, concentration (top-3 share + HHI), weighted-average leverage, and liquidation-proximity buckets ($ notional within 5% and 10% of estimated liq price, split long/short). Context, not a directional signal. Non-derivable fields are null (rendered '—'); liq distances are isolated-margin estimates, not exchange-reported. Anonymous callers get the top 10 symbols by gross; Trader+ get the full list.

| Parameter | In | Required | Description |
|---|---|---|---|
| `min_notional` | query | no | Minimum combined gross notional (USD) for a symbol to be included. Default `1000000`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `caveats` | array |  |
| `gated` | boolean | true for anonymous (top-10 only); full list at Trader+. |
| `min_notional` | number |  |
| `n_symbols` | integer |  |
| `ok` | boolean |  |
| `symbols` | array |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/crowding"
```

### `GET /v1/whales/dex-positions`

**On-chain perp positions** — keyless

Open perpetual positions on GMX v2 (Arbitrum/Avalanche) and Jupiter (Solana).

| Parameter | In | Required | Description |
|---|---|---|---|
| `venue` | query | no | Filter by venue. |
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `min_notional` | query | no | Minimum position notional in USD. |
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/dex-positions"
```

### `GET /v1/whales/events`

**Whale events** — keyless

Multi-chain whale transaction events (ETH, BSC, AVAX, Polygon, Arbitrum, Base, Optimism, Solana).

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | no | Filter by chain (e.g. ethereum, bsc, solana). Omit for all chains. |
| `hours` | query | no | Lookback window in hours. Default `24`. |
| `limit` | query | no | Max events, capped at 100. Default `50`. |
| `event_type` | query | no | Filter by event type (e.g. transfer, dex_swap). |
| `offset` | query | no | Pagination offset. Default `0`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `events` | array |  |
| `total` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/events"
```

### `GET /v1/whales/market-makers`

**Market-maker wallets** — keyless

Wallets classified as market makers rather than directional traders.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/market-makers"
```

### `GET /v1/whales/summary`

**Whale activity summary** — keyless

Per-chain whale activity summary (cached 120s).

Response fields:

| Field | Type | Description |
|---|---|---|
| `chains` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/summary"
```

### `GET /v1/whales/universe`

**Whale universe stats** — keyless

Size and composition of the tracked whale universe. Since 2026-10-01 a wallet whose fills could not be read is UNKNOWN, never zero: `fills` counts known / unknown / carried_forward wallets, `qualification` splits qualified / not_qualified / unknown / not_applicable (vaults), and `qualified_traders` counts only wallets whose fills are known, so it is a floor. In `pinned_preview`, `n_trades` and `win_rate` are null when unknown (they read 0 before), next to `fills_known`, `qualification` and `last_fills_ok_ts`.

Response fields:

| Field | Type | Description |
|---|---|---|
| `discovery_sources` | object |  |
| `fills` | object |  |
| `last_discovered` | string |  |
| `pinned_preview` | array |  |
| `qualification` | object |  |
| `qualified_traders` | integer |  |
| `seeded` | integer |  |
| `total` | integer |  |
| `vault_leaders` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/universe"
```

---

Regenerate: `python3 tools/build_public_spec.py`. Verify freshness in CI: `python3 tools/build_public_spec.py --check`.

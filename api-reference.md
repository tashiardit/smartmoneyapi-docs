# SmartMoneyAPI — API Reference

Base URL: `https://api.smartmoneyapi.com`  ·  Auth: `X-API-Key` header  ·  Not financial advice.

Authentication is the `X-API-Key` header on every request (primary). A session
JWT via `Authorization: Bearer …` is accepted as a fallback for browser/dashboard
sessions, but API clients should use `X-API-Key`. Never put your key in a URL.

## GET /v1/confirm — Trade confirmation
A multi-factor **confluence** read for a trade direction — derivatives + on-chain
+ whale positioning (+ optional social) blended into one score. It is decision
support, **not a guaranteed win-rate**. `/confirm` scores symbols with enough
resolved history (currently **BTC, ETH, SOL**); an untracked symbol returns an
explicit `NO_DATA` / `unsupported` result, not a fabricated `LOW`.

**Query params**

| Param | Required | Description |
|---|---|---|
| `symbol` | yes | Asset, e.g. `BTC`, `ETH`, `SOL` |
| `direction` | yes | `long` or `short` |
| `source` | no | Optional label for your signal source (logged) |

**Response fields**

| Field | Type | Meaning |
|---|---|---|
| `composite` | number | Composite confluence score in **[-1.0, 1.0]** (not 0–100, not a win-rate) |
| `base_composite` | number | Composite before post-filter adjustments |
| `confidence` | string | `HIGH`, `MEDIUM`, `LOW`, `VETO`, or `NO_DATA` |
| `action` | string | `CONFIRM_FULL`, `CONFIRM_REDUCED`, `CONFIRM_MINIMAL`, `VETO_SKIP`, `NO_DATA_SKIP` |
| `size_mult` | number | Suggested position-size multiplier (e.g. `0.0`, `0.5`, `1.0`, `1.5`) |
| `unsupported` | bool | `true` when the symbol is outside coverage (paired with `NO_DATA`) |
| `deriv_score` / `onchain_score` / `whale_score` / `x_score` | number | Per-leg sub-scores in [-1, 1] |
| `factors` | object | Transparent per-leg breakdown: `{score, weight, weighted, …}` per leg |
| `adjustments` | object | Signed post-filter tweaks (`agreement`, `trend`, `rsi_1h`, `news_macro`, `momentum`, `time_of_day`, `streak_decay`) |
| `weights` | object | The weight set actually used |
| `coverage` | object | `{derivatives, whale, onchain}` — which legs had real data |
| `weights_mode` | string | e.g. `free`, `full`, `free_x`, `full_x` |
| `reasons` | string[] | Human-readable context (funding, OI, whale flow, on-chain, …) |

The on-chain leg uses **free Coin Metrics** community data (MVRV / exchange
net-flow / active-address) when no Glassnode key is configured — see
`factors.onchain.source`.

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=ETH&direction=short"
```

```json
{
  "symbol": "ETH", "direction": "short",
  "composite": -0.31, "confidence": "MEDIUM", "action": "CONFIRM_REDUCED",
  "size_mult": 0.5,
  "deriv_score": -0.42, "onchain_score": -0.18, "whale_score": -0.30, "x_score": 0.0,
  "factors": {
    "derivatives": { "score": -0.42, "weight": 0.40, "weighted": -0.168 },
    "onchain": { "score": -0.18, "weight": 0.35, "weighted": -0.063, "source": "coinmetrics", "available": true },
    "whale": { "score": -0.30, "weight": 0.25, "weight_effective": 0.25, "staleness_factor": 1.0, "weighted": -0.075 },
    "x_sentiment": { "score": 0.0, "weight": 0.0, "weighted": 0.0 }
  },
  "adjustments": { "agreement": -0.02, "trend": 0.0, "rsi_1h": 0.0, "news_macro": 0.0, "momentum": 0.0, "time_of_day": 0.0, "streak_decay": 0.0 },
  "weights": { "derivatives": 0.40, "onchain": 0.35, "whale_intel": 0.25 },
  "coverage": { "derivatives": true, "whale": true, "onchain": true },
  "weights_mode": "free",
  "reasons": ["Funding rate negative across venues", "Whales 58% short"]
}
```

Untracked symbol (explicit no-data, honest):

```json
{ "symbol": "XYZ", "confidence": "NO_DATA", "action": "NO_DATA_SKIP",
  "unsupported": true, "composite": 0.0,
  "coverage": { "derivatives": false, "whale": false, "onchain": false } }
```

## GET /v1/liquidations — Liquidation levels + real executed heatmap
Returns two complementary views:
- **`levels`** — leverage-projected estimate of *where* liquidation clusters sit.
- **`realized_heatmap`** — the **REAL executed** forced-liquidation intensity
  (price × time matrix), aggregated live from public exchange WebSocket feeds:
  **Binance, OKX, Bybit, Bitget, BitMEX**. Present when the stream has data for
  the symbol (absent in a very calm market or just after startup).

**Query params:** `symbol` (default `BTC`).

Tier behaviour: **Trader** gets `cascade_risk`, nearest distances, and
`realized_totals` / `realized_by_side`. **Pro** gets full `levels` detail plus
the full `realized_heatmap` (matrices, per-price clusters, per-exchange counts).

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations?symbol=BTC"
```

```json
{
  "symbol": "BTC", "cascade_risk": "HIGH",
  "nearest_long_liq_pct": -3.2, "nearest_short_liq_pct": 4.1,
  "levels": { "long_levels": [ … ], "short_levels": [ … ] },
  "realized_heatmap": {
    "window_minutes": 240, "price_min": 91000.0, "price_max": 99000.0,
    "clusters": [ { "price": 93250.0, "notional": 4820000.0, "long_notional": 4820000.0, "short_notional": 0.0, "count": 37, "dominant_side": "long" } ],
    "by_side": { "long": 6100000.0, "short": 2400000.0 },
    "totals": { "long_liq_notional": 6100000.0, "short_liq_notional": 2400000.0, "total_notional": 8500000.0, "count": 214 },
    "exchanges": { "binance": 120, "okx": 40, "bybit": 34, "bitget": 12, "bitmex": 8 },
    "generated_at": 1710940821
  }
}
```

## GET /v1/liquidations/onchain — Executed DeFi lending liquidations (authenticated)
Executed lending-protocol liquidations captured **directly from the project's own
local BSC + Avalanche full nodes** — independent of any trading bot.

- BSC: Venus / Cream, Moolah (Lista DAO)
- Avalanche: AAVE V3/V2, Benqi, BankerJoe, Granary, Vinium

Requires an authenticated key (**Trader tier and above**). Pro tier additionally
returns `at_risk` positions (bot-dependent — may be absent).

**Query params:** `chain` (`bsc` | `avax`, omit for all), `limit` (default `100`, max `500`).

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations/onchain?chain=bsc&limit=50"
```

```json
{
  "chain": "bsc", "count": 2,
  "liquidations": [
    { "chain": "bsc", "protocol": "Venus", "borrower": "0x2be6…8dfa",
      "debt_symbol": "DAI", "debt_amount": 426.15, "repay_usd": 426.15,
      "collateral_symbol": "WBNB", "tx_hash": "0x718c…7c0e", "block": 89170816, "ts": 1710940200 }
  ],
  "summary": {
    "window_hours": 24, "buffer_size": 88, "enabled": true,
    "by_chain": { "bsc": { "count": 61, "repay_usd_known": 148230.55 } },
    "by_protocol": { "bsc:Venus": { "count": 61, "repay_usd_known": 148230.55 } },
    "nodes": { "bsc": { "reachable": true, "head_block": 89173010, "seconds_since_poll": 6, "events_total": 61 } }
  }
}
```

## POST /v1/webhooks — Register an outbound webhook (Pro)
Register an HTTPS URL to receive signed event pushes when signals fire. Body:

| Field | Type | Notes |
|---|---|---|
| `url` | string | HTTPS endpoint (must start with `https://`) |
| `events` | string[] | e.g. `["HIGH","MEDIUM","VETO"]` or `["*"]` |
| `symbols` | string[] | e.g. `["BTC","ETH"]` or `["*"]` |
| `secret` | string | Your signing secret, **≥ 16 chars** (stored hashed) |

```bash
curl -X POST -H "X-API-Key: YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://yourapp.com/hook","events":["HIGH","MEDIUM"],"symbols":["BTC","ETH"],"secret":"a-long-random-secret"}' \
  "https://api.smartmoneyapi.com/v1/webhooks"
```

**Delivery & signature verification.** Each delivery is a JSON `POST` with headers
`X-SmartMoney-Event` (the event name) and `X-SmartMoney-Signature` (an
HMAC-SHA256 hex digest). Deliveries retry up to 3× with backoff.

The HMAC **key** is the SHA-256 hex digest of the secret you registered (the
secret itself is only ever stored hashed). To verify a delivery, compute the
HMAC-SHA256 of the raw request body using that derived key and compare with a
constant-time check:

```python
import hashlib, hmac

def verify(raw_body: bytes, signature_header: str, my_secret: str) -> bool:
    key = hashlib.sha256(my_secret.encode()).hexdigest()      # HMAC key = sha256(secret) hex
    expected = hmac.new(key.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header)
```

## Alerts (Pro)
Custom threshold alerts. All under `/v1/alerts/*` and require the Pro tier.

| Method | Path | Description |
|---|---|---|
| GET | `/v1/alerts/conditions` | List your conditions + `available_metrics` + `available_operators` |
| POST | `/v1/alerts/conditions` | Create a condition (returns `{id, message}`, `201`) |
| DELETE | `/v1/alerts/conditions/{id}` | Delete a condition |
| GET | `/v1/alerts/history` | Recent trigger events (most recent first, ≤ 100) |

**Create body:** `name`, `metric`, `symbol` (default `BTC`), `operator`,
`threshold`, optional `delivery` (default `telegram`), `cooldown_minutes` (default `60`).

- **Operators:** `lt`, `gt`, `eq`, `crosses_above`, `crosses_below`
- **Metrics:** `funding_rate`, `global_lsr`, `long_pct`, `top_trader_lsr`,
  `taker_ratio`, `mvrv`, `sopr`, `exchange_net_flow`, `accumulation`,
  `whale_long_pct`, `whale_n_wallets`, `composite_long`, `composite_short`,
  `funding_spread` (the live list is returned by `GET /v1/alerts/conditions`)

```bash
curl -X POST -H "X-API-Key: YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"name":"BTC funding spike","metric":"funding_rate","symbol":"BTC","operator":"gt","threshold":0.05}' \
  "https://api.smartmoneyapi.com/v1/alerts/conditions"
```

## POST /v1/tradingview/webhook — Inbound TradingView alert
Receives a TradingView alert (TradingView cannot send custom headers, so it
authenticates via a `secret` field **in the JSON body**), runs it through
`/confirm`, and returns the confirmation. Does **not** use `X-API-Key`.

Body: `secret`, `symbol`, `direction` (`long`|`short`), optional `source`,
`timeframe`, `strategy`, `price`. Response wraps the confirmation and adds a
top-level `action` of `CONFIRMED` (daemon confidence HIGH/MEDIUM) or `VETOED`.

## Other public endpoints
| Method | Path | Description |
|---|---|---|
| GET | `/v1/stats` | Live site stats (win-rates with sample sizes + methodology) |
| GET | `/v1/whales/events` | Recent whale events (public) |
| GET | `/v1/whales/summary` | Whale positioning summary |
| GET | `/v1/derivatives/screener` | Derivatives screener (funding/OI/LSR) |
| GET | `/v1/onchain/*` | On-chain metrics (TVL, stablecoins, gas, …) |
| GET | `/v1/usage` | Your plan usage (authenticated) |
| GET | `/v1/stream/public-swaps` | Public SSE live-swap feed |
| WSS | `/v1/ws/live-swaps?ticket=…` | Paid live-swap firehose (exchange a key for a ticket via `POST /v1/ws/ticket`) |

## Rate limits
Limits depend on your plan (Free / Trader / Pro / Enterprise). See https://smartmoneyapi.com/pricing. On `429`, back off and upgrade for higher limits.

## Errors
JSON `{ "error": "...", "message": "..." }` with standard HTTP status codes (`401` invalid/missing key, `403` endpoint/symbol not on your tier, `429` rate-limited).

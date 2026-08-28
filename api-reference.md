# SmartMoneyAPI — API reference

**Generated file — do not hand-edit.** Produced by `tools/build_public_spec.py` from the live OpenAPI document at <https://smartmoneyapi.com/openapi.json (read from a local copy)>, on 2026-08-28. It documents 207 of the 263 paths the live API routes; the selection rule is stated in [openapi.yaml](openapi.yaml) and implemented in [tools/build_public_spec.py](tools/build_public_spec.py).

Base URL: `https://api.smartmoneyapi.com`

Auth: send `X-API-Key: <key>` on every request. Operations marked **keyless** answer without one, at a reduced row cap and a per-IP throttle. Never put a key in a URL.

Errors: `429` is a quota or throttle rejection; `403` means your tier does not include that operation or symbol. Errors a browser can reach are returned as `503`, never `502`/`504`.

> Not financial advice. Scores are a multi-factor confluence read, not a guaranteed win-rate. Past signal accuracy does not guarantee future results.

## Contents

- [Account](#account) — 1 endpoint
- [COT](#cot) — 4 endpoints
- [Copy-trading](#copy-trading) — 9 endpoints
- [DEX](#dex) — 4 endpoints
- [DeFiLlama](#defillama) — 11 endpoints
- [Derivatives](#derivatives) — 7 endpoints
- [ETF](#etf) — 2 endpoints
- [Equities](#equities) — 24 endpoints
- [Historical](#historical) — 4 endpoints
- [History](#history) — 10 endpoints
- [Integrations](#integrations) — 1 endpoint
- [Intelligence](#intelligence) — 6 endpoints
- [JSON-RPC](#json-rpc) — 6 endpoints
- [Liquidations](#liquidations) — 10 endpoints
- [Live chain](#live-chain) — 5 endpoints
- [Market](#market) — 11 endpoints
- [Meta](#meta) — 7 endpoints
- [News](#news) — 8 endpoints
- [Node](#node) — 13 endpoints
- [On-chain](#on-chain) — 7 endpoints
- [Options](#options) — 6 endpoints
- [Performance](#performance) — 3 endpoints
- [Screener](#screener) — 7 endpoints
- [Seasonality](#seasonality) — 6 endpoints
- [Signals](#signals) — 8 endpoints
- [Strategies](#strategies) — 6 endpoints
- [Technicals](#technicals) — 3 endpoints
- [Trading tools](#trading-tools) — 3 endpoints
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

Response fields:

| Field | Type | Description |
|---|---|---|
| `BTC` | object |  |
| `ETH` | — |  |
| `relative_strength` | — |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `history` | array |  |
| `meta` | object |  |
| `symbol` | string |  |
| `updated` | integer |  |
| `weeks` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/history"
```

### `GET /v1/cot/summary`

**COT summary** — keyless

CFTC Commitments of Traders positioning summary.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `categories` | object |  |
| `macd_confirmation` | object |  |
| `meta` | object |  |
| `net_change` | integer |  |
| `net_long` | integer |  |
| `open_interest` | integer |  |
| `pct_long` | number |  |
| `pct_short` | number |  |
| `report_date` | string |  |
| `signal` | string |  |
| `symbol` | string |  |
| `trend_4w` | array |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `current_net_long` | integer |  |
| `divergence` | string |  |
| `extreme` | string |  |
| `hedger_net` | integer |  |
| `mean_net_long` | integer |  |
| `momentum_4w` | integer |  |
| `percentile` | number |  |
| `speculator_net` | integer |  |
| `std_dev` | integer |  |
| `symbol` | string |  |
| `trend_series` | array |  |
| `updated` | integer |  |
| `weeks` | integer |  |
| `z_score` | number |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/cot/trend"
```

## Copy-trading

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

### `GET /v1/top-traders/history`

**Top-trader history** — key required — Pro (15,000 calls/day)

Historical position and PnL series for the tracked top traders.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/history"
```

### `GET /v1/top-traders/leaderboard`

**Top-trader leaderboard** — key required — Pro (15,000 calls/day)

Hyperliquid leaderboard traders ranked over the selected window.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/leaderboard"
```

### `GET /v1/top-traders/performance`

**Top-trader performance** — key required — Pro (15,000 calls/day)

Realised performance of the tracked top traders.

| Parameter | In | Required | Description |
|---|---|---|---|
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/performance"
```

### `GET /v1/top-traders/summary`

**Top-trader summary** — key required — Pro (15,000 calls/day)

Aggregate statistics for the tracked top traders.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/top-traders/summary"
```

## DEX

### `GET /v1/dex/pair`

**Pair details** — keyless

Details for a single DEX pair.

| Parameter | In | Required | Description |
|---|---|---|---|
| `chain` | query | yes | Chain slug (e.g. ethereum, bsc). |
| `address` | query | yes | Pair contract address. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/dex/pair"
```

### `GET /v1/dex/search`

**Search DEX pairs** — keyless

Search DexScreener pairs by name/symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `q` | query | yes | Search query. |
| `limit` | query | no | Max pairs. Default `20`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/dex/search"
```

### `GET /v1/dex/token`

**Token pairs** — keyless

All DEX pairs for a token address.

| Parameter | In | Required | Description |
|---|---|---|---|
| `address` | query | yes | Token contract address. |
| `limit` | query | no | Max pairs. Default `10`. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/dex/token"
```

### `GET /v1/dex/trending`

**Trending DEX pairs** — keyless

Trending pairs from DexScreener.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max pairs. Default `20`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `base_token` | object |  |
| `chain` | string |  |
| `created_at` | integer |  |
| `dex` | string |  |
| `fdv` | number |  |
| `liquidity_usd` | number |  |
| `pair_address` | string |  |
| `price_change_1h` | number |  |
| `price_change_24h` | number |  |
| `price_change_5m` | number |  |
| `price_change_6h` | number |  |
| `price_usd` | number |  |
| `quote_token` | object |  |
| `url` | string |  |
| `volume_24h` | number |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/dex/trending"
```

## DeFiLlama

### `GET /v1/defillama/all`

**All DeFiLlama data** — keyless

Every DeFiLlama dataset in one payload. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `borrow_rates` | object |  |
| `bridges` | object |  |
| `derivatives` | object |  |
| `fees` | object |  |
| `hacks` | object |  |
| `options` | object |  |
| `pools` | object |  |
| `price_momentum` | object |  |
| `raises` | object |  |
| `stablecoin_chains` | object |  |
| `treasuries` | object |  |
| `unlocks` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/all"
```

### `GET /v1/defillama/borrow-rates`

**Borrow rates** — key required — Trader (3,000 calls/day)

Lending-market borrow rates. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/borrow-rates"
```

### `GET /v1/defillama/bridges`

**Bridge volumes** — keyless

Cross-chain bridge volume. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `available` | boolean |  |
| `data_is_placeholder` | boolean |  |
| `error` | string |  |
| `remediation` | string |  |
| `source_note` | string |  |
| `status` | string |  |
| `top_bridges` | array |  |
| `total_24h` | integer |  |
| `total_7d` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/bridges"
```

### `GET /v1/defillama/derivatives`

**Perp DEX volumes** — keyless

Perpetual DEX volume rankings. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `available` | boolean |  |
| `data_is_placeholder` | boolean |  |
| `error` | string |  |
| `remediation` | string |  |
| `source_note` | string |  |
| `status` | string |  |
| `top_protocols` | array |  |
| `total_24h` | integer |  |
| `total_7d` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/derivatives"
```

### `GET /v1/defillama/fees`

**Protocol fees** — keyless

Protocol fee and revenue rankings. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `change_1d` | number |  |
| `top_protocols` | array |  |
| `total_fees_24h` | number |  |
| `total_fees_7d` | number |  |
| `total_revenue_24h` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/fees"
```

### `GET /v1/defillama/hacks`

**Hacks** — keyless

Logged protocol exploits and amounts lost. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `recent_hacks` | array |  |
| `total_30d_usd` | number |  |
| `total_all_time_usd` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/hacks"
```

### `GET /v1/defillama/momentum`

**Price momentum** — keyless

Cross-token price momentum. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `coins` | array |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/momentum"
```

### `GET /v1/defillama/raises`

**Fundraises** — keyless

Recent protocol fundraises. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `available` | boolean |  |
| `data_is_placeholder` | boolean |  |
| `error` | string |  |
| `recent_raises` | array |  |
| `remediation` | string |  |
| `source_note` | string |  |
| `status` | string |  |
| `total_raised_30d_usd` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/raises"
```

### `GET /v1/defillama/stablecoin-chains`

**Stablecoins by chain** — keyless

Stablecoin supply broken down by chain. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `chains` | array |  |
| `total_stablecoin_usd` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/stablecoin-chains"
```

### `GET /v1/defillama/treasuries`

**Protocol treasuries** — key required — Trader (3,000 calls/day)

Protocol treasury holdings. Sourced from DeFiLlama.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/defillama/treasuries"
```

### `GET /v1/defillama/unlocks`

**Token unlocks** — keyless

Upcoming token unlock schedule. Sourced from DeFiLlama.

Response fields:

| Field | Type | Description |
|---|---|---|
| `available` | boolean |  |
| `data_is_placeholder` | boolean |  |
| `error` | string |  |
| `events` | array |  |
| `remediation` | string |  |
| `source_note` | string |  |
| `status` | string |  |
| `total` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/defillama/unlocks"
```

## Derivatives

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `limited` | boolean |  |
| `opportunities` | array |  |
| `public` | boolean |  |
| `scanned_symbols` | integer |  |
| `ts` | integer |  |

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
| `public` | boolean |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `gainers` | array |  |
| `losers` | array |  |
| `public` | boolean |  |
| `timeframe` | string |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/oi-rankings"
```

### `GET /v1/derivatives/screener`

**Derivatives screener** — keyless

Cross-exchange derivatives screener (500+ symbols): funding, open interest, long/short ratio, signals. Anonymous callers get a fixed top-10 by OI (response carries public:true, limited:true); authenticated callers can sort/filter up to 200 rows.

| Parameter | In | Required | Description |
|---|---|---|---|
| `sort` | query | no | Sort field (authenticated only). Default `oi_usd`. |
| `dir` | query | no | Sort direction (authenticated only). One of: `asc`, `desc`. Default `desc`. |
| `limit` | query | no | Max rows, capped at 200 (authenticated only). Default `50`. |
| `min_oi` | query | no | Minimum open interest in USD (authenticated only). Default `0`. |
| `signal` | query | no | Filter by signal type (authenticated only). |

Response fields:

| Field | Type | Description |
|---|---|---|
| `limited` | boolean |  |
| `meta` | object |  |
| `public` | boolean |  |
| `sort_by` | string |  |
| `symbols` | array |  |
| `total_count` | integer |  |
| `unmeasured_for_sort` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/derivatives/screener"
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

**ETF flows** — keyless

Spot BTC/ETH ETF daily flows with per-fund breakdown (SoSoValue).

| Parameter | In | Required | Description |
|---|---|---|---|
| `asset` | query | no | ETF asset. One of: `BTC`, `ETH`. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `asset` | string |  |
| `current` | object |  |
| `etf_type` | string |  |
| `funds` | array |  |
| `history_recent` | array |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/etf/flows"
```

### `GET /v1/etf/history`

**ETF flow history** — key required — Pro (15,000 calls/day)

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

**Dark-pool prints** — keyless

Off-exchange (dark-pool) prints for the tracked tickers.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `limit` | query | no | Max rows returned. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/equity-flow/dark-pool"
```

### `GET /v1/equity-flow/gex`

**Equity gamma exposure** — keyless

Dealer gamma exposure by strike for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | yes | Ticker symbol. |

```bash
curl \
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

**Unusual options activity** — keyless

Unusual equity options prints ranked by a size/open-interest score.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | query | no | Filter by ticker. |
| `contract_type` | query | no | Contract type. One of: `call`, `put`. |
| `min_score` | query | no | Minimum unusualness score. |
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `contract_type` | string |  |
| `expiry_date` | string |  |
| `in_the_money` | integer |  |
| `iv` | number |  |
| `last_price` | number |  |
| `open_interest` | integer |  |
| `premium` | number |  |
| `snapshot_ts` | integer |  |
| `spot_price` | number |  |
| `strike` | number |  |
| `ticker` | string |  |
| `unusualness` | number |  |
| `vol_oi_ratio` | number |  |
| `volume` | integer |  |

```bash
curl \
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

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/activist-alerts"
```

### `GET /v1/stocks/congress/{ticker}`

**Congressional trades** — keyless

Disclosed congressional trades in one ticker, with the disclosure (PTR) link. Published as disclosure data, not as a signal — the long-horizon study found no tradable edge.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |
| `days` | query | no | Look-back window in days. |

```bash
curl \
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

**Institutional holders** — keyless

Institutional holders and position changes for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl \
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

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stocks/rankings"
```

### `GET /v1/stocks/short-interest/{ticker}`

**Short interest** — keyless

Reported short interest for one ticker.

| Parameter | In | Required | Description |
|---|---|---|---|
| `ticker` | path | yes | Equity ticker symbol. |

```bash
curl \
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

**Market OHLCV history** — keyless

Historical market data by CoinGecko coin id.

| Parameter | In | Required | Description |
|---|---|---|---|
| `coin` | query | no | CoinGecko coin id. Default `bitcoin`. |
| `days` | query | no | Days of history. Default `30`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `coin` | string |  |
| `count` | integer |  |
| `data` | array |  |
| `days` | integer |  |

```bash
curl \
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
| `partition_dir` | string |  |
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

Latest AI-written market commentary over the aggregated data. Commentary only — it is not a prediction and carries no measured edge.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/analysis"
```

### `GET /v1/analysis/status`

**AI analysis status** — keyless

Freshness and availability of the AI analysis loop.

Response fields:

| Field | Type | Description |
|---|---|---|
| `as_of` | string |  |
| `cached_count` | integer |  |
| `engine` | string |  |
| `fresh_count` | integer |  |
| `full_analysis` | object |  |
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

TIERS. Trader receives 24 of the 28 fields, listed per field below; the ladders are truncated to 5 levels per side (Pro: up to 10) and Pro additionally receives `nearest_status`, `nearest_excluded_modelled`, `nearest_exclusion_reason`, `realized_heatmap`. Anything a plan removed is named in `withheld` (`withheld_reason: "trader_plan"`), computed per response — so a short ladder does not report a boundary that removed nothing, and a missing key never has to stand in for both "not in your plan" and "the server had nothing".

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
| `compute_ms` | integer |  |
| `coverage` | object |  |
| `current_context` | object |  |
| `data_posture` | string | Fixed disclaimer: descriptive conditional statistics, not a signal. |
| `event_definition` | string |  |
| `generated_at` | integer |  |
| `honesty` | string |  |
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
| `by_regime` | object |  |
| `compute_ms` | integer |  |
| `dataset` | object |  |
| `event_definition` | string |  |
| `generated_at` | integer |  |
| `honesty` | string |  |
| `horizons` | array |  |
| `kind` | string |  |
| `n_events` | object |  |
| `per_symbol` | object |  |
| `pooled` | object |  |
| `posture` | string | States that events are an OI-cascade PROXY, not realized liquidations. |
| `span` | string |  |
| `stats_legend` | object |  |

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
| `cascade_status` | string |  |
| `clusters` | array |  |
| `current_price` | number |  |
| `empty` | boolean | True when there was nothing to simulate (no positions/OI for this symbol). Distinct from ok=false, which is a failure. |
| `estimated` | boolean | Always true. This endpoint is a model. |
| `exchanges` | array | Venue names contributing to this simulation. |
| `methodology` | object | Every model assumption, surfaced in the payload. |
| `move_pct` | number |  |
| `nearest_long_wall` | object | Nearest modelled long liquidation wall, or null when none is derivable. |
| `nearest_short_wall` | object |  |
| `oi_band_status` | object |  |
| `ok` | boolean |  |
| `realized_context` | object | REAL executed liquidations shown alongside the model for scale. Context only — it never makes the projection realized, and its own coverage span is stated so a short sample is not mistaken for a long one. |
| `symbol` | string |  |
| `target_price` | number |  |
| `total_oi_usd` | number |  |
| `triggered_count` | integer |  |
| `triggered_notional_usd` | number |  |
| `triggered_whale_usd` | number |  |
| `ts` | integer |  |
| `whale_positions_dropped_no_notional` | integer |  |
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

**Altcoin Season Index** — keyless

Altcoin season index derived from top-coin performance vs BTC. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `altcoins_outperforming` | integer |  |
| `altcoins_total` | integer |  |
| `btc_30d_change` | number |  |
| `btc_7d_change` | number |  |
| `label` | string |  |
| `period` | string |  |
| `score` | number |  |
| `top_performers` | array |  |
| `updated` | integer |  |
| `worst_performers` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/altseason"
```

### `GET /v1/market/basis`

**CME basis** — keyless

CME futures basis vs spot. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `futures` | array |  |
| `nearest_annualized` | number |  |
| `nearest_basis_pct` | number |  |
| `spot_price` | number |  |
| `updated` | integer |  |

```bash
curl \
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

Response fields:

| Field | Type | Description |
|---|---|---|
| `candles` | array |  |
| `count` | integer |  |
| `fetched_at` | integer |  |
| `interval` | string |  |
| `meta` | object |  |
| `pair` | string |  |
| `source` | string |  |
| `symbol` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/candles"
```

### `GET /v1/market/dominance`

**BTC dominance** — keyless

Bitcoin market-cap dominance. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `active_cryptos` | integer |  |
| `btc_dominance` | number |  |
| `eth_dominance` | number |  |
| `market_cap_change_24h` | number |  |
| `top_dominance` | array |  |
| `total_market_cap` | number |  |
| `total_volume_24h` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/dominance"
```

### `GET /v1/market/indices`

**All market indices** — keyless

All market indices in one response. Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `altcoin_season` | object |  |
| `cme_basis` | object |  |
| `dominance` | object |  |
| `volatility` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/market/indices"
```

### `GET /v1/market/volatility`

**Volatility index** — keyless

Crypto volatility gauge (Deribit). Public.

Response fields:

| Field | Type | Description |
|---|---|---|
| `btc` | object |  |
| `eth` | object |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `components` | object |  |
| `gauge_zone` | string |  |
| `label` | string |  |
| `prev_score` | number |  |
| `score` | number |  |
| `symbol` | string |  |
| `trend` | string |  |
| `updated_at` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `days` | integer |  |
| `history` | array |  |
| `symbol` | string |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mood/history"
```

### `GET /v1/mood/overview`

**Mood overview** — keyless

Mood reading across the tracked symbol universe. Served from cache; returns a warming-up marker rather than recomputing inline.

Response fields:

| Field | Type | Description |
|---|---|---|
| `symbols` | array |  |
| `total` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/mood/overview"
```

### `GET /v1/projection`

**Range projection** — keyless

Statistical range projection from realised volatility. A range, not a directional call.

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

Range projections across the symbol universe.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_correlation` | number |  |
| `count_matches` | integer |  |
| `current_price` | number |  |
| `direction` | string |  |
| `horizon_days` | integer |  |
| `probability_bearish` | integer |  |
| `probability_bullish` | integer |  |
| `projected_pct_bear` | number |  |
| `projected_pct_bull` | number |  |
| `robustness` | integer |  |
| `score` | integer |  |
| `signal_strength` | string |  |
| `symbol` | string |  |
| `ts` | integer |  |

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
| `status` | string |  |
| `ts` | number |  |

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

Canonical public site stats: exchange count, tracked derivatives symbols, measured signal win-rates with sample sizes (in-sample labelled) and the accruing out-of-sample forward holdout. Cached.

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_loss_pct` | number |  |
| `avg_win_pct` | number |  |
| `confirm_outcomes_n` | integer |  |
| `confirm_signals_n` | integer |  |
| `derivatives_symbols` | integer |  |
| `exchanges` | integer |  |
| `expectancy_pct` | number |  |
| `forward_holdout` | object |  |
| `high_n_forward` | integer |  |
| `high_status` | string |  |
| `high_winrate` | number |  |
| `high_winrate_forward` | number |  |
| `high_winrate_n` | integer |  |
| `last_updated` | string |  |
| `medium_winrate` | number |  |
| `medium_winrate_n` | integer |  |
| `overall_accuracy` | number |  |
| `overall_accuracy_forward` | number |  |
| `overall_accuracy_n` | integer |  |
| `overall_n_forward` | integer |  |
| `profit_factor` | number |  |
| `signal_count` | integer |  |
| `stats_source` | string |  |
| `tracked_symbols` | integer |  |
| `whale_count` | integer |  |
| `winrate_basis` | string |  |
| `winrate_horizon` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/stats"
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

Response fields:

| Field | Type | Description |
|---|---|---|
| `by_state` | object |  |
| `combined_accuracy` | object |  |
| `combined_formula_versions` | object |  |
| `daily_trend` | array |  |
| `days` | integer |  |
| `dropout` | object |  |
| `method` | string |  |
| `n_is` | string |  |
| `note` | — |  |
| `recent_snapshots` | array |  |
| `status` | string |  |
| `timeframe_accuracy` | object |  |
| `updated` | integer |  |
| `window` | object |  |
| `yield_accuracy` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `coverage` | object |  |
| `empty_reason` | — |  |
| `events` | array |  |
| `filters` | object |  |
| `has_more` | boolean |  |
| `max_page_limit` | integer |  |
| `next_cursor` | string |  |
| `page_limit` | integer |  |
| `status` | string |  |
| `total_is_capped` | boolean |  |
| `total_matching` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/archive"
```

### `GET /v1/news/coverage`

**News archive coverage** — keyless

What the archive actually contains: row count, oldest and newest timestamps and dates, span in days, and breakdowns by category and by source. Use it to render an honest coverage statement rather than implying records exist for dates we never retained.

Response fields:

| Field | Type | Description |
|---|---|---|
| `by_category` | object |  |
| `by_source` | object |  |
| `newest_date` | string |  |
| `newest_ts` | integer |  |
| `note` | string |  |
| `oldest_date` | string |  |
| `oldest_ts` | integer |  |
| `span_days` | number |  |
| `total_rows` | integer |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/coverage"
```

### `GET /v1/news/fear-greed`

**Fear & Greed index** — keyless

Crypto Fear & Greed index (Alternative.me).

Response fields:

| Field | Type | Description |
|---|---|---|
| `avg_7d` | number |  |
| `classification` | string |  |
| `meta` | object |  |
| `source` | string |  |
| `source_ts` | integer |  |
| `stale` | boolean |  |
| `trend_7d` | string |  |
| `ts` | integer |  |
| `updated` | integer |  |
| `value` | integer |  |
| `values_7d` | array |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `archive_endpoint` | string |  |
| `categories` | object |  |
| `count` | integer |  |
| `events` | array |  |
| `excluded_categories` | array |  |
| `limit_applied` | integer |  |
| `truncated` | boolean |  |
| `updated` | integer |  |
| `window_hours` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/general"
```

### `GET /v1/news/impact`

**News impact** — keyless

Current aggregated news impact state.

Response fields:

| Field | Type | Description |
|---|---|---|
| `active_alerts` | array |  |
| `active_count` | integer |  |
| `confidence_modifier` | number |  |
| `market_state` | string |  |
| `net_sentiment` | string |  |
| `news_direction` | integer |  |
| `news_modifier` | number |  |
| `news_severity` | number |  |
| `treasury_yield` | object |  |
| `updated` | integer |  |
| `yield_direction` | integer |  |
| `yield_modifier` | number |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/news/impact"
```

### `GET /v1/news/treasury-yield`

**Treasury yields** — keyless

US Treasury yield levels used by the macro classifier.

Response fields:

| Field | Type | Description |
|---|---|---|
| `change_7d` | number |  |
| `change_90d` | number |  |
| `daily_change` | number |  |
| `history` | array |  |
| `score` | number |  |
| `signal` | string |  |
| `ts` | integer |  |
| `updated` | integer |  |
| `yield_20y` | number |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `events` | array |  |
| `signal_types` | object |  |
| `updated` | integer |  |

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

**Deployer history** — key required — per-feature node entitlement

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

**Top holders** — key required — per-feature node entitlement

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

**BTC on-chain stats** — keyless

Bitcoin network stats: hashrate, difficulty, mempool, transaction counts (Blockchain.com).

Response fields:

| Field | Type | Description |
|---|---|---|
| `btc_onchain` | object |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/btc"
```

### `GET /v1/onchain/dex`

**DEX volumes** — keyless

Decentralised exchange volume rankings (DeFiLlama).

Response fields:

| Field | Type | Description |
|---|---|---|
| `change_1d` | number |  |
| `change_7d` | number |  |
| `top_dexes` | array |  |
| `total_24h` | number |  |
| `total_7d` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/dex"
```

### `GET /v1/onchain/gas`

**Ethereum gas** — keyless

Current Ethereum gas prices (Etherscan).

Response fields:

| Field | Type | Description |
|---|---|---|
| `base_fee` | number |  |
| `block` | string |  |
| `fast` | number |  |
| `proposed` | number |  |
| `safe` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/gas"
```

### `GET /v1/onchain/metrics`

**All on-chain metrics** — keyless

Aggregated on-chain metrics bundle (DeFiLlama TVL/stablecoins/DEX volumes, Blockchain.com BTC stats, Etherscan gas, CoinGecko global). Public.

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

**Stablecoin supply** — keyless

Stablecoin circulating supply breakdown (DeFiLlama).

Response fields:

| Field | Type | Description |
|---|---|---|
| `stablecoins` | array |  |
| `total_flow_24h` | number |  |
| `total_flow_7d` | number |  |
| `total_mcap` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/stablecoins"
```

### `GET /v1/onchain/tvl`

**TVL by chain** — keyless

DeFi total value locked per chain (DeFiLlama). Anonymous callers get the top 10 chains.

Response fields:

| Field | Type | Description |
|---|---|---|
| `top_chains` | array |  |
| `total_tvl` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/tvl"
```

### `GET /v1/onchain/yields`

**DeFi yields** — keyless

Top DeFi yield pools (DeFiLlama). Anonymous callers get the top 8 pools.

Response fields:

| Field | Type | Description |
|---|---|---|
| `pools` | array |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/onchain/yields"
```

## Options

### `GET /v1/options`

**Options index** — key required — Pro (15,000 calls/day)

Index of the available options endpoints.

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options"
```

### `GET /v1/options/chain`

**Options chain summary** — keyless

BTC/ETH options summary from Deribit: put/call ratio, max pain, open interest by strike, per-expiry breakdown.

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `currency` | string |  |
| `expiry_summary` | object |  |
| `max_pain` | object |  |
| `meta` | object |  |
| `oi_by_strike` | array |  |
| `pcr_oi` | number |  |
| `pcr_volume` | number |  |
| `total_call_oi` | number |  |
| `total_call_volume` | number |  |
| `total_put_oi` | number |  |
| `total_put_volume` | number |  |
| `underlying_price` | number |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/options/chain"
```

### `GET /v1/options/gex`

**Gamma exposure** — keyless

Dealer gamma-exposure profile by strike for BTC/ETH.

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `available` | boolean |  |
| `call_gex_total` | number |  |
| `convention` | string |  |
| `gamma_flip` | number |  |
| `gex_regime` | string |  |
| `net_gex` | number |  |
| `net_gex_raw` | number |  |
| `profile` | array |  |
| `profile_strikes` | integer |  |
| `put_gex_total` | number |  |
| `regime_note` | string |  |
| `scale` | string |  |
| `skew` | object |  |
| `source` | string |  |
| `spot_price` | number |  |
| `symbol` | string |  |
| `term_structure` | array |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/options/gex"
```

### `GET /v1/options/history`

**Options history** — key required — Pro (15,000 calls/day)

Historical options aggregates (put/call ratio, open interest).

| Parameter | In | Required | Description |
|---|---|---|---|
| `currency` | query | no | Options currency. One of: `BTC`, `ETH`. Default `BTC`. |
| `days` | query | no | Look-back window in days. |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/options/history"
```

### `GET /v1/options/overview`

**Options overview (BTC + ETH)** — keyless

Both BTC and ETH options summaries in one response.

Response fields:

| Field | Type | Description |
|---|---|---|
| `BTC` | object |  |
| `ETH` | object |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/options/overview"
```

### `GET /v1/options/pcr`

**Put/call ratio** — keyless

BTC options summary (put/call ratio focus). Same payload shape as /v1/options/chain with currency=BTC.

Response fields:

| Field | Type | Description |
|---|---|---|
| `currency` | string |  |
| `expiry_summary` | object |  |
| `max_pain` | object |  |
| `oi_by_strike` | array |  |
| `pcr_oi` | number |  |
| `pcr_volume` | number |  |
| `total_call_oi` | number |  |
| `total_call_volume` | number |  |
| `total_put_oi` | number |  |
| `total_put_volume` | number |  |
| `underlying_price` | number |  |
| `updated` | integer |  |

```bash
curl \
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
| `min_resolved_sample` | integer |  |
| `overall_accuracy` | number |  |
| `overall_resolved` | integer |  |
| `period_days` | integer |  |
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

CSV export of the tracked-signal performance log.

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
| `btc_overlay` | array |  |
| `confidence` | — |  |
| `cost_bases` | object |  |
| `curves` | array |  |
| `curves_gross` | array |  |
| `curves_net_fees` | array |  |
| `curves_net_fees_slip` | array |  |
| `disclaimer` | string |  |
| `forward_holdout` | object |  |
| `horizon` | string |  |
| `n_signals` | integer |  |
| `scorer_frozen_ts` | integer |  |
| `sizing_note` | string |  |
| `summary` | object |  |
| `timestamps` | array |  |
| `window_end` | integer |  |
| `window_start` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/performance/track-record"
```

## Screener

### `GET /v1/rankings`

**Symbol rankings** — keyless

Composite symbol rankings with the methodology used to build them.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `contrarian` | array |  |
| `funding_arb` | array |  |
| `momentum` | array |  |
| `seasonal_plays` | array |  |
| `updated_at` | integer |  |
| `whale_favorites` | array |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `composite_score` | number |  |
| `indicators` | object |  |
| `price` | number |  |
| `signal` | — |  |
| `state` | string |  |
| `strength` | integer |  |
| `symbol` | string |  |
| `ts` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `composite_score` | number |  |
| `indicators` | object |  |
| `price` | number |  |
| `signal` | string |  |
| `state` | string |  |
| `strength` | integer |  |
| `symbol` | string |  |
| `ts` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `composite_score` | number |  |
| `history` | array |  |
| `indicators` | object |  |
| `multi_timeframe` | object |  |
| `price` | number |  |
| `signal` | — |  |
| `state` | string |  |
| `strength` | integer |  |
| `symbol` | string |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/scanner/obs/symbol"
```

### `GET /v1/screener`

**Multi-factor screener** — keyless

Cross-symbol screener over derivatives, whale and technical factors.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `direction` | string |  |
| `sort_by` | string |  |
| `symbols` | array |  |
| `total_count` | integer |  |
| `updated_at` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/screener"
```

### `GET /v1/screener/rankings`

**Screener rankings** — keyless

Ranked screener output.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `contrarian` | array |  |
| `funding_arb` | array |  |
| `momentum` | array |  |
| `seasonal_plays` | array |  |
| `updated_at` | integer |  |
| `whale_favorites` | array |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/screener/rankings"
```

### `GET /v1/screener/symbol`

**Screener detail** — keyless

Full screener factor breakdown for one symbol.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `components` | object |  |
| `composite_score` | number |  |
| `direction` | string |  |
| `grade` | string |  |
| `partial_data` | boolean |  |
| `price` | number |  |
| `rank` | integer |  |
| `score_history` | array |  |
| `signal` | string |  |
| `symbol` | string |  |
| `symbol_full` | string |  |
| `total_symbols` | integer |  |
| `updated_at` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `best_months` | array |  |
| `current_month` | object |  |
| `data_years` | integer |  |
| `months` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |
| `updated` | integer |  |
| `worst_months` | array |  |
| `yearly_returns` | array |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `best_day` | object |  |
| `days` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |
| `updated` | integer |  |
| `worst_day` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `data` | object |  |
| `months` | array |  |
| `symbols` | array |  |
| `timeframe` | string |  |
| `updated` | integer |  |
| `win_rates` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `cumulative_ytd` | object |  |
| `months` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |
| `updated` | integer |  |
| `years` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `best_quarter` | object |  |
| `current_quarter` | object |  |
| `quarters` | array |  |
| `symbol` | string |  |
| `timeframe` | string |  |
| `updated` | integer |  |
| `worst_quarter` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `months` | array |  |
| `timeframe` | string |  |
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/seasonality/rankings"
```

## Signals

### `GET /v1/confirm`

**Smart-money confirmation** — key required — Free (100 calls/day)

Core smart-money confirmation for a symbol: verdict, composite score, confidence (HIGH/MEDIUM/LOW), component scores and reasons (proxied to the aggregation daemon, then tier-enriched with multi-timeframe views, AI analysis and Kelly sizing). Free tier: BTC only, delayed response, some fields stripped.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |
| `direction` | query | no | Trade direction to confirm. One of: `long`, `short`. Default `long`. |
| `account_size` | query | no | Account size in USD for Kelly position sizing (Pro only). |

```bash
curl -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm"
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

Current capitulation reading per symbol from the liquidation and funding panel.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `backtest` | object |  |
| `caveats` | array |  |
| `compute_ms` | integer |  |
| `generated_at` | integer |  |
| `n_scanned` | integer |  |
| `n_triggered` | integer |  |
| `n_triggered_validated` | integer |  |
| `posture` | string |  |
| `regime` | object |  |
| `spec` | object |  |
| `trigger_definition` | string |  |
| `triggered` | array |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `caveats` | array |  |
| `costs` | string |  |
| `cutoffs` | object |  |
| `dataset` | object |  |
| `generated_at` | integer |  |
| `kind` | string |  |
| `meta` | object |  |
| `per_symbol_test_E1_L5` | object |  |
| `profiles` | array |  |
| `shuffle_control` | object |  |
| `threshold_grid_E1_L5_test` | array |  |
| `trigger` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/capitulation/backtest"
```

### `GET /v1/signals/capitulation/walkforward`

**Capitulation walk-forward** — keyless

Walk-forward (out-of-sample) evaluation of the capitulation reading.

| Parameter | In | Required | Description |
|---|---|---|---|
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

Response fields:

| Field | Type | Description |
|---|---|---|
| `accrual_start_ts` | integer |  |
| `backfill_boundary_ts` | integer |  |
| `generated_at` | integer |  |
| `kind` | string |  |
| `n_backfill` | integer |  |
| `n_open` | integer |  |
| `n_resolved` | integer |  |
| `n_trades` | integer |  |
| `n_void` | integer |  |
| `notes` | array |  |
| `posture` | string |  |
| `profiles` | array |  |
| `trades` | array |  |

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
| `horizons` | object |  |
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

The resolved 4h/12h/24h/72h outcome of one logged signal.

| Parameter | In | Required | Description |
|---|---|---|---|
| `signal_id` | path | yes | Numeric signal id from /v1/signals/recent. |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/signals/{signal_id}/outcome"
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
| `meta` | object |  |
| `positions` | array |  |
| `updated` | integer |  |

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
| `meta` | object |  |
| `total_adjustments` | number |  |
| `total_pnl_usdt` | number |  |
| `updated` | integer |  |

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
| `meta` | object |  |
| `signal_types` | object |  |
| `total_signals` | integer |  |
| `unique_signal_types` | integer |  |
| `updated` | integer |  |

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
| `account_growth_percent` | number |  |
| `adjustments` | array |  |
| `avg_duration_hours` | number |  |
| `avg_leverage` | number |  |
| `avg_loser_pnl` | number |  |
| `avg_pnl_percent` | number |  |
| `avg_pnl_usdt` | number |  |
| `avg_winner_pnl` | number |  |
| `best_trade` | object |  |
| `current_equity` | number |  |
| `initial_equity` | number |  |
| `losing_trades` | integer |  |
| `max_drawdown_portfolio` | number |  |
| `max_drawdown_trade` | number |  |
| `meta` | object |  |
| `profit_factor` | number |  |
| `total_adjustments` | number |  |
| `total_pnl_percent` | number |  |
| `total_pnl_usdt` | number |  |
| `total_trades` | integer |  |
| `trades_by_direction` | object |  |
| `trades_by_exit_reason` | object |  |
| `updated` | integer |  |
| `win_rate` | number |  |
| `winning_trades` | integer |  |
| `worst_trade` | object |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `account` | integer |  |
| `all_symbols` | object |  |
| `meta` | object |  |
| `top_10` | array |  |
| `total_symbols` | integer |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `account` | integer |  |
| `limit` | integer |  |
| `meta` | object |  |
| `offset` | integer |  |
| `total` | integer |  |
| `trades` | array |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `interval` | string |  |
| `symbols` | array |  |
| `updated_at` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `bollinger` | object |  |
| `dpo` | object |  |
| `interval` | string |  |
| `macd` | object |  |
| `market_mood` | object |  |
| `obos` | string |  |
| `price` | object |  |
| `rsi` | object |  |
| `signals` | array |  |
| `speed` | object |  |
| `symbol` | string |  |
| `ts` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/ta/technicals"
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
| `updated` | integer |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whale-consensus"
```

### `GET /v1/whale-events`

**Whale events (authenticated)** — key required — Trader (3,000 calls/day)

Full whale-event feed with per-event PnL, leverage and margin detail.

| Parameter | In | Required | Description |
|---|---|---|---|
| `limit` | query | no | Max rows returned. |
| `symbol` | query | no | Base symbol, e.g. BTC. Default `BTC`. |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `filters` | object |  |
| `ok` | boolean |  |
| `positions` | array |  |
| `total` | integer |  |
| `ts` | integer |  |
| `venues` | array |  |

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
| `chain` | string |  |
| `count` | integer |  |
| `distinct` | integer |  |
| `events` | array |  |
| `hours` | integer |  |
| `limit` | integer |  |
| `max_id` | integer |  |
| `meta` | object |  |
| `next_url` | string |  |
| `offset` | integer |  |
| `since_id` | — |  |
| `total` | integer |  |
| `updated` | integer |  |

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

Response fields:

| Field | Type | Description |
|---|---|---|
| `count` | integer |  |
| `market_makers` | array |  |
| `window_days` | integer |  |

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
| `critical_24h` | integer |  |
| `net_flows` | object |  |
| `source_count` | integer |  |
| `sources_contributing` | array |  |
| `sources_silent` | array |  |
| `top_movers` | array |  |
| `updated` | integer |  |
| `volume_basis` | string |  |

```bash
curl \
  "https://api.smartmoneyapi.com/v1/whales/summary"
```

### `GET /v1/whales/universe`

**Whale universe stats** — keyless

Size and composition of the tracked whale universe.

Response fields:

| Field | Type | Description |
|---|---|---|
| `discovery_sources` | object |  |
| `last_discovered` | string |  |
| `pinned_preview` | array |  |
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

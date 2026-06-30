# SmartMoneyAPI — API Reference

Base URL: `https://api.smartmoneyapi.com`  ·  Auth: `X-API-Key` header  ·  Not financial advice.

## GET /v1/confirm — Trade confirmation
Confirm, reduce, or skip a trade idea using live market context.

**Query params**

| Param | Required | Description |
|---|---|---|
| `symbol` | yes | Asset, e.g. `BTC`, `ETH`, `SOL` |
| `direction` | yes | `long` or `short` |

**Response fields**

| Field | Type | Meaning |
|---|---|---|
| `action` | string | `CONFIRM` (take it), `REDUCE` (smaller size), `SKIP` (stand aside) |
| `confidence` | string | `HIGH`, `MEDIUM`, `LOW` |
| `composite_score` | number | 0–100 blended context score for the direction |
| `size_multiplier` | number | Suggested position-size factor (e.g. 1.0, 0.5, 0) |
| `reasons` | string[] | Human-readable context (funding, OI, whale flow, etc.) |

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=ETH&direction=short"
```

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
JSON `{ "error": "...", "message": "..." }` with standard HTTP status codes (`401` invalid/missing key, `402` paid feature, `429` rate-limited).

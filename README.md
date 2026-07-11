# SmartMoneyAPI — API Docs

**Trade-confirmation API for crypto bots.** Your strategy fires a long or short signal; one call to `/v1/confirm` checks derivatives, funding, open interest, liquidations, and whale positioning before your bot enters.

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Fapi.smartmoneyapi.com%2Fv1%2Fstats&label=API%20status&up_message=operational&down_message=degraded&color=22c55e)](https://status.smartmoneyapi.com)
[![Docs](https://img.shields.io/badge/interactive%20docs-smartmoneyapi.com-6366f1)](https://smartmoneyapi.com/docs.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)

---

## Resources

| | |
|---|---|
| Interactive docs | [smartmoneyapi.com/docs.html](https://smartmoneyapi.com/docs.html) |
| Live performance | [smartmoneyapi.com/performance.html](https://smartmoneyapi.com/performance.html) |
| Signal calibration | [smartmoneyapi.com/calibration.html](https://smartmoneyapi.com/calibration.html) |
| Pricing + free key | [smartmoneyapi.com/pricing.html](https://smartmoneyapi.com/pricing.html) |
| Python SDK | [github.com/tashiardit/smartmoneyapi-python](https://github.com/tashiardit/smartmoneyapi-python) |

---

## What's in this repo

| File | Description |
|---|---|
| [`api-reference.md`](api-reference.md) | Full endpoint reference with request/response examples |
| [`openapi.yaml`](openapi.yaml) | OpenAPI 3.0 spec (importable into Postman, Insomnia, etc.) |
| [`examples/quickstart.sh`](examples/quickstart.sh) | curl quickstart |
| [`examples/python_example.py`](examples/python_example.py) | Python (requests) |
| [`examples/node_example.js`](examples/node_example.js) | Node.js (fetch) |

---

## 30-second quickstart

```bash
# Get a free key at https://smartmoneyapi.com/pricing.html
curl -H "X-API-Key: YOUR_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=BTC&direction=long"
```

```json
{
  "symbol": "BTC",
  "direction": "long",
  "action": "CONFIRM_FULL",
  "confidence": "HIGH",
  "composite": 0.74,
  "size_mult": 1.5,
  "coverage": { "derivatives": true, "whale": true, "onchain": true },
  "reasons": ["Funding neutral across venues", "Open interest expanding long", "Whale flow 63% long"]
}
```

`action` ∈ `CONFIRM_FULL` / `CONFIRM_REDUCED` / `CONFIRM_MINIMAL` / `VETO_SKIP` / `NO_DATA_SKIP`.  
`composite` runs -1.0 → +1.0 — a multi-factor confluence read, **not a win-rate**.

---

## Tiers

| Tier | Calls / day | Notes |
|---|---|---|
| Free | 50 | BTC only, public endpoints |
| Trader | 1,000 | All symbols, full screener, liquidation heatmap |
| Pro | 5,000 | + Custom alerts, webhooks, full historical data |
| Enterprise | 100,000 | SLA, custom limits, raw data access |

---

## Authentication

Every request uses the `X-API-Key` header. Never put your key in a URL. Generate a key at [smartmoneyapi.com/dashboard.html](https://smartmoneyapi.com/dashboard.html).

---

> Not financial advice. Crypto trading involves substantial risk. Past signal accuracy does not guarantee future results.

## License

MIT — see [LICENSE](LICENSE).

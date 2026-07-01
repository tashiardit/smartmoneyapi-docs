# SmartMoneyAPI — Docs

**Trade confirmation API for crypto bots.** Your strategy gives a long or short signal; SmartMoneyAPI checks derivatives, funding, open interest, liquidations, whale positioning, and market context before your bot enters.

**What's inside:**
- **`/v1/confirm`** — multi-factor confluence score (derivatives + on-chain + whales) with a transparent per-leg `factors` breakdown. Not a guaranteed win-rate; untracked symbols return an explicit `NO_DATA`.
- **Real multi-exchange liquidation feed** — `/v1/liquidations` returns actual executed forced-liquidations (Binance/OKX/Bybit/Bitget/BitMEX) as a price×time `realized_heatmap`, alongside the leverage-projected estimate.
- **On-chain DeFi liquidations** — `/v1/liquidations/onchain` surfaces executed lending liquidations (Venus, AAVE, Benqi, …) captured from our own local BSC + Avalanche nodes.
- **Working webhooks & alerts** — register HMAC-signed outbound webhooks (`/v1/webhooks`), custom threshold alerts (`/v1/alerts/*`), and an inbound TradingView hook.

- 🌐 Site: https://smartmoneyapi.com
- 📚 Interactive docs: https://smartmoneyapi.com/docs
- 📈 Live performance: https://smartmoneyapi.com/performance
- 🔑 Get a free API key: https://smartmoneyapi.com/signup
- 💳 Pricing: https://smartmoneyapi.com/pricing

> Not financial advice. Crypto trading involves substantial risk, including loss of capital. Past signal accuracy does not guarantee future results.

## Quickstart (2 minutes)

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
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
  "reasons": ["Funding is neutral", "Open interest supports the move", "Whale flow is supportive"]
}
```

Your bot reads `action`: **`CONFIRM_FULL`** (take it, full size), **`CONFIRM_REDUCED` / `CONFIRM_MINIMAL`** (smaller size — see `size_mult`), or **`VETO_SKIP` / `NO_DATA_SKIP`** (stand aside). `composite` runs -1.0 → +1.0 and is a confluence read, **not** a win-rate. See [api-reference.md](api-reference.md) for the full reference and [openapi.yaml](openapi.yaml) for the spec.

## Authentication
All requests use the `X-API-Key` header. Never put your key in a URL. Create a key at https://smartmoneyapi.com/dashboard.

## Examples
- [examples/quickstart.sh](examples/quickstart.sh) — curl
- [examples/python_example.py](examples/python_example.py) — Python (requests)
- [examples/node_example.js](examples/node_example.js) — Node.js (fetch)

## License
MIT

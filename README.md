# SmartMoneyAPI — Docs

**Trade confirmation API for crypto bots.** Your strategy gives a long or short signal; SmartMoneyAPI checks derivatives, funding, open interest, liquidations, whale positioning, and market context before your bot enters.

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
  "action": "CONFIRM",
  "confidence": "HIGH",
  "composite_score": 78,
  "size_multiplier": 1.0,
  "reasons": ["Funding is neutral", "Open interest supports the move", "Whale flow is supportive"]
}
```

Your bot reads `action`: **CONFIRM** (take the trade), **REDUCE** (smaller size — see `size_multiplier`), or **SKIP** (stand aside). See [api-reference.md](api-reference.md) for the full reference and [openapi.yaml](openapi.yaml) for the spec.

## Authentication
All requests use the `X-API-Key` header. Never put your key in a URL. Create a key at https://smartmoneyapi.com/dashboard.

## Examples
- [examples/quickstart.sh](examples/quickstart.sh) — curl
- [examples/python_example.py](examples/python_example.py) — Python (requests)
- [examples/node_example.js](examples/node_example.js) — Node.js (fetch)

## License
MIT

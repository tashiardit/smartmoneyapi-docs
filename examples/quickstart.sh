#!/usr/bin/env bash
# SmartMoneyAPI quickstart — confirm a trade idea before your bot enters.
API_KEY="${SMARTMONEY_API_KEY:?set SMARTMONEY_API_KEY}"

# 1) Confirm a trade idea (reads action / confidence / composite / size_mult)
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=BTC&direction=long" | jq .

# 2) Real executed liquidation heatmap + leverage-projected levels
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations?symbol=BTC" | jq '.realized_heatmap.totals'

# 3) Executed on-chain DeFi liquidations from our BSC/AVAX nodes (Trader+)
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.smartmoneyapi.com/v1/liquidations/onchain?chain=bsc&limit=20" | jq '.count'

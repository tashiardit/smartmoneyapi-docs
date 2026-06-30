#!/usr/bin/env bash
# SmartMoneyAPI quickstart — confirm a trade idea before your bot enters.
API_KEY="${SMARTMONEY_API_KEY:?set SMARTMONEY_API_KEY}"
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.smartmoneyapi.com/v1/confirm?symbol=BTC&direction=long" | jq .

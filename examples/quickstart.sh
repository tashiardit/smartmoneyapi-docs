#!/usr/bin/env bash
# SmartMoneyAPI quickstart.
#
# Calls 1-3 need NO key. Call 4 does. Every response field referenced below was
# observed on a real call while this file was written (2026-08-28) — nothing here
# is illustrative.
set -euo pipefail
BASE="https://api.smartmoneyapi.com"

# 1) What is actually in the deep archive, and how far back it goes.
#    Keyless. Sums to ~115.7M rows across 9 tables, oldest row 2026-03-18.
curl -s "$BASE/v1/history/coverage" \
  | jq '[.tables | to_entries[] | {table: .key,
                                   rows: ((.value.live.rows // 0) + (.value.archive.rows // 0)),
                                   from: (.value.archive.from // .value.live.from)}]'

# 2) Federated read across the live DB and the cold archive in one response.
#    `sources` names every shard the answer came from; `truncated` says whether
#    you hit the row cap. A filter the archive cannot serve from an index is
#    rejected with 400 naming the ones it can, instead of being dropped and
#    quietly answering a wider question than you asked.
curl -s "$BASE/v1/history/whale_positions?symbol=BTC&days=7&limit=5" \
  | jq '{table, count, truncated, window, sources}'

# 3) Executed forced liquidations, bucketed by price and time. Keyless.
curl -s "$BASE/v1/liquidations/heatmap?symbol=BTC" \
  | jq '{symbol, window_minutes, price_buckets, time_bucket_minutes,
         price_min, price_max}'

# 4) Confirm a trade idea. Needs a key (Free tier: BTC, ETH, SOL).
#    Read `action`: CONFIRM_FULL / CONFIRM_REDUCED / CONFIRM_MINIMAL take it at
#    `size_mult` size; VETO_SKIP / NO_DATA_SKIP stand aside. NO_DATA_SKIP means
#    nothing was measured for that symbol — it is not a neutral or weak signal.
: "${SMARTMONEY_API_KEY:?export SMARTMONEY_API_KEY to run step 4}"
curl -s -H "X-API-Key: $SMARTMONEY_API_KEY" \
  "$BASE/v1/confirm?symbol=BTC&direction=long" \
  | jq '{symbol, direction, action, confidence, composite, size_mult}'

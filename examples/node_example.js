// SmartMoneyAPI — executed liquidations and the deep archive, no key required.
// Field names below were observed on real responses on 2026-08-28.
// Not financial advice.

const BASE = 'https://api.smartmoneyapi.com';

async function get(path) {
  const res = await fetch(`${BASE}${path}`, {
    headers: process.env.SMARTMONEY_API_KEY
      ? { 'X-API-Key': process.env.SMARTMONEY_API_KEY }
      : {},
  });
  if (!res.ok) throw new Error(`${path} -> HTTP ${res.status}`);
  return res.json();
}

(async () => {
  // Executed forced liquidations bucketed by price x time. Keyless.
  const heat = await get('/v1/liquidations/heatmap?symbol=BTC');
  console.log(
    `${heat.symbol}: ${heat.price_buckets} price buckets over ` +
    `${heat.window_minutes} min (${heat.price_min} - ${heat.price_max})`
  );

  // Which symbols have a realized liquidation feed at all, and how deep it goes.
  const { symbols } = await get('/v1/liquidations/symbols');
  for (const s of symbols.slice(0, 5)) {
    console.log(`${s.symbol}: ${s.count} events, $${s.total_notional} notional`);
  }

  // How far back the federated archive reaches.
  const cov = await get('/v1/history/coverage');
  const rows = Object.values(cov.tables).reduce(
    (n, t) => n + (t.live?.rows ?? 0) + (t.archive?.rows ?? 0), 0);
  console.log(`archive: ${rows.toLocaleString()} rows across ` +
              `${Object.keys(cov.tables).length} tables`);
})();

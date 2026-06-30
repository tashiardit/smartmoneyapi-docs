// SmartMoneyAPI — confirm a trade idea before entering (Node 18+, fetch).
const API_KEY = process.env.SMARTMONEY_API_KEY;
const BASE = "https://api.smartmoneyapi.com";

async function confirm(symbol, direction) {
  const u = new URL(BASE + "/v1/confirm");
  u.searchParams.set("symbol", symbol);
  u.searchParams.set("direction", direction);
  const r = await fetch(u, { headers: { "X-API-Key": API_KEY } });
  if (!r.ok) throw new Error("HTTP " + r.status);
  return r.json();
}

confirm("BTC", "long").then(res => {
  console.log(res.action, res.confidence, res.composite_score);
}); // Not financial advice. Crypto trading involves risk.

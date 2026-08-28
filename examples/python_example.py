"""SmartMoneyAPI — confirm a trade idea, then check it against the archive.

Every field read below was observed on a real response on 2026-08-28.
Not financial advice. `composite` is a confluence read, not a win-rate.
"""
import os

import requests

BASE = "https://api.smartmoneyapi.com"
TIMEOUT = 20


def confirm(symbol: str, direction: str, api_key: str) -> dict:
    """Multi-factor confluence check. Needs a key; Free tier covers BTC/ETH/SOL."""
    r = requests.get(f"{BASE}/v1/confirm",
                     params={"symbol": symbol, "direction": direction},
                     headers={"X-API-Key": api_key}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def whale_history(symbol: str, days: int = 7, limit: int = 500) -> dict:
    """Federated read across the live DB and the cold archive. No key needed.

    `sources` names every shard the answer came from. A filter the archive
    cannot serve from an index is REJECTED with 400 naming the ones it can
    (measured: `direction=long` over 200 days returns "filter direction has no
    index on whale_positions ... supported filters: symbol, wallet"), rather
    than being dropped and quietly answering a wider question than you asked.
    """
    r = requests.get(f"{BASE}/v1/history/whale_positions",
                     params={"symbol": symbol, "days": days, "limit": limit},
                     timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    hist = whale_history("BTC")
    print(f"{hist['count']} rows from {hist['sources']}, "
          f"truncated={hist['truncated']}")

    key = os.environ.get("SMARTMONEY_API_KEY")
    if not key:
        raise SystemExit("set SMARTMONEY_API_KEY for the /v1/confirm call")

    res = confirm("BTC", "long", key)
    print(res["action"], res["confidence"], res["composite"])
    if res["action"] == "NO_DATA_SKIP":
        # Explicit "nothing was measured", NOT a weak or neutral signal.
        print("No coverage for this symbol — stand aside.")
    elif res["action"].startswith("CONFIRM"):
        print(f"Enter at size x{res['size_mult']}")
    else:
        print("Standing aside:", res["action"])

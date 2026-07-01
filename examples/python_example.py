"""SmartMoneyAPI — confirm a trade idea before entering (Python, requests)."""
import os, requests

API_KEY = os.environ["SMARTMONEY_API_KEY"]
BASE = "https://api.smartmoneyapi.com"

def confirm(symbol: str, direction: str) -> dict:
    r = requests.get(f"{BASE}/v1/confirm",
                     params={"symbol": symbol, "direction": direction},
                     headers={"X-API-Key": API_KEY}, timeout=10)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    res = confirm("BTC", "long")
    print(res["action"], res["confidence"], res["composite"])
    if res["action"].startswith("CONFIRM"):
        print(f"Enter at size x{res['size_mult']}")
    else:
        print("Standing aside:", res["action"])  # VETO_SKIP / NO_DATA_SKIP
# Not financial advice. Crypto trading involves risk.

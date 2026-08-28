#!/usr/bin/env python3
"""Regenerate this repository from the live SmartMoneyAPI OpenAPI document.

This repo is a MIRROR. Nothing in openapi.yaml or api-reference.md is written by
hand — both are emitted by this script from the canonical spec the API itself
serves at https://smartmoneyapi.com/openapi.json. A hand-maintained mirror is
exactly what went stale before (it documented /v1/alerts/conditions/{id}, a route
that had been renamed to {condition_id} and answered 404), so the selection rule
below is executable rather than a list someone has to remember to update.

    python3 tools/build_public_spec.py                      # fetch the live spec
    python3 tools/build_public_spec.py --source local.json  # use a local copy
    python3 tools/build_public_spec.py --check              # CI: fail if stale

SELECTION RULE — an operation from the live spec is published here iff ALL of:

  1. Its HTTP method is GET. This mirror is a read-only DATA contract. Nothing
     that mutates state (creating alert rules, registering webhooks, minting
     WebSocket tickets, posting analytics events) is published, so a generated
     client built from this file cannot change anything in an account.
     ONE stated exception: the /rpc/v1/* JSON-RPC proxies are POST because
     JSON-RPC is a POST protocol, not because they change anything of ours —
     they are the transport of a read-only node product a customer buys, so
     they are published (see RPC_TRANSPORT_PREFIX).

  2. It carries the gateway's own `x-auth` and `x-tier` extensions. Those are
     derived in the upstream generator from the gateway's PUBLIC_DATA_ENDPOINTS
     set and from plans.json, not typed by hand, so the keyless/tier gating
     published here is the gating the server actually enforces. An operation
     missing them is not published, because its access contract is unknown.

  3. Its namespace (the path segment after /v1, or the /rpc/v1 prefix) is not in
     ACCOUNT_NAMESPACES below — the surface that acts on *your account* or on our
     own operations rather than returning market data. Those routes exist and are
     documented for signed-in users at https://smartmoneyapi.com/docs; they are
     left out of the public mirror because no integration calls them and
     publishing them only widens the surface people probe.

Everything else in the live spec is published, including paid tiers: a customer
evaluating the API should be able to read the exact shape of what a subscription
buys before paying for it.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import urllib.error
import urllib.request

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

LIVE_SPEC_URL = "https://smartmoneyapi.com/openapi.json"

# The single stated exception to the GET-only rule. JSON-RPC is a POST protocol;
# these proxy read-only node calls (eth_call, eth_getLogs, …) and change nothing
# in an account, so withholding them would hide a product rather than reduce the
# mutable surface.
RPC_TRANSPORT_PREFIX = "/rpc/v1/"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_OUT = os.path.join(REPO, "openapi.yaml")
REF_OUT = os.path.join(REPO, "api-reference.md")

# Namespaces deliberately withheld from the public mirror, each with the reason.
# Rule 3 above. Keep the reason — an entry with no reason is a hand-written list
# creeping back in.
ACCOUNT_NAMESPACES = {
    "alerts":       "per-account alert-condition configuration",
    "whale-alerts": "per-account whale alert rules and their delivery history",
    "webhooks":     "per-account outbound webhook registration",
    "referrals":    "affiliate programme; account- and payout-scoped",
    "portfolio":    "your own tracked holdings",
    "preferences":  "your own UI/account preferences",
    "watchlist":    "your own saved symbols",
    "serenity":     "one partner's curated list, not a product surface",
    "booking":      "sales-call scheduling",
    "contact":      "sales/contact form intake",
    "telegram":     "linking a Telegram account to yours",
    "assistant":    "signed-in chat assistant; not a data endpoint",
    "data":         "billing/purchase records for your account",
    "ws":           "mints a short-lived socket ticket for a signed-in session",
    "shadow-gate":  "internal research gate, not sold",
    "copytrade":    "internal shadow-book research, not sold",
    "track":        "first-party analytics ingest",
    "usage":        "your own account's quota counters",
}


def namespace(path: str) -> str:
    parts = [p for p in path.split("/") if p]
    if not parts:
        return ""
    if parts[0] == "rpc":
        return "rpc"
    if parts[0] == "v1":
        return parts[1] if len(parts) > 1 else ""
    return parts[0]


def load_spec(source: str) -> dict:
    if source.startswith(("http://", "https://")):
        with urllib.request.urlopen(source, timeout=60) as r:  # noqa: S310
            return json.loads(r.read().decode("utf-8"))
    with open(source, encoding="utf-8") as fh:
        return json.load(fh)


def select(spec: dict) -> tuple[dict, dict]:
    """Return (published_paths, stats)."""
    out, dropped = {}, {"method": 0, "no_gating": 0, "account": 0}
    for path, item in spec.get("paths", {}).items():
        ns = namespace(path)
        kept = {}
        for method, op in item.items():
            if not isinstance(op, dict):
                continue
            is_rpc = path.startswith(RPC_TRANSPORT_PREFIX)
            if method.lower() != "get" and not is_rpc:       # rule 1
                dropped["method"] += 1
                continue
            if "x-auth" not in op or "x-tier" not in op:     # rule 2
                dropped["no_gating"] += 1
                continue
            if ns in ACCOUNT_NAMESPACES:                     # rule 3
                dropped["account"] += 1
                continue
            kept[method] = op
        if kept:
            for shared in ("parameters", "summary", "description"):
                if shared in item:
                    kept[shared] = item[shared]
            out[path] = kept
    return dict(sorted(out.items())), dropped


RULE_TEXT = (
    "HOW THIS FILE IS PRODUCED — it is generated, never hand-edited.\n"
    "\n"
    "It is a filtered mirror of the document the API itself serves at "
    "https://smartmoneyapi.com/openapi.json, emitted by "
    "tools/build_public_spec.py in github.com/tashiardit/smartmoneyapi-docs. "
    "An operation from the live document appears here iff all three hold:\n"
    "\n"
    "  1. The method is GET. This mirror is a read-only DATA contract; nothing "
    "that mutates state or account configuration is published, so a client "
    "generated from this file cannot change anything in an account.\n"
    "  2. It carries x-auth and x-tier. Upstream those are derived from the "
    "gateway's own public-endpoint set and from plans.json rather than written "
    "by hand, so the gating printed on each operation here is the gating the "
    "server enforces.\n"
    "  3. Its namespace is not account-management or internal — the withheld "
    "set is listed in tools/build_public_spec.py with a reason for each, and "
    "covers routes that act on your account (alerts, webhooks, watchlist, "
    "portfolio, preferences, referrals, usage, telegram, assistant, purchases, "
    "socket tickets) or on our own operations.\n"
    "\n"
    "One stated exception to (1): the /rpc/v1/* JSON-RPC proxies are POST "
    "because JSON-RPC is a POST protocol, not because they change anything of "
    "ours. They proxy read-only node calls, so they are published.\n"
    "\n"
    "Paid tiers ARE published: you should be able to read the exact shape of "
    "what a subscription returns before paying for it. Per-operation x-auth "
    "says whether a key is needed at all; x-tier names the plan that unlocks "
    "it. Public operations answer without a key at a reduced row cap and a "
    "per-IP throttle."
)


def build(spec: dict, source: str) -> tuple[dict, dict]:
    paths, dropped = select(spec)
    live_desc = spec.get("info", {}).get("description", "").strip()
    generated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")
    out = {
        "openapi": spec.get("openapi", "3.0.3"),
        "info": {
            "title": spec.get("info", {}).get("title", "Smart Money API"),
            "version": spec.get("info", {}).get("version", "1.0.0"),
            "description": (
                f"{live_desc}\n\n{RULE_TEXT}\n\n"
                f"Mirror generated {generated} from {source}: "
                f"{len(paths)} of {len(spec.get('paths', {}))} live paths."
            ),
            "contact": spec.get("info", {}).get(
                "contact", {"url": "https://smartmoneyapi.com"}),
            "license": {"name": "MIT",
                        "url": "https://opensource.org/licenses/MIT"},
        },
        "servers": spec.get("servers", [{"url": "https://api.smartmoneyapi.com"}]),
        "security": spec.get("security", [{"ApiKeyAuth": []}]),
        "components": spec.get("components", {}),
        "paths": paths,
    }
    return out, dropped


# ---------------------------------------------------------------- reference md

def _params(op: dict, item: dict) -> list:
    seen, out = set(), []
    for p in list(item.get("parameters", [])) + list(op.get("parameters", [])):
        if not isinstance(p, dict) or p.get("name") in seen:
            continue
        seen.add(p.get("name"))
        out.append(p)
    return out


def _fields(op: dict) -> list:
    try:
        schema = (op["responses"]["200"]["content"]["application/json"]["schema"])
    except (KeyError, TypeError):
        return []
    props = schema.get("properties") or {}
    if not props and schema.get("type") == "array":
        props = (schema.get("items") or {}).get("properties") or {}
    return sorted(props.items())


def reference_md(spec: dict, source: str, live_total: int) -> str:
    generated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")
    groups: dict[str, list] = {}
    for path, item in spec["paths"].items():
        for method, op in item.items():
            if not isinstance(op, dict) or "x-auth" not in op:
                continue
            tag = (op.get("tags") or ["Other"])[0]
            groups.setdefault(tag, []).append((path, method.upper(), op, item))

    L = [
        "# SmartMoneyAPI — API reference",
        "",
        "**Generated file — do not hand-edit.** Produced by "
        "`tools/build_public_spec.py` from the live OpenAPI document at "
        f"<{source}>, on {generated}. It documents "
        f"{len(spec['paths'])} of the {live_total} paths the live API routes; "
        "the selection rule is stated in [openapi.yaml](openapi.yaml) and "
        "implemented in [tools/build_public_spec.py](tools/build_public_spec.py).",
        "",
        "Base URL: `https://api.smartmoneyapi.com`",
        "",
        "Auth: send `X-API-Key: <key>` on every request. Operations marked "
        "**keyless** answer without one, at a reduced row cap and a per-IP "
        "throttle. Never put a key in a URL.",
        "",
        "Errors: `429` is a quota or throttle rejection; `403` means your tier "
        "does not include that operation or symbol. Errors a browser can reach "
        "are returned as `503`, never `502`/`504`.",
        "",
        "> Not financial advice. Scores are a multi-factor confluence read, not "
        "a guaranteed win-rate. Past signal accuracy does not guarantee future "
        "results.",
        "",
        "## Contents",
        "",
    ]
    for tag in sorted(groups):
        anchor = tag.lower().replace(" ", "-").replace("/", "").replace("&", "")
        n = len(groups[tag])
        L.append(f"- [{tag}](#{anchor}) — {n} endpoint{'' if n == 1 else 's'}")
    L.append("")

    for tag in sorted(groups):
        L += [f"## {tag}", ""]
        for path, method, op, item in sorted(groups[tag]):
            keyless = op.get("x-auth") == "none"
            gate = "keyless" if keyless else f"key required — {op.get('x-tier')}"
            L += [f"### `{method} {path}`", ""]
            if op.get("summary"):
                L.append(f"**{op['summary']}** — {gate}")
            else:
                L.append(gate)
            L.append("")
            desc = (op.get("description") or "").strip()
            if desc:
                L += [desc, ""]
            params = _params(op, item)
            if params:
                L += ["| Parameter | In | Required | Description |",
                      "|---|---|---|---|"]
                for p in params:
                    d = (p.get("description") or "").replace("|", "\\|")
                    sch = p.get("schema") or {}
                    if sch.get("enum"):
                        d += (" One of: " +
                              ", ".join(f"`{e}`" for e in sch["enum"]) + ".")
                    if sch.get("default") is not None:
                        d += f" Default `{sch['default']}`."
                    L.append(f"| `{p.get('name')}` | {p.get('in')} | "
                             f"{'yes' if p.get('required') else 'no'} | "
                             f"{d.strip()} |")
                L.append("")
            fields = _fields(op)
            if fields:
                L += ["Response fields:", "",
                      "| Field | Type | Description |", "|---|---|---|"]
                for name, sch in fields:
                    if not isinstance(sch, dict):
                        sch = {}
                    typ = sch.get("type") or "—"
                    d = (sch.get("description") or "").replace("|", "\\|")
                    L.append(f"| `{name}` | {typ} | {d} |")
                L.append("")
            key_hdr = "" if keyless else '-H "X-API-Key: $SMARTMONEY_API_KEY" '
            if method == "POST":
                L += ["```bash",
                      f'curl -X POST {key_hdr}\\\n  -H "Content-Type: '
                      f'application/json" \\\n  -d \'{{"jsonrpc":"2.0","id":1,'
                      f'"method":"eth_blockNumber","params":[]}}\' \\\n  '
                      f'"https://api.smartmoneyapi.com{path}"',
                      "```", ""]
            else:
                L += ["```bash",
                      f'curl {key_hdr}\\\n  '
                      f'"https://api.smartmoneyapi.com{path}"',
                      "```", ""]
    L += ["---", "",
          "Regenerate: `python3 tools/build_public_spec.py`. "
          "Verify freshness in CI: `python3 tools/build_public_spec.py --check`.",
          ""]
    return "\n".join(L)


# ------------------------------------------------------------------- measuring
#
# The live document leaves the 200 response schema empty for most operations, so
# a mirror that only copied it would document endpoint names and nothing about
# what comes back. Rather than hand-write shapes — the exact thing that rots —
# --measure CALLS each keyless operation that needs no parameters and records the
# field names and JSON types it actually returned. Only names and types are
# recorded; no values are copied out of a response. Every operation touched this
# way is stamped with x-response-measured (the date) and x-response-note, so a
# reader can tell a measured shape from one the API itself declares, and can tell
# how old the measurement is. Nothing is guessed: an operation that could not be
# called keeps whatever the live document said about it, and the run prints how
# many that was.

_JSON_TYPE = {dict: "object", list: "array", str: "string", bool: "boolean",
              int: "integer", float: "number", type(None): None}


def _observe(value) -> dict:
    t = _JSON_TYPE.get(type(value))
    return {"type": t} if t else {}


def measure(spec: dict, base: str) -> dict:
    """Fill empty 200 schemas from what the live API actually returns."""
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")
    stats = {"measured": 0, "skipped": 0, "failed": 0, "corrected": 0}
    for path, item in spec["paths"].items():
        op = item.get("get")
        if not op or op.get("x-auth") != "none" or "{" in path:
            stats["skipped"] += 1
            continue
        params = list(item.get("parameters", [])) + list(op.get("parameters", []))
        if any(p.get("required") for p in params if isinstance(p, dict)):
            stats["skipped"] += 1
            continue
        try:
            with urllib.request.urlopen(base + path, timeout=30) as r:  # noqa: S310
                body = json.loads(r.read().decode("utf-8"))
        except Exception:
            stats["failed"] += 1
            continue
        try:
            schema = op["responses"]["200"]["content"]["application/json"]["schema"]
        except (KeyError, TypeError):
            continue
        if isinstance(body, list):
            if schema.get("type") != "array":
                op["responses"]["200"]["content"]["application/json"]["schema"] = {
                    "type": "array",
                    "items": _observe(body[0]) if body else {},
                }
                stats["corrected"] += 1
            sample = body[0] if body and isinstance(body[0], dict) else None
            target = op["responses"]["200"]["content"]["application/json"]["schema"]
            target.setdefault("items", {})
            if sample:
                props = target["items"].setdefault("properties", {})
                for k, v in sample.items():
                    props.setdefault(k, _observe(v))
        elif isinstance(body, dict):
            if schema.get("type") not in (None, "object"):
                schema["type"] = "object"
                stats["corrected"] += 1
            schema.setdefault("type", "object")
            props = schema.setdefault("properties", {})
            for k, v in body.items():
                if k in props and isinstance(props[k], dict):
                    if not props[k].get("type"):
                        props[k].update(_observe(v))
                else:
                    props.setdefault(k, _observe(v))
            schema["properties"] = dict(sorted(props.items()))
        else:
            continue
        op["x-response-measured"] = stamp
        op["x-response-note"] = (
            "Field names and types below were recorded from one real response on "
            + stamp + ", not written by hand. A field absent from that response "
            "is absent here even if the endpoint can return it, and optional "
            "fields are not marked required. Treat this as a floor, not a "
            "closed set.")
        stats["measured"] += 1
    return stats


class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _str_presenter(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_presenter)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", default=LIVE_SPEC_URL,
                    help=f"live spec URL or local path (default {LIVE_SPEC_URL})")
    ap.add_argument("--measure", metavar="BASE_URL", default=None,
                    help="call each keyless, parameterless GET against BASE_URL "
                         "and record the field names/types it really returns "
                         "into the empty response schemas")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the committed files differ from a rebuild")
    args = ap.parse_args()

    live = load_spec(args.source)
    label = (args.source if args.source.startswith("http")
             else f"{LIVE_SPEC_URL} (read from a local copy)")
    spec, dropped = build(live, label)
    measured = measure(spec, args.measure.rstrip("/")) if args.measure else None
    ref = reference_md(spec, label, len(live.get("paths", {})))
    yml = yaml.dump(spec, Dumper=_Dumper, sort_keys=False,
                    allow_unicode=True, width=100)

    ops = [o for i in spec["paths"].values() for o in i.values()
           if isinstance(o, dict) and "x-auth" in o]
    keyless = sum(1 for o in ops if o.get("x-auth") == "none")
    print(f"live paths      : {len(live.get('paths', {}))}")
    print(f"published paths : {len(spec['paths'])} ({len(ops)} operations, "
          f"{keyless} keyless)")
    print(f"withheld        : {dropped['method']} non-GET, "
          f"{dropped['account']} account/internal, "
          f"{dropped['no_gating']} missing x-auth/x-tier")
    if measured is not None:
        print(f"measured shapes : {measured['measured']} operations "
              f"({measured['corrected']} declared type corrected to match the "
              f"real response), {measured['failed']} calls failed, "
              f"{measured['skipped']} not callable without a key/parameter")

    if args.check:
        stale = []
        for out, new in ((SPEC_OUT, yml), (REF_OUT, ref)):
            cur = open(out, encoding="utf-8").read() if os.path.exists(out) else ""
            # Dates move every run; --check is about STRUCTURAL drift — a route
            # that appeared, vanished or was renamed. Drop the date-bearing
            # lines and compare everything else.
            def f(s):
                skip = ("Mirror generated", ", on 20", "x-response-measured",
                        "response on 20")
                return [ln for ln in s.splitlines()
                        if not any(k in ln for k in skip)]
            if f(cur) != f(new):
                stale.append(os.path.basename(out))
        if stale:
            print("STALE (rerun without --check): " + ", ".join(stale))
            return 1
        print("up to date with the live spec")
        return 0

    with open(SPEC_OUT, "w", encoding="utf-8") as fh:
        fh.write(yml)
    with open(REF_OUT, "w", encoding="utf-8") as fh:
        fh.write(ref)
    print(f"wrote {os.path.relpath(SPEC_OUT, REPO)} and "
          f"{os.path.relpath(REF_OUT, REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

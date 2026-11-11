#!/usr/bin/env python3
"""Expected 5-year CAGR of a stock at the current price, from the latest assumptions in <ticker>/history.csv.

Usage:
  python3 expected_cagr.py FTNT --price 123.45 [--price-date 2026-11-10] [--source "..."]
  python3 expected_cagr.py all --price AMZN=270.87 --price FTNT=123.57 ... [--price-date ...] [--source "..."]

The current prices come from the stock-quote skill (not fetched here).

One ticker: prints a JSON object (latest quarter, assumptions, current price with source and date,
fair price, gap with the fair price, CAGR per scenario at the current price and at the fair price).
"all": prints a JSON list of the same objects for every <ticker>/history.csv, sorted by the neutral
CAGR at the current price, descending (one --price TICKER=value per ticker).
Prices and market caps are in the stock's reporting currency (see "currency").
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
SCENARIOS = ["pessimistic", "neutral", "optimistic"]


def latest_rows(ticker):
    path = REPO / ticker.lower() / "history.csv"
    if not path.exists():
        raise SystemExit(f"{path} not found: unknown ticker")
    rows = list(csv.DictReader(path.open()))
    # last quarter in the file (rows are appended in chronological order)
    quarter = rows[-1]["quarter"]
    latest = [r for r in rows if r["quarter"] == quarter]
    # the most recent update of that quarter, if rewritten
    date = max(r["date"] for r in latest)
    latest = {r["scenario"]: r for r in latest if r["date"] == date}
    return quarter, date, latest


def col(row, prefix):
    return next(k for k in row if k.startswith(prefix))


def compute(ticker, price, price_date, source):
    quarter, date, rows = latest_rows(ticker)
    any_row = rows["neutral"]
    fair_col = col(any_row, "fair_price_")
    currency = fair_col.rsplit("_", 1)[1].upper()
    mcap_col = col(any_row, "end_mcap_")
    base_col = next(k for k in any_row if k.startswith("base_") and k != "base_definition")
    end_col = next(k for k in any_row if k.startswith("end_") and k not in (mcap_col, "end_multiple"))
    fair, shares = float(any_row[fair_col]), float(any_row["shares_m"])

    out = {
        "ticker": ticker, "quarter": quarter, "assumptions_date": date,
        "base_definition": any_row["base_definition"], "base": float(any_row[base_col]),
        "currency": currency, "shares_m": shares,
        "price": price, "price_date": price_date, "price_source": source,
        "fair_price": fair, "gap_pct": round((price / fair - 1) * 100, 1),
        "scenarios": {},
    }
    for s in SCENARIOS:
        r = rows[s]
        end_price = float(r[mcap_col]) / shares
        out["scenarios"][s] = {
            "growth_pct": round(float(r["growth_5y"]) * 100, 1),
            "end_multiple": float(r["end_multiple"]),
            "end_metric": float(r[end_col]),
            "end_mcap": float(r[mcap_col]),
            "end_price": round(end_price, 1),
            "cagr_at_price_pct": round(((end_price / price) ** 0.2 - 1) * 100, 1),
            "cagr_at_fair_price_pct": round(((end_price / fair) ** 0.2 - 1) * 100, 1),
        }
    return out


def main(argv):
    target = argv[0].upper()
    prices = [argv[i + 1] for i, a in enumerate(argv) if a == "--price"]

    def opt(name):
        return argv[argv.index(name) + 1] if name in argv else None

    price_date, source = opt("--price-date"), opt("--source") or "stock-quote skill"
    if not prices:
        sys.exit("--price is required (get it with the stock-quote skill)")

    if target != "ALL":
        print(json.dumps(compute(target, float(prices[0]), price_date, source), indent=2))
        return

    by_ticker = {k.upper(): float(v) for k, v in (p.split("=") for p in prices)}
    tickers = sorted(p.parent.name.upper() for p in REPO.glob("*/history.csv"))
    missing = [t for t in tickers if t not in by_ticker]
    if missing:
        sys.exit(f"missing --price TICKER=value for: {', '.join(missing)}")
    results = [compute(t, by_ticker[t], price_date, source) for t in tickers]
    results.sort(key=lambda r: r["scenarios"]["neutral"]["cagr_at_price_pct"], reverse=True)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])

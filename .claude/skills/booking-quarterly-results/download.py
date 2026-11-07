#!/usr/bin/env python3
"""Download Booking Holdings' quarterly documents from the Booking IR site (q4cdn file host).

Usage: download.py <year> <quarter>      e.g. download.py 2026 3
Saves under bkng/documents/earnings/<year> Q<n>/ (relative to the project root).
"""
import json, os, subprocess, sys, tempfile, urllib.error, urllib.parse, urllib.request

LIST_URL = "https://ir.bookingholdings.com/feed/FinancialReport.svc/GetFinancialReportList?" + urllib.parse.urlencode({
    "LanguageId": 1,
    "reportTypes": "First Quarter|Second Quarter|Third Quarter|Fourth Quarter|",
    "pageSize": -1, "pageNumber": 0, "tagList": "", "includeTags": "true", "year": -1, "excludeSelection": 1})
HOST = "https://s25.q4cdn.com/383369491"  # some older entries have a path relative to this host
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SUBTYPE = {1: "First Quarter", 2: "Second Quarter", 3: "Third Quarter", 4: "Fourth Quarter"}
# DocumentCategory -> local name suffix (webcast is a link to a player, not a file)
SUFFIX = {"news": "Press-Release", "presentation": "Presentation", "other": "Prepared-Remarks", "transcript": "Transcript"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "BKNG valuation script"}), timeout=60) as r:
        return r.read()


def save(dest, data):
    if os.path.exists(dest):
        print(f"already present: {dest}")
        return
    if not data.startswith(b"%PDF"):
        print(f"ERROR: not a PDF, not saved: {dest}")
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(dest), delete=False) as t:
        t.write(data)
    os.replace(t.name, dest)
    print(f"downloaded: {dest} ({len(data)} bytes)")


def main(year, q):
    reports = json.loads(get(LIST_URL))["GetFinancialReportListResult"]
    rep = next((r for r in reports if r["ReportYear"] == year and r["ReportSubType"] == SUBTYPE[q]), None)
    if not rep:
        sys.exit(f"MISSING: no report for {year} Q{q} on the IR site yet")
    out = os.path.join(ROOT, "bkng", "documents", "earnings", f"{year} Q{q}")
    for d in rep["Documents"]:
        cat = d["DocumentCategory"]
        if cat == "filing":
            suffix = "10-K" if q == 4 else "10-Q"
        elif cat in SUFFIX:
            suffix = SUFFIX[cat]
        else:
            continue
        path = d["DocumentPath"]
        url = HOST + path if path.startswith("/") else path
        dest = os.path.join(out, f"BKNG-{year}-Q{q}-{suffix}.pdf")
        if os.path.exists(dest):
            print(f"already present: {dest}")
            continue
        try:
            save(dest, get(url))
        except urllib.error.HTTPError as err:
            print(f"ERROR: HTTP {err.code} for {url}")
    have = {d["DocumentCategory"] for d in rep["Documents"]}
    for cat, name in SUFFIX.items():
        if cat not in have:
            print(f"MISSING: no {name} listed for {year} Q{q}")


if __name__ == "__main__":
    try:
        main(int(sys.argv[1]), int(sys.argv[2]))
    except urllib.error.HTTPError as err:
        sys.exit(f"STOP: HTTP {err.code} from the IR site; do not work around it, tell the user.")

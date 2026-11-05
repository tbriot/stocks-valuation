#!/usr/bin/env python3
"""Download Fortinet's 10-Q/10-K and earnings press release (8-K exhibit 99.1) from SEC EDGAR.

Usage: download.py <year> <quarter>      e.g. download.py 2026 3
Saves under ftnt/documents/earnings/<year> Q<n>/ (relative to the project root).
"""
import json, os, re, subprocess, sys, tempfile, time, urllib.request, urllib.error

CIK = "1262039"
# EDGAR requires a descriptive User-Agent with a contact e-mail. It is not written in the repository (public):
# it comes from EDGAR_USER_AGENT (for example "Your Name you@example.com"), else from `git config user.email`.
UA = os.environ.get("EDGAR_USER_AGENT") or "FTNT valuation " + subprocess.run(
    ["git", "config", "user.email"], capture_output=True, text=True).stdout.strip()
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
END = {1: "03-31", 2: "06-30", 3: "09-30", 4: "12-31"}


def get(url):
    time.sleep(0.2)  # stay well under EDGAR's 10 requests per second
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def save(dest, data):
    if os.path.exists(dest):
        print(f"already present: {dest}")
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(dest), delete=False) as t:
        t.write(data)
    os.replace(t.name, dest)
    print(f"downloaded: {dest} ({len(data)} bytes)")


def main(year, q):
    rec = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK.zfill(10)}.json"))["filings"]["recent"]
    rows = [dict(zip(rec, v)) for v in zip(*rec.values())]
    period = f"{year}-{END[q]}"
    form = "10-K" if q == 4 else "10-Q"
    out = os.path.join(ROOT, "ftnt", "documents", "earnings", f"{year} Q{q}")

    # 10-Q / 10-K
    f = next((r for r in rows if r["form"] == form and r["reportDate"] == period), None)
    if f:
        acc = f["accessionNumber"].replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}/{f['primaryDocument']}"
        print(f"{form} filed {f['filingDate']}: {url}")
        save(os.path.join(out, f"FTNT-{year}-Q{q}-{form}.htm"), get(url))
    else:
        print(f"MISSING: no {form} for {period} on EDGAR yet")

    # Earnings press release: 8-K item 2.02, filed after the period end, first one
    cands = sorted((r for r in rows if r["form"] == "8-K" and "2.02" in r["items"]
                    and r["filingDate"] > period), key=lambda r: r["filingDate"])
    if not cands:
        print("MISSING: no earnings 8-K yet (press release)")
        return
    e = cands[0]
    acc = e["accessionNumber"].replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}/index.json"))
    ex = next((i["name"] for i in idx["directory"]["item"] if re.search(r"ex-?99", i["name"], re.I)
               and i["name"].endswith((".htm", ".html"))), None)
    if not ex:
        print("MISSING: exhibit 99.1 not found in the 8-K")
        return
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}/{ex}"
    print(f"Press release (8-K filed {e['filingDate']}): {url}")
    save(os.path.join(out, f"FTNT-{year}-Q{q}-Press-Release.htm"), get(url))


if __name__ == "__main__":
    try:
        main(int(sys.argv[1]), int(sys.argv[2]))
    except urllib.error.HTTPError as err:
        sys.exit(f"STOP: EDGAR answered HTTP {err.code}; do not work around it, tell the user.")

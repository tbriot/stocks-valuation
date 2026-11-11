#!/usr/bin/env python3
"""Download Uber's quarterly documents from the Uber IR file host (s23.q4cdn.com/407969754).

Usage: download.py <year> <quarter>      e.g. download.py 2026 3
Saves under uber/documents/earnings/<year> Q<n>/ (relative to the project root).

The IR site has no document list: the URLs are predicted. Folders and file names vary a little from
one quarter to the next, so each document has several candidate URLs, tried in order. Some files sit
under doc_events/<year>/<Mon>/<day>/ (the earnings date): the days of the two months after the
quarter end are scanned for those.
"""
import datetime, os, sys, tempfile, urllib.error, urllib.request

HOST = "https://s23.q4cdn.com/407969754/files"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def request(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": "UBER valuation script"})
    return urllib.request.urlopen(req, timeout=60)


def exists(url):
    try:
        with request(url, "HEAD") as r:
            return r.status == 200
    except urllib.error.HTTPError as err:
        if err.code in (403, 404):
            return False
        raise


def event_dates(year, q):
    """Days of the two months after the quarter end (Q4: the next year's January and February)."""
    month = q * 3 + 1
    for m in (month, month + 1):
        y, mm = (year + 1, m - 12) if m > 12 else (year, m)
        d = datetime.date(y, mm, 1)
        while d.month == mm:
            yield d
            d += datetime.timedelta(days=1)


def candidates(kind, year, q):
    yy = year % 100
    base = f"{HOST}/doc_earnings/{year}/q{q}"
    if kind == "Press-Release":
        yield f"{base}/earnings-result/Uber-Q{q}-{yy}-Earnings-Press-Release.pdf"
    elif kind == "Supplemental-Data":
        name = f"Uber-Q{q}-{yy}-Earnings-Supplemental-Data.pdf"
        yield f"{base}/supplemental-info/{name}"
        yield from (f"{HOST}/doc_events/{d.year}/{d:%b}/{d:%d}/{name}" for d in event_dates(year, q))
    elif kind == "Prepared-Remarks":
        yield f"{base}/transcript/Uber-Q{q}-{yy}-Prepared-Remarks.pdf"
    elif kind == "Transcript":
        for name in (f"Uber-Q{q}-{yy}-Earnings-Call-Transcript.pdf", f"Uber-Q{q}-Earnings-Call-Transcript.pdf"):
            yield f"{HOST}/doc_financials/{year}/q{q}/{name}"
            yield from (f"{HOST}/doc_events/{d.year}/{d:%b}/{d:%d}/{name}" for d in event_dates(year, q))


def save(dest, url):
    with request(url) as r:
        data = r.read()
    if not data.startswith(b"%PDF"):
        print(f"ERROR: not a PDF, not saved: {url}")
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(dest), delete=False) as t:
        t.write(data)
    os.replace(t.name, dest)
    print(f"downloaded: {dest} ({len(data)} bytes) from {url}")


def main(year, q):
    out = os.path.join(ROOT, "uber", "documents", "earnings", f"{year} Q{q}")
    for kind in ("Press-Release", "Supplemental-Data", "Prepared-Remarks", "Transcript"):
        dest = os.path.join(out, f"UBER-{year}-Q{q}-{kind}.pdf")
        if os.path.exists(dest):
            print(f"already present: {dest}")
            continue
        url = next((u for u in candidates(kind, year, q) if exists(u)), None)
        if url:
            save(dest, url)
        else:
            print(f"MISSING: no {kind} found for {year} Q{q}")


if __name__ == "__main__":
    try:
        main(int(sys.argv[1]), int(sys.argv[2]))
    except urllib.error.HTTPError as err:
        sys.exit(f"STOP: HTTP {err.code} from the IR site; do not work around it, tell the user.")

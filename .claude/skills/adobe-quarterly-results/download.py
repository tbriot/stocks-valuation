#!/usr/bin/env python3
"""Download Adobe's quarterly documents from the Adobe IR "financial documents" page.

Usage: download.py <fiscal_year> <quarter>      e.g. download.py 2026 3
Saves under adbe/documents/earnings/<fiscal_year> Q<n>/ (relative to the project root).
The year and quarter are Adobe's fiscal ones (fiscal year ends the Friday closest to Nov 30).
"""
import os, re, sys, tempfile, urllib.error, urllib.parse, urllib.request
from html.parser import HTMLParser

PAGE = "https://www.adobe.com/investor-relations/financial-documents.html"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
# link label (lowercase) -> local name suffix; the filing is renamed 10-K for Q4
LABELS = {"form 10-q": "10-Q", "form 10-k": "10-K", "earnings press release": "Press-Release",
          "earnings script and slides": "Script-Slides", "earnings transcript": "Transcript",
          "investor datasheet": "Investor-Datasheet"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url), timeout=60) as r:
        return r.read()


class Page(HTMLParser):
    """Collects (fiscal year, section, label, url) for each link; sections are the h3 headings under each h2."""
    def __init__(self):
        super().__init__()
        self.year = self.section = self.tag = self.href = None
        self.text = ""
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.tag = tag if tag in ("h2", "h3", "a") else self.tag
        if tag in ("h2", "h3", "a"):
            self.text = ""
        if tag == "a":
            self.href = dict(attrs).get("href")

    def handle_data(self, data):
        self.text += data

    def handle_endtag(self, tag):
        t = " ".join(self.text.split())
        if tag == "h2":
            m = re.search(r"Fiscal year (\d{4})", t)
            self.year = int(m.group(1)) if m else None
        elif tag == "h3":
            self.section = t
        elif tag == "a" and self.href and self.year:
            self.links.append((self.year, self.section, t, self.href))


def save(dest, data):
    if not data.startswith(b"%PDF"):
        print(f"ERROR: not a PDF, not saved: {dest}")
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(dest), delete=False) as t:
        t.write(data)
    os.replace(t.name, dest)
    print(f"downloaded: {dest} ({len(data)} bytes)")


def main(year, q):
    p = Page()
    p.feed(get(PAGE).decode("utf-8"))
    found = {}
    for y, section, label, href in p.links:
        suffix = LABELS.get(label.lower())
        if y != year or not suffix:
            continue
        # the 10-K is under Q4 or under "Annual reports" of the fiscal year
        if section == f"Q{q}" or (q == 4 and suffix == "10-K" and section in ("Q4", "Annual reports")):
            found.setdefault(suffix, urllib.parse.urljoin(PAGE, href.split("#")[0]))
    if not found:
        sys.exit(f"MISSING: no document for fiscal {year} Q{q} on the IR page yet")
    out = os.path.join(ROOT, "adbe", "documents", "earnings", f"{year} Q{q}")
    for suffix, url in found.items():
        dest = os.path.join(out, f"ADBE-{year}-Q{q}-{suffix}.pdf")
        if os.path.exists(dest):
            print(f"already present: {dest}")
            continue
        try:
            save(dest, get(url))
        except urllib.error.HTTPError as err:
            print(f"ERROR: HTTP {err.code} for {url}")
    expected = ["10-K" if q == 4 else "10-Q", "Press-Release", "Script-Slides", "Transcript"]
    for s in expected:
        if s not in found:
            print(f"MISSING: no {s} listed for fiscal {year} Q{q}")


if __name__ == "__main__":
    try:
        main(int(sys.argv[1]), int(sys.argv[2]))
    except urllib.error.HTTPError as err:
        sys.exit(f"STOP: HTTP {err.code} from the IR site; do not work around it, tell the user.")

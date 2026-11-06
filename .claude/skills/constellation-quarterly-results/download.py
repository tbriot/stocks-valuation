#!/usr/bin/env python3
"""Download Constellation Software (CSU) quarterly documents from csisoftware.com.

Usage: download.py <year> <quarter>   (for example: download.py 2026 2)
Saves into csu/documents/earnings/<year> Q<n>/ at the project root.
"""
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

BASE = "https://www.csisoftware.com/wp-content/uploads"
ROOT = Path(__file__).resolve().parents[3]


def names(kind, y, n):
    yy = str(y)[2:]
    if kind == "MDA":
        return [f"CSI-MDA-Q{n}-{y}-Final"]
    if kind == "Financial-Statements":
        return [f"CSI-Financial-Statement-Q{n}{yy}-Final", f"CSI-Financial-Statements-Q{n}{yy}-Final"]
    return [f"Q{n}-{y}-Shareholder-Report"]


def months(y, n):
    """Upload folders (year, month) from the quarter end to 12 months later."""
    m = n * 3
    out = []
    for k in range(1, 13):
        mm = m + k
        out.append((y + (mm - 1) // 12, (mm - 1) % 12 + 1))
    return [(yy, mm) for yy, mm in out if date(yy, mm, 1) <= date.today()]


def http_code(url):
    r = subprocess.run(["curl", "-s", "-m", "20", "-o", "/dev/null", "-w", "%{http_code} %{content_type}", url],
                       capture_output=True, text=True)
    return r.stdout


def main():
    y, n = int(sys.argv[1]), int(sys.argv[2])
    dest = ROOT / "csu" / "documents" / "earnings" / f"{y} Q{n}"
    dest.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    for kind in ("MDA", "Financial-Statements", "Shareholder-Report"):
        target = dest / f"CSU-{y}-Q{n}-{kind}.pdf"
        if target.exists():
            print(f"{kind}: already present")
            continue
        found = None
        for yy, mm in months(y, n):
            for name in names(kind, y, n):
                url = f"{BASE}/{yy}/{mm:02d}/{name}.pdf"
                code = http_code(url)
                if code.startswith("200") and "pdf" in code:
                    found = url
                    break
                if code.startswith(("403", "429", "503")):
                    sys.exit(f"Blocked ({code}) on {url}: stop, do not work around.")
            if found:
                break
        if not found:
            print(f"{kind}: MISSING (not found under {BASE}/)")
            continue
        part = tmp / target.name
        subprocess.run(["curl", "-fsL", "-o", str(part), found], check=True)
        if b"%PDF" not in part.read_bytes()[:8]:
            print(f"{kind}: ERROR, not a PDF ({found}), left in {part}")
            continue
        part.rename(target)
        print(f"{kind}: downloaded {found}")


if __name__ == "__main__":
    main()

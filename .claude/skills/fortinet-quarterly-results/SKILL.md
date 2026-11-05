---
name: fortinet-quarterly-results
description: Download Fortinet's (FTNT) 10-Q (or 10-K for Q4) and earnings press release as HTML from SEC EDGAR and save them under ftnt/documents/earnings/<year> Q<n>/. Use when the user asks for Fortinet's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Fortinet quarterly results

Fortinet's IR site (`investor.fortinet.com`, including its `static-files/` PDFs) answers 403 to scripted requests: **do not use it**. SEC EDGAR is public and unprotected. It serves HTML (iXBRL), not PDF, so the files are saved as `.htm`.

## What is downloaded

| Document | Source | Local file name |
|---|---|---|
| 10-Q (Q1-Q3) or 10-K (Q4) | EDGAR filing, `reportDate` = quarter end | `FTNT-<year>-Q<n>-10-Q.htm` / `-10-K.htm` |
| Earnings press release | exhibit 99.1 of the 8-K item 2.02 filed after the quarter end | `FTNT-<year>-Q<n>-Press-Release.htm` |

Quarter mapping (calendar fiscal year): Q1 = March 31, Q2 = June 30, Q3 = September 30, Q4 = December 31. Fortinet reports the press release about 4 weeks after quarter end and files the 10-Q about 1 week later, so the 10-Q may be missing for a few days.

NOT available through this skill (manual download in the browser from https://investor.fortinet.com/quarterly-earnings/): the Earnings Presentation, the Prepared Remarks and the Supplemental Financials. The presentation and the supplemental data carry billings, RPO and guidance detail. Ask the user to put them in the same folder as `FTNT-<year>-Q<n>-Presentation.pdf`, `-Prepared-Remarks.pdf`, `-Supplemental.pdf`.

## Target quarter

- Default: the latest quarter. Start from the most recent quarter that has ended and step back until the press release is found.
- If the user names a quarter (for example "2026 Q1"), use that one.

## Procedure

Run from anywhere (the script finds the project root itself):

```
python3 .claude/skills/fortinet-quarterly-results/download.py <year> <quarter>
```

The script queries `https://data.sec.gov/submissions/CIK0001262039.json`, finds the filing, builds the URL under `https://www.sec.gov/Archives/edgar/data/1262039/<accession without dashes>/`, and writes the file through a temporary file. Existing files are never downloaded again ("already present"). It prints what was downloaded, already present or missing.

EDGAR requires a descriptive User-Agent with a contact e-mail. The repository is public, so the address is not written in the script: it is read from the `EDGAR_USER_AGENT` environment variable (for example `Your Name you@example.com`), else from `git config user.email`. Keep to a few requests; EDGAR's limit is 10 per second.

Then summarise: quarter, files downloaded, already present, missing (including the three manual documents above).

## Reading the files

The files are HTML, not PDF. Convert to text in `/tmp` before reading, for example with Python (`html.parser` or BeautifulSoup if installed) or `python3 -c` with `re` to strip tags, then grep the passages needed. The 10-Q is long: search it instead of reading it all.

## If something goes wrong

- Missing 10-Q or press release: report it without failing.
- HTTP 403 or 429 from EDGAR: stop and tell the user. Do not work around it.
- Never run `rm` (or any deletion) on a path built from a variable: Claude Code blocks it.

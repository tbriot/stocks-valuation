---
name: uber-quarterly-results
description: Download Uber's (UBER) quarterly financial documents (Press Release, Supplemental Data, Prepared Remarks and Transcript as PDFs) from the Uber Investor Relations file host and save them under uber/documents/earnings/<year> Q<n>/. Use when the user asks for Uber's or UBER's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Uber quarterly results

The IR site has no scriptable document list. The files are on `s23.q4cdn.com/407969754/files` and their URLs are predicted by the script, with several candidates per document (folders and names change a little between quarters).

## What is downloaded

| Document | Local file name | Candidate URLs |
|---|---|---|
| Press Release | `UBER-<year>-Q<n>-Press-Release.pdf` | `doc_earnings/<year>/q<n>/earnings-result/Uber-Q<n>-<yy>-Earnings-Press-Release.pdf` |
| Supplemental Data | `UBER-<year>-Q<n>-Supplemental-Data.pdf` | `doc_earnings/<year>/q<n>/supplemental-info/Uber-Q<n>-<yy>-Earnings-Supplemental-Data.pdf`, else `doc_events/<year>/<Mon>/<dd>/` (same name) |
| Prepared Remarks | `UBER-<year>-Q<n>-Prepared-Remarks.pdf` | `doc_earnings/<year>/q<n>/transcript/Uber-Q<n>-<yy>-Prepared-Remarks.pdf` |
| Transcript | `UBER-<year>-Q<n>-Transcript.pdf` | `doc_financials/<year>/q<n>/Uber-Q<n>-<yy>-Earnings-Call-Transcript.pdf`, else `doc_events/<year>/<Mon>/<dd>/` (name with or without `<yy>`) |

For the `doc_events` URLs the folder is the earnings date: the script scans the days of the two months after the quarter end (HEAD requests). The 10-Q/10-K is not downloaded (not hosted there); it can be fetched from SEC EDGAR if needed.

The fiscal year is the calendar year: Q1 = March 31, Q2 = June 30, Q3 = September 30, Q4 = December 31 (Q4 results come out in February of the next year, filed under the fiscal year). A document not published yet (the transcript comes a day or two after the release) is reported as missing, not as an error.

## Target quarter

- Default: the latest quarter. Uber reports about 5 weeks after quarter end (Q3 in early November). If nothing is found for it, step back one quarter.
- If the user names a quarter (for example "2026 Q1"), use that one.

## Procedure

Run from anywhere (the script finds the project root itself):

```
python3 .claude/skills/uber-quarterly-results/download.py <year> <quarter>
```

Existing files are never downloaded again ("already present"). Each file is checked to be a PDF and written through a temporary file. Then summarise: quarter, files downloaded, already present, missing, errors.

## If something goes wrong

- If a URL pattern changed and a document is reported missing while it exists on the IR site, tell the user: they can give the URL, and the script's candidates should be updated.
- On HTTP 403 or a challenge page the script stops: tell the user, do not work around the protection.
- Never run `rm` (or any deletion) on a path built from a variable: Claude Code blocks it.

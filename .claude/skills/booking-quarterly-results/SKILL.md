---
name: booking-quarterly-results
description: Download Booking Holdings' (BKNG) quarterly financial documents (Press Release, Presentation, Prepared Remarks, Transcript and 10-Q as PDFs, or 10-K for Q4) from the Booking Holdings Investor Relations site and save them under bkng/documents/earnings/<year> Q<n>/. Use when the user asks for Booking's or BKNG's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Booking Holdings quarterly results

The IR site exposes a JSON list of all reports and their documents, with the direct URLs (files hosted on `s25.q4cdn.com/383369491`). No guessing of file names is needed.

## What is downloaded

| IR `DocumentCategory` | Local file name |
|---|---|
| `news` (Press Release) | `BKNG-<year>-Q<n>-Press-Release.pdf` |
| `filing` (Quarterly Filing) | `BKNG-<year>-Q<n>-10-Q.pdf` (`-10-K.pdf` for Q4) |
| `presentation` | `BKNG-<year>-Q<n>-Presentation.pdf` |
| `other` (Prepared Remarks) | `BKNG-<year>-Q<n>-Prepared-Remarks.pdf` |
| `transcript` | `BKNG-<year>-Q<n>-Transcript.pdf` |

The webcast is a link to a player, not a file: it is skipped. Not every quarter has every document (for example the 2024 Q1-Q2 and 2023 Q4 entries have no presentation); a missing one is reported, not an error. The transcript can appear a day or two after the release.

Quarter mapping (calendar fiscal year): Q1 = March 31, Q2 = June 30, Q3 = September 30, Q4 = December 31. **Q4**: the "filing" is the 10-K.

## Target quarter

- Default: the latest quarter. Booking reports about 4-5 weeks after quarter end (Q3 results in early November). If the list has no entry for the most recent quarter, step back one quarter.
- If the user names a quarter (for example "2026 Q1"), use that one.

## Procedure

Run from anywhere (the script finds the project root itself):

```
python3 .claude/skills/booking-quarterly-results/download.py <year> <quarter>
```

The script reads `https://ir.bookingholdings.com/feed/FinancialReport.svc/GetFinancialReportList` (all quarters, `pageSize=-1`), picks the entry whose `ReportYear` and `ReportSubType` ("First Quarter" ... "Fourth Quarter") match, and downloads each document. Existing files are never downloaded again ("already present"). Each file is checked to be a PDF and written through a temporary file. It prints what was downloaded, already present, missing or in error.

Then summarise: quarter, files downloaded, already present, missing, errors.

## If something goes wrong

- Python's default User-Agent gets a 403 from the site; the script sends a descriptive one (`BKNG valuation script`). If it still answers 403 or shows a challenge page, stop and tell the user. Do not work around the protection (no browser headers or cookies).
- Some older entries have a path relative to the file host (for example 2024 Q1 press release); the script resolves them.
- Never run `rm` (or any deletion) on a path built from a variable: Claude Code blocks it.

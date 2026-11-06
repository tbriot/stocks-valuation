---
name: constellation-quarterly-results
description: Download Constellation Software's (CSU) quarterly financial documents (Management Discussion and Analysis, Financial Statements and Shareholder Report as PDFs) from the Constellation Software website and save them under csu/documents/earnings/<year> Q<n>/. Use when the user asks for Constellation's or CSU's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Constellation Software quarterly results

CSU reports in USD under IFRS. There is no 10-Q: the quarterly filings are the MD&A and the condensed financial statements (annual versions for Q4). The PDFs are served without protection by `www.csisoftware.com/wp-content/uploads/<year>/<month>/`. The upload month is not predictable (it is the month the file was published, and old quarters were re-uploaded in 2026/04), so the script scans the 12 months after the quarter end.

## What is downloaded

| Document | URL file name | Local file name |
|---|---|---|
| Management Discussion and Analysis | `CSI-MDA-Q<n>-<year>-Final.pdf` | `CSU-<year>-Q<n>-MDA.pdf` |
| Financial Statements | `CSI-Financial-Statement-Q<n><YY>-Final.pdf`, or `CSI-Financial-Statements-...` (both spellings exist) | `CSU-<year>-Q<n>-Financial-Statements.pdf` |
| Shareholder Report | `Q<n>-<year>-Shareholder-Report.pdf` | `CSU-<year>-Q<n>-Shareholder-Report.pdf` |

Quarter mapping: Q1 = March 31, Q2 = June 30, Q3 = September 30, Q4 = December 31. Q4 files are the annual MD&A and statements.

## Target quarter

- Default: the latest quarter that has ended. CSU reports about 5-6 weeks after quarter end (Q1 in May, Q2 in August, Q3 in early November, Q4 in February-March). If nothing is found, step back one quarter.
- If the user names a quarter, use that one.

## Procedure

Run from anywhere (the script finds the project root):

```
python3 .claude/skills/constellation-quarterly-results/download.py <year> <quarter>
```

It skips files already present, tests the candidate URLs with `curl`, downloads to a temporary directory, checks that the file is a PDF, then moves it into `csu/documents/earnings/<year> Q<n>/`. It prints one line per document: downloaded, already present or MISSING. It stops if the site answers 403/429/503: tell the user and do not work around the protection.

**Never run `rm` (or any deletion) on a path built from a variable**: Claude Code blocks it.

## If a document is missing

Report it without failing: the quarter may not be published yet (Q3 2026 was not online on 2026-11-06). If the file exists under another name, ask the user for the URL and add the variant to `names()` in `download.py` and to the table above. The statements are also filed on SEDAR+ (not scriptable).

---
name: alphabet-quarterly-results
description: Download Alphabet's (GOOG) quarterly financial documents (Earnings Release, Earnings Slides and 10-Q as PDFs, or 10-K for Q4) from the Alphabet Investor Relations site and save them under goog/documents/earnings/<year> Q<n>/. Use when the user asks for Alphabet's or Google's latest (or a specific) quarterly results, earnings documents or financial reports.
---

# Alphabet quarterly results

The IR site (https://abc.xyz/investor/) loads its lists through a JSON feed. Query that feed directly (`WebFetch` does not see the links).

## Feed

```
curl -sg "https://abc.xyz/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&reportTypes=First%20Quarter|Second%20Quarter|Third%20Quarter|Fourth%20Quarter&tagList=&includeTags=true&excludeSelection=1&pageNumber=0&pageSize=<N>&year=<Y>"
```

No API key is needed. The response holds `GetFinancialReportListResult`, a list of reports sorted from newest to oldest. Each report has `ReportYear`, `ReportSubType` (`First Quarter` … `Fourth Quarter`) and `Documents`. Each document has a `DocumentCategory`, a `DocumentTitle` and a `DocumentPath` (the file URL).

Parameters:
- Latest quarter: `pageSize=1&year=-1`. If its documents are incomplete (see below), also fetch `pageSize=-1&year=<year>`.
- A specific quarter: `pageSize=-1&year=<year>`, then filter on `ReportYear` and `ReportSubType`.
- `year=-1&pageSize=-1` returns the whole history: avoid it.

**The same quarter can be split across several report entries** (for example Q4 2025: one entry with the release and slides, another with the 10-K; Q3 2025: one entry with only the webcast). Merge the `Documents` of all entries with the same `ReportYear` and `ReportSubType` before looking for files.

## Documents to download

Identified by `DocumentCategory`, not by title:

| DocumentCategory | Local file name                          | Quarters |
|------------------|------------------------------------------|----------|
| `news`           | `GOOG-<year>-Q<n>-Earnings-Release.pdf`  | all      |
| `presentation`   | `GOOG-<year>-Q<n>-Presentation.pdf`      | all      |
| `tenq`           | `GOOG-<year>-Q<n>-10-Q.pdf`              | Q1-Q3    |
| `tenk`           | `GOOG-<year>-Q4-10-K.pdf`                | Q4 only  |

`tenq` and `tenk` each appear twice: a PDF (`DocumentTitle` = `PDF`, path ending in `.pdf`, on `s206.q4cdn.com`) and an HTML version (on sec.gov). Take the one whose path ends in `.pdf`; ignore the HTML one. Ignore `webcast` too (the call transcript is not downloaded).

Some paths are relative (e.g. `/investor/...`): only the `webcast` ones were seen that way, but if a wanted document has a relative path, prefix it with `https://abc.xyz`.

## Target quarter

- Default: the latest one.
- If the user names a quarter (e.g. "2026 Q1"), use the matching report.
- Mapping: `First Quarter`=Q1, `Second Quarter`=Q2, `Third Quarter`=Q3, `Fourth Quarter`=Q4.
- **Q4**: there is no 10-Q; Alphabet publishes a 10-K (`tenk`) instead, often as a separate report entry. Never look for a `tenq` in Q4.

## Destination

`goog/documents/earnings/<year> Q<n>/` at the project root (e.g. `goog/documents/earnings/2026 Q3/`; note the space, not a hyphen). Create the subdirectory if needed.

## Procedure

1. Call the feed, merge the entries of the target quarter and extract the URLs of the 3 documents (Earnings Release, Slides, and 10-Q for Q1-Q3 or 10-K for Q4), with `python3` or `jq`.
2. For each document, if the local file already exists, **do not download it again** and report it as "already present".
3. Otherwise download it with `curl -fL -o "$tmp/<name>" <url>` into a temporary directory (`tmp=$(mktemp -d)`), never directly into the destination.
4. Check with `file` that the result is really a PDF. If so, `mv` it to the destination. If not, report the error and leave it in the temporary directory.
5. End with a summary: quarter, files downloaded, already present, missing (e.g. 10-Q not yet published), errors.

**Never run `rm` (or any deletion) on a path built from a variable**: Claude Code blocks it. The temporary directory + `mv` flow makes deletion unnecessary.

A document may be absent from a recent report (e.g. the 10-Q is not always published on the day of the results): report it without failing.

## If access is blocked

If the feed or the q4cdn files answer 403 or otherwise refuse: stop and tell the user. Do not work around the protection (no fake User-Agent or browser-like headers).

# Raumer early-page PDF gap check

Local date: 29 October 2026 (fetches recorded in UTC in `manifest.json`).
Archive: Landesarchiv Sachsen-Anhalt, **Z 44, A 9a IIa Nr. 62**.

Exactly four individual PDF URLs were taken from the **DOWNLOAD** group of
the existing `lasa-raumer-mets.xml`, for archive scan numbers **5, 6, 8, 11**.
Each URL received one public read-only GET. No JPEG URL was retried and no
alternate URL was guessed. Exact URLs, METS file IDs, response types, sizes,
UTC timestamps and SHA-256 hashes are in `manifest.json`.

All four requests returned **HTTP 200** and a valid two-page PDF. This was
not successful recovery of the scans: each PDF's second page, rendered and
visually inspected separately, says **“Digitalisat nicht verfügbar”**
(digitized image unavailable). The first page contains catalogue metadata.

Consequently **no original date, place or signature can be read from these
four PDFs**. No judgement that they are inside or outside 1669–1673 is made.
The catalogue's date range is not a substitute for the missing manuscript.
The four early-page gaps remain gaps.

Evidence:

- `005.pdf`, `006.pdf`, `008.pdf`, `011.pdf`: unmodified downloaded responses.
- `005-2.png`, `006-2.png`, `008-2.png`, `011-2.png`: visually checked second pages.
- `assessment.json`: per-file content assessment and verified PDF hashes.
- `fetch_once.py`: exact METS parsing and one-shot fetching; it refuses to
  run again once `manifest.json` exists.

PDF handling followed the PDF skill's read-only render-and-inspect workflow.
All inputs retain their original hashes; no shared cipher solution, notes,
source files, status markers, or goals were changed. This finite route stops
here.

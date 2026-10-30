# HCP 1384 / pc_hcp_65 — Caesar −1 love postcard to W. Abbott

**Status: whole enciphered message read (48 letters). Three small points are disclosed below: one blotted letter restored, one uncrossed t, and two abbreviation groups kept literal. Review 1: ACCEPT.**

## Source and context

HC Portal cryptogram 1384 (`pc_hcp_65`), portal status Not solved, date and language Unknown, no transcription or solution attached (`source/metadata.md`, `SOURCES.md`). No published solution of this card was found or used.

Picture side: printed "Promenade Gardens, Malvern" (Tilley & Son, Ledbury, with the Great Malvern arms); no handwriting. Address side: plain address **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**; halfpenny Edward VII stamp; postmark reads WIMB… 10 PM, with the date not legible. The year is therefore not established from this card. The sister cards from the same couple are dated 1907–08. The plain heading is **"G. H. Sunday"** (G preferred, as on hcp-1388). The disc and building logo across both scans are a scanning overlay, not part of the card.

The message is on the address side, written across the left half; `work/reading.jpg` is the rotated view. Same recipient, hand, key and formulas as FINAL cards hcp-1386, 1388, 1395, 1402, 1403.

## Cipher and key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken as a hypothesis from the sister cards and tested on this card: every one of the 13 words below decodes to English with no exception.

## Transcription and plaintext

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. E L. Cpz. | MY. OWN. [E L.] BOY. |
| J. b[n]. Tpssz Nz. | I. A[M]. SORRY MY. |
| Mfuufs xbt. | LETTER WAS. |
| mbuf. | LATE. |
| Nz. N. & L. Gspn | MY. [N. & L.] FROM |
| zpvs Pxo E. L Hjsm | YOUR OWN [E. L] GIRL |

48 cipher letters, all with one key; `[n]` / `[M]` marks the one restored letter. The groups `E. L.` (twice) and `N. & L.` are abbreviations, kept literal as on the sister cards (shifted values would be D. K. and M. & K.; which, if either, is meant is not established).

**English:** "My own E. L. boy. I a[m] sorry my letter was late. My N. & L. from your own E. L. girl."

**Slovak:** „Môj vlastný E. L. chlapec. Je mi ľúto, že môj list prišiel neskoro. Moje N. & L. od tvojho vlastného E. L. dievčaťa."

## Command (from the repo root)

```bash
python3 -I ciphers/hcp-1384/work/decode.py
```

It checks the SHA-256 of all four image files and prints the plaintext from `work/transcription.json`, which is a manual transcription made by me (none was attached on the portal).

## Uncertainties

1. **`bn.` (AM), line 2: restoration.** The second letter sits in an ink blot. What shows through is a closed oval with a flat top, closer to `o` than `n`. Read literally `bo` gives AN; "I an sorry" is not a sentence, and only `n` makes the word, so `n` is a disclosed restoration. `J. bn` is also the formula on hcp-1393, 1395, 1403, 1406. The writer may have written `o` by slip; the blot prevents deciding.
2. **`xbt.` (WAS), line 3.** The final sign is one plain slanted stroke with no visible cross, and it is the only cipher lower-case t on this card, so there is no same-card comparison. It lies on the scanning overlay band, but the ink stays dark and no cross is visible. Only t gives a word here (`xbt` is on hcp-1402).
3. **`L` after `&`, line 5.** The sign has a hook at top and a foot at the base, and differs from the `L` in the two `E. L.` groups. Read L by the sister formula `N. & L.`; T or J are not excluded in isolation. **`N` in the same group:** same hook, stem and second leg as the N of `Nz`, so N is preferred, but a blot sits on its right side, where a third leg of M would be, so M is not fully excluded (see the `M. & L.` treatment on hcp-1395). Both are inside an abbreviation, so the message is unaffected.
4. **`E. L.`** Second letter differs in form between its two occurrences (a 4-like shape, a k-like shape). Dots differ too: line 1 has none between E and L, line 6 has none after L. Sister card hcp-1402 has `N. L.` at this place; this card clearly shows the ornate E, so E is what I report.
5. **Word boundaries and dots** follow the manuscript (corrected after review 1); dots are not significant. After `mbuf.` a long thin curved stroke with a hook runs to the line end: read as a closing flourish, not a letter. Case is as written; `mbuf` starts with a large m close in form to the capital of `Mfuufs`.
6. **Date:** not established. Below `10 PM` on the postmark the top of one more line survives: a D-like sign and a flat-topped sign. A month DE is only a tentative reading; day and year are lost.

## Why this is correct

Every word decodes under one fixed shift, with no free parameters tuned to this card; the result is a grammatical sentence plus the couple's standard opening and closing. `Mfuufs`, `Tpssz`, `Pxo`, `Hjsm`, `gspn`, `zpvs` and `Nz` all recur on independently reviewed sister cards. New relative to those formulas: `mbuf`, read from clear pixels.

## Credit

Solved by Claude Opus 5.5 on 2026-10-30. No earlier work on this number; the key comes from the finished sister cards (see their SOLUTION.md files for their credits).

## Response to review 1

Verdict ACCEPT, four minor findings, all addressed. No decoded letter changed; `python3 -I ciphers/hcp-1384/work/decode.py` re-run after the edits: hashes OK, 48 letters.

1. **Restoration not marked: fixed.** `work/transcription.json` now stores `b[n].`, and the table, translation and command output show `A[M]`.
2. **Unmentioned stroke, inexact dots: fixed.** I checked `review/work/flourish.jpg`, `r1b.jpg` and `r6b.jpg` and agree with the reviewer. The stroke is a closing flourish, now recorded in the flags and in Uncertainty 5. Dots are corrected to the card: `E L.` in line 1, `mbuf.` in line 4, `E. L` in line 6.
3. **First initial of `N. & L.`: fixed.** On `review/work/n_compare.jpg` I agree: N preferred, M not fully excluded because of the blot. Added to Uncertainty 3.
4. **Postmark: noted.** On `review/work/pm_date.jpg` I see the same remains; added to Uncertainty 6 as tentative. It sets no year.

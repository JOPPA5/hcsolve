ACCEPT

# Review 1 — HCP 1384 / pc_hcp_65 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands. I tried to break it and could not. All 48 cipher letters decode under one shift to a grammatical message. One letter (the `n` of `bn`) is a real restoration and is disclosed. Only minor points remain (findings below).

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1384/work/decode.py` ran: hashes of all four images OK, output equals the table in SOLUTION.md, 48 letters.
- **Independent decode.** `review/work/indep_decode.py` holds my own reading typed from my crops, not taken from `work/transcription.json`. It gives "my own boy i am sorry my letter was late my from your own girl" and 48 letters; my letter count by hand also gives 48. It prints all 26 shifts: only shift 1 gives English.
- **Transcription against the hires scan.** I rotated `work/hires/pc_hcp_65_adr.JPG` 90 degrees CCW and enlarged every row 3–8x (`review/work/r1a…r6b.jpg`, `mfuufs_full.jpg`, `blot.jpg`, `zpvs.jpg`, `n_compare.jpg`). Results by word:
  - `Nz`, `Pxo` (P with the long overhead flourish, both times), `Cpz`, `J`, `Tpssz` (bar over T), `Gspn`, `zpvs`, `Hjsm`: confirmed sign by sign.
  - `Mfuufs`: the second sign has an ascender and descending loop (`mfuufs_full.jpg`), unlike the non-descending b of `mbuf` directly below. So f, not b, as the solver says. M + f + u + u + f + s fits the strokes; the two u's run together in a smear but the count fits and is the same shape as on hcp-1403 (`work/body.jpg` there).
  - `mbuf`: m, b with closed bowl, u, f with descending loop. Clear. A new word for the family, no FINAL card has it, and it is read from pixels, not forced.
  - `xbt`: x, 6-like b, one plain slanted stroke, as disclosed. `xbl` would give WAK; hcp-1402 records a tall-upstroke t in this hand (in its SOLUTION.md; I did not compare its pixels).
- **Restoration `bn`.** `blot.jpg`: the sign after b is a closed oval with a flat top, inside a brown blot. It looks like `o`, and the solver says so. Nothing visible proves an `n`. The word is forced by sense ("I am sorry") and the sister formula, not by pixels. This is correctly called a restoration; a writer's slip is also correctly left open.
- **Key coverage.** One key covers all 48 letters; no exception, no nulls, nothing skipped.
- **Literal groups.** `E. L.` twice and `N. & L.` once are kept literal, same treatment as hcp-1386 and 1406. Ornate E is clear in both. L forms differ as disclosed (4-like, k-like, hooked).
- **Language and context.** Natural English of the period, and the couple's own formulas. Recipient (Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon) read on the scan, matches the sister cards. Picture side checked: "Promenade Gardens, Malvern", Tilley & Son, Ledbury, Great Malvern arms, no handwriting.
- **Solver's cross-references.** By grep of FINAL cards: `J. bn` on 1393, 1395, 1403, 1406; `xbt` on 1402; `Mfuufs`/`mfuufs`, `Tpssz` (1403), `Pxo`, `Hjsm`, `gspn`, `zpvs`, `Nz` all recur. `mbuf` is indeed new. All these claims hold.
- **Sources.** Portal has no solution attached (per SOURCES.md and metadata); nothing suggests a published solution was used.

## Findings

1. **Minor: the restoration is not marked in the plaintext.** The table row and the command output print `I. AM.` with no sign that the M is restored, and the JSON stores `bn` as if read, with only a side `flags` note. The status line and Uncertainty 1 do disclose it, so nothing is hidden, but a reader who takes only the plaintext will not see it. Fix: print `A[M]` in the table, the output and the report.
2. **Minor: an unmentioned stroke and inexact dots.** After `mbuf` the card has a dot and then a long thin curved stroke ending in a hook (`flourish.jpg`), at the end of the line. It looks like a closing flourish, not a letter, but neither the transcription nor the uncertainties mention it. Uncertainty 5 says dots follow the manuscript, yet the `mbuf` dot is missing; in line 1 I see no dot between E and L (`r1b.jpg`), and in line 6 there is a dot between E and L and none after (`r6b.jpg`). None of this affects the reading. Fix: mention the stroke and either correct the dots or say they are normalised.
3. **Minor: reading of the first initial in `N. & L.` is not discussed.** The sign (`n_compare.jpg`) has the same hook, stem and second leg as the N of `Nz`, so N is the right preference, but a blot sits on its right side where a third leg of M would be. The family treats this slot differently: hcp-1395 reads `M. & L.` as ciphertext (L. & K.). Uncertainty 3 covers only the L. Fix: add one sentence that M is not fully excluded because of the blot, and cite hcp-1395. No effect on the message.
4. **Minor: postmark.** "Date not legible" is fair, but below `10 PM` the top of a line survives on the stamp: a D-like sign and a further sign with a flat top (`pm_date.jpg`). A month DE is a tentative reading, nothing more; the day and year are lost. This could be noted so the next reader need not redo it. It does not establish a year.

No blockers or major findings.

## What I could not verify

- Whether the blotted letter was written `n` or `o`; the blot prevents it.
- The meaning of `E. L.` and `N. & L.`, and whether they are enciphered.
- The date and year of the card; the identity of the writer; the sense of G. H.
- The absence of a publication outside the portal (I ran no search; the orchestrator reports no register record).
- The t of `xbt` on hcp-1402 was not compared in pixels.

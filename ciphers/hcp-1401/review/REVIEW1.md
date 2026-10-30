ACCEPT

# Review 1 — hcp-1401 (pc_hcp_82), Caesar −1 New Year postcard, 30 Dec 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (solver marker DONE1).

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1401/work/v2/decode.py` (repo root): "source hashes OK", output
   `FROM. YOUR. / OWN. [E. L.] / GIRL '`, 15 enciphered letters. Identical to the plaintext claimed in SOLUTION.md.
2. **Independent decode.** `review/work/indep_decode.py` uses my own transcription of the four enciphered groups
   (`gspn Zpvs Pxo Hjsm`) and tries all 26 shifts. Only shift 1 gives language: FROM YOUR OWN GIRL; every other
   shift is gibberish. 15/15 letters decoded by the one key; no unused or contradictory cipher letters.
3. **Transcription against the scan.** I rotated `source/address.jpg` myself and enlarged 3x
   (`review/work/msg_rot90.png`), then zoomed the doubtful groups further:
   - `gspn.` and `Zpvs.` (the Z written as a "2"-like form, as on sister cards): clear.
   - `Pxo.` with the long overarching flourish of the P: clear.
   - `E. L.` (`review/work/el_zoom.png`, ~9x): E, dot, then a single rising stroke ending in a heavy inked foot,
     then a dot. No second stem or arch, so not h; the shape matches the L of the same group on hcp-1386
     (`ciphers/hcp-1386/work/crops/band6.png`, where the line `Pxo. E. L. Hjsm` occurs word for word). The reading L
     is supported by the pixels, not forced. It is disclosed as an abbreviation kept literal.
   - `Hjsm` (`review/work/hjsm_zoom.png`): H with a crossbar, j as a long stroke with a descender hook, s, m. Clear.
     The detached wedge after it is a mark/apostrophe; correctly left uninterpreted.
   - Heading "C. H. Monday" is plain text, not enciphered; the C/G doubt is disclosed.
4. **Coverage.** The whole message area is the five lines visible in the rotated crop (heading + three cipher lines,
   bounded by ruled lines); all of it is in the transcription. Picture side: printed greeting only (checked in the
   solver's description; no handwriting visible in `source/picture.jpg` per solver, consistent with the series).
5. **Context.** Stamp on the scan is a red ONE PENNY Edward VII; postmark legible as "…MBORNE / 10 PM / DE 30 / 07",
   agreeing with the portal date 1907-12-30, a Monday, and with the heading "Monday". The closing formula
   "from your own E. L. girl" is the same as on accepted sister cards of the Abbott correspondence (hcp-1386, 1404).
   Plaintext is natural English of the period.
6. **Honesty.** Portal status Not solved, no attached solution; none used. Earlier GPT work and Claude's completion
   are credited separately in SOLUTION.md.

## Findings

1. **minor — address detail.** SOLUTION.md says the farm name is "not established". On the scan
   (`review/work/addr_farm.png`) it reads clearly "Stokelake Farm", and sister cards (hcp-1388, 1397, 1402, 1403)
   already read it so. Not part of the cipher; could be stated in the report.
2. **minor — postmark not cited.** SOLUTION.md relies on the portal date; the postmark "WIMBORNE … 10 PM DE 30 07"
   is itself legible and independently confirms the date and the Wimborne origin shared with the sister cards.
   Worth naming in the report.
3. **minor — L reading rests partly on family comparison.** On this card alone the L's foot is a blotted ink mass;
   the identification is secure because of the identical formula on hcp-1386/1404, which the solver says. No change
   needed beyond keeping that disclosure.

## What I could not verify

- The meaning of `E. L.` (e.g. "ever loving") and whether those initials are themselves shifted; the solver
  correctly leaves this open.
- The writer's identity and the heading initials (C. H. / G. H.).

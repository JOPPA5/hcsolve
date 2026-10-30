ACCEPT

# Review 1 — hcp-1406 (pc_hcp_87), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1406/work/decode_v2.py` (from the repo root) prints the eight claimed lines and finishes with "source hashes OK; 64 enciphered letters decoded with one key (shift -1)". Its output matches the plaintext table in SOLUTION.md exactly.
2. **Independent decryption.** `review/work/indep.py` holds the 18 enciphered groups, typed by hand from my own reading of the scan, and applies its own shift of −1. All groups give English words: MY OWN BOY / LETTER THIS MORNING / VERY NICE / I AM INDOORS / ALL TO-DAY / MY FROM / OWN GIRL. That is 64 letters, the same count as the solver's. The key covers every enciphered letter. The abbreviations shift to D. K. and M. & K., which the solver also reports, and they are kept literal.
3. **Transcription against the pixels.** I rotated `source/address.jpg` 90° counter-clockwise and applied autocontrast. I checked these crops, enlarged 3–5×: `review/work/rot2x.png` (whole card), `r1`–`r5.png` (every message line), `last.png` (closing line), `boy.png`/`boy2.png` (Cpz), and `q1`–`q3.png` (marks at the line ends). My readings:
   - `C. H. Sunday.`: clear, ordinary writing.
   - `Nz. Pxo. E. L. Cpz.`: Nz, the P with a small crossing stroke on its stem plus `o`, and `E.` with a narrow L-stroke are all visible. In `Cpz` the C and p are clear. The final `z` sits on top of the printed grey "O" of the cipher-wheel overlay. Only a short dark stroke on the lower left of that O, followed by a dot, is ink. The `z` is therefore weakly attested, but the solver discloses this (uncertainty 2), and the whole greeting matches hcp-1386 letter for letter.
   - `Mfuufs uijt npsojoh`: clear. The j-descender of `npsojoh` makes the "V"-shaped mark below the line end, as the solver says.
   - `wfsz ojdf.`, `J. bn. joeppst`, `bmm "up-Ebz."`: clear. `Ebz` looks like "E62", but the quoted "to-Day" makes the reading unambiguous.
   - `Nz. N. & L. gspn.`: the `&` is a looped cross-shaped sign, and `gspn` is clear.
   - `Pxo. E. L. Hjsm.`: written as "Fo · El · HjSu". The P carries the same small cross on its stem as in line 2. The final `m` is a flat two-hump form. HJSM → GIRL fits the sister cards.
   No group is a forced restoration. The two weak spots, the `z` of Cpz and the x in Pxo, are both disclosed. Both also sit inside a fixed formula that recurs on hcp-1386 ("Nz. Pxo. E. L. Cpz." … "Pxo. E. L. Hjsm").
4. **Language and context.** The text is a short, coherent English note in the idiom of 1907–08. It matches the Abbott series (hcp-1386…1407) in recipient, shift, formulas and the quoted "to-Day". The address (Mr. Abbott, Stokelake Farm, Chudleigh, S. Devon) and the WIMBORNE postmark can be read on the scan. No date is claimed, which is correct because the postmark date cannot be read.
5. **Sources and credit.** The portal shows "Not solved" with no attachment, and the solver used no published solution. Earlier GPT work and the completion by Claude are credited truthfully.

## Findings

1. **minor – unrecorded marks near lines 2/3.** Two small tick marks stand before `wfsz` at the start of line 3 (`review/work/q3.png`, `q1.png`). They look like an opening quotation mark. A further small dash/tick stands left of the j-descender "V" at the end of line 2 (`q2.png`). SOLUTION.md explains only the "V". These marks may quote "very nice", the same device the writer uses for "to-Day". They do not change any letter, but the transcription should mention them, either as possible quotation marks or as stray marks.
2. **minor – weak `z` in `Cpz`.** The final `z` is mostly hidden by the printed overlay. The reading BOY rests partly on the formula from the sister card. This is disclosed correctly; the report should keep that wording and not present the letter as clearly seen.
3. **minor – meaning of E. L. / N. & L.** The abbreviations are left unresolved and kept literal. This is consistent with the family and disclosed. No action is needed beyond keeping it in the report.

## What I could not verify

- The meaning of E. L. and N. & L., and whether those letters are shifted.
- The postmark date (illegible), so the year cannot be confirmed from this card.
- I did not re-open the portal page. The metadata comes from the solver's capture of 2026-10-26.

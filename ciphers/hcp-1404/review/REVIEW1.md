ACCEPT

# Review 1 — hcp-1404 (pc_hcp_85)

Reviewer: Claude Opus 5.5, 2026-10-30. Solution under review: SOLUTION.md round 1 (GPT partial 2026-10-26, completed by Claude Opus 5.5 as solver 2026-10-29).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1404/work/v2/decode.py` (from repo root): source hashes OK; output
   `YOUR. OWN.` / `[E. L. | shifted: D. K.] GIRL.`, heading `G. H. Thursday.`, date `January 30th = 08`, "11 enciphered letters decoded + 2 abbreviation letters kept literal". Identical to `work/v2/plaintext.txt` and to the table in SOLUTION.md.
2. **Independent transcription from the pixels.** I cropped `source/address.jpg` myself (PIL, rotated 90° CCW, 3x / 6x / 9x): `review/work/message_rot3x.png`, `review/work/lines12_6x.png`, `review/work/EL_9x.png`. My reading, sign by sign:
   - heading: `G. H. Thursday.` (plain; first initial could be C, as on hcp-1386 "C. H.") — not ciphertext;
   - line 1: `Zpvs. Pxo.` — Z (2-shaped with descender), p, v, c-like terminal s; P with long top stroke looping right over the line, x, o, full stop. Agrees with the solver;
   - line 2: `E-l. Hjsm.` — cursive E, short dash, tall single stroke (L/l), then H (two crossed downstrokes), j (long descender, dotless), s, m (the m drawn as a run of minims), full stop. Agrees with the solver;
   - date `January 30th = 08` (plain).
   No other writing exists on either side (picture side: printed caption "Fritton Decoy, Norfolk Broads" only; address side: address, stamp, printed text).
3. **E. L. field.** Compared with `ciphers/hcp-1386/work/crops/band6.png` ("Pxo E-l Hjsm", same hand): the E, the dash separator and the tall l-stroke are the same forms, in the same slot of the same formula. The reading "E. L." is supported by the pixels, not forced from context. The rejection of a numeral "1" is reasonable.
4. **Own decoder.** `review/work/my_decode.py` decodes my own reading with shift −1: ZPVS PXO HJSM -> YOUR OWN GIRL; a full 0–25 shift scan gives English only at −1. Every enciphered letter (11/11) is covered by the one key; the abbreviation group is the only non-decoded material and is disclosed.
5. **Context.** Postmark "JA 30 08" matches the written date "January 30th 08" and the portal date 1908-01-30; addressee Mrs W. Abbott, Chudleigh, S. Devon, as on the other cards of the hcp-1386…1407 family; the formula "your own (E. L.) girl" recurs on hcp-1386 and hcp-1397 (FINAL). Period English, natural.
6. **Honesty.** Portal status Not solved, no attached solution; SOLUTION.md credits the GPT partial work and the Claude completion truthfully; the E. L. treatment and the s/P letter forms are disclosed as uncertainties.

## Findings

1. **(minor) Status of the E. L. group is inconsistent across the family.** On hcp-1395 the analogous closing initials were treated as *ciphertext* ("M. & L." -> L. & K.), while here and on hcp-1386/1401 "E. L." is kept literal. SOLUTION.md does disclose that "whether the initials are themselves shifted is undecided" and prints D. K. alongside, so nothing is hidden; but the report should state the family-level inconsistency explicitly (E. L. literal could be "ever loving"; D. K. shifted has no obvious expansion, which mildly favours literal).
2. **(minor) Notation.** On the card the separator is a dash and the L is written as a lower-case-looking tall stroke ("E-l."); the transcription normalises it to "E. L.". This is disclosed in the notes field of `transcription.json` and SOLUTION.md uncertainty 1; just keep the normalisation explicit in the PDF.
3. **(minor) Heading initial.** "G. H." vs "C. H." (hcp-1386 reads "C. H." in the same slot). Not ciphertext and disclosed; the report should keep it as uncertain rather than assert G.
4. **(minor) Older files.** `work/decode.py` / `work/plaintext.txt` still print "D [..] Girl" (the earlier partial GPT version, decoding the E with the cipher). SOLUTION.md labels them as superseded; fine, but the report should cite only `work/v2/`.

## What I could not verify

- The meaning of "E. L." (and whether it is enciphered); the card alone cannot settle it.
- The exact farm name in the address (not ciphertext).
- Only the 1024x674 scan is available; at that resolution all 11 cipher letters and the abbreviation are nevertheless unambiguous.

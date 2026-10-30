ACCEPT

# Review 1 — HCP 1387 (pc_hcp_68), Caesar +1 postcard to W. Abbott, 1 Dec 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Tried to refute the solution. The reading stands. Only minor points remain.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1387/work/solve.py`: the source hashes check out and it prints the 7 rows exactly as the SOLUTION.md table shows them (68 letters, −1 shift, round trip OK).
2. **Independent decryption.** `review/work/indep_decode.py` is my own −1 Caesar over `work/transcript_full.json`. Run as `python3 -I review/work/indep_decode.py work/transcript_full.json`, it gives the same seven lines and 68 letters. A single fixed key covers every letter. No per-word adjustments are needed.
3. **Transcription vs scan.** I made my own crop of `source/address.jpg` (message area, rotated 90° CCW, 3x: `review/work/msg3x.png`). I also enlarged the following:
   - row 3 (`row3.png`)
   - rows 6–7 (`rows67.png`)
   - the last word (`girl.png`)
   - the row-6 middle group (`row6mid.png`)
   - z forms side by side (`zcompare.png`)

   Rows 1, 2, 4, 5 match the ink letter by letter: Nz. Pxo. E.h Cpz. / Mfuufs uijt / Uibolt wfsz. / Nvdi gps bmm. Row 3 reads n-p-s, then a long upstroke whose descender loops below the line (this writer's j, as in uijt), then o-h. There is no second o, so the literal "moring" is right and is disclosed. Row 6 "Nz. … Gspn" and row 7 "Zpvs Pxo. E.h" are clear.
4. **Language and context.** The text is idiomatic Edwardian English love-card prose ("Thanks very much for all", "From your own … girl"). It matches the accepted sister card hcp-1397 ("Love from your own girl") and the hcp-1386 pattern "My own … Boy / Your own … Girl". The postmark reads WIMBORNE DE 1 07, and 1 Dec 1907 was a Sunday, which agrees with the plain heading "G. H. Sunday". The address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon matches the series.
5. **Sources and credit.** The portal status was Not solved and nothing was attached. No published solution was used. The earlier GPT partial work and the Claude completion are credited separately, and the claims in each part match the files.

## Findings

1. **Row 7 "Hjsm" → Girl (minor).** The glyph after H has a bowl at the top of its stem, much like this writer's p (cf. Zpvs, Gspn). This means a literal "Hp?n" cannot be fully excluded. However, the descender ends in a left-curling hook rather than the straight p descender, and that fits j. The other sister-card review (hcp-1388) also reads GIRL from H-j-s-m. The solver discloses that the reading partly depends on context. I accept the reading. The report should keep the caveat.
2. **Row 6 middle group "h.v y." (minor).** The second sign is a looped 2/v-like form. My comparison (`zcompare.png`) shows it is larger and ends in an upstroke, unlike the flat-based z of Nz/Cpz. Still, an alternative z reading (→ "g.y") should be named next to v. The group is correctly left unexpanded and is disclosed as the main residual.
3. **"E.h" → "D.g" / "darling?" (minor).** The solver assumes this abbreviation is enciphered. The sister card hcp-1388 deliberately leaves open whether "E.h." is enciphered (D.g) or written in plain (E.h., e.g. a pet name or initials). The bracketed "[darling?]" in the reading and translation is a guess and should be labelled as one. Better still, the report should mention the plain "E.h." alternative.
4. **Postmark hour (minor).** `transcript_full.json` states "WIMBORNE 10 PM DE 1 07", but Uncertainty 6 says the hour is not settled. On the scan it reads "10 PM". Make the two consistent.

## What I could not verify

- The meaning of "h.v y." and of "E.h", and the expansion of "D." in the plain aside "going to D."
- The identity of the writer G. H. (C. H. is not excluded) and of W. Abbott beyond the address.
- The portal pages themselves (I did not re-read them; I relied on `source/metadata.md`).

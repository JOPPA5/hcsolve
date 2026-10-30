ACCEPT

# Review 1 of hcp-1347 (pc_hcp_28)

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1, against `SOLUTION.md` as handed over with `DONE1`. The solver was also Claude Opus 5.5 (a separate session), so this is not a cross-provider review.

The reading stands: Caesar -1, English, all 58 enciphered letters accounted for. One letter is a disclosed restoration. The findings below are minor and none changes the plaintext.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1347/work/decode.py` ran clean: "hashes OK", 58 letters, 4 literal initial tokens, and output identical to the table in `SOLUTION.md`.
2. **Hashes.** `shasum -a 256` of the four image files matches `work/source-sha256.json` and `SOURCES.md`.
3. **Independent decryption.** `review/work/indep.py` holds the ciphertext retyped from my own crops, without importing solver files, and tries all 26 shifts. Only shift 1 gives English (MY OWN BOY / I AM GOING TO / THE MINSTER / SUNDAY NIGHT / NOT ALONE / YOUR OWN GIRL). Letter count is 58, matching the solver. No other shift yields even one word group.
4. **Transcription against pixels.** I rotated `work/hires/pc_hcp_28_adr.JPG` 90 degrees anticlockwise and went through every row at 3x (`review/work/r1.png` … `r7b.png`). The doubtful signs were checked at 6-10x (`review/work/zoom.py`, `z_*.png`, `z_pj.png`, `z_blot_c.png`). Every token matches, including the placement of dots, the dash after the first M, the absence of a dot after L in line 2, and the clear quotation marks around line 6.
5. **Context.**
   - 9 August 1907 was a Friday and 11 August a Sunday (computed in `indep.py`).
   - Postmark WIMBORNE 10 PM AU 9 07 and the address (Mr W. Abbott, Stokelake Farm, Chudleigh, Devon) are visible.
   - The picture side reads "Lady Chapel, Wimborne Minster" with no handwriting, and carries number 14276.
   - MINSTER therefore agrees with both the picture and the postmark, and it arises from the cipher, not from any choice of the solver.
6. **Sister-card claims.** `Njotufs` occurs in no other `SOLUTION.md`, so the claim that the word is new holds. `Tvoebz`, `J. bn. hpjoh` and the C. H./G. H. doubt are on hcp-1355 as stated. `Nz Pxo … Cpz` and `Pxo. M. L. Hjsm` are on hcp-1365.
7. **Language and disclosure.** The plaintext is natural period English for a short lover's note. The Slovak translation is sound. The solver says no published solution was used and no web search was run. Uncertainties are listed.

## Disputed signs, judged on the pixels

- **Final `m` of `Hjsm`:** not legible, correctly called a restoration.
  - The smear (`z_hjsm.png`, `z_blot_c.png`) has a clear doubled stem and two further dark masses to the right. That spacing is compatible with three minims but does not prove them.
  - The doubled stem is taller than this writer's normal minim (about 33 hires px against about 23 for the `u` of `Opu`). The solver's "fits a smeared m" is therefore on the generous side, though an entry stroke of that height is not impossible.
  - GIRL rests on the visible `Hjs` plus the closing formula. That is enough to read it, as long as it stays labelled as a restoration.
- **`e` of `Tvoebz`:** I agree with e. `z_e.png` shows a broad leaf-shaped head with a slightly lighter interior, wider than a plain c terminal, so it looks like a filled loop. It is the only e in the ciphertext, so there is no comparison sign on this card, as the solver's dependence on hcp-1355 implies.
- **`Ojhiu`:** h plus three minims and one dot, confirmed (`z_hiu.png`). The dot stands about one minim to the right of the expected place after allowing for slant, so "slightly right" is fair.
- **`M. L.`:** the sign has a hook, a stem, an arch with a leg, and a short second leg in both places (`r2.png`, `z_m7.png`). The `N` of `Nz` has one leg (`r2.png`). The solver's M is defensible, and N is disclosed as possible.

## Findings

1. **minor. `GIRL` is printed as if fully read.** The table in `SOLUTION.md`, `work/transcription.json` and the decoder output give `Hjsm` / GIRL with no mark on the line itself. The restoration appears only in the uncertainty list and a JSON note. Fix: write `Hjs[m]` / GIR[L] in the table and in the report. The decoder can keep its count, stating 57 letters read plus 1 restored.
2. **minor. Two smudged signs in `hpjoh` are not disclosed.** The stem of `p` is heavily blotted, and the arch of the final `h` is swallowed by a blot, leaving only a dark spot at the foot (`r3.png`, `z_hpjoh.png`). The `j` has no visible dot (`z_pj.png`). None of this threatens GOING, but "what remains uncertain" should say so.
3. **minor. `M. L.` and `N. L.` differ across the family.** hcp-1365 and this card print `M. L.`, while hcp-1368 and hcp-1402 print `N. L.` for what appears to be the same group, and hcp-1402 describes it as a two-arch N. The solver discloses this. The literal form printed in the plaintext is still a choice, and the report should say the two may be one group, not imply two different initials.
4. **minor. Stem height of the restored `m`.** Uncertainty 1 should say that the visible stem is taller than a normal minim of this hand, so the pixels alone neither show nor confirm an m.

## What I could not verify

- The meaning of `G. H.` and `M. L.`, and whether the initials are enciphered.
- Whether the heading is G or C: the sign reads as G to me, but the doubt stands as disclosed.
- Whether a published solution exists: I ran no web search either.
- The inference that "Sunday night" is 11 August 1907, which is reasonable but not stated on the card.

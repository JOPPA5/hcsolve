ACCEPT

# Review 1 of hcp-1158 (reviewer: Claude Opus 5.5, 2026-11-02)

I tried to refute the reading and could not. The key, the transcription and the plaintext all hold on the pixels of the whole card. Five minor corrections remain. None changes a word of the reading.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1158/work/decode.py` runs. All four scan hashes pass. It reports 316 signs (314 by table, 2 by sense), 26 distinct signs, and its 19 lines match the plaintext in SOLUTION.md apart from the disclosed normalisation.
2. **Independent transcription and decode.** I re-keyed all 316 signs from my own contrast-enhanced crops of the hires scan (`review/work/gr.py`, `g*_*.png`), line by line, into `review/work/my_decode.py`. That script uses only the hcp-1174 key table, not this card's additions. Run it with `python3 -I ciphers/hcp-1158/review/work/my_decode.py`.
   - My token stream is identical to `work/transcription.txt` (316 = 316, `identical True`). I read the card with the solver's transcription already in view, so this is a careful check, not a blind second reading.
   - With no sense repairs and no new signs the text already reads `terem virág kis kertemben`, `a boldogság révébe`, and so on.
   - Only three things fall outside the transferred table: `4.` in `va[4.]`, `e[4.]máshoz`, `ho[4.]ha`, `lé[4.]`; `6` in `gondol[6]`; and the literal `szentet` and `dirágszálom`.
3. **Key coverage.** Every sign on the card is covered. 24 of the 26 distinct signs come from the FINAL sister key. `4.` = gy is stable across four separate words. `6` = j is a single occurrence, but the alternatives give no word (`gondol` + n is impossible, and d is `3`).
4. **Disputed signs, enlarged 4-6x** (`review/work/z*.py`, `z_*.png`):
   - `3` in `virágszálom`: no dot. Confirmed.
   - Comma on the last sign of `szentem`: real, in the same ink. Confirmed.
   - `kincsem`: crossed 7 with the lower part under the blot. Confirmed.
   - `hű`: plain 5, one dot lower left of the 1, thick tick at the flag end. As the solver describes it.
   - `meglásd`: lower dot plain. A blue speck for the upper dot does show beside the printed "Printed in Germany" lettering.
   - `ezt a`: uncrossed flat-topped `1.`. Confirmed.
   - `üdvözöl`: `0,` then true `9,` then `0,` with the comma touching the bowl. Confirmed.
   - `beevezünk`: first sign is `1,`, uncrossed.
5. **Language and context.** The text is natural period Hungarian love verse with rhymed couplets (`leszünk/beevezünk`, `virágszálom/párom`, `babám/rám`), and the third-person closing is grammatical. Sziber Margitka, Szomolya, u. p. Bogács, Mezőkövesd and the signature Árpád all fit the family. Forcing is not plausible: the same table yields 18 lines of connected rhymed text.
6. **Open parts.** The note, margin (`Mezőkövesd: 1916, I/11.`) and address are read correctly on the hires scan. The picture side has no writing. The English and Slovak translations are faithful.
7. **Honesty.** The portal attaches no solution, the solver says so, and it states what it did not check (the HistoCrypt article, a verse-source search). `hcp-1158` is not in `skip.txt` or `register-exclusions.json`. A grep of the sister SOLUTION files found the verse on no other card.

## Findings

1. **minor: wrong count for `4.`.** SOLUTION.md says `4.` = gy "occurs 5 times". Both transcriptions have it 4 times (`vagy`, `egymáshoz`, `hogyha`, `légy`). Correct the number.
2. **minor: closing marks not recorded.** Line 18 has a heavy `)` after `kedvesed` and another after `Árpád` (`review/work/z_par.png`). No opening bracket is visible. Neither mark is in `work/transcription.txt` or SOLUTION.md, while hcp-1174 prints such brackets. The salutation's `!` is also omitted. Note them, since SOLUTION.md describes the card's punctuation when arguing about the `szentem` comma.
3. **minor: overwritten sign not disclosed.** The `8` in `egymáshoz` carries a heavy extra stroke through its upper loop, like a correction (`review/work/z_em.png`). It still reads as 8 and the word is secure, but it belongs in the uncertainties.
4. **minor: silent normalisation in the clear note.** I see no accent on the `e` of `szeretnék`, so the card seems to have `szeretnek`, yet the note is printed with the accent. Line-end hyphens after `szíves` and `neki` are also dropped. SOLUTION.md lists its normalisations for the cipher only. Say the note is normalised too, or print it literally.
5. **minor: muddled verse-layout sentence, and postmark not attempted fully.** "Line breaks of the verse are mine except where the card breaks" is misleading: each verse line is one card line (lines 1-16). State that plainly. On the postmark, turning the scan about 56 degrees (`review/work/z_pm56.png`) brings the date strip level. A group ending in 6 and a day group beginning with 1 are visible, which would suit 916 and January but is not secure. The 1915-vs-1916 point in uncertainty 11 can be softened accordingly, without claiming a reading.

## Could not verify

- The date strip of the postmark, so the 1916 date rests on the writer's own margin note.
- The sign under the blot in `kincsem`: any dot or comma would be hidden, so k rests on the word.
- Whether the comma on `szentem` is a slip or punctuation, and whether the missing dot in `virágszálom` is a slip. The sense is not in doubt in either case.
- Whether the verse is a printed or popular text, and who Pista is.
- Whether the HistoCrypt article discusses this card. I did not check it either.

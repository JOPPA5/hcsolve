ACCEPT

# Review 1 of hcp-1145 (Claude Opus 5.5, reviewer, 2026-11-02)

The attempt to refute this reading failed. The transcription, the key and the Hungarian text all hold. The remaining issues are three minor corrections to the write-up. None of them changes a letter of the plaintext.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1145/work/decode.py` runs. All 4 hashes are OK (I also recomputed them with `shasum`). It reports 385 cipher signs, 28 distinct, 74 words, 4 read by sense, and its output matches the plaintext in `SOLUTION.md`. The assertion folds accents, so it tests letters only, as the solution says.
2. **Independent transcription and decode.** I read every cipher row from my own 4x-of-scan crops of the hires image (`review/work/rows.py`, `r01_0.png` to `r21_1.png`) and typed the signs by row into `review/work/own_decode.py`, with the key entered separately. Result in `review/work/own_decode.out`: 385 signs, the same count, and **0 token differences** from the "as seen" side of the solver's tokens. My transcription was made after I had seen the solver's, so it is a sign-by-sign check, not a blind one.
3. **Whole-card coverage.** Every cipher row is accounted for. Nothing lies outside rows 1 to 20 except the clear date, the margin `I →`, the rules and the printed red `3526 2`. The picture side has no writing (only the collection stamp). The key covers all 385 signs with no gaps; with the raw values, the only non-words are the four disclosed spots: `pistádal`, `sodal`, `vszgy`, `ádpád`.
4. **The four "read by sense" signs, checked on the pixels** (`work/crops/f.png`, `a.png`, `s.png`, `h.png`, and my rows 4, 10, 17, 20):
   - `vagy`: the card shows a crossed `7` with its dot, and a heavy overwrite with a grey smear above it. Disclosed correctly. The word is fixed by the verse.
   - `Pistával`: plain `3`, no dot. Confirmed.
   - `szóval`: plain `3`, no dot. Confirmed. `szódal` is not a word here.
   - `Árpád`: plain `3` in the box, no comma. Confirmed. hcp-1174 does have `1' 3, 9 1' 3`.
   All four are marked `x>y` in the transcription and disclosed in `SOLUTION.md`.
5. **Other hard signs.** `hadjuk`: the upper dot merges with the flag, the lower dot is clear (`c.png`). `0,` versus `9` in `többet`, `gyötrelem`: the sense needs `0,` and the pixels allow it. `kedvesem`: the last sign is a clear `8`, not `3`. The dash under its first sign is the same size and colour as the broken dashed row above the date, and is probably part of it, so reading `7` is right.
6. **Key against sister cards.** hcp-1174's `work/decode.py` holds the same 13-sign heading and the signature. hcp-1179 has `1,` = b. hcp-1178 has `-dal` for `-ddal`. hcp-1175's notes do hold `4.` = l and `1` = é, as the solution says. No sign value here conflicts with the FINAL cards.
7. **Language and context.** The text is period Hungarian with a rhyming quatrain and couplet. The spelling habits (single t, `hadjuk`) are consistent. 12 Feb 1916 was a **Saturday** and 15 Feb a Tuesday, which fits well: this card promises "Sunday", and hcp-1174 three days later apologises for not coming. The solution does not state this; it adds support. The clear date and address read as stated. Postmark: FEB 12 is clear; the year digits are overstruck and I do not rely on them.
8. **Honesty.** No published solution is used. The new and inherited key values are separated, and the unchecked HistoCrypt article is stated.

## Findings

1. **minor: false claim in "Why I believe it is correct".** It says the four new signs "each recur in several unrelated words". Counts from `review/work/own_decode.py`: `4.` 7 times and `6` 6 times, but **`4` occurs once** (felmegyünk) and **`6.` occurs once** (anyám). Those two values rest on a single word each. Both words are secure in context, so the reading stands, but the sentence must be corrected to say so.
2. **minor: `kedvesem` translation is not sound.** "I remain, my faithful sweetheart, and your adorer" and the Slovak "zostávam, moja verná milá, i tvoj ctiteľ" take `hűséges` with `kedvesem`, which leaves the sentence broken. The natural parse is `maradok hűséges, kedvesem, és imádód` = "I remain faithful, my sweetheart, and your adorer" (sk: "zostávam verný, moja milá, a tvoj ctiteľ"). The alternative that `kedvesem` is a slip for `kedvesed` ("your faithful sweetheart", compare hcp-1174) should also be stated. Hungarian text unchanged. Note that the plaintext as punctuated needs the comma after `hűséges`.
3. **minor: punctuation claim.** `SOLUTION.md` says the writer's `;` is noted in `work/transcription.txt`, but there `;` is the word separator and the card's semicolon after `többet` is not recorded. Its dot sits above the comma of the final `8,`. Add a comment line, or change the sentence.

## Observations, no change needed

- `Pistádal` for `Pistáddal` is a true alternative and is disclosed. Given `-dal` on hcp-1178, the sign as written has a real reading here, unlike `szódal`. The solver's choice of `Pistával` is reasonable, and the report should carry the alternative.
- Whose mother is meant and where "there" is remain thin, as disclosed.
- The `I` in the margin stays unexplained, as disclosed. It does not touch the reading.
- Under the run's rule for completeness, every word is understood, so this is a full solution. Register type `MASC` is appropriate.

## What I could not verify

- Whether the HistoCrypt article linked from the portal discusses this card. I did not open it.
- Whether the verses have a printed source. I did not search.
- The postmark year.
- Whether the box around the signature is by the same hand or later. The brown line differs from the sign ink, but the signs inside match the writer's digits.

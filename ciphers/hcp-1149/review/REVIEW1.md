ACCEPT

# Review 1 of hcp-1149 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I tried to break it sign by sign on the hires scan and found no wrong word. Only minor points remain, and all of them are about how the signs are reported. None changes the sense.

## What I verified and how

1. Command. `python3 -I ciphers/hcp-1149/work/decode.py` from the repo root: hashes OK (4 files), `493 cipher signs, 30 distinct`, every line agrees. The output matches the Plaintext section of SOLUTION.md apart from the stated normalisation. I also recomputed all four SHA-256 values with `shasum`. They match SOURCES.md.
2. How the script works. It decodes the tokens and compares them with a hard-coded `EXPECT` after folding, then prints `EXPECT`, not the decoded string. The folding (`u`/`ú`/`ű` to `ü`, `ó` to `o`, `í` to `i`, `ő` to `ö`) only removes distinctions the key does not make, so the check is real and the printed text is what was checked.
3. Independent decoder. `review/work/stats.py` has its own key, written from the hcp-1174 table and the consonant series, and imports nothing from the solver. It gives the same text, 493 signs, 30 distinct, and no unmapped sign. Raw output has `tüdtünk`, `bükdos`, `sügára`, `borülás`, as the solver disclosed for `:1`. No sign is left over and there are no gaps.
4. Transcription against pixels. I did not sample. I read every row myself from hires crops at 1.8x to 4x, without using the solver's crops (`review/work/rcrop.py`, `crops/L1-L6`, `R1`, `Z1`, `B1`, `B2`, `V1`, `X1-X7`, `Y1-Y4`): salutation, all 12 letter rows including their right ends, box 1, box 2, box 3, all 5 vertical rows. Every sign agrees with `work/transcription.txt` except the one in finding 1. The hand is large and clear, and most marks are unambiguous.
5. Solver's flagged points, each checked on the pixels:
   - `sötét`, `üdvözöl`, `ölel`: the `0,` is a 0 with fused comma, so it looks like `9,`. This is the same behaviour as hcp-1174. `7, 9 8, 2. 8,` would give nothing, and a true 9 in this hand has a long straight stem. Sense-assisted, but sound.
   - `dörgött`, `vettem`: the first `8,` has a tail running out of the body. Sound.
   - `4,` in `világom` and `hűséges`: comma fused into the hooked stem. Sound; a plain 4 (`f`) gives no word.
   - `7,` in `boldogságom`: hooked tail. Sound.
   - faint upper dots of `1:` in `szerencsésen`, `vettem`, `kedvesed`: both marks present or the brown trace visible. Sound.
   - `S` in box 2: looped open capital, not a digit. Sound.
   - `Reám`: the pixels look like `Reoim`, as the solver says. No other word fits. Sound.
   - `kérd`: one `3` after `3,`. Confirmed: `7 2. 3, 3`.
   - tick at the foot of the `7` in the first `értünk`: visible, a tick and not a separate comma.
6. Key and new values.
   - Counts: `2` 1, `5.` 1, `6` 3, `6.` 3, `4` 5, `4.` 13. All the recurrence claims in "Why I believe it is correct" hold. Note that `2` = c occurs only in `kacagni`, so it rests on one word.
   - Salutation and signature agree sign for sign with the hcp-1174 script: `2. 3 1: 7,`, `8 1. 3, 4, 1 8, 7 1' 8`, `1' 3, 9 1' 3`, and `7 1: 3 3. 1: 7, 1: 3`.
   - No value conflicts with hcp-1174, 1178 or 1179.
   - The key has a structure the solver does not state, which supports the new values independently of this card: the plain digits are b c d f h j k m p in order (with 1 needing its own mark for b), the comma series is cs r g l n s t z, and the dot series pairs the digraphs gy, ny, sz with their base g, n, s. `4.` and `6.` are the values that pattern predicts.
7. Language and context. Period Hungarian throughout, and a coherent story. `félegyre` = by half past twelve is correct, as are both translations. `terem / szerelem` rhymes across open and cipher text, which is a real check, because the open half fixes the rhyme. The vertical verse's `-om` chain also holds. Sender and addressee agree with the family and with the open address, which I read: Őnsg., Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács. The written date reads `1916, IV/26` and agrees with the file name.
8. Picture side, which SOLUTION.md does not mention: a printed couple with lilacs, no writing. The speckled patch at the top left is surface damage on the hires scan, not script. So nothing unread exists on the card.
9. Sources. The portal status and absence of an attached solution are as stated in `source/metadata.md`. Nothing in the directory suggests use of a published solution.

## Findings

1. **Minor. `legalább`, sign 4 of `1' 1, 1,` is not a clean `1'`.** On `review/work/crops/Z1.png` the sign carries a clear high dot and also a small separate dark dot at the foot, which by the solver's own convention is `1:`, giving `legalebb`. A true `1'` such as in `lámpát` has no lower dot. The dot may be a stray speck or a slip; `legalább` is certain as a word. But the transcription prints `1'` and the uncertainties do not list it. Fix: list it under sense-assisted calls.
2. **Minor. First sign of `hűséges` is not in SOLUTION.md.** On `crops/Y3.png` the sign is a closed S-shape close to an 8, and its overbar sits detached to the right, over the following `:1`. NOTES.md records that it was first read as 8. `5` is right (`mű-` gives no word, and 8 in this hand is compact with no bar), but this is a sense-assisted call and belongs in uncertainty 1, which currently mentions only the comma of `4,` in that word.
3. **Minor. `5.` in `ilen` is better taken as ly, and items 3 and 6 disagree.** Item 3 leaves ly open, while item 6 states `ilen` as a writer's spelling and the key has `5.` = l. The series in point 6 above favours ly on structure: `4,`/`4.` g/gy, `6,`/`6.` n/ny, `7,`/`7.` s/sz, and so `5,`/`5.` l/ly. `ilyen` is the exact place that value would be used. Against it, hcp-1178 and 1179 use `5.` for plain l (`csókollak`, `legszeb`). The value is not settled by one occurrence and the meaning is the same, but the entry should state the argument and items 3 and 6 should agree, for instance by removing `ilen` from the list of misspellings or marking it as conditional.
4. **Minor. Punctuation list is incomplete, and the picture side is not mentioned.** Item 7 omits the dash after `raj` at the row end (a hyphen, in effect) and the dash after the second `sugára`. The `!` after the salutation is printed in the plaintext but not transcribed. SOLUTION.md should say the picture side has no writing, since the completeness rule covers the whole card.
5. **Minor. "Box 2 does not rhyme" is too strong.** `életet / szeretlek` is at most an imperfect assonance. Harmless; "no clean rhyme" would be accurate.

## What I could not verify

- The postmark. Inked over the stamps; on `crops/P1.png` no date or place can be read, so the date rests on the written one, as the solver says.
- Whether the verses are from a published poem, and whether the HistoCrypt article linked by the portal discusses this card. I searched for neither. The solver disclosed the same limits.
- The value of `2` = c outside this one word, and u under `:1` as a designed value and not an economy of the writer's; both fit but are single-family evidence.
- The role of the mark rows along the vertical verse and the double stroke at the end of `elhoztam`.

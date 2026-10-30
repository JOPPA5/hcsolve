REVISE

# Review 1 of hcp-1826 (pc_hcp_507)

Reviewer: Claude Opus 5.5, 2026-10-30. Key and reading order stand, and 296 of the 300 signs are confirmed. One word at the end of T5 is misread and needs correcting before FINAL.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1826/work/decode.py` from the repo root. Source hashes OK, 300 signs, 29 forms, no unkeyed token. Its output matches the plaintext in SOLUTION.md character for character.
- Independent decoder: `review/work/indep.py`. I typed the rows myself from my own crops, without word division and in my own notation, and parsed them with a separate key. Result: 300 letters against the solver's 300. The only difference is the last word of T5 (see finding 1).
- Scans: `review/work/crops*.py` make contrast-enhanced 3x to 10x crops of `work/hires/pc_hcp_507_adr.JPG`, in `review/work/crops/`. I read all 18 rows (S01-S12, T1-T6) sign by sign, not just a sample. Every row agrees with work/transcription.txt except finding 1.
- Key: consistent over the whole card. The solver's consonant run b=19 to v=3 skipping vowels, y=0 holds, and each form has one value. All 14 keyed `1'` have a visible dot and no bare `1` occurs as a letter.
- Reading order: S12 "Let me" continues into T1 "knew if you"; the upside-down block runs from the card centre to the edge and ends in the signature.
- Language and context: ordinary American English of the 1910s with plausible spelling slips. "Carrie" agrees with the pencil name on the picture side. The address reads Miss Fannie J. Roberts, Bloomville, Delaware Co., N.Y., R.D. #1, as in SOURCES.md. The portal shows no solution. There is no sign of a published source; I searched only ciphers/*/SOLUTION.md, which has no other Carrie card.
- Solver's disclosed uncertainties checked on the pixels: "planing" (one 9, confirmed), "knew" (2 with dot, confirmed), "anothe reason" (nothing between 2' and 6, confirmed), S10 "Aug." (the faded sign has the 5's separate top bar, so 15 = g, confirmed), "soun" (5 [0 0] 9, second box closed on the right, confirmed), 1:48 (a colon of a tick and a dot, then 4 and 8 with its top bar, confirmed).

## Findings

1. **major: T5 last word is "what", not "with".** The transcription gives `0' 1' 4 14`. On the card (`review/work/crops/with.png`, `with_rot.png`, `with_compare.png`) the signs are 0' 1 4 X 4, and the correct division is `0' 14 X 4` = what.
   - The dot in the corner belongs to the 0'. There is no dot after the 1, although all 14 other i on the card have one. The solver noted the missing dot and explained it away.
   - The fourth sign is not a thin 1 stroke. It has a top bar running left and a bulge at mid-height, and it is about twice as wide as a 1. That is the Z-like sign X, its foot merged into the final 4 because the writer ran out of card.
   - 14 X 4 is the same ending as "that" in S03 (4 14 X 4), shown in the comparison panel. "with" in S11 shows the expected 0' 1' 4 1 4 with its dot, and it does not look like this.
   - Sense: "I just as soon help you what I can any way." is one plain sentence. The solver's "help you with [it]. I can anyway." adds an object the card does not have and splits the sentence in two.
   - The sign is cramped, so this is a strong reading rather than a certain one; say so. Fix in work/transcription.txt (`0' 14 X 4`), the literal plaintext, normalized English and Slovak translation, and replace the uncertainty bullet for T5. The Slovak should become something like "Rada by som ti pomohla, ako len budem môcť." The total stays 300 signs.

2. **minor: "Why this is correct" and the T6 uncertainty are worded too strongly.** T6 is called "the one reading supported mainly by the word itself" although the T5 note admitted the same problem. Reword after the fix.

3. **minor: stray dot at T6 not disclosed.** A dot sits above the first stroke of (18) (`review/work/crops/sig.png`). It does not belong to the 2' of "love", whose dot is further left. It may be a stray or a period after "love". The circle reading stands: the arc over the 8 is visible and the pencil signature confirms Carrie. Mention it.

4. **minor: dating evidence can be stated better.** The postmark shows "JU", a third letter I cannot decide (L or N), and "191" (`review/work/crops/postmark.png`). The text's "until the last of Aug." agrees with a June or July mailing; add that. The pencil surname reads best as Craig on an enhanced crop (`review/work/crops/pencil.png`), with the g descender visible. SOLUTION.md may prefer Craig while keeping it marked as uncertain. It is outside the cipher.

## Could not verify

- The upper arc of the postmark (town name) and the last digit of the year are not legible, so no exact date.
- "B" and "T." remain unexpanded. Bloomville for B is a reasonable guess only, and it is correctly marked with a question mark.
- Whether the writer meant o or u in the boxes closed on both sides (S09 "until", S10 "of", S12 "reason"): settled by the word only, as disclosed.
- Finding 1 rests on a low-resolution corner of 5 cramped signs; no higher scan exists in work/hires.

## Required before FINAL

Fix finding 1 and rerun the decoder. Findings 2 to 4 are small text edits. The solution need not return for a second review if only these changes are made.

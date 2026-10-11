REVISE

Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), 2026-10-11. Round 1 of `hcp-351`. Read `ciphers/hcp-350/review/REVIEW1.md` first: the verification, the limit on my independence and the general findings there apply here too. The scripts are in `ciphers/hcp-350/review/work/`.

The decipherment stands. The verdict is REVISE only because the ciphertext file still contains letters that an independent blind reading contradicts, and that reading gives better Slovak under your own key. Fix those, then finish; no second round is needed unless the key changes.

## What I verified

- My own decoder (`independent.py`) reproduces the stored plaintext for all 385 letters from `key.json` and re-encrypts it exactly.
- The 351 key shares both rings and the distance table with the 350 key; the masks differ in one stop (48 in place of 0).
- A blind transcription of this scan, made by a second Claude instance before any plaintext existed, differs from your final `ciphertext.txt` at 5 positions out of 385. Decoded with your key it reads as the same message (`blind_check.py`, output in `run-output.txt`).
- Plaintext of 350 at position *i* against plaintext of 351 at *i*+1, for *i* = 21…374: identical except at five positions (81, 85, 122, 230, 315). The two copies carry the same text.

## Findings

**1. Positions 11 and 12: `RW` should very probably be `PM` – major.**
Your text has group 3 as `RWQKK` and decodes the opening as `ZMNOHZJHMOZNOSTTI`. The blind reader has `PMQKK`, the same as in 350, and under your key that gives `ZMNOHYCHMOZNOSTTI` – "z mnohých možností", correct Slovak. The first 20 cipher letters of the two messages are otherwise identical, so a difference here was always suspect. SOLUTION.md calls this stretch "damaged"; it is more likely a misreading. Recheck the two glyphs on the scan and correct them if the scan allows.

**2. Position 86: `R` or `P` – minor.**
You now prefer `R`, which decodes to `PSEDAVAIUCI`. The blind reader has `P`, which decodes to `PREDAVAIUCI`, the word that is there in 350. I have not looked at the glyph. If the scan really shows R, keep R and say that the plaintext letter is then a garble; do not present R as preferred without mentioning that P gives the correct word.

**3. Position 231: `L` or `I` – minor.**
Same situation. `L` gives `EXIITUIE`, `I` gives `EXISTUIE`, and the blind reader has `I`. You already carry this as the `collated-moderate` variant. With an independent reading agreeing, I would make it the default and keep `L` as the noted alternative.

**4. Position 73 goes the other way – no action.**
The blind reader has `U` where you have `O`; your letter gives `SUVELMI` and theirs `SLVELMI`. Yours is right, and the blind reader had marked that cell as unsure.

**5. The inserted and dropped letters should be stated plainly – minor.**
Relative to 350, this copy has one extra letter at position 21 (`MOZNOSTTI`) and lacks the `E` of `ROZHODNUTIE` near the end, which is why the two bodies run one place apart for 354 letters and realign for the last ten. That is the whole explanation of the offset-plus-one relation. It deserves one clear sentence in SOLUTION.md and the report.

**6. Date – minor.**
The second reader read the round postmark as `-2 III 44-23` and the handwritten number as `816/1229`. That puts this telegram on 2 March 1944, right after 350 (28 February), which fits the consecutive numbers 3001 and 3002. The portal date 1944-11-03 is then probably a day/month confusion. SOLUTION.md mentions a "date caveat"; state the reading and the conflict explicitly, and record it in SOURCES.md. I did not read the postmark myself.

**7. Model attribution inside the file – minor.**
The header names "GPT-6 Astra" and later sections "GPT-6.1 Sol". Say once, clearly, which model did what.

## What I could not verify

As for 350: the physical machine model, individual glyphs on the scan, the labels of the rare letters on the input ring, and your control experiments.

## What the solver should do

1. Recheck positions 11, 12, 86 and 231 on the scan and update `ciphertext.txt`, `pixel-manifest.json` and the stored plaintext accordingly. Report what the scan shows for each, whichever way it goes.
2. Address findings 5 to 7 in SOLUTION.md.
3. Then produce the report. No register entry without the human's go-ahead; see the note at the end of the 350 review.

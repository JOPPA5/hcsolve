ACCEPT

# Review 1 — hcp-1505 (pc_hcp_186), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1505/work/decode2.py` (from repo root):
   source hashes OK, 102 signs, 1 restored; the literal output matches the plaintext
   in SOLUTION.md word for word (IAM GOING / FOR MY SUIT TO NIGHT SO / WILL NOT HAVE
   TIME TO / WRITE BUT WILL SEND A / LETTEI TOMOIIOW HAVE / A GOOD DA lOVE TO BOTH /
   YOUR OWN).
2. **Independent transcription and decoder.** I re-read every number myself from
   rotated 2–6x crops of `source/address-large.jpg` (`review/work/crop.py`,
   `enh.py`; crops `whole.png`, `iam.png`, `top.png`, `l2.png`, `l4.png`, `da.png`,
   `gap.png`, `gap_enh.png`, `patch.png`, `love.png`, `a26.png`, `own.png`,
   `hdr.png`) and typed my own transcription (`review/work/my_transcription.txt`).
   My decoder (`review/work/my_decode.py`, key n -> reversed alphabet, 1=Z…26=A)
   gives the identical 102-number decryption. The key covers the whole ciphertext;
   every value used (2–26) is decoded by the same fixed table.
3. **Sign-by-sign checks of the disputed/restored signs.**
   - 7 vs 4 (NOT 13.12.7, TO 7.12, TIME 7.18.14.22): the writer's 7 is a Y-like
     hooked form with a descender, his 4 an open h-like form (WILL, WRITE, OWN
     12.4.13). Distinction is clear in `l2.png`, `own.png`. Confirmed.
   - LETTER / TOMORROW: `l4.png` shows clearly underlined **18** at the end of
     LETTER and 18.18 in TOMORROW. R = 9 in FOR, WRITE, YOUR. So the R->18 slip is
     a real writing slip, not a misreading, and it is disclosed and corrected only
     in the normalised line. Accepted.
   - Group after GOOD: `da.png` shows 23 (open-curved 3, unlike the flat-based 2s
     of 22) and 26 (same looped 6 as in 26 = A on line 4, `a26.png`; not the
     writer's 4). Reading 23.26 = DA confirmed, followed by a dot.
   - First sign of LOVE: `gap.png`/`gap_enh.png` show a 5 whose underline extends
     to the left of the 5, inside a lighter, abraded patch of paper. Consistent with
     a 15 whose 1 has faded. Restoration to L is the only value giving a word, and
     it is disclosed and marked in the transcription (`15r`) and output (lower case).
   - Ordinary rows sampled (lines 1, 2, 3, 5, 7) all match the transcription.
4. **Language/context.** Idiomatic WWI-era English ("going for my suit to-night",
   "will send a letter tomorrow", "love to both", "your own Fred"). Plain header
   "Scotland … Dear Ethel" visible (`hdr.png`); address Barnsley, Yorks, England.
   24 March 1917 was a Saturday (python datetime), matching "Sat." in the header.
5. **Sources/credit.** Portal status Not solved, no attached solution; SOLUTION.md
   credits the GPT solver's key identification and partial transcription and the
   Claude completion truthfully. No published solution used.

## Findings

1. **minor — possible lost sign before LOVE should be disclosed.** Between "23 26."
   and the faded "[1]5" there is a gap of about 60 px (room for 2–3 numbers) lying in
   the same abraded, lighter patch that removed the 1 of 15 (`patch.png`). A faded
   2 (= Y, giving DAY) or other sign there cannot be excluded, though the dot
   directly after 26 argues against a Y belonging to that word. SOLUTION.md
   uncertainty 2 should mention the abraded gap explicitly, not only "Y omitted",
   while keeping DA as the literal reading.
2. **minor — "IAM written as one group" is not what the pixels show.** In `iam.png`
   the gap between 18 and 26 is about as wide as the gap between 14 and 20, i.e.
   the writer most likely wrote I / AM as separate words. Harmless for the reading;
   correct the statement (uncertainty 4) and optionally the transcription.
3. **minor — underlining is not perfectly systematic.** SOLUTION.md says two-digit
   numbers are underlined; 14 in TOMORROW (line 5) is not underlined (`l4.png`).
   No reading depends on it, but the statement should be softened ("mostly
   underlined").

## What I could not verify

- The postmark is not legible in the scan; the date 24 March 1917 is taken from the
  portal metadata only.
- The addressee's name (Mrs … Baxter?) and "Sat. noon" were not re-read in detail;
  they do not affect the decryption.
- Whether anything was written in the abraded gap before LOVE (finding 1).

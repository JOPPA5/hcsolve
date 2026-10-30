ACCEPT

# Review 1 of hcp-1503 (pc_hcp_184): Morse love note to Miss Curtis, Lincoln

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (marker DONE1).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1503/work/decode.py` (run from the repo root): all three source SHA-256 checks are OK. Its output matches the plaintext claimed in SOLUTION.md line for line (HD + A..L).
2. **Independent decoder.** `review/work/mydecode.py` uses my own Morse table and parser, run as `python3 -I review/work/mydecode.py work/transcription.txt`. It gives the same 13 lines. Every token is a valid International Morse letter, with no adjustments and no extra cipher layer. The only non-letter tokens are the one `(.)` (line A) and the one `~` flourish (line L). The transcription has 189 letters and 484 Morse elements.
3. **Transcription against the scan.** I made my own enlargements of `source/address-large.jpg` with PIL (4x row strips `top_*`, `r0..r5_*`, `bottom_*`; 7-8x spot crops `rather.png`, `setting.png`, `coon.png`, all in `review/work/`). I read these sign by sign:
   - HD and line A: the separators are clear. MONDAY / SWEETHEART / WIFIE are confirmed, and so is the isolated tiny raised dot before the W of WIFIE.
   - Line B, RATHER (x≈447-530): I see `.-.` `.-` `-`, then a merged cluster at x≈495-509, a mark on the rule, and `.-.`. The cluster is compatible with 4 dots (H). Its width and lumps support at least 3-4 dots, and the surrounding letters fix the word.
   - Line D: `-..` `.-.` `.` `.-` `-..` `..-.` `..-` `.-..` `.-..` `-.--` / `-` `..` `.-.` `.` `-..` / `-` `---` is confirmed, plus the smear on the rule.
   - Line E: N I G H T / I V E / B E E N / S E T T I N + the blot on the rule + a dot. The blot is one dark mass with a tail. I cannot see two separate dashes in it (see finding 2).
   - Lines G, H, I (sample): MAKE MY C..., HANG ON, YOU LIKE ... are confirmed element by element.
   - Line J, COON: `-.-.` `---` `---` `-.` is compatible. The last dash of the second O lies on the rule, as disclosed.
   - Lines K and L: WORSE THAN, and BEFORE, flourish, C U C K O O are confirmed. Line L is cramped but legible.
4. **Language and context.** The text is natural Edwardian English ("work went down rather flat", "to-night", "how should you like that job"). Its grammar runs across line breaks, and noise forced into words does not produce that. The address (Miss Curtis, Laurel House, Riseholme Rd, Lincoln), the Tooting S.W. postmark with year ..05, and the halfpenny Edward VII stamp all fit 1905. "Suvtis" in the portal catalogue is indeed a misreading of "Curtis". 1905-06-20 was a Tuesday (computed), so MONDAY = 19 June is consistent with the postmark.
5. **Sources and credit.** The portal showed Not solved with no attachments. No published solution is used. The earlier GPT triage (MONDAY, SWEETHEART) is credited truthfully, and the rest is credited to Claude Opus 5.5. The racial slur "coon" is rendered literally with a historical note, which is appropriate.

## Findings

1. **minor – wrong element count.** SOLUTION.md ("Why I believe it is correct") says "about 330 Morse elements". The transcription actually has 484 elements in 189 letters (counted by `review/work/mydecode.py`). Correct the figure.
2. **minor – SETTING final G is partly context-driven.** At 8x (`review/work/setting.png`) the mark at x≈514 is a single heavy blot on the printed rule with one visible tail. Two merged dashes cannot be told apart from one dash there. Read as one dash, the last letter would be `-.` (N), giving "SETTINN". The reading `--.` is therefore chosen from the word, not from the pixels. Uncertainty 4 discloses the blot but says "I read the blot as two merged dashes". It should say plainly that the element count of this letter is not decidable from the scan and that G is restored from context.
3. **minor – same point for the H of RATHER and the last O of COON.** Both are disclosed (uncertainties 2 and 6), and both readings are the only ones that give words. The "Coverage" paragraph should still list them alongside items 1/3/5/7 as context-supported rather than pixel-certain. As written, it says that all elements are "read from the pixels".
4. **minor – `(.)` printed in the running plaintext.** The decoder emits "SWEETHEART (.) WIFIE" in the running text. That is acceptable as a diplomatic transcription. The normalised English and the report should state once that the dot is omitted there, which the normalised text already does implicitly.

## What I could not verify

- I did not re-derive every single letter separator on all 13 lines. I checked HD, A, B (RATHER), D, E, G, H, I, J (COON), K and L in full or in part. Lines C and F were checked only at 4x overview level, and they are consistent.
- The exact day/month on the postmark is not legible to me. The date rests on the portal metadata.
- The identity of "Cuckoo" and of Miss Curtis of Laurel House, Lincoln cannot be checked from the card.

# Notes hcp-898

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — solver pass (Claude Opus 5.5), result: PARTIAL, no marker

What the card holds (picture side, work/hires/..._pic.jpg, 3410x2265):
- Top line in plain German Kurrent: "für deine lb. Karte!" (the preceding words run off the top edge; not read).
- Right block: ~16 lines of cipher in invented signs, written over the picture; the lower 5-6 lines
  (y ~1300-2000 px, x ~2400-3300) are overprinted by the grey HCPortal "Cipher Collection" watermark.
- Left block: ~14 lines of the same cipher over the dark photo area, ending ".62/6." (repeated on the bottom margin).
- Vertical writing along the left edge (cipher signs, read sideways).
- Address side not yet examined in this pass.

Cipher observations (from 2-4x crops of the red channel; red channel + contrast stretch 95..150
removes most of the watermark, see work/stretch_full.png, work/z/, work/ln/):
- "x" (a small cross) occurs between groups and behaves like a word separator; "-.-" / "---" also occur,
  apparently as dashes/pauses. A long oblique "/" stroke occurs inside groups (letter, not divider).
- Sign inventory seen so far (provisional labels): i (dotted stroke), I (bare stroke), T (stroke with top bar),
  k (K-like), 6, H, 2, S (long-s loop), L (open c/l loop), 3, 88 (double loop, possibly one sign),
  w, phi (circle with descender), P, X, p, r. About 17-20 signs: consistent with a monoalphabetic substitution.
- Recurring group H T phi H 3 T 2 (three times) and phi H 3 alone (twice).
- Provisional transcription of the clearest lines is in this log only (not verified sign-by-sign):
    Sw x Li/I x | Tk/I x w3 x /2 --- 88iiLr x wik | 26 x i x L6HTk x LTTk iiLS |
    HTphiH3T2 x S6/ x 886k x i6 | 8iiL -.- 1ux /p6/ x i6/I x | Sw x TI2T x 26/i x PTphiH3T2 |
    88ik x /i2S x /Tik x Hiw/ x 268i x | i6w/T x HTphiH3T2 x iTk -.- TILTk | ...
- Trigram hill-climbs against a small German reference text (scratch, not kept) gave no readable German
  with either "x = separator" or "x = letter". The reference corpus was too small to be decisive.

Why this stops:
- The card holds about 30 lines of cipher, and several sign classes (i / I / T, 8 / 88, L / l-loop, the k variants)
  are not yet separated reliably. Part of the right block is covered by the watermark, so a complete
  sign-by-sign transcription cannot be made to the required standard in this pass, and no key was established.
- No published solution of this card was found in the repo; no web search was made.

Next steps for a later pass: transcribe all lines sign by sign into work/transcription.txt with a sign ledger;
build a larger German n-gram model (for example from the German plaintexts of FINAL cards hcp-899, 905, 962, 995,
1016, 1017, 1021); test the word-pattern ABCADBE (H T phi H 3 T 2) against a German word list; look at the
address side and the vertical margin text.

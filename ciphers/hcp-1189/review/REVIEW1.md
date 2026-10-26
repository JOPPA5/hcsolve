ACCEPT

# Review 1 — HCP 1189 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **DEAR VELMA / I LOVE YOU. is correct.** All 17 signs read independently from the scan agree with the solver's transcription, and they decode under one consistent dot-count Pigpen key. The only weak points are two dot counts in VELMA. The solver flagged them, and the recipient's name on the card settles them.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1189/work/decode.py` runs. The hashes match `shasum -a 256 source/*.jpg`, and the output matches `SOLUTION.md`: `DEAR VELMA / I LOVE YOU.`, 17 glyphs, 11 distinct.
2. **Independent decoder.** I wrote `review/work/review_decode.py` from scratch, without importing the solver's code. It uses the 9 cells of the #-grid three times; the number of dots selects the block (1: A–I, 2: J–R, 3: S–Z). On the solver's transcription it prints `MATCHES CLAIMED`. Repeated letters keep their sign: E = C1 ×3, L = BL2 ×2, O = L2 ×2, V = R3 ×2, A = BR1 ×2.
3. **Independent reading of the scan.** I made crops at 3×, 5–7× and 20× (`review/work/r1.png`, `r2.png`, `z-velma.png`, `z-velma-V.png`, `z-love2.png`) and a contrast-enhanced version (`zc-velma-VM.png`), then read every sign. `review/work/reviewer-reading.txt` is identical to the solver's tokens and decodes to the same text (`MATCHES CLAIMED`). Sign by sign:
   - line 1: `⊐·` D, `□·` E, `┘·` A, `Γ··` R | `⊐(··/···)` V, `□(blob)` E, `L··` L, `⊐··` M, `┘·` A
   - line 2: `Γ·` I | `L··` L, `⊏··` O, `⊐···` V (three separate dots, very clear), `□·` E | `7···` Y, `⊏··` O, `L···` U, then a full stop.
4. **Context.** The address is "Miss Velma Cornel, Hanford, Calif.", which matches the catalogue's recipient "Velma Cornel". The picture side is a printed Dwig comic card ("How can you do it on 9.50 per?"). The address side is printed "POST CARD … Germany, Serie No 49" and carries a green 1-cent Washington stamp of the 1908–1914 type. A machine cancel shows a day of "30" but no legible year. All of this fits c. 1909–1915, and the solver correctly claims no date.
5. **Prior solutions.** I found nothing indicating a published solution was used. The key transfer from HCP 1193/1190 is disclosed.

## Findings

1. **minor: V and E of VELMA are decided by the address, not by counting dots.** In `zc-velma-VM.png` the first sign of VELMA shows **two** separable dots. That is the same as the `⊐··` (M) two signs later; the right-hand dot is elongated and may be two dots merged. The E carries one wide blob, about twice the width of a single dot. Read strictly by visible dots, the word could be MELMA, or with other merges VNLMA. The solver mentions "closely clustered dots" and a "dark single-dot blob". `SOLUTION.md` should state plainly that the visible count for the V is two, and that R3 is chosen because VELMA is the addressee's name. As it stands, the address match is described only as corroboration. The V in LOVE, with three clear dots, supports R3 = V as part of the key.

2. **minor: the reproduction command only round-trips a manual token list.** The solver discloses this. The tokens are a genuine as-seen transcription, which I checked against the scan, so the command is adequate. The roundtrip assertion should not be cited as evidence.

No blocker or major issues.

## What I could not verify

- The exact dot counts in the V and E of VELMA (finding 1).
- The postmark town and year.
- Whether a decipherment has been published elsewhere.

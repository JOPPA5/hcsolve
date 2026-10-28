REVISE

# Review 1 — HCP 1532 / pc_hcp_213 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-28. Short version: **the key and the reading are right.** I re-read all eight body rows and the right-edge margin sign by sign. Of the 497 signs, I read 495 exactly as the solver did. One sign is a definite misreading that hides a writer's slip: the first TEPRVE is written **TEBRVE** (finding 1). One sign is ambiguous and was silently resolved (finding 2). The verdict is REVISE only because `SOLUTION.md` says outright that "No base letter is inserted, removed or substituted", and that is not true for the transcription as handed over. The plaintext and translation stand. The fix is local, and I see no need for another full review round.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1532/work/decode.py` (run from the repo root) exits 0. It prints the 9 literal rows shown in `SOLUTION.md` exactly, then `Verified: 497 cipher units; 1 CH units; 498 base letters`. The script is read-only (no writes) and standard-library only. `git status` shows no change in `work/` after running it.
2. **Independent decoder.** `review/work/decode_review.py` is my own decoder. It does not import the solver's code. It reads a key JSON and a cipher text file and reports any sign not in the key. I typed `review/work/key_review.json` from the family table. It is identical to `work/key.json` (checked programmatically): 22 shapes, a bijection, and `ř` → CH. Decoding the solver's transcription (`solver_cipher.txt`, extracted from `work/transcription.json`) gives output byte-identical to the solver's printout (`solver_decoded_by_reviewer.txt`). All 497 units are in the key, and there are no unknown symbols.
3. **Independent reading of the scan.** I cropped `source/picture.jpg` with `ffmpeg` (`review/work/crop.sh`). Each row is cut into three slope-corrected 4× strips (`r1_0.png` … `r8_2.png`), with 7–14× details (`z_*.png`, `v_*.png`, `cmp_*.png`). The margin is rotated 90° clockwise (`z_margin.png`). I read every sign before comparing with the solver. My reading is in `review/work/reading_review.txt` (same shape labels), and its decoding is in `reading_review_decoded.txt`. `diff` against the solver's transcription:

   | Place | Solver | Reviewer | Finding |
   |---|---|---|---|
   | R01, 1st TEPRVE, 3rd sign | `b` (P) | **`p` (B)** → literal TEBRVE | 1 |
   | R08, OD before TVEHO, 2nd sign | `t` (D) | `d`-bowl with a `t`-crossbar, ambiguous | 2 |
   | R07, V URADE | `f 2h6t5` | `f2h6t5` (written joined) | spacing only, not a finding |

   Everything else agrees sign for sign. That includes all the places the solver flagged: ZDA-LI (`qt6-84`), whose first sign has the hooked z-descender (`z_zdali.png` against `z_za.png` and `z_ktery.png`); LEPE; SOBOTNI; BYL; MUSIL (`n2c48`); the single CH in DUCHU; and NESCISLNEKRATE, written without the second E (`z_nescisl.png`). I agree that no letter should be inserted there. The marginal continuation `r86f4mg2 84p6.` = HLAVINKU LIBA is complete. I found **no other cipher text**: the flower area, top and left edges (`z_topleft.png`), the date area (`z_date.png`) and the whole address side (`addr_small.png`) have none, and no cancelled signs either.
4. **Language and context.** This is fluent, period-typical Czech of 1903. It has archaic forms: *musil*, *odložiti*, *nýbrž*, *poněvadž*, *zda-li*, *psánko*, *nesčíslněkráte*. The portal date and the handwritten date `2.XI.1903` fall on a **Monday**. That fits the text: a "Saturday card" (*lístek sobotní*) arrived only "this morning", and the writer was in the office "again all day yesterday". The arrival postmark is ŽIROVNICE ✱ SEROWITZ, legible as `… / 11 V / 03` (day digit cut off, `z_pm_day.png`), and the departure postmark is PRAHA. Both fit the address (Anna Tichá, teacher, Žirovnice u Počátek) and the "Pepouš in Prague" correspondence of HCP 1533/1535. The signature PEPOUSE matches the sister cards.
5. **Prior solutions.** The portal shows Not solved and no attachment. The Egorov / Cipher-Atelier family key and the transfer from HCP 1520–1527 are disclosed in `SOURCES.md`/`SOLUTION.md`, and the solver presents the key as transferred, not discovered. I found no sign that a published plaintext of pc_hcp_213 was used.

## Findings

1. **minor — R01's first TEPRVE is written with `p` (B), not `b` (P). The literal text is TEBRVE.** Evidence: `review/work/cmp_teprve_r1_r2_byl.png` puts R01 `d5?hf5` next to R02 `d5bhf5` and the `p` of BYL. In R01, the third sign is the descender-stroke `p` form, the same as in BYL and BRZO elsewhere in the family. R02's TEPRVE has the looped ascender `b`. The solver recorded `d5bhf5` in both rows. Fixing this does not change the meaning, since *teprve* is obvious. But the transcription is then wrong at one sign, and `SOLUTION.md`'s "No base letter is inserted, removed or substituted" is not accurate. It is the same kind of writer's slip the solver correctly keeps elsewhere (NESCISLNEKRATE). **Required:** change R01 to `d5phf5` (literal TEBRVE) and normalise to *teprve* only in the editorial Czech. Update the B/P inventory counts if `index.csv`/`manifest.json` carry per-class counts.
2. **minor — R08 OD: the second sign is ambiguous.** Evidence: `review/work/v_od_r8.png`, `cmp_od_r8.png`. The sign has a closed left bowl like this hand's `d` (T, cf. *df5r3* right after it). It also has a short horizontal bar across the ascender like `t` (D, cf. DRAHOU and DUCHU). It looks like either a `d` corrected to `t`, or the reverse. OD is certainly the intended word. The solver should still record the sign as seen, e.g. "bowl + crossbar, t/d ambiguous, read D". It should not appear as a clean `t`.
3. **minor — reproduction metadata.** `SOLUTION.md` describes the procedure and the controls well. However, `SOLUTION.md` still has stale text: it says the candidate has "no … independent-provider review, PDF, register entry or state marker", and that "Root must inspect and validate before its handover". This should be updated in the final version, which should also summarise this review.

## Required for closing

- R01: `d5bhf5` → `d5phf5` (literal TEBRVE), disclosed as a writer's slip and normalised editorially. Regenerate the record hashes.
- R08: note the ambiguous `t`/`d` sign in OD.
- If these are done exactly, the solution can go to FINAL without another review round.

## What I could not verify

- Accents and diacritic pen marks. The solver rightly treats them as editorial, and I did not audit them.
- The day digit of the arrival postmark. I also did not read the departure postmark's date.
- The writer's identity ("Pepouš"), and whether a decipherment of pc_hcp_213 exists outside the sources the solver checked.

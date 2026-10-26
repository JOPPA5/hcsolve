ACCEPT

# Review 1 — HCP 1446 / pc_hcp_127 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct and complete.** The cipher is a Caesar shift (each cipher letter is the plain letter moved one place back: plain = cipher + 1). I read all 64 cipher letters on `source/address.jpg` myself and got the same text. The disclosed signature uncertainty (JOHN vs MOHN) is settled in favour of JOHN by a detail the solver did not mention. The other findings are minor transcription and record-keeping points.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1446/work/decode.py` runs (exit 0), the source checksums pass, and it prints the claimed text with `Letters: 64`.
2. **Independent decoder.** `review/work/caesar_review.py` (my own code) applied to my own transcription `review/work/my-transcription.txt` gives (`review/work/my-output.txt`):
   ```
   THANKS VERY MUCH FOR / THE CARD YOU, SENT ME, / AND GOOD WISHES / YOURS / SINCERELY / JOHN.   (64 letters)
   ```
   A letters-only comparison with the solver's output is **identical** (64 = 64). There is one shift for every letter and no exceptions. Shift 0 gives `SGZMJR UDQX…`, and no other shift gives English.
3. **Independent reading of the scan.** I made ffmpeg crops, rotated 90° clockwise and upscaled 2.5–5× (`review/work/cols1.png`, `cols2.png`, `row1b.png`, `sincerely.png`, `sig.png`). My reading, line by line:

   | Line | My reading | vs. solver `work/transcription.txt` |
   |---|---|---|
   | 1 | SGZMJR UDQX LTBG ENQ | solver `L TBG` (finding 2) |
   | 2 | SGD BZQC XNT, RDMS LD, | same |
   | 3 | ZMC FNNC VHRGDR | same |
   | 4 | XNTQR | same |
   | 5 | RHMBDQDKX | solver `RHMB DQDKX` (finding 2) |
   | 6 | INGM. | same, apart from the final full stop |

   Letter shapes I checked in particular: the decorated initial `S` of SGZMJR. The `Q`s (UDQX, ENQ, BZQC, XNTQR, DQDKX), which have a clear tail and cannot be O. The `C` vs `G` in BZQC / FNNC (no bar, so C) and in LTBG / VHRGDR (bar, so G).
4. **Missed cipher text.** I checked the whole address side and the picture side. The only other handwriting is the plain address `Miss N. J. Sawdy / The Manse / Nayland` and a plain cursive date along the lower left edge, rotated, reading **`Jan 30th 07.`** (`review/work/cursive.png`). The picture side has only the printed caption `THE GREAT WHEEL EARLS COURT LONDON`. The cipher wheel and symbols on both sides are the portal's watermark. **No cipher letters are left untranscribed.**
5. **Context.** The postmark reads `NAYLAND / B / JA 30 / 07` (`review/work/stamp.png`), on a halfpenny Edward VII stamp. That agrees with the handwritten `Jan 30th 07` and the portal date 1907-01-30 (a Wednesday). Nayland is in Suffolk, England, which fits the portal's location "Europe", the British stamp and the Croydon printer's imprint (`P.P. & P. Co. Croydon`). The plaintext is a short, idiomatic English thank-you note. Its spelling and punctuation (`YOU,` / `ME,`) are literal.
6. **Prior solutions.** The portal status is Not solved. The cipher is not in `skip.txt` and `pc_hcp_127` is not in the register snapshot in `ciphers/hcp-1450/work/`. I found no sign that a published solution was used.

## Findings

1. **minor (strengthens the claim) — the signature is JOHN, not MOHN.** In `review/work/sig.png` the first sign of `INGM` has a **dot above it** (a dotted i, upscaled ×4). Its foot turns to the *left*. Both `L`s this writer makes (`LTBG`, `LD`) have a horizontal foot going to the *right*. So the first sign is I, and the signature is JOHN. The solver disclosed the I/L doubt honestly but did not use this evidence. Please add it and downgrade "MOHN" to a rejected alternative. The writer's identity remains unknown, as the solver says.
2. **minor — two word gaps that I cannot see.** `work/transcription.txt` writes `L TBG` (line 1) and `RHMB DQDKX` (line 5), and the literal output therefore prints `M UCH` and `SINC ERELY`. In my crops (`row1b.png`, `sincerely.png`) the gap after `L` is about the same as the space between other letters, and `RHMBDQDKX` runs evenly with no larger gap. These spaces are probably artefacts of the solver's reading, not features of the card. Remove them, or describe them as "possible slight gap". The decoded text does not change.
3. **minor — card context not recorded.** `SOLUTION.md` uses the portal's recipient "N.F.Sawdy". On the card the second initial looks more like `J` (`review/work/addr.png`), although in this copperplate F and J are close. The card also gives `The Manse, Nayland`, a postmark `NAYLAND JA 30 07` and a written date `Jan 30th 07`. All of these are missing from `SOLUTION.md`/`NOTES.md` and belong in the report.
4. **minor — protocol.** The `source/` directory's mtime (15:15:09) and the `work/` directory's mtime (15:12:14) are later than `DONE1` (15:04:00), so a file was added to or removed from both directories after the marker. The image hashes in `work/source-sha256.json` still match, so the source images themselves are unchanged. No watcher was started (`NOTES.md` says this was by the user's instruction).

## What I could not verify

- The identity of "John" and the exact second initial of the recipient (F or J).
- Whether a decipherment has been published elsewhere. I did not search the web.

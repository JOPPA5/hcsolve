REVISE

# Review 1 — HCP 1506 / pc_hcp_187 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is right.** I re-read the card digit by digit and get the same English love letter under the same number key, and that key is shared with HCP 1507. I found two places where the transcription does not match the card. One of them changes a word: the card says **COME DOWN**, not COME TOWN (finding 1). The other is a token that was silently normalized (finding 2). Two pieces of numeric text on the card were left undecoded although the key decodes them (finding 3). These are corrections to the record. The reading itself stands, so the verdict is REVISE, not REJECT.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1506/work/decode.py` runs without error (rc 0). The source hash checks pass, and the output is byte-identical to `work/plaintext.txt` (`diff` is empty): 14 lines, "Numeric positions: 161". The solver says plainly that the script only maps `work/transcription.txt` through the key and does not check the reading of the image. I agree that is the right description.
2. **Independent decoder.** `review/work/review_decode.py` is my own script and imports nothing from `work/`. The key is typed from `SOLUTION.md`. Numbers that are not in the key are printed as `[n]` and are not dropped. On the solver's transcription it reproduces the solver's text exactly. On my own reading (`review/work/my_transcription.txt`) it gives:
   ```
   XXX
   OH MY DEAR / GIRL WHAT ID / THE MATTER HAVE / I DONE SOMETHIHG /
   WRONG OR ARENT Y / OU FEELING WELL / HONEY I HAVE W / ORRIED VERY MUCH /
   ARE YOU TIED OF ME / IF SO [2]OU OUGHT TO G / YOUR REASON YOU /
   BETTER COME DOWN / Sat night YOUR / FRIEY
   -- cipher tokens: 164; unmapped tokens: [2]
   ```
   Token diff, solver → reviewer: line 10 `26.7.16` → `2.7.16`, line 12 `8.7.21.25` → `18.7.21.25`, plus the header `24.24.24`. No other differences.
3. **Independent reading of the scan.** I rotated `source/address-large.jpg` by 270° (`review/work/msg_r.jpg`), cut it into 4× half-line strips (`review/work/crops.sh`) and made 6–8× details of every doubtful place (`review/work/l*.jpg`, `z_*.jpg`). I read all 14 lines before I compared them with `work/transcription.txt`. Lines 1–9, 11, 13 and 14 agree token for token.
4. **Key consistency.** One number maps to one letter everywhere, and no number would need two values: 18=D in DEAR/DONE/TIED/WORRIED/DOWN, 22=H in OH/WHAT/THE/HAVE/HONEY/MUCH, 25=N in DONE/WRONG/ARENT/FEELING/HONEY/REASON/DOWN. The writer slips that remain (ID, SOMETHIHG, TIED, FRIEY) cannot be removed by changing the key, because each of the numbers involved is fixed by several other words. The same key decodes the companion card HCP 1507, which adds 9=P, 14=K and 24=X.
5. **Language and context.** This is natural colloquial American English of the period, and every line continues the one before ("Honey I have worried very much"; "If so you ought to give your reason"). It matches the card's own context: the picture side is printed "I ISS VAITING YET. VHYFORE SUCH SILENCE", and VAITING and SILENCE are underlined by hand. The postmark is KNOXVILLE PA, MAY, 1913. The address is Miss Leah Doane, Little Marsh, Pa. Little Marsh lies a few miles from Knoxville (Tioga Co.), which fits "come down Sat night". HCP 1507, a card from the same sender to the same recipient on May 10, 1913, uses the same key.
6. **Prior solutions.** The portal tab capture (`source/metadata.md`) shows Not solved with no attached transcription or solution, and the register snapshot has no match. I found nothing in the files suggesting that an outside solution was used.

## Findings

1. **major (transcription) / minor (meaning): line 12 reads `18.7.21.25` = DOWN, not `8.7.21.25` = TOWN.** See `review/work/l12down.jpg` and the 4× strip. The first token of the last word is a separate stroke `1` followed by the looped `8`. It is the same two-stroke form as `18` in DEAR (`l1dear.jpg`). A bare `8` in this hand has no leading stroke (THE, TO, TIED). The literal text is therefore "YOU BETTER COME DOWN Sat night". That is idiomatic, and it removes the editorial "[to] town" in the proposed sense. `SOLUTION.md`, `transcription.txt`, `plaintext.txt` and the translation need correcting. (Compare HCP 1507, where TOWN is a real `8.7.21.25` with no leading stroke.)
2. **major (transcription honesty) / minor (meaning): line 10 has a lone `2` where the solver writes `26`.** See `review/work/l10you.jpg` and `l10you2.jpg`. In `IF SO _OU OUGHT`, the token before `.7.16` is a single `2` followed by a dot. Under the printed grey watermark lettering at that spot there is no `6`; a dark-ink `6` would show over it, as it does elsewhere. `2` is not in the key, so the literal decryption is `[2]OU`, which is plainly a slip for YOU. `SOLUTION.md` says "All other wording above is literal" and lists every other writer error (ID, SOMETHIHG, TIED, G, FRIEY), so this silent normalization should be listed with them.
3. **minor: numeric text outside the body is decodable and was not decoded.** (a) Under the date, the underlined group `24.24.24` (`review/work/date.jpg`) decodes to **XXX** (kisses) with 24=X from HCP 1507. (b) The picture side has `3.25.12` written upside down in the panel (`review/work/pic_nums180.jpg`; the 5 has its detached flag) = **ENA** (meaning unclear, possibly a name or initials). It also has `24` twice beside the caption = **X**, **X**. `SOLUTION.md` excludes these as "peripheral numeric annotations"; they should be recorded and decoded (or listed as undecoded) so that the claim covers all the ciphertext on the card.
4. **minor: further sign-level uncertainties to list.**
   (a) DONE (line 4): the `5` of `25` has no visible detached flag, so it is shaped like the `26` forms. N is the only sensible reading.
   (b) The closing `11.4.17.3.26` (`review/work/l14.jpg`): the last sign is the same flagless b-shape, so it could be a flagless `25`. That gives FRIEN, which is closer to FRIEND than FRIEY. The solver's "not silently expanded" stance is correct, but the 25/26 alternative should be stated.
   (c) HONEY (line 7): the `5` is overwritten with a heavy blot.
   (d) The `26` of VERY (line 8) is retraced.
5. **minor: presentation.** The date reads roughly "May 2[?], 13", and the postmark day is unclear (7 or 2). Neither the solver nor I can read it confidently. Many spaces are missing in `SOLUTION.md`/`NOTES.md` ("on2026-10-26", "is17.18", "single13"), which makes the uncertainty list hard to read.

## Required for closing

- Change line 12 to `18.7.21.25` (DOWN) and line 10 to `2.7.16` (marked as a writer slip for 26). Regenerate the plaintext, the proposed sense and the translation.
- Record XXX (header), ENA and the picture-side X's, or list them explicitly as decoded peripheral text.
- Add the 25/26 ambiguities (DONE, FRIEY/FRIEN) to the uncertainty list.

If these changes are made as described, I see no need for another review round.

## What I could not verify

- The date digits and the postmark day.
- Whether the closing sign is a flagless 25 or a 26.
- The signature ("Ezra" vs catalogue "Egna"): the second letter has a descender loop (z or g) and the third could be r or n. I leave it unresolved, as the solver did.
- Whether the solution has been published elsewhere. I relied on the solver's portal capture and register snapshot.

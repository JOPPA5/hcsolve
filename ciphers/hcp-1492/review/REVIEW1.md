REVISE

# Review 1 — HCP 1492 / pc_hcp_173 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment of the four numeric lines is correct** — I re-read every number from the scan and get exactly the solver's 37 values and `DEAR CHICKEN / HOW ARE YOU / LOTS OF LOVE / FLOSSIE`. The verdict is REVISE because the card carries a fifth, separate numeric group in the same pencil, `24 24 24`, which the solver neither transcribed nor mentioned, although `SOLUTION.md` states that every numeric position is decoded (finding 1). Under the same key it reads `XXX` (kisses). It confirms the key and adds to the message; it does not change anything already claimed.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1492/work/decode.py` runs, hashes pass, prints the four lines and `Encrypted numeric positions: 37`.
2. **Independent reading of the scan.** `review/work/crops.sh` (sips; PIL is not installed): message area rotated 180°, upscaled (`msg_big.png`), plus 6–7× details of the number block (`nL_big.png`, `nR_big.png`) and of the group under the printed heading (`x24_big.png`). My reading, punctuation as written (`review/work/my-transcription.txt`):

   ```
   4.5.1.18.  3.8.9.3.11.5.14.
   8.15.23-  1.18.5.  25.15.21?
   12.15.20.19  15.6.  12.15.22.5.
   6.12.15.19.19.9.5.
   24 24 24.            (below "PRINTED OR WRITTEN MATTER", same orientation and pencil)
   ```

   The first four lines are number-for-number identical to `work/transcription.txt` (checked with `diff` after normalising separators).
3. **Independent decode.** `python3 -I review/work/decode_review.py review/work/my-transcription.txt` (own A1Z26 decoder, does not import the solver's code):
   ```
   DEAR CHICKEN
   HOW ARE YOU?
   LOTS OF LOVE
   FLOSSIE
   X X X
   numbers: 40 distinct: 19 conflicts: []
   ```
   All 40 values are in 1–26; a direct alphabet has no possible conflicts, and none is needed.
4. **Plain text and context.** The plain-ink pencil message reads: "Dear Jack. I hope you will like this card. I am sure you will be surprised by it. Up-eyes. Good-bye, from Flossie." and, upper corner, "This is you 'making eyes'" beside a drawn face. The picture side is a hand-painted landscape, which fits "I hope you will like this card … surprised by it". "Chicken" as a pet name for Jack fits the teasing tone. Address `J. Stalland Esq., 41 Oak Road, Horfield, Bristol`. Written dateline `10-6-11. 11.28 P.M.`; machine postmark `BRISTOL 1.30 AM JUN 11 11` — written late on 10 June, posted in the small hours of 11 June 1911, consistent with the portal date 1911-06-11.
5. **Prior solutions.** No register entry for URL 1492 / `pc_hcp_173` in `work/register-snapshot.json` (grep); not in `skip.txt`.

## Findings

1. **major (coverage) / minor (meaning) — the group `24 24 24` is missing.** Crop `review/work/x24_big.png` (and `msg_big.png`, lower middle): three `24`s, the last followed by a full stop, written in the same grey pencil and the same (upside-down-to-the-print) orientation as the message, directly under the printed "PRINTED OR WRITTEN MATTER". 24 = X under the claimed key, so the group reads `XXX`, the usual kisses at the end of a love note. It is not a postal or dealer mark. `SOLUTION.md` says "All 37 numeric cipher positions decode" and "No unresolved numeric position remains"; the card has 40. Add the group to the transcription, plaintext and translation (or, if the solver reads it differently, say why it is excluded).
2. **minor — ciphertext punctuation is dropped and one mark is misattributed.** The `?` after `25.15.21` is written on the card; the solver lists the question mark among editorial punctuation. Numbers are separated by dots, words by wider gaps, and there is a dash after `8.15.23`. The transcription file keeps only word breaks. Recording the card's own punctuation would let the diplomatic text show that "how are you?" is the writer's.
3. **minor — description of `3.8`.** `SOLUTION.md` says the 3 and 8 of CHICKEN are "closely written". In `nL_big.png` they are as clearly separated by a dot as every other pair (`3·8·9·3·11·5·14·`). Harmless, but the uncertainty section warns about something that is not there.
4. **minor — undisclosed overlap.** The `1` of the first `12` on line 3 (`L` of LOTS) touches the inverted `JUN` of the postmark; only its lower part is clean. `12` is certain from context and from the visible stroke, but this is the one number on the card that is physically damaged and should be listed instead of finding 3.

## What I could not verify

- The marks `8 P.R.B.` (or `S. P.R.B.`) in the top corner: I take them, like the solver, as a later collector's/dealer's note, but I cannot prove it.
- Identities of Jack Stalland and Flossie beyond the card; the solver makes no identity claim.
- Whether a decipherment has been published elsewhere; I relied on the register snapshot.

## Required for closing

Add `24 24 24` → `XXX` to the transcription, plaintext and translation, update the count to 40, and adjust the uncertainty notes (findings 2–4). No further review round is needed for that.

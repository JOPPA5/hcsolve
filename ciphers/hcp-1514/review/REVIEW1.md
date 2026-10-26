ACCEPT

# Review 1 — HCP 1514 / pc_hcp_195 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** The greeting is A1Z26 numbers. In the body each word is rotated by one letter: the first letter is moved to the end for encryption, and the decoder moves the last letter back to the front. I re-read the whole card from the scan and get the same message. One letter count is doubtful (`untill` vs `until`), and two places are partly obscured. All of these are minor.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1514/work/decode.py` runs (exit 0) and prints the claimed 7 lines, 18 numeric positions and 89 letters. It decodes the solver's manual transcription and does not read the image.
2. **Independent reading of the scan.** The message is written sideways. I cropped `source/address-large.jpg`, rotated 270° clockwise and upscaled 4–9× with sips (`review/work/r-a.png` … `r-g.png`, `r-tues.png`, `r-night.png`, `r-until.png`), then read every word. My transcription is `review/work/my-transcription.txt`:

   ```
   13.25. / 19.23.5.5.20.5.19.20 / 4.1.18.12.9.14.7. / 19.
   halls otn eb. pu ntilu
   uesdayt ot ightn. opeh
   ouy rea ellw. uiteq a
   reatt ot aveh ti inef
   ithw estb ovel.
   romf. ackJ.
   ```

   It is identical to the solver's except `ntilu` vs `ntillu` (finding 1).
3. **Independent decoder.** `python3 -I review/work/decode_review.py review/work/my-transcription.txt` applies A1Z26 to the numbers and rotates each word's last letter to the front:

   ```
   MY / SWEETEST / DARLING / S
   shall not be. up until
   tuesday to night. hope
   you are well. quite a
   treat to have it fine
   with best love.
   from. Jack.
   # numeric positions=18 letters=88
   ```

   All 18 numbers are in 1–26. All 22 letter words obey the same single rotation, with no exceptions and no leftovers. The key covers the whole message, including the signature.
4. **Context.** The postmark reads ALTON HANTS, 5.15 PM, FE 12 06. 12 February 1906 was a **Monday**, so "shall not be up until Tuesday tonight" means the next evening, which is consistent. The address side has "Local", consistent with a card posted in Alton to Alton. The greeting initial `S` matches the addressee's initial. A two-part system (numbers for the greeting, word rotation for the body) matches the portal description "transposition and also substitution".
5. **Disclosure.** Literal spellings are kept and flagged (`untill`, `to night`), and nothing is expanded or identified beyond the evidence. No published solution is mentioned or used, as far as I can see.

## Findings

1. **minor — `untill` may be `until`.** Detail in `review/work/r-until.png` (8×). I see `n`, a crossed `t`, a short `i`, **one** looped `l`, then `u`. That is `ntilu` → `until`. Compare `halls` in line 1, whose `ll` is two clearly separate loops. I cannot rule out a second, short `l` at 1024 px, so this is not certain either way. Please list it as an uncertain letter count rather than asserting the misspelling `untill` as literal.
2. **minor — undisclosed obscured letter.** The first letter of `ouy` (line 3) is partly covered by an ink blot (`r-e.png`, `r-f.png`). `you` is certain from context, but the blot should be mentioned.
3. **minor — some letters are read from context.** In `uesdayt` the `e`/`s` and the `d` are cramped, and the `t`-cross stands above the `a` (`r-tues.png`). In `ightn` the final `n` is a weak, `e`-like stroke (`r-night.png`). Neither reading is in doubt given the rotation rule and the date, but `SOLUTION.md` names only `halls`/`ellw` as letters needing attention.
4. **minor — recipient name.** `source/metadata.md` follows the catalogue's "S. Bauks". Detail in `review/work/addr-name.png`: the third letter has the pointed tops of a `u`. However, the writer of the address may be a different hand from the writer of the message, and `n`/`u` confusion is common in this script. **Banks** is a common surname; "Bauks" is very rare. `SOLUTION.md` relies on the recipient's initial `S`, so the report should give the surname as "Bauks (possibly Banks)" rather than as certain.

## What I could not verify

- Whether the writer wrote one or two `l`s in `until` (finding 1).
- The minute in the postmark time (5.15 PM is my reading).
- Publication elsewhere: I relied on the solver's register check and did not search the web.

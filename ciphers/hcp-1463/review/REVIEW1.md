ACCEPT

# Review 1 — HCP 1463 / pc_hcp_144 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct and the transcription matches the card number for number.** I re-read all 149 enciphered numbers from `source/address-large.jpg` myself and get the same sequence as `work/transcription.txt`. A1Z26 gives a complete, natural English love note. The findings below are small and concern the record (metadata, wording), not the reading.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1463/work/decode.py` exits 0; its output is byte-identical to `work/plaintext-check.txt` (`diff` empty). The script checks the source hashes and decodes each token of the transcription; it does not read the image (the solver says so).
2. **Independent reading of the scan.** I cut the address side into 3× strips (`review/work/r01-03.png`, `r04-06.png`, `r07-09.png`, `r10-12.png`, `r13-14.png`) and 4–9× details (`z-*.png`, `top.png`, `z-address.png`) with `review/work/crop.sh` (sips) and read every number before comparing with the solver's file. My transcription is written into `review/work/review_decode.py`.
3. **Independent decoder.** `python3 -I ciphers/hcp-1463/review/work/review_decode.py ciphers/hcp-1463/work/transcription.txt` → my own A1Z26 decode of my own reading:

   ```
   MY DEAR ADA / THANKS FOR LETTER / THIS MORNING / WILL COME ANE /
   SEE YOU TOMORROW / NIGHT DEAR WILL / COME BETWEEN / 7.30&8 GOODNIGHT /
   DEAREST IT WILL / SOON BE HERE / WITH MUCH LOVE / FROM YOUR OWN /
   KKKKKK WALT
   letter positions: 149   distinct values: 1-9,11-15,18-23,25
   ```

   Compared with the solver's file the number sequences are identical once the last card row is read in physical order (the six `11`s stand at the left of the same row as `23.1.12.20`; the solver lists WALT first). All values are in 1–26, so the key covers the entire ciphertext; no number needs two values.
4. **Plaintext and context.** Idiomatic Edwardian English ("thanks for letter this morning", "with much love from your own Walt"). Addressee on the card is *Miss Ada Nicholls*, matching "My dear Ada". The writer's own dating at the top of the card reads `11/xi/04 9.15 pm`; the postmark is `10 AM NO 12 04`; so the card was written on Friday evening 11 Nov 1904 and posted Saturday morning, and "tomorrow night … between 7.30 & 8" means Saturday 12 Nov. Consistent.
5. **Disclosure.** ANE is kept literal (the last number of row 4 is a clear `5`, `z-r05.png`), AND is given only as interpretation; KKKKKK is not over-interpreted; the transcription is declared as the solver's own. No sign of a published solution being used.

## Findings

1. **minor — one number not flagged as hard to read.** In TOMORROW (`20.15-13.15.18.18.15.23`, row 5) the second `18` (4th group after `13`) looks very much like `15` at this resolution (`review/work/z-tomorrow.png`); the writer's 8 is a narrow pointed form. Reading it as 15 would give TOMOROOW, so `18` is clearly what is meant and I agree with the solver's value, but `SOLUTION.md` lists other doubtful places (initial 13, ANE, the 11s) and not this one. Add it to the uncertainty list.
2. **minor — the date and address in `source/metadata.md` are misread.** The writer's date line reads `11/xi/04 9.15 pm` (roman `xi` = November; `review/work/z-date.png`, `z-date2.png`), not `12/11/04, 9.35pm`. The street is `41. Welbeck Street, Cavendish Square, London W.` (`review/work/z-address.png`), not `14 Melleek Street` — Welbeck Street does adjoin Cavendish Square. Neither affects the cipher. Since `source/` must not be changed after download, put the corrected readings in `SOLUTION.md`/the report rather than editing `metadata.md`; the report should use 11 Nov 1904 as the date of writing (portal date 1904-11-12 is the postmark).
3. **minor — row order of the last line.** The six `11`s and the signature `23.1.12.20` are one physical row, Ks on the left. `transcription.txt` puts WALT on its own row above the Ks. Harmless for decoding, but the transcription should follow the card if it claims to keep "physical line breaks".
4. **minor — text quality of `SOLUTION.md`/`NOTES.md`.** Spaces are missing between words and numbers throughout ("All149", "Not solved2026-10-26", "7.30&8is"). Fix before the text goes into the PDF report.

## What I could not verify

- Whether "KKKKKK" (six 11s) means kisses; I agree it should stay uninterpreted.
- The identity of Walt and Ada Nicholls; no external lookup made.
- Whether a decipherment is published elsewhere; I relied on the solver's statement and the register snapshot and did not repeat a web search.

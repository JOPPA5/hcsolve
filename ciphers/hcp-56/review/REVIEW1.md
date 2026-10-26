REVISE

# Review 1 — HCP 56 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **ROT13 is correct and the first eight and a half lines are read correctly, but the end of the message is misread.**
- The last cipher line is `Sbaq ybir sebz`, which decodes to **"Fond love from"**. The solver has `Lbhef rire bayl` ("Yours ever only"), and no such line is on the card.
- The solver dropped a word: line 9 ends `lbh qrne.`, which decodes to "you **dear**."

The key stands; the transcription and plaintext need correcting.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-56/work/decode.py` runs (exit 0) and prints the claimed 10 lines and "ROT13 roundtrip exact". It applies ROT13 to the solver's manual transcription in `work/ciphertext.txt`, so it cannot catch reading errors.
2. **Independent reading of the scan.** The message is written sideways in faint pencil. I rotated `source/postcard-large.jpg` 270° clockwise and upscaled the strips (`review/work/r-all.png` whole message 2×; `r-1.png` … `r-5.png` 3×; `r-close.png`, `r-dear.png`, `r-you.png`, `r-sig.png` 6–8×). I read every word and recorded the result in `review/work/my-transcription.txt`.
3. **Independent decoder.** `python3 -I review/work/decode_review.py review/work/my-transcription.txt` applies the Caesar shift 13 to letters only:

   ```
   i thought i would send
   this to tell you how
   happy i was last night.
   i love you ten times more
   than ever now if such is
   possible. In spite of the
   Captains sermon i am
   afraid i am an idolator
   for i simply worship you dear.
   Fond love from
   # letters: 183
   ```

   Diff against `work/ciphertext.txt` (after normalising the lowercase `v`): lines 1–8 are identical. Lines 9–10 differ:

   ```
   < sbe V fvzcyl jbefuvc lbh qrne.
   < Sbaq ybir sebz
   ---
   > sbe V fvzcyl jbefuvc lbh.
   > Lbhef rire bayl
   ```

4. **Key consistency.** A single fixed shift explains every word, with no exceptions. Shift 13 is its own inverse, so the claimed key and the claimed encryption are the same.
5. **Context.** The address is Miss D. Conway, Tunstall, Market Drayton, Salop, and the postmark is Market Drayton, 8.30 PM, SP 13 06. Both match the portal metadata. This is natural Edwardian English. With my reading the closing becomes the conventional **"Fond love from"**, followed directly by the plain-text signature (`Cecil`, provisional, as the solver says). That is a coherence check the solver's "Yours ever only" fails: that phrase is unidiomatic and leaves no lead-in to the signature.

## Findings

1. **major — the closing line is misread.** Details in `review/work/r-close.png` and `r-all.png`.
   - The line under the message has three 4-letter words: `S b a q`, `y b i r`, `s e b z`.
   - The first word opens with the same looped capital S-form the writer uses elsewhere. The second has a clear descender `y` and a dotted `i`. The third ends in a `z` with a descender.
   - ROT13 gives `Fond love from`.

   The solver's `Lbhef rire bayl` has the wrong letter count (5-4-4) and letter shapes not present on the card. Fix `work/ciphertext.txt`, the plaintext, the translation (`S láskou` / `S vrúcnou láskou` instead of `Navždy iba tvoj`), and the note "Closing appears Yours ever only" in `NOTES.md`.
2. **major — a word is omitted at the end of line 9.** Detail in `review/work/r-dear.png` (6×) and `r-you.png` (8×). After `lbh` the card has a four-letter word followed by a full stop: `q r n e`. Its first letter is the writer's `g`-like `q`, the same form as in `jbhyq`, `fraq`, `nsenvq` and `Sbaq`. ROT13 gives `dear`. Reading the first letter as `g` gives `tear`, which does not fit the sentence. The text is "for I simply worship you dear." `SOLUTION.md` claims "No ciphertext fragments were omitted", but this word was left out of the transcription.
3. **minor — the case of `v` is normalised silently.** The writer writes the pronoun as a lowercase `v` throughout (`v gubhtug v jbhyq`, `v nz`). Only `Va` (`In`) and `Pncgnvaf` carry capitals. The transcription silently uses `V`. This does not change the plaintext, but a diplomatic transcription should keep the lowercase form or say that it was normalised.
4. **minor — the signature.** I agree the signature is in plain text and begins with a capital `C`. ROT13 of `Cecil` would be `Prpvy`, which is not what is written. At this resolution I can only call the reading `Cecil` compatible, so keep it provisional.

## Required for closing

- Correct lines 9–10 of `work/ciphertext.txt` to `sbe V fvzcyl jbefuvc lbh qrne.` and `Sbaq ybir sebz`, then regenerate the plaintext and translation.
- Remove "Yours ever only" from `SOLUTION.md` and `NOTES.md`, and note the lowercase `v`.

These are reading corrections under an unchanged key. Once they are made, I see no need for a further review round.

## What I could not verify

- The picture side: the portal provides only this image, as the solver states.
- The signature beyond its first letters (finding 4).
- Who "the Captain" was. I agree the solver should not speculate.
- Publication elsewhere: I relied on the solver's register check and did not search the web.

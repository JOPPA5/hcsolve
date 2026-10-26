REVISE

# Review 1 — HCP 1187 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the key is right and most of the body reading is right**. I read the whole card again myself, sign by sign. The solver's transcription leaves out three signs at the end of line 7. Those signs read **FOR**, so the closing is "God bless you my dear for / ever", not "my dear. / Ever." The transcription is also wrong for the last sign of FLOWING. The claim that the key "was applied to the entire eight-line cryptogram" is therefore not true. The first sign of the signature is most likely a dotted square (J).

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1187/work/decode.py` runs. The source hashes in `work/source-sha256.json` match `shasum -a 256 source/*.jpg`. The output matches the plaintext block in `SOLUTION.md` exactly (154 mapped glyphs plus 1 unresolved).
2. **Independent decoder.** I wrote `review/work/review_decode.py` from scratch and did not import the solver's code. The key is the standard #-grid filled in pairs (undotted, dotted), with A/B in the bottom-right outline cell, and the four X-wedges for S–Z. The decoder asserts that the 26 tokens map one-to-one to the 26 letters.
   - `python3 -I review/work/review_decode.py work/transcription.txt review/work/claimed.txt` gives `MATCHES CLAIMED`. The solver's tokens therefore really do decode to the claimed text under the stated key.
   - I found no sign in the body that would need two different values. The signs that repeat (YOU ×4, SOON ×2, ARE, LETTER, BETTER, the TL1=R in eleven places) all keep their values.
3. **Independent reading of the scan.** I rotated `source/address-large.jpg` 90° clockwise (`review/work/rot.png`) and made crops of every line at 4–6× (`L*-1/2/3.png`, `L*a/b.png`). I made 9–18× details of every doubtful place (`z-*.png`), plus contrast-enhanced versions made with ffmpeg (`zc-*.png`, via `zoomc.sh`). I read the card without using `work/transcription.txt`, then compared. My reading is `review/work/reviewer-reading.txt`:

   ```
   $ python3 -I review/work/review_decode.py review/work/reviewer-reading.txt review/work/claimed.txt
   YOU ARE A PRECIOUS
   DARLING A LETTER SO SOON
   I AM QUITE CONVINCED AND
   HAPPY NOW I KNOW YOU ARE
   BETTER MY HEART IS JuST OVER
   FLOWINQ FOR YOU WITH LovE
   GOD BLESS YOU MY DEAR fOR
   EvER WILL WRITE SOON jIM
   158 glyph positions; uncertain readings (lower-case): [...]
   DIFFERS FROM CLAIMED   (lines 6, 7, 8)
   ```

   | Line | My reading | vs. solver |
   |---|---|---|
   | 1 | YOU ARE A PRECIOUS | same |
   | 2 | DARLING A LETTER SO SOON | same |
   | 3 | I AM QUITE CONVINCED AND | same. In CONVINCED, C and E overlap the printed BRITISH MADE, but ⊔ and L can be separated (`zc-L3-ced.png`) |
   | 4 | HAPPY NOW I KNOW YOU ARE | same (read at 4×, postmark overlaps ARE) |
   | 5 | BETTER MY HEART IS JUST OVER | same. The U of JUST is a dark sign written over the printed divider line, compatible with `>` (`z-L5-just.png`) |
   | 6 | FLOWIN**Q** FOR YOU WITH LOVE | **differs**, finding 2. The O and V of LOVE are under a printed outline letter (`z-L6-love.png`) |
   | 7 | GOD BLESS YOU MY DEAR **FOR** | **differs**, finding 1 |
   | 8 | EVER WILL WRITE SOON **J**IM | signature, finding 3. The V of EVER is a hasty `>`-like sign with a dot, close to a dotted `7` (N) |

4. **Language and context.** The enciphered part is natural, informal English love-letter prose ("You are a precious darling!", "My heart is just overflowing for you with love"). It fits the unencrypted introduction. That reads approximately: "Just thought you might like to have a look at the Ducks don't they look Sweet: hope you are both keeping well. we are all just A.1. not quite so hot now we have had a lovely rain & everything is lovely & fresh. (here's a puzzle for you can you do it)" (`review/work/cursive.png`). The picture side is captioned "Swans with Cygnets". The address is Miss N. Harrison, 67 Limes Rd, Croydon, Surrey. The 1d red George V stamp gives 1912 or later. The solver's notes call the introduction one "about the swans", but the writer says "Ducks". That is trivial, but the report should quote the card.
5. **Prior solutions.** I found nothing in the files suggesting a published solution was used. The solver says the key was transferred from its own HCP 1188 work, and says so openly. I did not repeat the web search.

## Findings

1. **major: three signs at the end of line 7 are not transcribed. They read FOR.** The details are `review/work/z-L7-dear-for.png` (6×) and `zc-L7-for.png` (10×, contrast). After `⊔· L ┘ Γ·` (DEAR) and a separator dot there are three more handwritten signs, partly over the hollow printed letter of POST CARD:
   - a slanted `L` with a dot (BL1 = F). This one is the least certain, because it sits inside the printed outline.
   - a clear `⊓` (T0 = O), its left stem drawn over the printed stroke.
   - a clear `Γ·` (TL1 = R), followed by a separator dot.

   Line 7 then reaches the same right margin as line 6 (≈x 580 in `rot.png`); in the solver's transcription it stops at ≈x 450. The closing therefore reads **GOD BLESS YOU MY DEAR FOR EVER. WILL WRITE SOON. JIM**, i.e. "for ever / forever". The solver's "my dear. Ever." with a stand-alone "Ever." is an artefact of the omission. Its note "Preserve the literal closing DEAR / EVER … without changing it to DEAREST" shows the line end was looked at, but the signs were not entered. Consequences:
   - the transcription, the plaintext and the translation must add FOR;
   - the statements "applied to the entire eight-line cryptogram" and "The readable body contains no unresolved token" must be corrected.

2. **major (transcription) / minor (meaning): the last sign of FLOWING is not R0.** Details: `z-L6-G2.png`, `zc-L6-G.png`. It is a heavily inked `Γ`: a stem on the **left** and a top stroke running right, ending in a blob, with no right side and no bottom. That is the TL outline (Q, or R if the following dot counts). The writer's real G (R0, `⊐` with top, right and bottom) is drawn quite differently, in DARLING (`z-L2-ng.png`) and in GOD. The dot after the sign is at baseline height in the gap, so it is probably the word separator. The literal is therefore **FLOWINQ**, which is clearly a writer's slip for FLOWING. The diplomatic transcription must record `TL0` (or `TL0/TL1`) and list "G" as an editorial correction, as was done for the other cards.

3. **minor: the signature's first sign is most likely J (C1).** Detail: `z-L8-sig2.png`. A handwritten closed square is visible, overlapping the printed "I" of BRITISH (serifs above and below, stem through the right side). There is a dark dot inside it, darker than the printed strokes. The next two signs are a clear `□` (I) and `7` (M). I read **J?IM → Jim**, with C1 as the probable value. Keeping it flagged is acceptable, but the solver should say that a closed square with a probable dot is visible. Do not present it as an unreadable sign.

4. **minor: weak signs that should be listed as uncertain.** These are not disputed readings, but the solver says only in general terms that "several weak dots and shapes" exist:
   - U in JUST (line 5), written over the printed divider line;
   - O and V in LOVE (line 6), under a printed outline letter. Only a stroke and a low dot are visible;
   - V in EVER (line 8). The sign is between `>` and `7`; `>1` = V is preferred only by context;
   - F of the new FOR (finding 1).

5. **minor: the reproduction command only round-trips a manual token list.** The solver discloses this honestly. The README wants a command that produces the plaintext from the source and the key. For a graphic cipher, that means a sign-by-sign as-seen transcription, which is what `work/transcription.txt` is meant to be. It must be corrected per findings 1–3. The "exact known-token roundtrip" assertion is tautological and should not be cited as evidence.

## Required for closing

- Add `BL1 T0 TL1` (FOR) at the end of line 7 of `work/transcription.txt`, and update the plaintext, the normalized text, the translation and the coverage statements.
- Record the last sign of FLOWING as the TL outline and mark G as an editorial correction.
- Update the signature note (closed square with probable dot, so J is probable) and list the weak signs from finding 4.

With these changes I see no need for another review round. The changes are additions to the record, and the key is unaffected.

## What I could not verify

- Dots on signs that overlap the printed POST CARD / BRITISH MADE or the postmark (line 4 ARE, line 6 LOVE, line 7 F of FOR, line 8 J). For these I can only say the readings are compatible with what is visible.
- Lines 4 and 5 were read at 4× only, apart from JUST. Every sign matched the solver at that scale.
- The postmark date (illegible at 1024 px) and the identity of "Jim" and of Miss N. Harrison.
- Whether a decipherment has been published elsewhere.

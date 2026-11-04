# hcp-1100 Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. There was no earlier solver work on this number. The orchestrator captured the scans and metadata on the same day. The portal attaches no transcription and no solution, so the transcription is my own (`work/transcription.txt`). A short web search found no published solution of this card (see SOURCES.md).

## Card

- HC Portal 1100, `cpc_1908-10-30_UK_Clapham_UK_Somerset_`, T. Schrödel collection, status Not solved.
- Picture postcard "Begging a seat" (two Blenheim spaniels), imprint "The H... Co. Publishing Co., Holborn Place, London W.C." (partly covered by writing), Series 2167 D, printed in Germany.
- Address in plain English: Mr D. Salvidge, Rose Bud Cottage, Walrow(?), Nr Highbridge, Somerset. The stamp is a ½d Edward VII. The postmark reads CLAPHAM, 12.15 AM, OC 30 08.
- The message is in invented signs. It is written across the left half of the address side and along its left edge, with the card turned 90°. Three short lines sit at the top, with the card turned 180°. The words "P.C's" and "from May" are in plain letters. There is no writing on the picture side. The stamp is still affixed and intact. Nothing is visible at its perforated edges or in the dotted stamp box, and the picture side carries only the printed title and verse. The area under the stamp could not be inspected, because the stamp has not been lifted.

## Cipher type and key

The cipher is a monoalphabetic substitution (MASC) with invented signs. Words are kept and each word ends with a dot. Several plaintext letters are written in more than one shape. I list these shapes separately rather than forcing them into one sign. Shape codes are in `work/decode.py`:

| Letter | Sign (rot. 90° view) | Variants seen |
|---|---|---|
| A | round C | angular C (B02), thin arc ( (MAY, THAN), Γ-like hook (RATHER, HAVE in T03) |
| D | 7 | |
| E | b | b with top bar (FEEL), solid triangular b (WELL, HAVE in T03), loop-and-stem (RATHER, TREASURE) |
| F | stroke with hyphen at left | |
| G | P | |
| H | Y shape with heavy ink foot | |
| I | plain stroke | |
| J | dagger cross | |
| K | Cyrillic Л shape | |
| L | epsilon Ɛ | reversed 3 (WELL, FEEL, ONLY), z-hook (LOSE) |
| M | hook with horizontal bar | |
| N | ч / y shape with left arm | η shape (LINE in B02) |
| O | square □ | open 4-like box with stem (ONE) |
| P | 9 | |
| Q | closed downward triangle ∇ | |
| R | hooked h | |
| S | stroke with foot at lower left and tick at upper right | |
| T | u with tall right stem | tall plain stroke (ANYTHING), d-loop with crossbar (TREASURE) |
| U | V with stem | V with tick (UNHAPPY) |
| V | stroke with curl at the top | |
| W | hyphen + N | |
| Y | V/Y with pennant or triangle (open or filled) | |
| & | ∂-like sign standing alone (B04) | |

B, C, X and Z do not occur.

## Plaintext (original English, line by line; dots between words dropped)

```
B01 MAY DEAREST PET JUST A
B02 LINE AND I HOPE THIS
B03 WILL FIND YOU QUITE
B04 WELL & HAPPY I FEEL
B05 SO UNHAPPY WHEN I
B06 THINK OF MAY LOOSING
B07 MAY ONLY DARLING I HAVE
B08 WRITTEN A LINE TO
B09 YOUR MOTHER OH DEAR
B10 ONE I WOULD GIVE
B11 ANYTHING RATHER [about four signs struck out]
B12 THAN LOSE MAY TREASURE
T01 I MUST SAY TA TA
T02 WITH LOVE
T03 I HAVE A SET OF TESE  P.C's   (P.C's in plain letters)
T04 from May                         (plain letters)
```

Running text: "May dearest pet, just a line and I hope this will find you quite well & happy. I feel so unhappy when I think of May loosing May only darling. I have written a line to your mother. Oh dear one, I would give anything rather than lose May treasure. I must say ta ta. With love (from May). I have a set of these P.C's."

All four occurrences of the possessive are spelled with three signs, M-A-Y (B01, B06, B07, B12). They read naturally as "my", so the writer, who signs "May", is probably punning on her name or spelling "my" as "May". I keep the literal MAY in the plaintext and give "my" in the translations.

### English (normalised)

My dearest pet, just a line, and I hope this will find you quite well and happy. I feel so unhappy when I think of my losing my only darling. I have written a line to your mother. Oh, dear one, I would give anything rather than lose my treasure. I must say ta-ta. With love, from May. I have a set of these postcards.

### Slovak

Môj najdrahší miláčik, len pár riadkov a dúfam, že ťa zastihnú celkom zdravého a šťastného. Cítim sa taká nešťastná, keď pomyslím na to, že strácam svojho jediného miláčika. Napísala som pár riadkov tvojej mame. Ach, drahý, dala by som čokoľvek, len aby som nestratila svoj poklad. Musím sa rozlúčiť, pá-pá. S láskou, May. Mám sadu týchto pohľadníc.

## Command (run from the repo root)

```
python3 -I ciphers/hcp-1100/work/decode.py
```

The script checks the SHA-256 of the four source images (source/ and work/hires/), then applies the sign key to `work/transcription.txt` and prints the plaintext above.

## Uncertainties

1. **Sign variants.** The writer forms several letters in two to four shapes (see the table). Each variant was assigned from the word it occurs in. The single-occurrence variants rest on word sense: A angular C (AND), N η (LINE), O 4-box (ONE), T tall stroke (ANYTHING), T d-loop with crossbar (TREASURE), U V-with-tick (UNHAPPY), L z-hook (LOSE), E b with top bar (FEEL). The 'arc' A (thin "(", in MAY and THAN) and the Γ-like hook A (RATHER, HAVE) may be one A shape drawn with more or less hook; in THAN the arc has a small hook at the top. Kept as separate codes, this does not affect the plaintext. The η sign in B02 LINE is close in shape to the Л sign for K (THINK). I read it N because "just a LIKE" makes no sense and LINE recurs in B08 with the ordinary N sign.
2. **"&" in B04** is a single ∂-like sign standing alone between WELL and HAPPY. Its value (& / "and") comes from word sense only. Unlike every other word on the card it has no word dot after it, which fits a logogram rather than an enciphered letter.
3. **MAY = "my"?** The four three-sign M-A-Y groups are read literally. Their meaning "my" is an interpretation.
4. **"TESE" (T03)** has no H sign on the card. This is a writer's omission for THESE. I did not restore it.
5. **Struck-out group at the end of B11:** about four signs crossed through with a heavy line. It probably began THAN, which then opens B12, but it is not decoded and does not count.
6. **Order of the top lines.** T01 to T03 run downwards when the card is turned 180°. "from May" stands to the right, between T02 and T03. It may close "With love" or belong to the P.C's line. The reading does not change.
7. **Spelling.** LOOSING (for losing) and TA TA are as written. The place name in the address (Walrow?) is plain handwriting, not part of the cipher, and is uncertain.

## Why I believe it is correct

- Every sign in the 12 body lines and 3 top lines is decoded. Only the struck-out group is left. The result is coherent period English: a 1908 love note with the formulas "just a line and I hope this will find you quite well", "I must say ta-ta" and "with love".
- The key was found from internal patterns (…IчP = ING three times, double letters in WELL/WILL/HAPPY/LOOSING/WRITTEN, single-letter words I and A). It was then confirmed on independent words: DEAREST, DEAR, DARLING (D, R); MOTHER, WITH, RATHER (T, H); HOPE, HAPPY, UNHAPPY (P); LOVE, HAVE, GIVE (V).
- The plain-letter "P.C's" at the end of T03 fits the deciphered "I HAVE A SET OF TESE" in front of it. The signature "from May" fits the four M-A-Y groups.
- No sister card is in the repo (no other card to Salvidge or from Clapham), so the key is reconstructed from this card alone.

## Response to review 1

Review 1 (verdict ACCEPT) had four minor findings. All are addressed in this file; none changes the reading, and `python3 -I ciphers/hcp-1100/work/decode.py` was re-run afterwards with identical output ("source hashes OK", B01–B12, T01–T04 as above).

1. **"Under the stamp" claim too strong.** Agreed and fixed in the Card section: nothing is visible at the stamp edges or in the stamp box, and the area under the affixed stamp could not be inspected. I re-checked the enlarged stamp crop (review/work/stamp.png) and the picture side: no ink at the perforations, no writing in the picture, the edges or the verse. The type stays MASC; nothing seen supports adding Steganography for this card (the stamp-box messages reported by the team belong to the Hungarian Árokszállás/Jolánka series, not to this English card).
2. **bb (FEEL) missing from the single-occurrence list.** Added to Uncertainty 1. While checking the list I also removed "E solid b", which occurs twice (WELL in B04, HAVE in T03) and so is not single-occurrence.
3. **"&" has no word dot.** Added to Uncertainty 2 as support for the logogram reading.
4. **arc A and Γ-hook A look alike.** Noted in Uncertainty 1; they may be one A shape. Codes kept separate; plaintext unchanged.

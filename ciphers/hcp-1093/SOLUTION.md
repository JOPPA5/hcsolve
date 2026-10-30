# HCP1093 — solution (round 1)

Postcard, T. Schrödel collection, catalogue date 1913-04-15, postmarked
Shawford, addressed to Miss Unsworth, Park Lane, Twyford, nr Winchester,
Hants. Portal status at capture: Not solved; no transcription or solution
attached (see SOURCES.md). No published solution of this card was found or used.

## Credit

Image capture, metadata, the key hypothesis (transferred from sister cards
HCP1187/HCP1188) and a partial reading were done on 2026-10-25 by an OpenAI
GPT solver (GPT-6 Astra / GPT-6.1 Sol). On 2026-10-30 Claude Opus 5.5
re-collated every sign on enlarged crops, resolved the open points
(B of BRUCE, the two middle words, the blotted sign, the signature, the
final row of kisses), rewrote the transcription and decoder.

## Cipher type and key

Pigpen (monoalphabetic), the "interleaved" variant used on HCP1187/HCP1188:
each outline gives a pair of letters, undotted = first, dotted = second.

| Outline (strokes present) | Undotted | Dotted |
|---|---|---|
| bottom+right (⅃) | A | B |
| bottom+left+right (⊔) | C | D |
| bottom+left (L) | E | F |
| top+bottom+right (⊐) | G | H |
| four sides (□) | I | J |
| top+bottom+left (⊏) | K | L |
| top+right (⌝) | M | N |
| top+left+right (⊓) | O | P |
| top+left (⌜) | Q | R |
| V (point down) | S | T |
| > (point right) | U | V |
| < (point left) | W | X |
| ^ (point up) | Y | Z |

The cipher is written on the address side, perpendicular to the address
(work/upright.jpg is the scan rotated so the cipher reads upright).

## Plaintext (English)

```
DEAREST BETTY, WHAT ABOUT THIS FOR A PHOTO OF BRUCE? SHALL GO TO BED
EARLY TONIGHT, FEELS TIRED OR SOMETHING. COLD A LITTLE BETTER.
WITH FONDEST LOVE AND KISSES FROM YOURS EVER BOB  XXXXXXXXX
```

Punctuation is editorial (the card has commas/full stops after most words).
SHALL GO TO BED / FEELS TIRED has no expressed subject (postcard style);
it may refer to Bruce or to the writer. The picture side shows a dog
("Don't make me laugh"), so Bruce is most likely the dog in the photo.

**English (normalised):** Dearest Betty, what about this for a photo of
Bruce? [I/he] shall go to bed early tonight, feel(s) tired or something.
Cold a little better. With fondest love and kisses from yours ever, Bob. xxxxxxxxx

**Slovak:** Najdrahšia Betty, čo povieš na toto ako fotku Brucea? Dnes večer
pôjde(m) skoro spať, je (som) unavený alebo čo. Nádcha je trochu lepšia.
S najvrúcnejšou láskou a bozkami, navždy tvoj Bob. xxxxxxxxx

## Reproduce (one command, from the repo root)

```sh
python3 -I ciphers/hcp-1093/work/decode.py
```

It verifies the SHA-256 of the files in source/, decodes
work/transcription.txt (152 signs) with the key above, prints a literal
and an emended reading, and asserts that the emended text equals the
plaintext given here.

## Uncertainties (all disclosed)

1. **Encipherment slips, 3 signs.** In FEELS (2nd and 3rd letter) and TIRED
   (4th letter) the writer drew ⅃ (bottom+right, = A) where E (L, bottom+left)
   is needed; literal text is FAALS TIRAD. Elsewhere on the card E and A are
   kept distinct, so this is probably a local slip (a mirror confusion is a guess, not established) confined to two adjacent
   words. The emendation to E is editorial; the literal reading is printed
   by the decoder.
2. **TIRED, signs 3-4** are written close together and almost touch, so they
   could be misread as one dotted box (J, "TIJD"). Read as ⌜· (R) followed
   by ⅃ because the top stroke stops short of the right stroke; the
   alternative gives no English.
3. **Ink blot (restoration).** The 2nd sign of BETTER (row 8) is covered by
   an ink blot; a vertical and a bottom stroke are discernible, dot not
   determinable. Restored as E: B?TTER with "cold a little …" admits only
   BETTER. Printed in lower case in the literal output.
4. **Signature BOB.** The dot of the first B lies over the upside-down
   printed publisher line. Its pixels (darkest ~106,90,74) are darker and
   less orange than any printed-ink pixel in the area (~182,142,115) and
   match the pen dots, so it is read as a pen dot (B, not A). The signature
   is underlined.
5. The dot inside the V of TIRED (T vs S) is faint but present on the 10x crop.
6. Word divisions SOME THING (line break) and the final 9 dotted < signs
   (= X, kisses) are as written.

## Why it is correct

- One fixed 26-letter key, already established on sister cards of the same
  collection, decodes all 152 signs; 148 directly, 3 via a single
  consistent mirror slip, 1 under a blot.
- The result is fluent, idiomatic Edwardian English postcard prose with a
  conventional greeting and closing, and fits the card (photo of a dog,
  English addressee in Hampshire, 1913).
- Every sign was checked on 3-10x enlarged crops of the scan; the earlier
  provisional readings were verified, not copied.

## Response to review 1

Verdict ACCEPT, three minor findings.

1. **Kiss row has 9 signs, not 8 — accepted and fixed.** I re-cropped the
   bottom row of work/upright.jpg (box 330,940–630,1010, enlarged 4x, saved
   as work/kisses-row.png) and count nine separate dotted `<` signs, the
   leftmost standing a little apart under "Published by E. A. Schwerdtfeger";
   I had missed that one. work/transcription.txt now has 9 × `<1`,
   work/decode.py asserts XXXXXXXXX, and the plaintext, translations and
   sign counts above now read 9 kisses and 152 signs (148 read directly).
   Re-ran `python3 -I ciphers/hcp-1093/work/decode.py`: source hashes OK,
   152 signs, emended text matches. The message itself is unchanged.
2. **"Mirror slip" is speculative — agreed.** The explanation of why the
   writer drew ⅃ for E three times is a guess and is labelled as such in the
   report; the literal reading FAALS TIRAD and the count of 3 emended signs
   are shown next to the normalised text in the report as well as here.
3. **Faint dot in the T of TIRED — no change needed.** Already disclosed
   (Uncertainty 5); the reviewer agrees that the dot is present and that
   the undotted reading (SIRED) gives no sense.

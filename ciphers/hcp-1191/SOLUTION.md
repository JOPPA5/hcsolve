# hcp-1191: SOLUTION (round 1)

HC Portal 1191, file name `cpc_1907-09-07_USA_Coshocton, Ohio_USA_Canal, Lewisville, Ohio_`. It is a US one-cent McKinley postal card, Tobias Schrödel collection. It is postmarked COSHOCTON OHIO SEP 6 4-PM 1907, with a receiving mark CANAL LEWISVILLE OHIO SEP 7 1907. It is addressed in clear to "J E Fortune, Canal Lewisville, O."

The portal status is Not solved, with no transcription and no solution attached. A short web search on 2026-11-03 found no published solution. All of the work below is by Claude Opus 5.5 (2026-11-03); no earlier work exists on this number.

## Cipher type and key

The cipher is a simple monoalphabetic substitution (MASC) with invented symbols. The whole message side, 268 decoded cipher signs plus one struck-out mark, is enciphered, except for the date digits "5 1907". Words are separated by small ticks, dots or gaps.

The image file `picture-large.jpg` is the message side, since a US postal card has no picture. It is scanned rotated by 90°, so to read it upright, turn it 90° counter-clockwise. The last line curves up the right-hand edge.

Key (full descriptions in `work/key.tsv`):

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| A | rhombus with one diagonal | N | box open at top with a middle bar (like ㅂ) |
| B | right-triangle wedge | O | circle with a slash leaving at lower left |
| C | downward triangle ∇ | P | "7" |
| D | crescent "(" | R | "+" |
| E | circle with a horizontal bar (θ) | S | square on a stem |
| F | "4"-like sign | T | dome (half disc, flat side down); once each as an inverted bowl in GOT and PAINT |
| G | 2–3 verticals with a crossbar (卅) | U | circle with a central dot ⊙ |
| H | circle on a stem ♀ | W | circle with a short stroke on its left |
| I | X (often with a top bar) | Y | "%"-like slash with two dots |
| J | asterisk (one occurrence, by word sense) | M | V with a tail or base stroke |
| K | vertical with two crossbars | ? | Y-shaped sign, once (line 1) |
| L | ÷ | | |

Q, V, X and Z do not occur.

The key was found from the text itself. The repeated word ⊸θ÷÷ was taken as WELL. Three words ending in the same four signs gave -IGHT (NIGHT, NIGHT, RIGHT). After that, THE, THIS, GUESS, TIME and ALL FOR THIS TIME fixed the remaining letters.

## Plaintext (original English, line by line as written)

```
SET 5 1907
WELL ?OS I THOUGHT
I WOULD WRITE YOU A
FEW LINE TO LET YOU
KNOW THAT WE ARE
ALL WELL AND HOPEING
ARE THE SANE WELL WE
WILL GO UP TO PA A
SUNDAY NOT A SATDAY
NIGHT SO YOU CAN
COME A ROUN SATDAY
NIGHT WELL JAKE I
GOT NY BUGGY PAINT
ALL RIGHT WELL I
GUESS THIS WILL BE
ALL FOR THIS TIME
SO CLOSE HOPE TO
SEE A SATDAY
SO GOODBY
FROM PETE AND EDNA
```

Normalised: "Sept. 5, 1907. Well [?]os, I thought I would write you a few line[s] to let you know that we are all well and hoping [you] are the same. Well, we will go up to Pa['s] a Sunday, not a Saturday night, so you can come around Saturday night. Well Jake, I got my buggy paint[ed] all right. Well, I guess this will be all for this time, so close. Hope to see [you] a Saturday. So goodbye, from Pete and Edna."

"A Sunday", "a Saturday" is the old colloquial "a-" meaning "on" (on Sunday, on Saturday). It is used the same way all three times.

English: Sept. 5, 1907. Well [?]os, I thought I would write you a few lines to let you know that we are all well and hope you are the same. Well, we will go up to Pa's on Sunday, not on Saturday night, so you can come round on Saturday night. Well Jake, I got my buggy painted all right. Well, I guess this will be all for this time, so I close. Hope to see you on Saturday. So goodbye, from Pete and Edna.

Slovak: 5. sept. 1907. Nuž [?]os, pomyslel som si, že ti napíšem pár riadkov, aby si vedel, že sme všetci zdraví, a dúfame, že ty tiež. Nuž, v nedeľu pôjdeme hore k otcovi, nie v sobotu večer, takže v sobotu večer môžeš prísť k nám. Nuž, Jake, dal som si v poriadku natrieť bričku. Nuž, myslím, že to bude zatiaľ všetko, tak končím. Dúfam, že sa uvidíme v sobotu. Tak zbohom, Pete a Edna.

## Reproduce (one command, from the repo root)

```sh
python3 -I ciphers/hcp-1191/work/decode.py
```

The script checks the SHA-256 of `source/picture-large.jpg`, `source/address-large.jpg` and the hi-res message scan. It then decodes `work/transcription.txt` (sign codes, a manual transcription by the solver) with `work/key.tsv`, and prints the plaintext above. A saved copy of the output is in `work/plaintext.txt`.

## Uncertainties (all disclosed)

1. **"?OS" in line 1.** The first sign is a Y-shaped mark that occurs nowhere else. It is the name of the person addressed. The likely reading is JOS (Jos., Joseph), but the asterisk in JAKE was also read as J, and one key should not have two J signs. The word is reported literally as "?OS". It is the only unread word.
2. **J in JAKE.** The asterisk occurs only once. J rests on word sense: it is the only unused letter that makes a word with -AKE. It fits the recipient's initial J.
3. **Blotted sign in LINE** (line 3). A heavy ink blot covers one sign between L and NE. It is restored as I (FEW LINE[S]), and this is a disclosed restoration. "LINE" without S is as written.
4. **Struck-out sign** before SEE (line 17). It is a blotted mark with a stem, treated as a deletion and not as a letter.
5. **Faint signs.**
   - Line 4, "WE" (THAT WE ARE): both signs lie under the HCPortal collection stamp and are faint. Violet-ink separation shows a circle with a left stroke (W) and a circle with a bar (E).
   - Line 7, "TO": the T is on an abraded patch and reads as a faint dome.
   - Line 7: a pale ghost stroke before the P of PA is ignored.
   - Line 10, ROUN: the R is overwritten (a + is visible). The U is a circle whose central dot is not clearly visible, so U rests partly on word sense.
6. **Spellings by the writer, kept literally.** These are HOPEING, LINE, ROUN (around), SATDAY three times (Saturday), GOODBY and PAINT (painted). SET in the header is the month: the date "5 1907" is in clear, and the postmark is Sep 6, 1907. The writer seems to have written S-E-T for Sept.
7. **N where M is expected, twice.** These are SANE (for same) and NY (for my). The N in NY is a clean ㅂ-shaped N, identical to the N of NOT, SUNDAY and CAN. The N in SANE is overwritten: it has the ㅂ shape with extra strokes at the top right (review/work/same.jpg), so the writer may have tried to correct it, possibly towards M. M is written elsewhere with its own V-shaped sign (COME, TIME, FROM). I read N literally and take these as writer's slips.
8. **Two forms of T.** The inverted bowl in GOT and PAINT is read as T by word sense, as a flipped form of the dome.
9. **Line-end mark in line 6.** After WE at the end of line 6 (SANE WELL WE) there is a short curved stroke "(", smaller and thinner than the crescent D of SUNDAY and AND. It is taken as a line-end divider, not as D (WED gives no sense), and is not transcribed.
10. **Word division.** "AND / EDNA" on the curved last line has no visible divider. "I / THOUGHT" in line 1 has a clear gap. The final sign of THOUGHT is a dome with a small extra stroke and dot.

## Steganography check

The card is a printed US postal card: the stamp is imprinted, so nothing can be hidden under it. The address side carries only the clear address, the printed card text, two postmarks and the portal's collection stamp, and no additional writing was seen. There is no picture side. No hidden or unenciphered message was found, so the type is plain MASC.

## Why I believe it is correct

- One fixed key covers every sign on the card. It gives 20 lines of coherent, period-typical American English: a rural family letter about visiting Pa on Sunday, a painted buggy, and "so goodbye".
- The decode is not driven by one guess. Recurring units decode consistently in every occurrence: WELL 5× (lines 1, 5, 6, 11, 13), ALL 3× (lines 5, 13, 15), NIGHT/RIGHT, THIS 2×, YOU 3×, SATDAY 3× and SUNDAY.
- Rare letters (F, K, B, C, P, J) each produce real words in context: FEW, FOR, FROM, KNOW, BE, BUGGY, GOODBY, CAN, CLOSE, COME, PA, PETE, HOPE.
- The header date agrees with the Coshocton postmark of the next day, Sep 6, 1907.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict ACCEPT with four minor findings. Changes were made by Claude Opus 5.5 (solver) on 2026-11-03. The decoded text is unchanged.

1. **Wrong counts (fixed).** I recounted over work/plaintext.txt with a script: WELL 5×, ALL 3×, THIS 2×, YOU 3×, SATDAY 3×. The transcription has 268 decoded cipher signs plus one struck-out mark (269 marks, the reviewer's figure). The intro and "Why I believe it is correct" now give these numbers.
2. **Line-end mark in line 6 (fixed).** On review/work/l6end.jpg I see the small "(" after WE. It is smaller and thinner than the crescent D. It is now disclosed as uncertainty 9 and treated as a line-end divider. The transcription is unchanged, because the mark is not a letter.
3. **N in SANE is overwritten (fixed).** I agree from review/work/same.jpg: the sign has extra strokes at the top right. Uncertainty 7 now says so and no longer calls the two N signs identical. The literal reading N is kept.
4. **"?OS" unread (no change needed).** It stays literal as the only unread word, a single name in the salutation. JOS remains a hypothesis only.

Reproduction re-run after the edits: `python3 -I ciphers/hcp-1191/work/decode.py` prints "source hashes OK" and output identical to work/plaintext.txt.

Steganography, rechecked at the human's request (hidden messages under stamps on other card series): this card is a US one-cent postal card with an imprinted stamp, so there is no stamp to lift, and the solver and the reviewer both found no extra writing on either side. The type stays plain MASC.

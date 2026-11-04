# HCP 998 — solution (Claude Opus 5.5, 2026-11-03)

Status: **complete reading**. A few points are noted under "Uncertainties". There was no earlier work on this number. The portal shows the card as Not solved and attaches no transcription or solution. A short web search on 2026-11-03 (Klausis Krypto Kolumne / Schrödel postcards; Zwingenberg, Rimbach, Sophie Goes) turned up no published solution of this card. All transcription, key reconstruction and decipherment below are by Claude Opus 5.5.

## Card
Picture postcard (painted gateway scene). Posted at BERLIN (the date on the stamp cancellation is mostly covered; the sender's date line says "Am 25.11.01."). Addressed to Fräulein Sophie Goes, Rimbach i. Odenwald. A second postmark at the left, dated 26.11.01 7-8V, shows only the end of its town name ("…CH"), which fits RIMBACH (arrival there). The card was then forwarded: the receiving stamp reads ZWINGENBERG (HESSEN) 27.11.01 8-9V. The address side is in plain Kurrent and contains no cipher. The message is on the picture side, written at 90° to the picture, in invented signs.

## Cipher type and key
Simple monoalphabetic substitution (MASC) of German. The signs are invented, many of them shaped like Latin or Greek letters. A long-s-like stroke (∫) divides the words. "=" under the last sign of a line marks a hyphenated word. Umlauts are shown with a diaeresis over the cipher sign. The date line "Am 25.11.01." is in plain writing.

| sign (code) | plain | | sign (code) | plain |
|---|---|---|---|---|
| loop-b `B` | m | | slanted zero `0` | f |
| small circle `o` | e | | cup with diaeresis `Y"` | ü |
| H `H` | i | | circle with inner loop + diaeresis `Q"` | ü |
| six `6` | n | | rho `p` | r |
| v `V` | s | | vertical stroke `1` | b |
| open box with inner hook `U` | o | | tilde `z` | z |
| plus `+` | p | | lambda-like `A` | t |
| serifed I `I` | h | | backslash `\` | c |
| triangle `D` | v | | rounded double cup `W` | w |
| T / T with bar `T` | l | | pi `P` | l |
| slanted stroke `/`, short tick `'` | d | | short horizontal stroke `-` | g |
| x `x` (x with diaeresis = ä) | a | | raised epsilon `u` | u |
| hooked k `K` | k | | | |

Letters j, q, y and ß do not occur. The key has two homophone pairs: `T`/`P` = l and `/`/`'` = d. Two different signs, `Y"` and `Q"`, both carry a diaeresis and both read ü (each occurs once).

## Command (run from the repo root)
```
python3 -I ciphers/hcp-998/work/decode.py
```
The command checks the SHA-256 of both source images, then applies `work/key.json` to the sign-by-sign transcription in `work/transcription.txt`. Output:
```
Am 25.11.01. (plain) mein sophin — vielen vielen dank für deinen lieben brief, sobald ich zeit habe schreibe ich dir. einstweilen sei zärtlich geküsst mein liebstes von deiner tr. freundin magda.
```

## Plaintext (German, normalised)
Am 25.11.01. Mein Sophin — vielen, vielen Dank für Deinen lieben Brief; sobald ich Zeit habe, schreibe ich Dir. Einstweilen sei zärtlich geküsst, mein Liebstes, von Deiner tr[euen] Freundin Magda.

## English
On 25.11.01. My Sophie (written "Sophin") — many, many thanks for your dear letter; as soon as I have time I shall write to you. Meanwhile be tenderly kissed, my dearest, by your faithful friend Magda.

## Slovak
Dňa 25.11.01. Moja Sofia (napísané „Sophin“) — veľmi, veľmi pekne ďakujem za tvoj milý list; len čo budem mať čas, napíšem ti. Zatiaľ ťa nežne bozkáva, moja najmilšia, tvoja verná priateľka Magda.

## Address side (plain, not enciphered)
- Address: "Fräulein Sophie Goes, Rimbach i. Odenwald". "Rimbach" and "i. Odenwald" are struck through in blue.
- Forwarding notes. Purple pencil: "334 in Zwingenberg, Bergstraße / b. Herrn Diefenbach / Schmitt 26/11" (the last is a postman's name and date). Blue pencil, lower left: "Zwingenberg … Bergstraße". Blue pencil, top: one word plus "26/11", most likely the forwarding note "nachgesch[ickt]" ("forwarded"; the letter shapes n-a-ch-g-ſ-ch are visible). That one blue word is not securely read. The purple "Diefenbach" and "Schmitt" are read from Kurrent and partly rest on word sense. These notes are postal handling, not part of the message.
- Postmarks: BERLIN on the stamp (date mostly covered); at the left, a strike dated 26.11.01 7-8V whose town name is only partly visible ("…CH", most likely RIMBACH, the arrival office); ZWINGENBERG (HESSEN) 27.11.01 8-9V after forwarding.
- Steganography check: the 5-Pf Germania stamp is on the card and its area shows nothing written around it. Nothing can be seen under the stamp in the scan. The painted picture and the margins show no hidden writing. Unlike the Jolánka series, this card carries no visible stamp-box message. Writing hidden under the stamp cannot be excluded from a scan alone.

## Uncertainties
1. "Sophin": the cipher spells s-o-p-h-i-n (`V U + I H 6`), not "Sophie". The address confirms the name Sophie, so this is an affectionate or dialect form, or a slip. It is reported as written, not corrected.
2. "tr." is an abbreviation written in cipher (`A p .`). The expansion "treuen" is a conventional reading, not something on the card.
3. The long dash after "Sophin" is taken as punctuation. It is much longer than the g sign `-`.
4. Letters that rest partly on word sense: ü is written as two different signs (`Y"` in "für", `Q"` in "geküsst"); u occurs only once (`u`, the raised epsilon in "Freundin"); the short tick `'` = d occurs only in "sobald"; and the stroke direction tells `/` = d from `-` = g (word sense confirms d in Dank, deinen, deiner, Freundin, Magda and g in geküsst, Magda).
5. The address-side notes are only partly read (see above). They belong to the post office, not to the message.

## Why it is correct
Every cipher sign on the card (9 lines, 142 letter signs) decodes with a single consistent key. Eleven frequent signs recur across many independent words (mein ×2, vielen ×2, ich ×2, deinen/deiner, lieben/liebstes). The text is a coherent, idiomatic German postcard of 1901 ("Vielen Dank für Deinen lieben Brief … sobald ich Zeit habe, schreibe ich Dir"). The name fits the address (Sophie) and gives a plausible sender signature (Magda). Hyphenation marks fall at real syllable breaks (schrei=be, einstwei=len, ge=küsst).

## Response to review 1

Review 1 (verdict ACCEPT, four minor findings). The reviewer's independent transcription matched mine in all 142 letter signs; no decoded letter changes.

1. **Left postmark (fixed).** Agreed. On the reviewer's crop (`review/work/adr_leftpm.jpg`) and on the full address side, the inverted ring of the 26.11.01 7-8V strike shows only "…CH" at the top, not BERLIN. The card description and the postmark list now call it a strike whose town name is only partly visible, most likely RIMBACH (arrival office), and keep the BERLIN strike on the stamp separate, with its date mostly covered.
2. **Blue forwarding word (fixed).** Agreed that the shapes n-a-ch-g-ſ-ch are visible; "nachgesch[ickt]" is now named as the likely reading. It stays marked as not securely read. It is a single postal word, not part of the message.
3. **Name in the translations (fixed).** The English and Slovak translations now say that the card writes "Sophin".
4. **"tr." (no change needed).** The expansion stays bracketed, tr[euen], and is listed under uncertainties.

Steganography check, repeated after the human's note on the Jolánka series (hidden messages under or near the stamp): the stamp area of this card, the margins and the painted picture show no hidden writing, and the reviewer confirmed this independently (`review/work/adr_stamp.jpg`). Nothing under the affixed stamp can be seen in a scan. The type therefore stays MASC, not "MASC + Steganography".

Re-run after the edits: `python3 -I ciphers/hcp-998/work/decode.py` prints both hashes OK and the same plaintext as above (the edits touched only SOLUTION.md text, not work/).

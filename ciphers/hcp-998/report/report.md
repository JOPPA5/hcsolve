# HCP 998: a German friendship postcard from Magda to Sophie Goes (1901)

Human solver: Tomáš Pavuk

**Status: deciphered in full (142 of 142 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 998 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/998), portal name cpc_1901-11-25_DE_Ber_DE_Zwingenberg (Hessen)_, part of Tobias Schrödel's collection of cryptographic postcards (private collection; the portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 about the collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Sophie, with no transcription or solution attached.

It is a picture postcard with a painted sepia scene of an arched gateway among trees. The message is written on the picture side, below the painting when the card is held upright (in the scan the card lies on its side). It opens with the plain date **Am 25.11.01.** ("On 25.11.1901") and continues in nine lines of invented signs.

The address side is in plain German Kurrent: **Fräulein Sophie Goes, Rimbach i. Odenwald.** It carries a 5-Pfennig Germania stamp cancelled BERLIN (date mostly covered). A second postmark at the left, dated 26.11.01 7-8V, shows only the end of its town name ("…CH"), which fits RIMBACH, the arrival office. "Rimbach" and "i. Odenwald" are struck through in blue, and forwarding notes in purple and blue pencil send the card on to Zwingenberg an der Bergstraße, where it was stamped ZWINGENBERG (HESSEN) 27.11.01 8-9V.

![Picture side turned upright: the painted gateway and, below it, the plain date line and nine lines of cipher (work/picture-upright.jpg)](../work/picture-upright.jpg)

![Address side: Fräulein Sophie Goes, Rimbach i. Odenwald, with the BERLIN stamp cancellation, the partly legible "…CH" strike of 26.11.01, the ZWINGENBERG (HESSEN) arrival stamp and the forwarding notes (source/address-large.jpg)](../source/address-large.jpg)

All work on this number (transcription, key reconstruction, decipherment) was done by Claude Opus 5.5 on 2026-11-03; there was no earlier work. A short web search (Schrödel postcards, Zwingenberg, Rimbach, Sophie Goes) found no published solution of this card.

## Method

The cipher block was read manually, sign by sign, from the un-converted high-resolution scan of the picture side (3469 x 2298 pixels), turned 90° counter-clockwise so that the plain date line is at the top, and enlarged line by line. Each sign received a short code (for example `B` for the loop-b shape, `o` for the small circle, `6` for the six-shape), and the transcription was recorded line by line in work/transcription.txt. A long-s-like stroke separates the words, an "=" under the last sign of a line marks a hyphenated word, and umlauts are shown by a diaeresis over the cipher sign.

The 142 letter signs fall into 27 sign types. The key was found from recurring words: a three-sign word occurring twice ("ich"), a five-sign word repeated at the start ("vielen vielen"), then "Dank", "Brief" and "habe". With those letters in place the rest of the text read as an ordinary German letter (sobald, Zeit, schreibe, einstweilen, zärtlich geküsst, liebstes, von deiner tr. Freundin Magda), and every sign received exactly one plain letter (with two homophone pairs, see below).

In review a second, independent Claude Opus 5.5 agent cut its own tiles from the high-resolution scan, read all nine lines itself, wrote its own sign names and key (review/work/my_decode.py), and obtained the same plaintext, character for character.

## Key

Simple monoalphabetic substitution (MASC) of German with invented signs, many shaped like Latin or Greek letters. The names are conventional labels for the handwritten shapes.

| sign | plain | sign | plain | sign | plain |
|---|---|---|---|---|---|
| loop-b | m | small circle | e | H | i |
| six | n | v | s | open box with inner hook | o |
| plus | p | serifed I | h | triangle | v |
| T (with or without top bar) | l | pi | l | long slanted stroke | d |
| short tick | d | x | a (with diaeresis: ä) | hooked k | k |
| slanted zero | f | cup with diaeresis | ü | circle with inner loop + diaeresis | ü |
| rho | r | vertical stroke | b | tilde | z |
| lambda-like | t | backslash | c | rounded double cup | w |
| short horizontal stroke | g | raised epsilon | u | | |

The plain letters j, q, x, y and ß do not occur. There are two homophone pairs: T and pi both stand for l (pi only in "-len" of "einstwei=len"), and the long slanted stroke and the short tick both stand for d (the tick only in "sobald"). The two ü signs are also different shapes, each used once. The date line is written in plain Kurrent.

## Plaintext

Literal decipherment, as printed by the reproduction command (lower case, as the cipher has no capitals):

```text
Am 25.11.01. (plain) mein sophin — vielen vielen dank für deinen lieben brief,
sobald ich zeit habe schreibe ich dir. einstweilen sei zärtlich geküsst mein
liebstes von deiner tr. freundin magda.
```

Normalised German:

**Am 25.11.01. Mein Sophin — vielen, vielen Dank für Deinen lieben Brief; sobald ich Zeit habe, schreibe ich Dir. Einstweilen sei zärtlich geküsst, mein Liebstes, von Deiner tr[euen] Freundin Magda.**

English translation: **On 25.11.01. My Sophie (written "Sophin") — many, many thanks for your dear letter; as soon as I have time I shall write to you. Meanwhile be tenderly kissed, my dearest, by your faithful friend Magda.**

Slovak translation: **Dňa 25.11.01. Moja Sofia (napísané „Sophin“) — veľmi, veľmi pekne ďakujem za tvoj milý list; len čo budem mať čas, napíšem ti. Zatiaľ ťa nežne bozkáva, moja najmilšia, tvoja verná priateľka Magda.**

Notes on the reading:

- **Sophin.** The cipher spells s-o-p-h-i-n; its last sign is the same six-shape (n) as in "mein" and "vielen", not the small circle (e). The address confirms the name Sophie, so "Sophin" is an affectionate or dialect form, or a slip; it is reported as written.
- **tr.** is an abbreviation written in cipher; "treuen" (faithful) is the conventional expansion, not something on the card.
- Hyphenation marks fall at real syllable breaks: schrei=be, einstwei=len, ge=küsst.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-998/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both source images, then applies the key in work/key.json to the sign-by-sign transcription in work/transcription.txt and prints the literal plaintext above (on one line). It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **"Sophin"** for Sophie and the expansion **tr[euen]**, see above.
- **Signs that rest partly on word sense:** the two different ü signs (one in "für", one in "geküsst"), the single u (raised epsilon, in "Freundin"), the short-tick d (only in "sobald"), and the distinction between the long slanted stroke (d) and the short horizontal stroke (g), which "Magda" shows side by side.
- The long dash after "Sophin" is read as punctuation; it is much longer than the g stroke.
- **Address-side notes** are postal handling, not part of the message. The purple notes ("334 in Zwingenberg, Bergstraße / b. Herrn Diefenbach / Schmitt 26/11") are read from Kurrent and partly rest on word sense. The blue word at the top, followed by "26/11", is not securely read; its letter shapes suggest "nachgesch[ickt]" ("forwarded"). The town name in the left postmark is only partly visible ("…CH", most likely RIMBACH).
- **Steganography.** Several postcard series carry a hidden message under or beside the stamp. On this card the stamp area, the margins and the painted picture were checked at full resolution by both solver and reviewer and show no hidden writing. The stamp is still affixed, so anything written beneath it cannot be seen in a scan. The cipher type is therefore given as MASC, not MASC + Steganography.
- The identities of Sophie Goes and of the sender Magda are not established beyond the card.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic, a separate agent), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), cut its own enlarged tiles from the high-resolution scan, read all 142 signs itself and decoded them with its own key; its reading agreed with the solver's in every position. It confirmed the shape distinctions t/b and d/g, the two ü signs, the pi-shaped l, the n at the end of "Sophin", the comma after "brief", and that no hidden writing is visible around the stamp or in the picture. Its four findings were minor:

- **Left postmark.** The 26.11.01 7-8V strike had been described as a second BERLIN strike; its visible letters are "…CH", which fits RIMBACH. Corrected.
- **Blue forwarding word.** "nachgesch[ickt]" is now named as the likely reading; it remains marked as not securely read.
- **Name in the translations.** The English and Slovak translations now note that the card writes "Sophin".
- **"tr."** No change needed; the expansion stays bracketed.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 998, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/998 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3054/conversions/cpc_1901-11-25_DE_Ber_DE_Zwingenberg-(Hessen)__pic-large.jpg (source/picture-large.jpg); un-converted original in work/hires/.
- Address side: https://api.hcportal.eu/media/3055/conversions/cpc_1901-11-25_DE_Ber_DE_Zwingenberg-(Hessen)__adr-large.jpg (source/address-large.jpg); un-converted original in work/hires/.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03 by the orchestrator: no entry for this card.

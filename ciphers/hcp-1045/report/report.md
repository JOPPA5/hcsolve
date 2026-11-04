# HCP 1045 (cpc_1909-10-12_DE_-(Schlesien)_DE_Hier_fritzlehmann-09): Susi's number-cipher reproach to Fritz Lehmann

Human solver: Tomáš Pavuk

**Status: deciphered in full (133 of 133 cipher numbers); independent review 1 verdict ACCEPT, five minor findings addressed, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1045 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1045), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as a general reference for the collection. The portal name gives the date 12 October 1909.

The picture side is a printed photographic card titled "Gretchen", with the Faust caption "Nach ihm nur schau' ich zum Fenster hinaus, / Nach ihm nur geh' ich aus dem Haus." and publisher number 4034-6; it carries no handwriting. The address side has a Germania 5-pfennig stamp of the Deutsches Reich; the postmark shows "...(SCHLESIEN)" and "...10.09", the rest is covered. The address is in plain Kurrent pencil: **An Herrn Fritz Lehmann, Hier, Alte ...straße** ("To Mr Fritz Lehmann, here [local delivery], Alte ... street"); the street name is only partly legible under the portal watermark and may read "Alte Landschaftstraße".

The message is a pencil block of dotted numbers written sideways on the left half of the address side (ten lines plus a one-word last line), and a three-line note squeezed diagonally into the free top-left corner of the block.

The card belongs to a group of cards to Fritz Lehmann in the same collection. The sister cards HCP 1113 and HCP 1134, also signed "Susi", use the same number cipher; this card was read with that key, which also stands on this card alone (it fits every number).

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![Message block turned upright, from the high-resolution scan; the corner note is at the top left (review/work/block_full.png)](../review/work/block_full.png)

![Corner note turned to its writing direction and contrast-stretched (review/work/corner_rm38.png)](../review/work/corner_rm38.png)

![Picture side, printed only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made by Claude Opus 5.5 from the un-converted high-resolution scan of the address side (work/hires/). The block was turned upright and every number was read on 3-5x enlargements (work/crops/); the corner note was rotated to its own writing direction. Doubtful signs (the overwritten first numeral of MIT, the faint last digit of HEUT, the dark question marks, the umlaut ticks) were compared with other occurrences of the same shapes on the card. No OCR was used and no earlier transcription existed.

The number set (2 to 26, no 1, no number above 26) and the sister cards pointed to a plain number alphabet. The key A=2 ... Z=26 with J omitted decodes all 133 numbers into German; no number is left over and no letter is adjusted. The decoding is reproduced by one command from the repository root, `python3 -I ciphers/hcp-1045/work/decode.py`, which first checks the SHA-256 of the scans and then decodes work/transcription.txt.

The reviewer, a separate Claude Opus 5.5 agent, made its own crops, read all lines independently, wrote its own decoder with its own table (review/work/my_decode.py) and obtained the same numbers and the same German text.

## Key

Number substitution (simple monoalphabetic), German, 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Conventions on the card: dots separate letters, dashes separate words. A double tick over a number marks an umlaut (2 with ticks = Ä, 21 with ticks = Ü). A bar over a number doubles the letter (14 with bar = NN in DENN). A darker diagonal cross stroke over the first number of a noun or name (F of Fritz and Freude, K of Karte, G of Gezanke, Gesundheit, Gruß) marks a capital and does not change the letter. ß is written SZ. "!" and "?" are written as plain punctuation.

Numbers occurring on this card: 2 3 5 6 7 8 9 10 11 12 13 14 15 18 19 20 21 23 26.

## Plaintext

Transcription, line by line (x = capital cross stroke, " = umlaut ticks, ^ = umlaut not marked on the card and supplied by word sense, = = bar over the number, | = separator dot the writer left out):

```text
[corner]  23.15. - 3.10.19.20. - 5.21. - 9.6.21.20 ?
12.10.6.3.6.18. 7x.18.10.20.26. !
6.3.6.14. - 5.6.10.6.14.6. - 11x.2.18.
20.6. - 6.18.9.2.12.20.6.14. - 21^x.3.6.18.
23.2.19. - 10.19.20. - 5.6.14=. - 5.2|19.26. -
7.21".18. - 6.10.14. - 7.15.18.20.23.2".18.
6.14.5.6.19. - 8x.6.26.2.14.11.6. ?
10.19.20. - 5.2.19. - 5.10.6. -
7x.18.6.21.5.6. - 2.21.7. - 13.6.10.
14.6. - 8x.6.19.21.14.5.9.6|10.20. ?
13.10.20. - 8x.18.21.19.26. -
19.21.19.10.
```

Decoded German, as written (line breaks of the card kept):

```text
WO BIST DU HEUT?
LIEBER FRITZ!
EBEN DEIENE KAR
TE ERHALTEN ÜBER
WAS IST DENN DASZ
FÜR EIN FORTWÄR
ENDES GEZANKE?
IST DAS DIE
FREUDE AUF MEI
NE GESUNDHEIT?
MIT GRUSZ
SUSI
```

Normalised German: "Lieber Fritz! Eben deine Karte erhalten. Über was ist denn das für ein fortwährendes Gezanke? Ist das die Freude auf meine Gesundheit? Mit Gruß, Susi. – Wo bist du heut?"

English: "Dear Fritz! Just received your card. What is all this constant bickering about? Is that the joy over my health? With greetings, Susi. – Where are you today?"

Slovak: "Milý Fritz! Práve som dostala tvoj lístok. O čom je to ustavičné hašterenie? To je tá radosť z môjho zdravia? S pozdravom Susi. – Kde si dnes?"

"Freude auf meine Gesundheit" echoes the toast formula "auf meine Gesundheit" ("to my health"), so the question may be ironic: "Is that how you drink to my health?" (Slovak: "Takto pripíjaš na moje zdravie?").

The corner note "Wo bist du heut?" stands above the first line in the free corner; it may be a postscript or a heading. Its text is certain, its place in the reading order is not.

## What remains uncertain

1. **DASZ** (line 4): written 5 . 219 . 26 with no dot inside 219. Only the split 2|19 gives a word (D-A-S-Z, "daß" written for "das"); 21|9 would give DUHZ. The digits are clear; the split rests on word sense.
2. **GESUNDHEIT** (line 9): written 9.610.20 with no dot between 6 and 10. The split 6|10 is the only one possible (61 is outside the table).
3. **MIT** (line 10): the first numeral is a long 1-stroke with a looped foot, possibly a 23 overwritten to 13. 13 = M gives MIT GRUSZ; 23 would give "WIT". The reviewer also reads 13 on the pixels, but M rests partly on word sense.
4. **Ü of ÜBER** (line 3): the 21 carries no umlaut ticks. A double tick at the right end of line 2, directly after KAR, is read as the Kurrent double hyphen dividing KAR-TE. The literal reading is UBER; Ü rests on word sense.
5. **HEUT** (corner note): the last number runs to the card's edge; the 2 is clear, the 0 is faint. 20 = T is the only letter that makes a word after HEU.
6. The dark marks after GEZANKE and GESUNDHEIT are read as question marks, the same shape as the clear "?" closing the corner note.
7. Writer's spellings kept as written: DEIENE (for deine), DASZ (for das), FORTWÄRENDES (without H).
8. Hidden writing: the picture side carries only print, and the stamp is still affixed with no pencil traces at its edges. Nothing under the stamp can be checked on these scans. A separate pencil cross on the printed "Cartões Postaes / Briefkaart" line carries no number and is not part of the message.
9. "Susi" is a nickname; her identity is unknown. The street name of the address is read only tentatively.

## Review and what changed

Review 1 (a separate Claude Opus 5.5 agent) gave the verdict **ACCEPT**. It re-ran the command, decoded the card with its own table and its own transcription, checked the transcription against the high-resolution scan line by line, and inspected the picture side and the stamp. Its five findings were all minor and none changed the decoded text:

1. The Ü of ÜBER had been described as marked by ticks over its 21; in fact the ticks stand after KAR at the end of the previous line. Now described as the word-division mark of KAR-TE, with Ü resting on word sense (transcription notation 21^).
2. A second missing separator dot (GESUNDHEIT, 9.610.20) was not disclosed. Now disclosed in the transcription and the uncertainties.
3. "Freude auf meine Gesundheit" may be an ironic toast formula. The translation is now neutral and the alternative is given.
4. The street name of the address had been left unread. A tentative reading "Alte Landschaftstraße" is now given; it is not part of the message.
5. The sister cards had been called proof of the key while still in review. The wording now says the key is the same as on HCP 1113 and 1134 and stands on this card alone.

After the changes the command was re-run: the scan checksums match and the output is identical to round 1. A short web search found no published solution of this card.

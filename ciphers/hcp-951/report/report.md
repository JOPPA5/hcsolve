# HCP 951 (cpc_1940-01-05_DE__DE_Sturzbach_): a sender's name hidden in numbers, Döbeln 1940

Human solver: Tomáš Pavuk

**Status: deciphered in full (30 of 30 enciphered numbers); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 951 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/951), portal name cpc_1940-01-05_DE__DE_Sturzbach_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Hugo Dunkel, date 1940-01-05, with no transcription or solution attached. A short web search found no published solution of this card.

The picture side is a printed view "Döbeln – Bürgergarten mit Blick auf die Kaserne" (Döbeln, a town in Saxony). The address side carries a 6-Pfennig Hindenburg stamp of the Deutsches Reich with the slogan cancel "Vermeidet Rundfunk-Störungen!" ("Avoid radio interference!"), which fits the portal date of early January 1940. The card is addressed to **Herrn Hugo Dunkel, Stürzbach, Thüringer Wald**. "Stürzbach" is written clearly, but no such place is attested in the Thuringian Forest; the place meant is almost certainly Stützerbach, so the spelling is the writer's.

![Picture side: Döbeln, Bürgergarten (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: message with the number block on the left, address to Hugo Dunkel on the right (source/address-large.jpg)](../source/address-large.jpg)

## The message

The message is written in German in a Kurrent hand. It opens in plain words:

"Viele Grüße von hier, sendet Ihnen wohl bekannt, doch rätselhaft genannt."
("Many greetings from here, sent to you by one well known, yet called puzzling.")

Then follow four lines of numbers separated by commas, and the card closes in plain words: "Noch alles Gute zum Jahreswechsel." ("All the best for the turn of the year.") The numbers are the "puzzling" part: the sender's name and address.

## Method

The transcription is manual, made from the un-converted high-resolution scan of the address side, enlarged row by row (work/crops/l1.png to l4.png). No OCR was used and the portal supplied no transcription. All numbers lie between 1 and 26, which immediately suggests the alphabet position cipher A=1, B=2 … Z=26. Applied to every number, it gives a name, a town and a street with no exceptions.

The decoding is done by one script, work/decode.py, which first checks the SHA-256 of the source images and then decodes work/transcription.txt:

```text
python3 -I ciphers/hcp-951/work/decode.py
```

The reviewer cropped the four rows independently, read every number again, and decoded them with its own script; the readings agree in all 30 enciphered positions.

## Key

Number substitution, A=1, B=2 … Z=26 (a simple monoalphabetic substitution, register type MASC). Commas separate letters; a comma with a short downward tick marks the end of a word. The umlaut ö is written as plain O and ß as a single S. The house number 19 at the end is written as an ordinary number and is not enciphered.

| 1 A | 2 B | 3 C | 4 D | 5 E | 6 F | 7 G | 8 H | 9 I |
|---|---|---|---|---|---|---|---|---|
| 10 J | 11 K | 12 L | 13 M | 14 N | 15 O | 16 P | 17 Q | 18 R |
| 19 S | 20 T | 21 U | 22 V | 23 W | 24 X | 25 Y | 26 Z | |

## Ciphertext and plaintext

```text
9,12,19,5, 19,3,8,23,1,18,26,5     ILSE SCHWARZE
4,15,2,5,12,14                     DOBELN
2,18,5,9,20,5,                     BREITE
19,20,18,1,19,5, 14,18, 19         STRASE NR 19
```

![Row 1 of the number block (work/crops/l1.png)](../work/crops/l1.png)

Normalised German: **Ilse Schwarze, Döbeln, Breitestraße Nr. 19**

English: Ilse Schwarze, Döbeln, Breite Street no. 19 (the sender's name and address).

Slovak: Ilse Schwarze, Döbeln, Breitestraße (Široká ulica) č. 19 (meno a adresa odosielateľky).

The plain parts in Slovak: "Veľa pozdravov odtiaľto vám posiela dobre známa, no záhadná nazvaná." … "Ešte všetko dobré k prelomu roka."

## Other writing on the card

- In the middle of the card, in ink, a plain note (probably by the recipient, writing out the solution): "Ilse Schwarze / Döbeln i/S / Breitestr. 19" ("i/S" = in Sachsen, in Saxony). It matches the decryption word for word and confirms it independently. After "Schwarze" a long flourish or strike runs into the ruled line.
- Along the bottom edge, in pencil, a later remark: "Kennst du das/die […]fräulein [aus] Döbeln? !?" ("Do you know the […] young lady from Döbeln?"; SK "Poznáš tú […] slečnu z Döbelnu?"). The compound ends clearly in "-fräulein"; its first half ("Probe-" or "Post-"?) is not read.
- No writing was found on the picture side, and the stamp area shows no hidden text (see below).

![The plain note "Ilse Schwarze / Döbeln i/S / Breitestr. 19" (work/crops/plain.png)](../work/crops/plain.png)

## Uncertainties

1. Row 1 ends "1,18265" with no commas between 18, 26 and 5. It is split as 18,26,5 = RZE, the only split that gives a word.
2. The first sign of row 3 is a looped 2 (B), of the same shape as the 2 in "20" on the same row; the alternative 9 would give IREITE. The B reading also agrees with word sense and with the plain note "Breitestr.".
3. The 8 in "3,8" (row 1) is drawn open at the top, like "&", but has the same shape as the other 8s on the card; read as H (SCH).
4. The final 19 is taken as a literal house number; decoded, it would give S ("Nr. S"). The plain note says "Breitestr. 19".
5. In the pencil remark, the first half of one compound word and the exact article are not read. This is a later remark, not part of the sender's message.
6. Steganography check: postcards of this kind sometimes hide writing under the stamp, in the picture or along the edges. The picture side carries only the printed caption. Above the slogan cancel and left of the stamp there are a few faint marks (a pale N-like and v-like stroke, a short diagonal stroke); on enhanced crops they form no letters or digits and look like ink transfer or stray marks. Whatever might be written under the stamp itself cannot be checked from a scan.
7. The identity of Ilse Schwarze and Hugo Dunkel is not known.

## Why the solution is believed correct

- Every one of the 30 enciphered numbers decodes under the trivial A=1..Z=26 key, with no exceptions, into a name, a town and a street.
- The town Döbeln matches the picture side, and the plain note on the card ("Ilse Schwarze / Döbeln i/S / Breitestr. 19") matches the decryption word for word.
- The plain text frames it: the sender is "well known, yet called puzzling" and hides her name and address in numbers.

## Review and what changed

The solution was handed over by Claude Opus 5.5 and checked by a separate Claude Opus 5.5 reviewer, who ran the solver's command, decoded the number block independently from its own crops, re-read every number against the high-resolution scan, and checked the plain parts and the context. Verdict: **ACCEPT**, with four minor findings:

1. The unread pencil word could be narrowed to "[…]fräulein": adopted.
2. "Stürzbach" should be noted as the writer's spelling of Stützerbach: adopted.
3. Faint marks near the stamp should be disclosed: re-examined on an enhanced crop, disclosed as non-text (uncertainty 6).
4. The register type is MASC, not "MASC + Steganography", since no hidden text was found: agreed.

None of these changed the decoded text.

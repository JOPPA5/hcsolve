# HCP 1197: "to your beloved bridegroom" – a number-cipher greeting from Frankfurt, 1899

Human solver: Tomáš Pavuk

**Status: deciphered in full (24 of 24 number groups; one digit restored under the collection stamp); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1197 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1197), portal name cpc_1899-02-14_DE_Frankfurt Sachsenhausen_DE__, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Käthchen Walther, with no transcription or solution attached.

It is a German picture postcard: a girl and a boy in a straw hat sit in a meadow, with the printed caption "O Jugendzeit, O schöne Zeit!" ("O youth, O lovely time!"). The address side reads **Fräulein Käthchen Walther, Hofconfection, Sachsenhausen, Dreieichstraße 1. St.**, with one further word below, probably "Laden" (shop). "Hofconfection" names a court-appointed ladies' clothing business; the address is in Sachsenhausen, the district of Frankfurt am Main south of the river. A 5 Pfennig Reichspost stamp is affixed **upside down**. The large postmark FRANKFURT (MAIN)-SACHSENHAUSEN reads **4.2.99, 8-9 N**, so the card was posted on 4 February 1899 (the portal file name gives 14 February 1899; a stroke before the "4" on the stamp's cancel could be a digit 1 or the box edge). The card was sent within the same city.

![Picture side: plain Kurrent message with the two lines of numbers, and old pencil capitals along the lower edge (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Fräulein Käthchen Walther, Hofconfection, Sachsenhausen; inverted 5 Pf stamp at left, postmark 4.2.99 at top right (source/address-large.jpg)](../source/address-large.jpg)

The message is written on the picture side in German Kurrent script. It is plain text except for two lines of comma-separated numbers. The sender is deliberately anonymous: the card calls him "unnamed and only too well known".

Along the lower edge of the picture side someone (the recipient or a later owner) has already written a decipherment in pencil capitals: a large "DEINEN" and then "GELIEBTEN BRAUTIG", which runs into the printed HCPortal collection stamp. This old reading was not used to find the key; the key below was found from the numbers alone and then compared with it.

## Method

The transcription is manual. The solver read the Kurrent text and the numbers from the high-resolution original of the picture side (work/hires/), enlarging the lines and the stamp area. Two places lie under the HCPortal collection stamp that was printed on the scan:

- the "19" in the second word of line 1: its "1" shows as a slanted stroke through the stamp's letter "C" and its "9" loop over the "P"; it is read from the pixels;
- the last group of line 2: a clear "1" is followed by a second digit hidden under the stamp; a dark diagonal stroke shows that a digit is there, but its shape cannot be read.

The numbers run from 1 to 20, which suggests a letter-number substitution in alphabet order. Plain A = 1 … Z = 26 gives "DEIMEM GEKIEBSEM BQATSIGAL", which is not German. The German school alphabet without J (I and J share one number) gives "DEINEN GELIEBTEN BRAUTIGA_", three German words. The only letter that completes the last word is M (= 12), so the hidden digit is restored as 2.

A short script (work/decode.py) checks the SHA-256 of the four images, reads the transcription (work/transcription.txt) and prints the plaintext. The reviewer wrote an independent decoder (review/work/verify.py), made its own crops of every group, and got the same result.

## Key

Monoalphabetic number substitution (register type MASC), letters numbered in alphabet order with J omitted. The umlaut Ä is written as plain A.

| Plain | A | B | C | D | E | F | G | H | I | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| Plain | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Letters used on this card: A B D E G I L M N R T U.

## Plaintext

Ciphertext as transcribed ([2] = digit restored under the collection stamp):

```text
4,5,9,13,5,13 – 7,5,11,9,5,2,19,5,13
2,17,1,20,19,9,7,1,1[2]
```

Decoded:

```text
D E I N E N   G E L I E B T E N
B R A U T I G A M
```

The whole message (German; the numeric lines decoded in capitals):

```text
Gruß aus Frankfurt a/M
sendet dir
dieser kleine Junge hier.
Ungenannt und nur
zu gut bekannt.
Liebe Grüße an:
DEINEN GELIEBTEN
BRÄUTIGAM
und an – – – –
"   " Fräulein Schwester
```

**German:** Gruß aus Frankfurt a/M sendet dir dieser kleine Junge hier. Ungenannt und nur zu gut bekannt. Liebe Grüße an: deinen geliebten Bräutigam und an – – – – [Liebe Grüße an] Fräulein Schwester.

**English:** Greetings from Frankfurt am Main are sent to you by this little boy here. Unnamed and only too well known. Love to: your beloved bridegroom, and to – – – – [love to] Miss Sister.

**Slovak:** Pozdrav z Frankfurtu nad Mohanom ti posiela tento malý chlapec tu. Nemenovaný a až príliš dobre známy. Srdečné pozdravy: tvojmu milovanému ženíchovi a – – – – [srdečné pozdravy] slečne sestre.

Notes on the reading:

- "dieser kleine Junge hier" points at the boy in the picture: the anonymous sender presents himself as the boy sitting next to the girl.
- "deinen geliebten Bräutigam" is correct German accusative after "Liebe Grüße an". Only this phrase is enciphered; the rest of the card is open, so the cipher hides the most teasing part of the message from a casual reader.
- The dashes after "und an" are written on the card as a teasing blank; the ditto marks on the next line repeat "Liebe Grüße an" before "Fräulein Schwester" ("Miss Sister", the recipient's sister).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1197/work/decode.py
```

It uses only the Python standard library, checks the SHA-256 of the four images, and prints `DEINEN GELIEBTEN / BRAUTIGAm` (lower case marks the restored letter).

## Uncertainties

- **Restored letter.** The last digit of BRÄUTIGAM (the "2" of 12 = M) is hidden under the printed HCPortal collection stamp. A digit is visibly there, but its shape cannot be read; M is the only letter that makes a word. The old pencil decipherment stops at "BRAUTIG" and does not confirm it.
- **"19" under the stamp** in GELIEBTEN is read from visible ink, not restored.
- **Kurrent letters resting partly on word sense:** "Liebe" (capital L against V) and the middle letters of "Schwester", which lie partly under the stamp (initial S and "ster" are clear).
- **Pencil word on the girl's skirt.** A faint pencil word, beginning with a K-like capital and "…th…", is plausibly "Käthchen", labelling the girl with the recipient's name. It is not confirmed letter by letter; it is a single plain word, not ciphertext.
- **Address word** under the street line, read as "Laden", is uncertain (not part of the message).
- **Inverted stamp.** The stamp is upside down. In the "stamp language" of the time this is often listed as a love signal, but published tables differ, so no meaning is claimed. Nothing is written around the stamp, and what is under it cannot be seen.
- **Date:** 4 February 1899 from the clear postmark; the portal gives 14 February 1899. A faded circular postmark on the picture side is illegible.
- **Sender** is deliberately anonymous; no name to check.
- **Prior solution:** a web search on 2026-11-03 found no published solution of this card; the only earlier decipherment is the anonymous pencil note on the card itself, credited above.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, decoded the card with its own independent script (confirming that the J-less numbering is forced, since plain A–Z numbering gives nonsense), checked every group on its own 3× crops of the high-resolution scan, confirmed the "19" under the stamp and the existence of a hidden second digit in the last group, read the plain Kurrent text independently with the same result, and checked the stamp box and picture side for hidden writing (none found). Its four findings were minor and are reflected here:

- **Inverted stamp:** now recorded as a possible stamp-language signal, without a claimed meaning.
- **Date:** one explicit date given (4 February 1899 from the postmark, possibly 14 February per the portal).
- **Pencil decipherment:** now stated to agree only up to "BRAUTIG", so it does not confirm the restored M.
- **Register type:** stays MASC; no steganographic part was found on this card.

No decoded letter changed as a result of the review. All work on this card (capture, transcription, decipherment, review response and this report) was done by Claude Opus 5.5; there was no earlier GPT work on this number.

## Sources

- HC Portal record 1197, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1197 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3651/conversions/cpc_1899-02-14_DE_Frankfurt-Sachsenhausen_DE___pic-large.jpg (source/picture-large.jpg) and the original https://api.hcportal.eu/media/3651/cpc_1899-02-14_DE_Frankfurt-Sachsenhausen_DE___pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3652/conversions/cpc_1899-02-14_DE_Frankfurt-Sachsenhausen_DE___adr-large.jpg (source/address-large.jpg) and the original in work/hires/.
- Portal reference for the collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.

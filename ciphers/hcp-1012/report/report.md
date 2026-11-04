# HCP 1012 (cpc_-11-12_DE_Hof_DE_Selb_): a number-cipher note to Fräulein Rosa Lang in Selb

Human solver: Tomáš Pavuk

**Status: deciphered in full (every cipher number explained by one rule); independent review 1 verdict REVISE, all findings addressed, no change to the decoded cipher text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1012 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1012), portal name cpc_-11-12_DE_Hof_DE_Selb_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, language Unknown, sender Unknown, recipient Fräulein Lang, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

It is a picture postcard of the "Liebesträume" series: an art-nouveau lady with a red book, with a printed four-line verse ("Ich fühle Deinen Odem / Mich überall umwehn / Wohin die Augen schweifen / Wähn ich Dein Bild zu sehn!") which someone has rubbed and partly struck through in pencil. The message is written in pencil across the picture side; the card has to be turned 90° counter-clockwise to read it. In that orientation a short postscript runs up the left margin.

The address side is in plain Kurrent: **Wohlgeboren / Fräulein Rosa Lang / Selb / Kirchplatz**. It carries a Bavarian 5-Pfennig stamp (arms type), postmark HOF 12 NOV and arrival postmark SELB 13 NOV; no year is legible. The stamp type suggests about 1900–1910, which is not proven. Hof and Selb are neighbouring towns in Upper Franconia, Bavaria. A pencil "25.194" in the margin is a collector's or dealer's number.

![Picture side turned to reading orientation (work/picture-rotated.jpg)](../work/picture-rotated.jpg)

![Address side: Fräulein Rosa Lang, Selb, Kirchplatz; Bavarian stamp, Hof and Selb postmarks (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual, read by the solver from the un-converted portal originals (work/hires/) turned to reading orientation and enlarged; the portal gave no transcription. The text is a mixture of plain Kurrent German words and words written as dot-separated numbers.

Three number words gave a crib straight away: 11.23.14.7.17.25.11.19 after a word like "Brief" suggested ERHALTEN ("received"), 8.23.15.11.12 = BRIEF and 8 11.24.25.11.19 = BESTEN (in "besten Dank"). These fix A=7, B=8, E=11, F=12, H=14, I=15, L=17, N=19, R=23, S=24, T=25: each letter is its position in the alphabet plus 6, with one step at J, which is left out. The rest of the card confirms the rule with G=13, K=16, O=20, U=26 and Z=31 (AUFKLÄRUNG, FOLGT, SONNTAG, ZEIT, TAGE). K=16 next to L=17 in AUFKLÄRUNG shows that J is missing from the alphabet.

The reproduction command `python3 -I ciphers/hcp-1012/work/decode.py` (from the repository root) checks the SHA-256 of the source images and decodes work/transcription.txt with the key.

Both sides were searched for hidden writing (under or around the stamp, along the edges, inside the picture and in the struck-through verse), since other cards of the collection carry steganographic notes. Nothing was found; the area under the stamp cannot be seen on the scan.

## Key

Number substitution over the 25-letter alphabet without J (a simple monoalphabetic substitution, register type MASC):

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |

Numbers that occur on the card: 7 8 11 12 13 14 15 16 17 19 20 23 24 25 26 31. All of them fit the rule; none is left over. The writer sometimes leaves a letter in plain Kurrent inside a number word (f, u, nn, ch, h) and writes Ä as the number 7 with an umlaut mark above it.

## Transcription

Reading orientation, line by line. Numbers are cipher; ordinary words are plain Kurrent; 7^ is the number 7 with an umlaut mark.

```text
8.23.15.12, 11.23.14.7.17.25.11.19, 8: 11.24.25.11.19
Dank für 7.26.f.16.17.7^.23.u.19.13,
Entschuldigen Diese(n?) Karte!
8.23.15.11.12, 12.20.17.13.25, 24.20.nn.25.7.13,
(F) der 19.15.ch.25 11.h.11.23, 31.11.15.25,
der 7.17.17.11 25.7.13.11
Stunden! H. Gruss.   [monogram signature]
(left margin:) Freundlichst auch ihre(?),
```

## Plaintext and translation

German (cipher words decoded; brackets are editorial):

> Brif [sic] erhalten, besten Dank für Aufklärung. Entschuldigen [Sie] diese(n?) Karte! Brief folgt Sonntag, der [= da] nicht eher Zeit, der [= da] alle Tage Stunden! H[erzlichen] Gruss. [monogram]
> Margin: Freundlichst auch Ihre(?),

English:

> Letter received, many thanks for the explanation. [Please] excuse this card! A letter will follow on Sunday, since [I have] no time earlier, since [I have] lessons every day! Warm regards. [monogram]
> Margin: "Most kindly, also your ..." (if "Ihre", a closing formula leading into the monogram; preferred), or "Kindest [regards] to her too" (if "ihr(e)" = her).

Slovak:

> List som dostal(a), srdečná vďaka za vysvetlenie. Prepáčte [mi] túto pohľadnicu! List príde v nedeľu, keďže skôr nemám čas, lebo mám každý deň hodiny! Srdečný pozdrav. [monogram]
> Okraj: "Najsrdečnejšie, aj Vaša ..." (ak "Ihre", záverečná formula; preferované), alebo "Najsrdečnejšie aj jej" (ak "ihr(e)").

The note is an ordinary short message: thanks for a letter that explained something, an apology for answering only with a postcard, and a promise of a proper letter on Sunday because the writer has lessons ("Stunden") every day.

## Uncertainties

1. The first word is 8.23.15.12 = BRIF, without E; the same word is written in full later (8.23.15.11.12 = BRIEF). Kept as written.
2. "8: 11.24…" – the colon after 8 is read as a separator with a stray dot. Dots over some 1s are the writer's habit and are not signs.
3. The two plain words before "nicht eher" and "alle Tage" are read from the pixels as Kurrent "der"; the sense wants "da" (since). The translation "since" rests on word sense. Before the first "der" stands a separate F-shaped mark, unexplained (perhaps a false start or correction).
4. Plain letters inside number words (f, u, nn, ch, h): "nn" and "ch" are small and their reading is supported by the words they complete.
5. "Entschuldigen Diese(n?) Karte": the card has no "Sie"; it is supplied editorially. The last stroke of "Diese(n/r)" is uncertain; the meaning does not change.
6. "H. Gruss" is taken as "Herzlichen Gruss" (word sense).
7. The signature monogram (like "Ad." or "Ht.") is not read; it is a single signature item.
8. The last word of the postscript (ihr / ihre / Ihre) is uncertain; both readings are given.
9. No hidden message was found; the area under the stamp cannot be inspected.
10. The year is not legible; about 1900–1910 is an estimate from the stamp type.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, wrote its own decoder (review/work/my_decode.py) from its own reading of the card, and confirmed the key and every number group sign for sign. It also confirmed from the card that J is omitted from the alphabet. Verdict **REVISE**, with five findings:

1. (major) The transcription had "Entschuldigen Sie diese Karte", but there is no separate "Sie" on the card; the word after "Entschuldigen" is one word, "Diese(n/r)". Fixed: transcribed as written, "[Sie]" marked as editorial.
2. (minor) The Ä of AUFKLÄRUNG is the cipher number 7 with an umlaut mark, not a plain Kurrent ä. Fixed in the transcription and the decoder.
3. (minor) The "F" before the first "der" is a separate mark, not a lead-in stroke. Now recorded as an unexplained mark.
4. (minor) The postscript translation gave only one of two readings, and its position was described only for the scan as delivered. Both readings are now given, "Ihre" preferred; the position is described in reading orientation.
5. (minor) The register type is MASC; no steganographic note was found, so "MASC + Steganography" does not apply.

None of the changes alters the decoded cipher text.

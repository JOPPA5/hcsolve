# HCP 1034 (cpc_1904-09-05_DE_Munster_DE_Bremen_): Fritz to Tilly, Münster 1904

Human solver: Tomáš Pavuk

**Status: deciphered in full (92 of 92 cipher signs, plus one abandoned sign); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1034 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1034), portal name cpc_1904-09-05_DE_Munster_DE_Bremen_, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see also the HistoCrypt paper linked from the portal record, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Mathilde Meyer, with no transcription or solution attached.

The picture side shows a printed view captioned "Wersepartie bei Handorf" (the river Werse at Handorf, near Münster); the publisher's line reads "Verlag: Richard Borek, Braunschweig". The address side is written in plain German: **Fräulein / Mathilde Meyer / in Bremen / Caprivi Str. 6.** It carries a 5-Pfennig Germania stamp cancelled **MÜNSTER 5.9.04** and an arrival mark **BREMEN 6.9.04**.

The message is on the picture side and has two parts:

1. **Plain text in Kurrent script** along the top, with the date "Münster, d. 5/9 1904." written into the first line.
2. **Cipher**: five rows of invented symbols below and to the right of the plain lines, plus one single extra sign just right of the church spire.

The salutation "Tilly" is a pet form of Mathilde, the addressee; the cipher part is signed "Fritz". The written date, the Münster cancel and the next-day Bremen arrival mark agree, and the picture of Handorf fits a writer in Münster.

![Picture side: plain Kurrent text at the top, five cipher rows below it and the lone sign by the church spire (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Fräulein Mathilde Meyer, Bremen, Caprivi Str. 6; Germania stamp cancelled MÜNSTER 5.9.04 (source/address-large.jpg)](../source/address-large.jpg)

## Method

Everything was read by hand from the un-converted high-resolution scan (work/hires/), enlarged 3 to 5 times in per-row crops (work/z/ and the row crops rA1.png to rE1.png and c_l1a.png to c_r2.png in work/). No OCR was used, and the portal supplied no transcription.

The key was recovered without outside help. The opening came from an eight-sign group in row B whose first and last signs are the same: in a German letter closing this gives **herzlich** (h ... h). From there the frequent group TRId OV L gave **ich**, the signs with two and three vertical strokes gave **n** and **m** ("Indem ich mich"), and the rest followed word by word: "für deine liebe", "verbleibe ich mit", "Gruß und Kuß", "dein tr. Fritz". The writer spells ß as two signs, s + z, just as the Kurrent ß is a long s joined to a z; this confirms the values of the s and z signs on its own.

Every sign was then checked against all its other occurrences on the card, and the full transcription was decoded with one fixed key by a script.

## Key

Simple monoalphabetic substitution with invented symbols (register type MASC). The labels are conventional names for the drawn shapes.

| Sign | Shape | Letter |
|---|---|---|
| TRI | open triangle, no dot | I (capital) |
| TRId | triangle with a dot | i |
| VTRd | downward triangle with a dot | i (variant) |
| H2 | two verticals with a crossbar | n |
| H3 | three verticals with a crossbar | m |
| SQ | square, flat-bottomed box | d |
| D | D-shape, hollow or inked solid | e |
| OV | narrow closed oval | c (see uncertainty 1) |
| L | L-shape with a hook | h |
| XL | crossed, looped X | f / F |
| U | u-shape, open at the top | u |
| R | r-shape | r |
| P | P-shape | l |
| N | N zigzag, or V with a hook | b |
| X | small crossed loop | a |
| XG | tall X | G (capital) |
| S | k-like sign (long s) | s |
| Z8 | 8-shape (Kurrent z) | z |
| THk | circle or c with a bar and a tick | k |
| CX | circle struck through diagonally | t |
| DAG | double-dagger cross | v |

Four letters have two drawn forms (i, e, b, k); no sign stands for two letters, with the one exception described under uncertainty 1.

## Transcription and plaintext

Transcription in reading order ("/" is a word gap; punctuation as drawn):

```text
A  TRI H2 SQ D H3 / TRId OV L / H3 TRId OV L / XL U R / SQ D TRId H2 D P TRId D N D
B  X OV XL / H3 D R THk / S X H3 / THk D TRId CX / L D R Z8 P TRId OV L - N D SQ X H2 .
   (lone THk right of the church spire)
C  THk D , / DAG D R / N P D TRId N D / VTRd OV L / H3 TRId CX / XG R U S Z8 / U H2 SQ
D  THk U S Z8
E  SQ D TRId H2 / CX R . / XL R TRId CX Z8 .
```

Literal decryption (word gaps as drawn):

```text
A  Indem ich mich fur deineliebe
B  auf merk sam keit herzlich-bedan.
   [k]
C  ke, ver bleibe ich mit Grusz und
D  kusz
E  dein tr. fritz.
```

Full card in German (plain part and cipher part, normalised):

**Liebe Tilly! Du mußt heute schon mit einer Karte zufrieden sein, da es schon sehr spät geworden ist, und du doch morgen einen Brief bekommst. [cipher:] Indem ich mich für deine liebe Aufmerksamkeit herzlich bedanke, verbleibe ich mit Gruß und Kuß dein tr[euer] Fritz. Münster, d. 5/9 1904.**

English translation: **Dear Tilly! Today you will have to make do with just a card, since it has already got very late and you will be getting a letter tomorrow anyway. Thanking you warmly for your kind attentiveness, I remain, with greetings and a kiss, your faithful Fritz. Münster, 5 September 1904.**

Slovak translation: **Milá Tilly! Dnes sa musíš uspokojiť len s pohľadnicou, lebo je už veľmi neskoro a zajtra aj tak dostaneš list. Srdečne ti ďakujem za tvoju milú pozornosť a zostávam s pozdravom a bozkom tvoj verný Fritz. Münster, 5. 9. 1904.**

The cipher part is a conventional German letter closing of the period ("Indem ich mich ... herzlich bedanke, verbleibe ich ..."), and it follows naturally from the plain lines: the writer excuses the short card, promises a letter, thanks her and signs off with a kiss. That last, more intimate part is the one he enciphered.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1034/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both scans in source/ and both originals in work/hires/, decodes the manual transcription with the key, and prints each row, the literal plaintext and the normalised sentence. The transcription step itself is manual; it was confirmed independently in review.

## Uncertainties

1. **The second sign of "Auf".** It is a closed narrow oval, the same glyph as the c in every "ich" (four times, including "herzlich"). The writer's u in "für", "Gruß", "und" and "Kuß" is clearly open at the top. So the card literally has a c-sign here, and the reading u rests on word sense alone ("Aufmerksamkeit"; the other 11 signs of the word fit the key). It is a writer's slip or a badly closed u.
2. **The lone sign by the spire.** A single k-sign stands right of the church spire at the height of row B, where row B ends with "bedan.". Row C begins "ke,". The lone sign is read as an abandoned start of "ke" that the writer rewrote on the next line; it is left out of the plaintext. The word is "bedanke" either way. The dot after "bedan" is taken as a line-break mark, and a short dash joins "herzlich" to "bedan.".
3. **The dark figure at the end of row A.** A small dark figure (a person with a staff) touches the last sign of "liebe" at the card edge. Its tone and grain match the printed picture. The sentence needs no further sign there.
4. **"tr."** is read as the usual abbreviation of "treuer" (faithful).
5. **Plain Kurrent letters.** "heute", "zufrieden" (split "zu- / frieden") and "spät" rest partly on word sense; the reviewer read the plain text independently and agreed. No word of the card is left unread.
6. **Under the stamp.** The scans cannot show what is under the stamp, and no writing shows at its edges. On other series of cipher postcards (for example the Hungarian cards to Tóth Jolánka) a hidden message under the stamp is common, so a hidden message here **cannot be excluded** from the scans alone; only the physical card could settle it. Nothing visible on this card is steganographic, so the type is given as MASC.
7. **People.** "Fritz" has no surname on the card; Mathilde Meyer of Caprivistraße 6, Bremen, is known only from the address.

No published solution of this card was found: the portal status is Not solved with no attached solution, and the AI Decipherment Register had no record for it on 2026-11-03.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent of the same model as the solver; round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (all hash checks OK, output identical to the claimed plaintext), made its own crops of the high-resolution scan, transcribed all five rows with its own sign names and decoded them with its own script (review/work/verify.py); it obtained the same text and the same count of 92 signs, with a consistent key. It also read the plain Kurrent text and the address side independently and agreed. Its three findings were minor:

- **Hyphen in row B.** A joining dash between "herzlich" and "bedan." was missing from the transcription. It has been added to the transcription and the script; no letter changed.
- **Evidence for "Auf".** The contrast between the open-topped u and the closed oval (c) is now given as the evidence in uncertainty 1; the reading is unchanged.
- **Stamp.** The report now states plainly that a message under the stamp cannot be excluded from the scans (uncertainty 6). The register type stays MASC.

No decoded letter changed as a result of the review.

## Credits

Capture, transcription, key recovery, decipherment, this report and the register entry: Claude Opus 5.5 (Anthropic), 2026-11-03. There was no earlier AI work on this card. Independent review: a separate Claude Opus 5.5 agent. Human solver: Tomáš Pavuk.

## Sources

- HC Portal record 1034, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1034 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3162/conversions/cpc_1904-09-05_DE_Munster_DE_Bremen__pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3162/cpc_1904-09-05_DE_Munster_DE_Bremen__pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3163/conversions/cpc_1904-09-05_DE_Munster_DE_Bremen__adr-large.jpg (source/address-large.jpg); original in work/hires/.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03.

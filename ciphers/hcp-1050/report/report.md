# HCP 1050: a number-cipher postcard from Minna to Fritz Lehmann (Schweidnitz, 1910)

Human solver: Tomáš Pavuk

**Status: deciphered in full (200 of 200 cipher numbers); independent review 1 verdict ACCEPT, one letter corrected (KONTEN to KÖNTEN).** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1050 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1050), portal name cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as a general reference for the collection.

The address side carries a green Germania 5-pfennig stamp (still affixed) cancelled **SCHWEIDNITZ 17.3.10** (17 March 1910; Schweidnitz is today Świdnica, Poland). It is addressed in plain Kurrent handwriting to **Herrn Fritz Lehmann, Königszelt, Bahnhofstr. N. 1** (Königszelt, today Jaworzyna Śląska, a railway junction a few kilometres from Schweidnitz). The left half of the card is filled with seventeen pencil lines of dotted numbers: this is the cipher. A short plain-Kurrent pencil note, written upside down, stands at the top centre: it is the sender's return address. The picture side is a printed photo card titled "Kommt ein Vogel geflogen!" with a printed verse and the publisher number 3309/6; it bears no handwriting.

The card belongs to a series of cipher cards to Fritz Lehmann in the same collection. The same number table was already established on the sister cards HCP 1134 and HCP 1113 in this repository (and also used on HCP 1060). This card was therefore read with a **known, transferred key**, checked against every number here; it is not a blind key recovery.

![Address side: cipher in seventeen pencil lines on the left, the upside-down return address at the top centre, the Schweidnitz postmark and the address to Fritz Lehmann, Königszelt (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed card "Kommt ein Vogel geflogen!", no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**, made by Claude Opus 5.5 on 2026-11-03 from the un-converted high-resolution scan of the address side (3469 x 2298 pixels), line by line, with 3x enlargements of every doubtful place. No OCR was used and the portal supplied no transcription. The numbers are separated by dots, words by dashes. Three extra marks are used by the writer:

- a double tick over a number marks an umlaut (15 with ticks = Ö, 21 with ticks = Ü);
- a bar over 13 doubles it (MM, in ZUSAMMEN and GEKOMMEN);
- "=" at the end of a line is the German hyphenation sign (the word continues on the next line).

The numbers used on the card are 2 to 16, 18 to 23 and 26; every one of the 200 numbers decodes with the table below, and none is left over or out of range. A short script (work/decode.py) checks the SHA-256 hashes of the scans and decodes the transcription file (work/transcription.txt).

In review a second, independent Claude Opus 5.5 agent cut its own strips from the high-resolution scan, typed its own transcription of all seventeen lines and decoded it with its own script. Its text agreed with the solver's except for one umlaut (see Review summary), which has been corrected.

## Key

Number substitution (monoalphabetic), German. The 25-letter alphabet without J is numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Q, X and Y (17, 24, 25) do not occur on this card. Umlaut is marked by a double tick over the base letter's number, doubling by a bar.

## Plaintext

Transcription, line by line (" = umlaut ticks over the number, _ = bar over it, = = hyphenation sign):

```text
12.10.6.3.6.18 - 7.18.10.20.26
6.14.5.12.10.4.9 - 6.10.14
12.6.3.6.14.19 - 26.6.10.4.9.6.14
22.15.10.14 - 5.10.18 - 21.14.5
7.18.6.21.6 - 13.10.4.9 - 19.6.9.18
5.2.19 - 6.19 - 19.4.9.15.14
3.6.19.19.6.18 - 8.6.9.20 - 22.10.6=
12.6.10.4.9.20 - 11.15".14.20.6.14
23.10.6.18 - 19.15.14.20.2.8
23.10.6.5.6.18 - 26.21.19.2.13_.6.14
19.6.10.14 - 23.2.19 - 10.19.20
5.6.14.14 - 19.15 - 16.12.15".20.26=
12.10.4.9 - 21".3.6.18 - 5.10.4.9
8.6.11.15.13_.6.14? - 8.21.20.6 - 3.6.19.19.6=
18.21.14.8 - 3.2.12.5.10.8.6.14 - 23.10.6=
5.6.18.19.6.9.14 - 8.18.21.19.26 - 11.21.19.26
13.10.14.14.2
```

Decoded German, as written (the writer's own spellings kept):

```text
LIEBER FRITZ
ENDLICH EIN
LEBENS ZEICHEN
VOIN DIR UND
FREUE MICH SEHR
DAS ES SCHON
BESSER GEHT
VIELEICHT KÖNTEN
WIER SONTAG
WIEDER ZUSAMMEN
SEIN WAS IST
DENN SO
PLÖTZLICH ÜBER DICH
GEKOMMEN? GUTE
BESSERUNG BALDIGEN
WIEDERSEHN GRUSZ KUSZ
MINNA
```

Normalised German (spelling, punctuation and the words in brackets are editorial):

**Lieber Fritz! Endlich ein Lebenszeichen von dir, und [ich] freue mich sehr, dass es [dir] schon besser geht. Vielleicht könnten wir Sonntag wieder zusammen sein. Was ist denn so plötzlich über dich gekommen? Gute Besserung, [auf] baldiges Wiedersehen. Gruß, Kuss, Minna.**

English translation: **Dear Fritz! At last a sign of life from you, and I am very glad that you are already better. Perhaps we could be together again on Sunday. Whatever came over you so suddenly? Get well soon, and see you again soon. Greetings, a kiss, Minna.**

Slovak translation: **Milý Fritz! Konečne od teba znak života a veľmi sa teším, že ti je už lepšie. Možno by sme mohli byť v nedeľu znova spolu. Čo ťa to tak náhle prepadlo? Skoro sa uzdrav a dovidenia čoskoro. Pozdrav, bozk, Minna.**

The plain return address (upside down, top centre, not enciphered) reads approximately: "Abs. M. L.(?) b. Fr. Sch...tke(?) / Schweidnitz Graben(?)str. / N. 3 II Hof", that is "Sender: M. L., care of Mrs Sch...tke, Schweidnitz, Grabenstraße(?) no. 3, second floor, rear building". The initial M fits the signature Minna, and the town matches the postmark.

Notes on the reading:

- The writer spells as she speaks: VOIN for "von", VIELEICHT with one L, KÖNTEN for "könnten", WIER for "wir", SONTAG with one N, GRUSZ and KUSZ with SZ for ß, BALDIGEN for "baldiges", WIEDERSEHN. These are decoded as written, not corrected; the 10 in VOIN is clearly written.
- The doubling bars fall exactly on the MM of ZUSAMMEN and GEKOMMEN, the umlaut ticks on KÖNTEN, PLÖTZLICH and ÜBER, and the hyphenation signs on real word breaks (VIE=LEICHT, PLÖTZ=LICH, BESSE=RUNG, WIE=DERSEHN). This regularity is good evidence that the reading is right.
- The content is a short note from a girlfriend: Fritz has evidently been ill, she is glad he is recovering and proposes to meet on Sunday.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1050/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two source scans and the two high-resolution originals in work/hires/, decodes work/transcription.txt with the key above and prints the seventeen lines and the run-on text.

## Uncertainties

- **SO (line 12).** The second number of 19.15 is retraced or overwritten and looks blotted; the 1 and the flag of the 5 are visible. Reading it as 15 = O rests partly on word sense ("was ist denn so plötzlich ...").
- **BESSE= (line 14).** The two 19s of 3.6.19.19.6 are written without a separating dot, the second partly on the printed green divider line; read as 19.19 = SS.
- **"?" after GEKOMMEN** is a question-mark-shaped sign on the card, taken as punctuation.
- **Return address.** The second initial (L?), the landlady's surname (Kurrent "Sch...tke") and the vowel of the street name (Graben-?) are not firmly legible to either solver or reviewer. These are names in an address line; the rest of the note reads, and it does not affect the message.
- **Steganography.** Some postcards in the Schrödel collection hide a message under the stamp. On this card the stamp is still affixed, so the area beneath it cannot be inspected on the scans; nothing is visible at its edges, and the picture side carries only printed text. No hidden message is claimed, and none can be excluded.
- The key was transferred from the sister Lehmann cards HCP 1134 and HCP 1113, not recovered blind from this card; it decodes all 200 numbers here without change.
- One web search (2026-11-03) found no published solution of this card; the AI Decipherment Register had no record for it.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), cut its own strips of the high-resolution scan, typed its own transcription and decoded it with its own script; the only difference was one umlaut. It confirmed the bars over 13, the reading 20 (not 26) in GUTE, VOIN with a clear 10, and that the specks above line 9 are paper noise. Its four minor findings and what changed:

- **KÖNTEN.** A double tick stands above the 15 of KÖNTEN (line 8), placed like the tick over ÜBER; the solver had missed it. The transcription and plaintext now read KÖNTEN; the reproduction command was re-run and matches the reviewer's text.
- **Number count.** The card carries 200 numbers, not "about 95" as SOLUTION.md first said; corrected.
- **SO** and **the return address** remain disclosed as uncertain, as above.

The reviewer and solver agree on the cipher type MASC (number substitution); with the stamp still in place, no steganographic part can be shown on this card.

## Sources

- HC Portal record 1050, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1050 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3210/conversions/cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11_pic-large.jpg (source/picture-large.jpg); original in work/hires/.
- Address side: https://api.hcportal.eu/media/3211/conversions/cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11_adr-large.jpg (source/address-large.jpg); original in work/hires/.
- Key: sister Lehmann cards in this repository, ciphers/hcp-1134/SOLUTION.md and ciphers/hcp-1113/SOLUTION.md.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03.

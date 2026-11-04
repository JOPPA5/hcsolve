# HCP 1134: a numbered love note from "Susi" to Fritz Lehmann (1910)

Human solver: Tomáš Pavuk

**Status: deciphered in full (86 of 86 numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1134 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1134), portal name cpc_1910-03-11_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-10, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The only reference given is Schrödel's survey article on the collection (HistoCrypt 2021).

The picture side is a view of **Fürstenstein Schloß** (Fürstenstein Castle, today Zamek Książ near Wałbrzych, Poland), published by Kunstverlag Herm. Adam, Freiburg i. Schl. The address side is postmarked **FREIBURG (SCHLES.) 11.3.10** (11 March 1910) and addressed in plain Kurrent to "Herrn Fritz Lehmann, Schweidnitz", with a street name and house number "No 6" (the street name is read only loosely and is not part of the cipher). Freiburg in Schlesien (Świebodzice) and Schweidnitz (Świdnica) are neighbouring towns in Lower Silesia, then in Germany.

The cipher message is written on the address side, turned sideways, left of the dividing line: eight rows of numbers separated by dots, words separated by dashes, the last row being the signature.

![Picture side: Fürstenstein Castle (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Cipher text turned upright, from the high-resolution scan (work/crops/text_rot.png)](../work/crops/text_rot.png)

The card is one of a series of postcards to Fritz Lehmann in Schweidnitz in the same collection (HCP 913, 978, 979, 1044–1047, 1050, 1051, 1060, 1113, 1134). No work existed on the sister cards when this one was read, so nothing was taken from them.

## Method

The transcription is **manual** and was made by Claude Opus 5.5 from the un-converted high-resolution scan of the address side, turned upright and enlarged (crops in work/crops/). The portal supplied no transcription.

The numbers run only from 2 to 26, which points to a plain letter numbering. The first word, 12.10.6.3.6.19, has the pattern x-y-E-z-E-w, and the frequent short word 5.10.6 suggested DIE; together these give LIEBES. That fixed the first letters, and they fit the alphabet without J numbered from 2 (A = 2, B = 3, … I = 10, K = 11, … Z = 26). With this table the second word becomes SCHÄTZCHEN and the rest of the card decodes without any adjustment. A double tick written over a number is an umlaut (2" = Ä, 21" = Ü), and ß is written as SZ.

In review a second, independent Claude Opus 5.5 agent re-read all 86 numbers from its own crops, decoded them with its own script and obtained identical text, letter for letter.

## Key

Number substitution (monoalphabetic), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Additional conventions: a double tick over a number marks an umlaut (2" = Ä, 21" = Ü); ß is written SZ (19.26). Numbers that occur on this card: 2 3 4 5 6 7 8 9 10 11 12 14 15 18 19 20 21 23 26; every one decodes under this single table.

## Plaintext

Transcription, row by row:

```text
12.10.6.3.6.19 - 19.4.9.2".20.26.4.9.6.14 -
19.6.14.5.6 - 5.10.6.18 - 5.10.6 -
3.6.19.20.6.14 - 8.18.21".19.26.6 -
5.6.10.14.6.14 - 23.21.14.19.4.9 -
7.21".18 - 19.15.14.14.20.2.8 -
11.2.14.14 - 10.4.9 - 14.10.4.9.20 -
6.18.7.21".12.12.6.14 -
19.21.19.10.
```

Decoded, row by row:

```text
LIEBES SCHÄTZCHEN
SENDE DIER DIE
BESTEN GRÜSZE
DEINEN WUNSCH
FÜR SONNTAG
KANN ICH NICHT
ERFÜLLEN
SUSI
```

German, normalised: "Liebes Schätzchen! Sende dir die besten Grüße. Deinen Wunsch für Sonntag kann ich nicht erfüllen. Susi."

English: "Dear sweetheart! I send you my best regards. I cannot fulfil your wish for Sunday. Susi."

Slovak: "Milý miláčik! Posielam ti najsrdečnejšie pozdravy. Tvoje želanie na nedeľu ti nemôžem splniť. Susi."

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1134/work/decode.py
```

The script checks the SHA-256 of both source scans and of the high-resolution address scan, then decodes work/transcription.txt with the key above and prints the eight decoded rows.

## Uncertainties

1. **W of WUNSCH.** The first number of row 4 was overwritten: a 22 and a 23 are written over each other. 23 = W gives WUNSCH; 22 = V would give "VUNSCH". The choice of W rests on word sense; the pixels alone show both layers.
2. **DIER.** 5.10.6.18 is clearly spelled with 6 = E; it is the writer's phonetic spelling of "dir", not a misreading.
3. **Umlaut of FÜR.** The double tick belonging to FÜR stands low, just below the 10 of row 4 and above the 21 of row 5; it is read as the umlaut of FÜR and not as an extra sign. FUR or FÜR, the reading is the same.
4. **Signature.** "Susi" is a first name or nickname; the writer's identity is unknown.
5. **Hidden writing.** The picture side carries no writing beyond the printed caption. The stamp is still affixed and no ink is visible at its edges, so anything written underneath cannot be inspected from the scans. No steganographic part was found, so the cipher type is given as MASC only.

## Review summary

An independent Claude Opus 5.5 reviewer re-ran the reproduction command, decoded its own re-reading of the scan with its own script (identical result), checked the transcription number by number against enlarged crops, and inspected the stamp area and the picture side. Verdict: **ACCEPT**, with four minor findings:

1. Overwritten W numeral: agreed with the solver's reading and its disclosure; no change.
2. The handover stated the wrong number count (61); corrected to 86.
3. Placement of the FÜR umlaut: agreed, disclosed; no change.
4. Whether the article linked by the portal was checked: it has now been checked (see Sources). It contains collection statistics and eight sample cards, none of them this card, and no key or plaintext for the Lehmann series. The reading is therefore not taken from any published source.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1134 and its two scans (source/, work/hires/), captured 2026-11-03; details in SOURCES.md.
- T. Schrödel, "Cryptographic postcards", Proceedings of the 4th International Conference on Historical Cryptology HistoCrypt 2021, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (consulted; does not treat this card).
- Earlier work: none. Transcription, key reconstruction and decipherment by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent.

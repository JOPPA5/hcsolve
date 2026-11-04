# hcp-1134 – Solution (round 1, with response to review 1)

Card: HC Portal cryptogram 1134, `cpc_1910-03-11_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-10`, T. Schrödel collection.
Picture side "Fürstenstein Schloß" (Kunstverlag Herm. Adam, Freiburg i. Schl.). Postmark FREIBURG (SCHLES.) 11.3.10; addressed in plain
Kurrent "An Herrn Fritz Lehmann, Schweidnitz, Bögendorferstraße(?) No 6" (street name not part of the cipher; read loosely).
Portal status: Not solved, no transcription or solution attached. Transcription below is my own (Claude Opus 5.5) from the high-resolution scan.
No published solution of this card was found (one web search, 2026-11-03). No earlier work existed in this directory; sister Lehmann
directories in this repo had no work yet, so nothing was taken from them.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J is numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Numbers are separated by dots, words by dashes. A double tick over a number (2, 21) is an umlaut: 2" = Ä, 21" = Ü. ß is written SZ (19.26).
Numbers actually used: 2 3 4 5 6 7 8 9 10 11 12 14 15 18 19 20 21 23 26; every one decodes under this single table.

## Transcription (work/transcription.txt)

```
12.10.6.3.6.19 - 19.4.9.2".20.26.4.9.6.14 -
19.6.14.5.6 - 5.10.6.18 - 5.10.6 -
3.6.19.20.6.14 - 8.18.21".19.26.6 -
5.6.10.14.6.14 - 23.21.14.19.4.9 -
7.21".18 - 19.15.14.14.20.2.8 -
11.2.14.14 - 10.4.9 - 14.10.4.9.20 -
6.18.7.21".12.12.6.14 -
19.21.19.10.
```

## Plaintext (German, as written)

LIEBES SCHÄTZCHEN – SENDE DIER DIE BESTEN GRÜSZE – DEINEN WUNSCH FÜR SONNTAG KANN ICH NICHT ERFÜLLEN – SUSI

Normalised: "Liebes Schätzchen! Sende dir die besten Grüße. Deinen Wunsch für Sonntag kann ich nicht erfüllen. Susi."

English: "Dear sweetheart! I send you my best regards. I cannot fulfil your wish for Sunday. Susi."

Slovak: "Milý miláčik! Posielam ti najsrdečnejšie pozdravy. Tvoje želanie na nedeľu ti nemôžem splniť. Susi."

## Command (from repo root)

```
python3 -I ciphers/hcp-1134/work/decode.py
```

It checks the SHA-256 of both source scans and the hi-res address scan, then decodes work/transcription.txt with the key above.

## Uncertainties

1. Line 4, first number of WUNSCH: the writer overwrote one numeral with another (a 22 and a 23 written over each other, see
   work/crops/w23.png). The final stroke reads as 3, i.e. 23 = W; 22 would be V ("VUNSCH"). W is supported by word sense; the pixels
   alone are ambiguous between the two layers.
2. "DIER" (5.10.6.18) is spelled with E on the card – clearly 6 – so it is the writer's phonetic spelling of "dir", not a reading error.
3. Marks: the ″ between 10 and 14 in line 4 (DEINEN) sits at the baseline under the Ü-mark of FÜR on the next line; I take it as that umlaut
   mark straying, not as an extra sign. The gap inside 3.6.19 . 20.6.14 (BES TEN) is just spacing.
4. The signature "SUSI" is a name/nickname; identity unknown.
5. Steganography check: the picture side has no writing beyond the printed caption. The stamp is still affixed, so anything under it
   cannot be inspected on these scans; no ink traces show at the stamp edges.

## Why I believe it is correct

One fixed table decodes all 8 lines (86 numbers) into fluent, period-typical German with no leftover signs; the first two words alone
(LIEBES SCHÄTZCHEN) fix 10 letters, and the rest then follows without any adjustment. The umlaut marks fall exactly where German needs Ä/Ü
(Schätzchen, Grüße, für, erfüllen). Content (a short love note signed Susi, refusing a Sunday meeting) fits a postcard to a young man.

## Response to review 1

Verdict ACCEPT. Reading unchanged; `python3 -I ciphers/hcp-1134/work/decode.py` re-run 2026-11-03: three SHA-256 checks OK, output identical
(LIEBES SCHÄTZCHEN / SENDE DIER DIE / BESTEN GRÜSZE / DEINEN WUNSCH / FÜR SONNTAG / KANN ICH NICHT / ERFÜLLEN / SUSI).

1. Overwritten W numeral (minor) – agree, no change. Already disclosed as uncertainty 1: both layers are visible
   (work/crops/w23.png); 23 = W rests on word sense (WUNSCH), 22 would give VUNSCH.
2. Wrong count (minor) – fixed. The transcription holds 86 numbers (8 rows incl. signature), not 61; corrected in
   "Why I believe it is correct" above and used in the report.
3. Umlaut on FÜR (minor) – agree, no change. On work/crops/text_rot.png the double tick sits just below "10," in row 4,
   i.e. directly above the 21 of row 5; it is the umlaut of FÜR, already disclosed as uncertainty 3. FUR/FÜR does not change the reading.
4. Published-solution check (minor) – done. I opened the portal's linked article, T. Schrödel, "Cryptographic postcards",
   Proc. HistoCrypt 2021, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (PDF download/166/122/65). It gives collection
   statistics (428 cards, 24 sender/recipient sets, cipher types, symbol classes) and an addendum of eight sample cards; none of the
   eight is this card (no Fürstenstein view, no Lehmann address), and the text names no recipient, no plaintext and no key for the
   Lehmann cards. So no published solution of this card or of its alphabet was found; the reading remains my own.

Steganography: as the reviewer confirmed, nothing is written on the picture side beyond the printed caption, and the stamp is still
affixed with no ink at its edges; nothing hidden could be inspected. Register type therefore stays `MASC`, not `MASC + Steganography`.

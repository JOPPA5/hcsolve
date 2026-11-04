# hcp-1051 – Solution (round 1)

Card: HC Portal cryptogram 1051, `cpc_1910-03-31_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-12`, T. Schrödel collection.
Address side: Germania 5 Pf stamp, postmark SCHWEIDNITZ 31.3.10; addressed in plain Kurrent "Herrn Fritz Lehmann, Schweidnitz,
Bögen...straße(?) No 6" (street name not part of the cipher; read loosely). Heading in Kurrent "Schweidnitz d. 31/3 10" (the month
digit looks like an 8 on the scan; the postmark gives 31.3.10). The message is 9 pencil lines of numbers on the left half.
Picture side: printed photo card "Kommt ein Vogel geflogen! / Und der Sommer ist kommen und mein Schätzchen ist weit." (publisher
mark B.N.K., no. 33090/4); no handwriting found (contrast-enhanced crops work/crops/pic_left.png, pic_right.png).
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5,
2026-11-03) from the high-resolution scan in work/hires/. No earlier work existed in this directory. One web search (2026-11-03)
found no published solution of this card. The key was taken from the finished Lehmann sister cards hcp-1113 and hcp-1134 (same
recipient) and tested here; it decodes every number on this card.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words. Numbers used: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 18 19 20 21 23 26.

## Transcription (work/transcription.txt)

```
12.10.6.3.6.18 - 7.18.10.20.26 -
10.4.9 - 11.15.13.13.6 - 9.6.21.20 -
23.10.6.5.6.18 - 6.10.14
3.10.19.4.9.6.14 - 26.26
5.10.18 - 23.6.14 - 6.19 -
18.6.4.9.20 / 10.19.20 -
9.6.18.26 / 12.10.6.14 -
8.18.21.19 - 21 - 11.21.19
5.6.10.14.6 - 13.10.14.14.2 -
```
('/' = word break written on the card only as a dot, not a dash.)

## Plaintext

German as written: LIEBER FRITZ – ICH KOMME HEUT – WIEDER EIN BISCHEN ZZ [=ZU] DIR – WEN ES RECHT IST – HERZLIEN [=HERZLEIN] –
GRUS U KUS – DEINE MINNA

Normalised: "Lieber Fritz! Ich komme heut wieder ein bisschen zu dir, wenn es recht ist, Herzlein. Gruß u. Kuss, deine Minna."

English: "Dear Fritz! I am coming to you again for a little while today, if that is all right, sweetheart. Greetings and a kiss,
your Minna."

Slovak: "Milý Fritz! Dnes zase na chvíľku prídem k tebe, ak ti to vyhovuje, srdiečko. Pozdrav a bozk, tvoja Minna."

## Command (from repo root)

```
python3 -I ciphers/hcp-1051/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, then decodes work/transcription.txt with the key above.

## Uncertainties (all word-sense calls disclosed)

1. Line 4, "26.26": both groups are clearly 2+6 (work/crops/zu.png); the 6 of the first is retraced. Literally ZZ; "zu dir" needs
   26.21. I take it as a writer slip and read ZU by word sense; the pixels do not show a 21.
2. Line 7, "9.6.18.26 . 12.10.6.14" = HERZ LIEN, run together with a plain dot (the 1 of 12 is retraced darker). I read it as
   "Herzlein" (sweetheart) with the writer's I/E swapped (ie habit). The pixels give LIEN; HERZLEIN is word sense.
3. Line 2, last group of HEUT: the 2 is clear; the second numeral is crossed by the printed green divider line and partly hidden by it.
   Its visible remains fit 0, giving 20 = T; T rests on word sense (restoration of a print-obscured sign).
4. Line 1, LIEBER: "6.3" are written close together with a faint low dot between them (work/crops/l1a.png); 6 and 3 are clear.
5. Spellings as written: BISCHEN (bisschen), WEN (wenn), GRUS / KUS (Gruß / Kuss), HEUT (heute). Not reading errors.
6. Signature MINNA: a first name; identity unknown. The sister cards hcp-1113 and hcp-1134 (same key, same recipient) are signed
   SUSI; whether Susi and Minna are the same person/hand is not established here.
7. Steganography check: the stamp is still affixed, so anything under it cannot be inspected on these scans; no ink shows at its
   edges. Picture side: printed captions and publisher numbers only.
8. Heading month digit (plain Kurrent, not cipher): looks like 8; postmark and file name give March (31.3.10).

## Why I believe it is correct

One fixed table, identical to the one on the Lehmann sister cards hcp-1113 and hcp-1134, decodes all 9 lines (83 numbers, 83 letters) into
coherent colloquial German: an announced visit to Fritz, signed Minna, matching the love-card picture. Only two disclosed writer
slips (ZZ for ZU, LIEN for LEIN) and one print-obscured digit needed word sense; no number is left undecoded.

## Response to review 1

Verdict ACCEPT, four minor findings. The reading is unchanged.

1. Number count (fixed). "55 numbers" was wrong. Counting the cipher groups of work/transcription.txt (comment lines excluded)
   gives 83 numbers, and the decoded output has 83 letters. "Why I believe it is correct" now says 83. Re-ran
   `python3 -I ciphers/hcp-1051/work/decode.py`: four SHA-256 checks OK, output unchanged.
2. The 10 in FRITZ (added as uncertainty 9 below). Checked again on the reviewer's zoom review/work/fritz3.png: the group before it
   is 18 with a closed, crossed 8 (R); the third group is "1" plus a small open loop with no crossing stroke, the writer's 0, so
   10 = I. 18 there would give FRRTZ, which also fails on word sense, but the call rests on the pixels.
3. Address street (re-read, still loose). On work/crops/address.png the street word reads "..ögen str. No 6": the capital is a
   Kurrent loop that could be L or B, the rest "ögen" plus abbreviated "str." The street name is outside the cipher and does not
   affect the reading; it stays marked uncertain.
4. Signature (agreed). MINNA here, SUSI on hcp-1113/1134. The report keeps them as separately signed cards and does not claim one
   writer.

Steganography: as the reviewer confirms, the stamp is affixed and no ink shows at its edges; the picture side has only print. No
hidden message is visible on these scans, so the type stays MASC (not "MASC + Steganography").

Added uncertainty:

9. Line 1, FRITZ, third group 10 (I): open 0 loop without crossing, distinct from the crossed 8 of the preceding 18 (review/work/fritz3.png).

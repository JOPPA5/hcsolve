# HCP 1010 (cpc_--_DE__DE_Hier_): a teasing number-cipher postcard to Helene Schlauch

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict REVISE (one hidden group missed in round 1), all findings addressed, reading of the main text unchanged.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1010 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1010), portal name cpc_--_DE__DE_Hier_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Helene Schlauch, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

It is an embossed picture postcard showing a young man in a hat leaning towards a girl at a wooden fence, with foliage behind them. The address side is in plain German Kurrent and is not enciphered: "Fräulein Helene Schlauch, Hier, Rathskeller" ("Miss Helene Schlauch, local, Rathskeller"), so the card was delivered locally, probably to someone working or living at a town-hall cellar restaurant. The stamp has been removed; the stamp box shows only bare paper and glue residue. There is no postmark, date or signature, so the card can only be dated loosely to around 1900 from its style.

All the ciphertext is on the picture side, in three places:

- two lines of numbers along the bottom edge, written upside down relative to the scan;
- number groups on the cross-boards of the fence, in the picture itself;
- one short number group on the brim of the young man's hat.

The last two are hidden in the picture (steganography). The scan as published is landscape with the figures lying on their side; orientations below refer to it.

![Picture side as scanned (source/picture-large.jpg)](../source/picture-large.jpg)

![Fence boards, scan turned 90° counter-clockwise: 17 5 21 / 2 24 19 / 5 25 / 5 21 16 5 7 (review/work/fence2.png)](../review/work/fence2.png)

![Hat brim, scan turned 90° clockwise: 7 2(1) 18 20, the end lost in the dark shading (work/crops/hat_cw.png)](../work/crops/hat_cw.png)

## Method

The transcription is manual, from the high-resolution scan (3469 × 2298 px) kept in work/hires/. Each passage was cropped, turned and enlarged 3–5 times, partly with channel separation and high-pass filtering to lift pencil from the embossed shading. No transcription was supplied by the portal.

The numbers run from 1 to 25 and nothing higher: a number substitution of a 24- or 25-letter alphabet. The frequent 5, 8 and 9 and the bigram "9 5" (IE) fit E, H and I with A = 1, but 25 was far too frequent for Y or Z. The word "12 24 12 5 25 19" = MOMENT showed that J is omitted and that N–Z are numbered downwards from 25. The full key then decodes every passage into German with no leftover number.

In review, the reviewer rebuilt the key separately, made its own transcription and decoded it with its own script. It got the same text for the bottom lines and the fence, and it found the hat-brim group, which the solver had missed in round 1.

## Key

The alphabet without J, A–M numbered 1–12 upwards and N–Z numbered 25–13 downwards:

| A | B | C | D | E | F | G | H | I | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 |

Umlauts are written as the base number with two strokes above it (1 with strokes = Ä, 18 with strokes = Ü). F, P, Q, X, Y and Z do not occur; their values follow from the pattern.

## Ciphertext

"|" separates words, a bracket marks a restored digit (hidden by the collection stamp, damage or shading, or read on word sense).

```text
A (bottom, upside down):
4 [5] 21 | 2 18 21 20 [3] 8 5 | 9 20 19 | 10 18: 8 25 5 21 . | 8 9 5 21 | 16 9 5 | 20 9 5 | 20 5 8 5 25 .
B (bottom, upside down):
16 1 20 | 16 9 21 4 | 16 2[4] 8 11 | 9 12 | 25 1: 3 8 20 19 5 25 | 12 24 12 5 25 19 | 8 9 5 21 | 7 5 20 3 8 5 8 5 25 .
C (fence boards):
17 5 21 | 2 24 19 | 5 25 | 5 21 | 16 5 7
H (hat brim):
7 2[1] 18 20 [20]
```

## Plaintext and translation

German:

- A: Der Bursche ist kühner. Hier, wie Sie sehen.
- B: Was wird wohl im nächsten Moment hier geschehen.
- C (fence): Verbotener Weg.
- H (hat brim): Gruss (Gruß).

Read as one text: "Der Bursche ist kühner hier, wie Sie sehen. Was wird wohl im nächsten Moment hier geschehen? — Verbotener Weg. — Gruß."

English: "The lad is bolder here, as you see. What will happen here in the next moment? — [on the fence:] Forbidden path. — [on the hat brim:] Greetings."

This translation follows the reading in which "hier" belongs to the first clause. The card has a full stop after "kühner", so the alternative is "The lad is bolder. Here, as you see."

Slovak: "Mládenec je tu odvážnejší, ako vidíte. Čo sa tu asi stane v najbližšej chvíli? — [na plote:] Zakázaná cesta. — [na okraji klobúka:] Pozdrav."

The text is a playful comment on the picture: the young man courting the girl, a caption-like "what happens next?", and "forbidden path" written on the very fence he leans over.

## Uncertainties

- Restorations under the HCPortal collection stamp or on damaged spots, each the only letter that makes the word: the E of "Der", the C (and part of the R) of "Bursche", the 4 of 24 = O in "wohl".
- Fence, first sign: at a damaged board edge it could be 17 (V) or 13 (Z); 17 rests on word sense (VERBOTENER).
- Hat brim: "7 . 18 20" is clear. The second group is a 2 followed by a stroke shaped like this writer's crossed 4; it is read 21 (R) on word sense, because 24 (O) gives GOUS…, which is no word. After 20 the brim is in dark shading, and the final 20 (second S) is a restoration from a faint trace. Without it the word is still GRUS = Gruß.
- Clause boundary after "kühner" (see the translation).
- A long pencil line runs through part of line B; the digits under it are clear, and it is taken as an incidental stroke.
- No date, sender or signature.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1010/work/decode.py
```

The script checks the SHA-256 hashes of the source images, prints the key and decodes work/transcription.txt; restored letters are printed in lower case. Output: "DeR BURScHE IST KÜHNER. HIER WIE SIE SEHEN." / "WAS WIRD WoHL IM NÄCHSTEN MOMENT HIER GESCHEHEN." / "VER BOT EN ER WEG" / "GrUSs".

## Review and what changed

The reviewer (a separate Claude Opus 5.5 agent) ran the command, decoded with its own script, checked the transcription against the high-resolution scan and searched the whole picture and the stamp box. It confirmed the key and the reading of the bottom lines and the fence, and gave the verdict REVISE with five findings:

1. (major) A fourth cipher group on the young man's hat brim had been missed, and the claim that every number on the card was used was wrong. Fixed: the group was read on new enlargements, added to the transcription and decoded as GRUS(S), "Gruß"; its uncertain digits are disclosed above.
2. (minor) The fence text had been said to read with the card turned clockwise; it is counter-clockwise. Corrected.
3. (minor) The first fence number (17 or 13) rests partly on word sense. Added to the uncertainties.
4. (minor) The translation must say which clause boundary it follows. Done.
5. (minor) The register type MASC + Steganography was confirmed.

The main text did not change; one greeting word was added.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic) on 2026-11-03; independent review by a separate Claude Opus 5.5 agent. No published solution of this card was found or used.

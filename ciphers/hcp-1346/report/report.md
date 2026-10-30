# HCP 1346 (pc_hcp_27): a German love postcard from August to M. Scheck, 1901

Human solver: Tomáš Pavuk

**Status: deciphered in full (290 of 290 cipher signs; 2 dots in one word emended); independent review 1 verdict REVISE, findings addressed, decoded text unchanged.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1346 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1346), portal name pc_hcp_27, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1901-04-16, language Unknown, location Europe, sender Unknown, recipient M Scheck, with no transcription or solution attached.

It is an embossed rose postcard. Pencil digits run across the picture side, in a main block of rows, an upside-down line at the top edge and two margin lines at the left. The address side is in plain script: tentatively *Fräulein M. Scheck in Neunkirchen*, with a street line ending in *-park* that was only partly read. The stamp is a German Reich 5 Pf. Germania, with a St. Johann postmark of 16.4.01 and a Neunkirchen arrival postmark of the same day. Both towns are in the Saar region, so German was expected.

No published decipherment was found or used, but no separate literature search was made beyond the portal page and this repository. All transcription and decipherment is by Claude Opus 5.5 on 2026-10-30; there was no earlier work on this number. The key is new here: no sister card in the repository uses it.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side (source/address-large.jpg)](../source/address-large.jpg)

## Method

The solver transcribed the digits by hand from enlarged crops of the original scan (work/hires/pc_hcp_27_pic.JPG). The pencil is faint and the portal's grey watermark crosses the middle of the card.

Reading ten digits as ten letters failed: it gives triple letters and too few signs. Two-digit and three-letter schemes failed too. The break came from the small dots, which are not random: 2 is nearly always followed by a dot, and `2.4` is frequent. Taking "digit plus dot" as a separate sign gave 20 signs. Then `5 2. 4` = *ich*, and the long words followed: *schreiben*, *Liebe*, *konnte*, *Sonntag*, *einverstanden*. Heavy, widely spaced dots and line ends separate the words. The first-pass transcription had many errors, which were corrected by rereading the signs at 5–8× magnification.

Final count: 2. occurs 15 times, always before 4 (CH), and plain 2 occurs three times, always as F.

## Key

Monoalphabetic substitution with 20 signs: each digit plain or followed by a small dot.

| Digit | Plain sign | Dotted sign |
|---|---|---|
| 0 | M | A |
| 1 | E | B/V |
| 2 | F | C |
| 3 | G | D |
| 4 | H | P |
| 5 | I | Z |
| 6 | K | R |
| 7 | L | S |
| 8 | N | T |
| 9 | O/Ö | U/Ü |

B and V share a sign. Umlauts are not marked. J, Q, W, X and Y do not occur on the card. The plain signs run E–I, K, L and N, O in digit order, and the dotted signs run A–D and R–U, which supports the key independently of the text. Z standing where Q would be expected is an oddity.

## Plaintext

Reading order: the main block from top to bottom, then the upside-down top line (T16), then the margin lines (M17).

Digits as transcribed, one row per line. `|` separates words, a dot belongs to the digit before it, `~` marks a doubtful sign, and `a=b` means the card has a but the text reads b.

```text
R01: 0 5 6. | 7 5 1 1. 1 | 0 5 6.
R02: 8.~ 1 5 7 | 5 2. 4 | 0 5 8. | 3. 5 6.
R03: 3. 1~ 5 8 1 8 | 7. 2. 4 0 1 6. 5.~
R04: 2 9. 4 7 1 | 6 9 8 8 8. 1
R05: 5 2.~ 4 | 8 9.~ 6. | 0. 9. 2
R06: 3. 1 6. | 7.~ 8. 1~ 7 7 1
R07: 0. 7 7 1 7. | 0. 8 3. 1 6. 8
R08: 3. 1~ 8 | 4. 7 0. 8 | 2 9. 6. | 7. 9 8 8 8. 0. 3
R09: 8. 1 5 7 1 | 5 2. 4 | 3. 5 6. | 8 9 2. 4
R10: 0 5 8. | 9. 8 3. | 7. 2. 4 6. 1 5 1. 1 | 0 5 6.
R11: 9 1.~ | 3. 9. | 1 5 8 1. 1 6. 7. 8. 0. 8 3. 1 8 | 1. 5 7. 8.
R12: 3. 0.~ | 5 2. 4 | 3 1~ 7.~ 8.~ 1~ 6.~ 8 | 0. 1.~ 1 8 3. | 7. 4. 0. 8.
R13: 8 0. 2.~ 4 | 4 0. 9.~ 7.~ 1 | 6 0. 0 | 6 9 8 8 8. 1 | 5 2. 4 | 3. 5 6.
R14: 8 9 2. 4 | 8 5 2. 4 8. | 1 4 1 6. | 7.~ 2.~ 4~ 6.~ 1 5 1. 1 8 | 0 5 8. | 4 1 6. 5.~
R15: 7 5 2. 4 1 0 | 6 9. 7.~ | 1.~ 1 6. 1. 7~ 1 5 1. 8. | 3. 1 5 8 | 3. 5 2. 4 | 8 5~ 1~
T16: 1.~ 1 6. 7~ 0. 7. 7. 1 8 3. 1 6. | 0. 9. 3 9. 7.~ 8.~
M17: 3. 0. 7. | 7. 2. 4 6. 1 5 1. 1 8 | 3.=3~ 5 8~ 3.=3~ | 5 8 | 1 5 7 1
```

German, normalised (punctuation is editorial, because the cipher has none):

```text
Mir, liebe Mir!
Teil ich mit dir deinen Schmerz, fühle, könnte ich nur auf der Stelle alles ändern,
den Plan für Sonntag teile ich dir noch mit, und schreibe mir, ob du einverstanden bist.
Da ich gestern Abend spät nach Hause kam, konnte ich dir noch nicht eher schreiben.
Mit herzlichem Kuß verbleibt dein dich nie verlassender August.
[margin] Das Schreiben ging in Eile.
```

**English:** Mir, dear Mir! I share your pain with you, I feel it; if only I could change everything on the spot. I will still let you know the plan for Sunday, and write to me whether you agree. Since I got home late yesterday evening, I could not write to you any sooner. With a heartfelt kiss I remain your August, who will never leave you. [Margin] This was written in haste.

**Slovensky:** Mir, milá Mir! Delím sa s tebou o tvoju bolesť, cítim ju; keby som len mohol hneď na mieste všetko zmeniť. Plán na nedeľu ti ešte oznámim a napíš mi, či súhlasíš. Keďže som včera večer prišiel domov neskoro, nemohol som ti napísať skôr. So srdečným bozkom ostáva tvoj August, ktorý ťa nikdy neopustí. [Na okraji] Písané v zhone.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1346/work/decode.py
```

The script checks the hashes of the source files, decodes work/transcription.txt with work/key.json and prints the text with the first letter of each shared sign (so *fuhle*, *berbleibt*). It ends with the emendation note and the line "290 signs, 36 marked ~, 2 emended, 0 unkeyed".

## Uncertainties

36 of the 290 signs carry `~`: their shape or dot cannot be settled from the pixels alone.

- **`ging` (M17) is an emendation and the weakest word.** Both 3s carry a low dot, so the card literally says DIND, which is no word. *Das Schreiben ging in Eile* needs G, so a writer's slip or stray dots is assumed. Plain 3 = G rests on *Sonntag*, *gestern* and *August*, and on the digit order.

![Margin lines with the word ging at the lower left: low dots under the first 3 and after the last 3 (review/work/m17b.png)](../review/work/m17b.png)

- **`nie` (end of R15)** at first sight looks like `8 3 7`. It is read `8 5 1`, because this writer's 5 usually has a long top bar running over the next sign, and the last sign lacks the hooked head and crossbar of this writer's 7. A short gap remains between the stem and the bar. The phrase *dich nie verlassender* confirms the reading.
- **Similar digits.** The 2 and 9 are confused in places (*ich* in R05, *nach* in R13). The writer's flagged 1 can resemble 4 or 7. The first sign of *Teil* (R02), on the watermark edge, rests on context and on the clear 8. in R09.
- **Watermark.** In *schreiben* (R14) and *gestern* (R12) several signs lie on or beside the watermark.
- **Z = dotted 5** rests on two cases (*Schmerz*, *herz-*), each with a dot at a line end that could be taken for a divider. Plain 5 would give *Schmeri*, *heri*.
- **Faint dots** in *Hause*, *Da*, *abend*, *Kuß*, *verbleibt* and *August*: the letters there rest on the word, not on a visible dot.
- **The name "Mir"** is read clearly twice. That it is a pet name of the addressee M. Scheck is a guess. The sender's identity is known only from the signature *August*.
- **Interpretation.** *fühle* could belong to either neighbouring clause. *konnte* and *könnte* are not distinguished by the cipher: R04 is taken as subjunctive, R13 as past.
- **Not read:** the full street line of the address.

## Review summary

An independent Claude Opus 5.5 reviewer tried to refute the solution. It ran the decoder, wrote its own decoder with a separately typed key (same text), compared every row with 3× crops of the original scan and the weak words at 6–12×, and found no alternative key or text. Verdict: **REVISE**. The six findings and what changed:

1. Major: the two dots on the 3s of `ging` were not disclosed. Now recorded as an emendation in the transcription and printed by the decoder.
2. Minor: first sign of *Teil* now marked doubtful.
3. Minor: V of *verbleibt* now marked doubtful.
4. Minor: uneven doubt marking fixed (*nach*, *gestern*), and the 2/9 confusion is described as general. The count rose from 30 to 36.
5. Minor: the note on `nie` restated with the pixel argument; the solver keeps the reservation about the gap by the top bar.
6. Minor: the stale statistic on 2 was recounted.

The decoded text did not change.

## Sources

- HC Portal record 1346: https://crypto.hcportal.eu/dashboard/cryptograms/1346 (metadata, picture side and address side, captured 2026-10-30).
- Details of the working files: SOURCES.md, NOTES.md, SOLUTION.md and review/REVIEW1.md in the cipher directory.

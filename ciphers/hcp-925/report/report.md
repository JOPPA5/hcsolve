# HCP 925 (cpc_1903-05-03_DE_Wollstein_DE_Volsheim_): birthday wishes in numbers from Kätchen to Heinrich

Human solver: Tomáš Pavuk

**Status: deciphered in full (140 number groups, all decoded with one key); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 925 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/925), portal name cpc_1903-05-03_DE_Wollstein_DE_Volsheim_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Heinrich Lechtahler, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166) as its general reference.

The card is an embossed greeting card with forget-me-nots, lilies of the valley and the printed heading **"Der Ferne ein Gruss"** ("A greeting to the distant one"), with a printed love verse in the lower left corner. The whole message is written on the picture side as rows of numbers separated by dots.

The address side is in plain German writing: **S. H. Heinrich Lechtahler, Wohlgeboren, Volxheim in Rh.**, followed by one more Kurrent word (see Uncertainties). Volxheim is a village in Rheinhessen (then Grand Duchy of Hesse, today Rhineland-Palatinate). The card carries a 5-Pfennig Germania stamp "Deutsches Reich" (issued from 1902). The postmark shows "W..." at the left of the ring, the date 3 and month 5 in the centre, and "...HESS..." at the bottom; with the address and the portal file name (1903-05-03, "Wollstein") this points to **Wöllstein (Rheinhessen)**, the village next to Volxheim, on **3 May 1903**. The town name itself is not fully legible, so this is an inference.

![Picture side: the number rows under "Der Ferne ein Gruss" (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Heinrich Lechtahler, Volxheim in Rheinhessen; Germania stamp with the postmark (source/address-large.jpg)](../source/address-large.jpg)

![Postmark at higher resolution: "W..." at the left, "...HESS..." at the bottom of the ring (work/crops/postmark_hr.png)](../work/crops/postmark_hr.png)

## Method

There was no portal transcription. The solver (Claude Opus 5.5) read every row from the un-converted original scan (work/hires/), enlarging each row 2.5 to 3 times (crops in work/crops/), and wrote the numbers into work/transcription.txt. The rows contain only the numbers 1 to 25, of which 15, 16, 21, 23 and 24 do not occur. Three short rows near the end, 18.5.13.4.5.19 / 4.5.9.13 / 11.9.5.2.11.9.13.7, stand on their own like a closing formula; read as alphabet positions they give SENDET / DEIN / LIEBLING ("sends your darling"), and the same key then reads every other group on the card. Whether J is counted was settled by the text itself: K is 10 (GEDANKE, KATCHEN), W is 22 (ERWACHTE) and Z is 25 (ZUM), so the alphabet has 25 letters without J.

The difficult signs were compared with other occurrences of the same digit in the same hand: the writer's 17 ("1" plus a curled 7) against 19 ("1" plus a looped 9), 14 (crossed 4) against 19, and 12 against 17 in the signature. The command below checks the scan hashes and decodes the whole transcription.

In review, a separate Claude Opus 5.5 agent made its own crops of every row, wrote its own transcription and its own key into review/work/indep_decode.py, and decoded it. Its reading of all 140 groups is digit-for-digit identical to the solver's.

## Key

Simple monoalphabetic substitution by alphabet position (register type MASC), J omitted:

| Plain | No. | Plain | No. | Plain | No. | Plain | No. | Plain | No. |
|---|---|---|---|---|---|---|---|---|---|
| A | 1 | F | 6 | L | 11 | Q | 16 | V | 21 |
| B | 2 | G | 7 | M | 12 | R | 17 | W | 22 |
| C | 3 | H | 8 | N | 13 | S | 18 | X | 23 |
| D | 4 | I | 9 | O | 14 | T | 19 | Y | 24 |
| E | 5 | K | 10 | P | 15 | U | 20 | Z | 25 |

No word dividers are used; umlauts are written without dots (U for Ü, A for Ä).

## Plaintext

Transcription row by row (the circled group stands under the end of the first long row and continues it; "1|3" marks two digits written together without a dot):

```text
25.20.12.7.5.2.20.19.18.19.1.7.5
1.11.18.9.3.8.8.5.20.19.5.6.17.20.8.5.17.20.8.5.17.22.1|3   (circled) 8.19.5
20.13.4.1.13.12.5.9.13.5.13.11.9.5.2.11.9.13.7.4.1.3.8.19.5
6.9.5.11.12.9.17.4.5.17.7.5.4.1.13.10.5.5.9.13
8.5.20.19.12.20.18.18.5.9.13.7.5.2.20.19.18.19.1.7.18.5.9.13
18.5.13.4.5.19
4.5.9.13
11.9.5.2.11.9.13.7
10.1.19.3.8.5.13.8.14.19.19.20.12
```

Literal decoding:

```text
ZUMGEBUTSTAGE
ALSICHHEUTEFRUHERUHERWAC + HTE
UNDANMEINENLIEBLINGDACHTE
FIELMIRDERGEDANKEEIN
HEUTMUSSEINGEBUTSTAGSEIN
SENDET
DEIN
LIEBLING
KATCHENHOTTUM
```

German, word-divided and normalised (the R of Geburtstag and the deletion of the repeated "uher" are editorial):

**Zum Geburtstage! Als ich heute früh erwachte und an meinen Liebling dachte, fiel mir der Gedanke ein: Heut muss ein Geburtstag sein. Sendet dein Liebling Kätchen Hottum.**

English translation: **For your birthday! When I woke up early this morning and thought of my darling, it occurred to me: today must be a birthday. Sent by your darling Kätchen Hottum.**

Slovak translation: **K narodeninám! Keď som sa dnes ráno zobudila a myslela na svojho miláčika, prišlo mi na um: dnes musia byť narodeniny. Posiela tvoj miláčik Kätchen Hottum.**

The message is a short, playful birthday greeting from a sweetheart, signed Kätchen (Käthchen, a pet form of Katharina), and fits the sentimental card and its printed verse. The Slovak uses feminine verb forms because the sender is a woman.

## Uncertainties

- **GEBUTSTAG, twice.** Both times the sign after U is 19 (T), clearly a "1" with a looped 9, not the writer's 17 (R). The writer left out the R twice (or wrote T for it); the reading Geburtstag rests on word sense. Solver and reviewer agree on the digits.
- **FRUHERUHERWAC.** The digits 6.17.20.8.5.17.20.8.5.17.22 are clear; the group UHER is written twice. The sense is "früh erwachte" (or "früher erwachte" with a stray UH); only the emendation rests on word sense, the meaning is the same either way.
- **1|3 at the end of the first long row.** The last two digits are written joined. Read as 1.3 (A, C) because 13 (N) would give ERWN, while A C plus the circled 8.19.5 (HTE) gives ERWACHTE. This rests on word sense.
- **The circled group** 8.19.5 is taken as the continuation of the full first row (no room was left on the line).
- **DACHTE and the signature.** The 8 in DACHTE is heavily retraced but is an 8; the 14 (O) in HOTTUM is the writer's crossed 4 and is distinct from 19; the final sign is 12 (M) with a long tail, not 17. The surname is reported literally as Hottum; neither Kätchen Hottum nor Heinrich Lechtahler was looked up in records. "Lechtahler" follows the portal and agrees with the address.
- **Address side.** Before "Heinrich" stand two looped capitals, read "S. H." or "Sr. H.", evidently an honorific of the "Herrn" kind whose exact expansion is uncertain. The last Kurrent word under "in Rh." has a looped descender and a final ß-shape; "Rheinheß." (Rheinhessen written out) is a possible reading, but it is not secure and is left unread. This single address word does not affect the message.
- **Postmark.** Wöllstein (Rheinhessen) is inferred from the visible "W..." and "...HESS..." and the neighbouring address; the full town name is not legible.
- **Under the stamp.** Both sides were searched for hidden, reversed, tiny or edge writing (stamp box, margins, the printed verse, the picture); none was found. The stamp is still on the card, so nothing under it can be seen on the scans and a hidden note there cannot be excluded. The cipher type is therefore given as MASC, not MASC + Steganography.

![Last address word, not securely read (work/crops/addr_low_hr.png)](../work/crops/addr_low_hr.png)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-925/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two portal scans and the two un-converted originals, decodes work/transcription.txt with the alphabet-position key (J omitted), and prints every row with its decoding and the full letter string. It does not read the images; the transcription is manual and was confirmed independently in review.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), read every row itself from its own crops at up to 4x, and decoded its own transcription with its own key; all 140 groups matched digit for digit, and every group decodes with no second meaning needed. It confirmed on the pixels the 19 in both GEBUTSTAG, the joined 1|3, the circled HTE, the 8 of DACHTE and the 14 and final 12 of the signature, judged the German fluent and period-typical, and found no hidden writing and no sign of a borrowed solution. Its four findings were minor:

- **Unread address word.** A high-resolution crop was added and a tentative reading given; the word stays marked as unread.
- **Postmark.** The visible "...HESS..." at the bottom of the ring is now cited in support of Wöllstein (Rheinhessen).
- **Address abbreviation.** The "S. H." before Heinrich is now given as written instead of being rendered "Herrn".
- **Cipher type and stamp.** Type MASC confirmed; this report states that the area under the stamp could not be inspected.

No decoded letter changed as a result of the review. Transcription, key reconstruction, decipherment, response to review and this report are by Claude Opus 5.5; there was no earlier GPT work on this card.

## Sources

- HC Portal record 925, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/925 (source/metadata.md; download URLs of the scans in SOURCES.md).
- Picture side and address side: source/picture-large.jpg, source/address-large.jpg; un-converted originals in work/hires/.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card. A short web search found no published solution.

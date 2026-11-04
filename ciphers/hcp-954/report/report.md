# HCP 954 (cpc_1902-07-06_DE_Heide_DE_Jever_martha-03): a number-cipher love card from Carl to Martha Ihnken

Human solver: Tomáš Pavuk

**Status: deciphered in full (140 of 140 cipher numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 954 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/954), portal name cpc_1902-07-06_DE_Heide_DE_Jever_martha-03, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Martha Ihnken, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). A short web search found no published solution of this card.

The picture side is a printed colour card with a yellow rose and a river landscape (publisher number 2832). The message is written over it in pencil, in twelve lines of numbers separated by slashes and dots.

The address side is in plain German Kurrent handwriting: **Fräulein Martha Ihnken, bei Frau Wwe. Ihnken, Jever (Oldenburg)**, with a street line (apparently "...Elisabeth...") partly hidden under the HCPortal watermark. It carries a green 5-Pfennig Germania stamp cancelled HEIDE 6.7.02 (Heide in Holstein, 6 July 1902) and an arrival postmark of 7.7.02. The street line is not part of the message.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Fräulein Martha Ihnken, Jever (Oldenburg); stamp cancelled HEIDE 6.7.02 (source/address-large.jpg)](../source/address-large.jpg)

**Hidden writing.** In this collection messages are often hidden under the stamp (for example on nearly every card of the Jolánka series). On this card the stamp is still attached; no marks come out from under its edges, and no writing is visible along the card edges or in the picture other than the number message. What may lie under the stamp cannot be checked from a scan. The card is therefore classified as plain number substitution (MASC), not MASC + Steganography.

## Method

The solver (Claude Opus 5.5) read all twelve pencil lines by hand from enlarged crops of the full-resolution original scan (work/hires/, crops in work/crops/), and wrote the reading to work/transcription.txt. No OCR was used. The first test was the group "9 3 8", which occurs four times: under A=1, B=2, ... it reads ICH ("I"), with 4 9 3 8 = DICH and 12 9 3 8 = MICH. K comes out as 10, not 11, which shows that the alphabet omits J. With that key every number on the card decodes into connected German, and the slashes drawn on the card fall exactly at the word boundaries.

There was no earlier work on this number; all transcription and decipherment are by Claude Opus 5.5. In review, a separate Claude Opus 5.5 agent made its own crops, transcribed all twelve lines independently and decoded them with its own script (review/work/indep_decode.py). Its 140 numbers matched the solver's exactly.

![Lines 1-2 of the pencil message (review crop)](../review/work/c_top.png)

![Lines 7-9: BRIEF HAST DU DOCH ERHALTEN? (review crop)](../review/work/c_mid.png)

## Key

Simple monoalphabetic number substitution: each letter is replaced by its position in a 25-letter alphabet without J.

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Writing conventions on this card:

- Ü is written as 20 with two dots above it (FÜR, GRÜSZE).
- ß is written as SZ (18 25).
- Slashes divide words; dots between numbers are separators with no letter value.
- The writer's figure 4 sometimes looks like an "x" (in DOCH, line 8, and FREUNDLICHE, line 9).

Values used on the card: 1-14, 17-20, 22, 25. There is no unused or conflicting value.

## Plaintext

Transcription and decipherment, line by line as on the card ("20u" = 20 with umlaut dots):

```text
L01 2 5 . 18 . 19 5 13 / 4 1 . 13 . 10 . / 6 . 20u 17 / 4 5
    BE.S.TEN / DA.N.K. / F.ÜR / DE
L02 9 13 5 / 11 . 9 5 2 5 13 / 10 1 17 19 5 13 /
    INE / L.IEBEN / KARTEN /
L03 22 9 5 / 18 5 8 13 5 / 9 3 8 . / 12 9 . 3 8
    WIE / SEHNE / ICH. / MI.CH
L04 25 20 / 4 9 . 17 / 12 5 9 13 5 / 7 20 19 5 / 12 .
    ZU / DI.R / MEINE / GUTE / M.
L05 9 . 3 8 / 11 9 5 2 5 / 4 9 3 8 / 4 . 14 3 8
    I.CH / LIEBE / DICH / D.OCH
L06 18 . 14 / 18 5 8 17 . 12 5 9 13 5 13
    S.O / SEHR.MEINEN
L07 2 . 17 9 5 6 . / 8 1 18 19 / 4 20 /
    B.RIEF. / HAST / DU /
L08 4 14 3 8 / 5 17 8 1 11 19 5 13 ?
    DOCH / ERHALTEN?
L09 6 17 5 20 13 4 11 9 3 8 5 /
    FREUNDLICHE /
L10 7 17 20u 18 25 5
    GRÜSZE
L11 5 22 9 7
    EWIG
L12 4 5 9 13 3 1 17 11
    DEINCARL
```

German, with normal punctuation:

**Besten Dank für deine lieben Karten. Wie sehne ich mich zu dir, meine gute M.! Ich liebe dich doch so sehr. Meinen Brief hast du doch erhalten? Freundliche Grüße [written GRÜSZE], ewig dein Carl.**

English translation: **Many thanks for your dear cards. How I long for you, my good M.! I love you so very much. You did get my letter, didn't you? Kind regards, forever your Carl.**

Slovak translation: **Srdečná vďaka za tvoje milé pohľadnice. Ako veľmi po tebe túžim, moja dobrá M.! Veď ťa tak veľmi ľúbim. Môj list si predsa dostala? Priateľské pozdravy, navždy tvoj Carl.**

"M." is most likely the initial of the addressee, Martha. The sender signs as Carl; his surname is not known.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-954/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans, decodes work/transcription.txt with the key above, prints the line-by-line decipherment and the letter stream, and checks that the word division of the plaintext reproduces the stream exactly. It does not read the image; the transcription is manual and was confirmed independently in review.

## Uncertainties

- **GRÜSZE (line 10).** "7 17 20u 18" are clear. The next figure, 25, has a faint 5 standing on the edge of a printed leaf, followed by a darker 5 whose top stroke runs on into a slash. Reading 18 25 5 = SZE (sz for ß) is the only reading that gives a word; "18 2 5" would give SBE. The faint second figure of 25 is the one sign whose reading rests on word sense.
- **HAST (line 7).** The first figure is a tall, angular 8 with an open top (similar to the 8 of "18" next to it). 8 = H gives "hast"; 11 (L, "last") fits neither the shape nor the sentence.
- **DOCH (line 8).** Written "4 1x 3 8": the x-shaped sign is this writer's 4 (as in FREUNDLICHE), and the 3 is written over another figure. The word is clear from the sentence and from the other DOCH in line 5.
- **"M."** is read as Martha's initial; the cipher value M is clear.
- **DEIN CARL** has no slash between the two words; the division is by sense.
- **Under the stamp.** The stamp is attached; nothing under it can be inspected from the scan.
- The street line of the address is partly illegible under the watermark; it is plain writing, not cipher.

## Review summary and changes

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, transcribed and decoded the card independently with an identical result (140 numbers, same letter stream), checked the hard spots sign by sign on the hi-res scan, and confirmed the language, context and translations. Verdict: **ACCEPT**, with four minor findings:

1. The solution stated 147 numbers; the correct count is 140. Corrected.
2. The question mark stands at the end of line 8 (ERHALTEN?), not at the end of line 7. Moved in the transcription; the decoded letters are unchanged.
3. Hidden writing under the stamp: the stamp is attached, so this cannot be checked; nothing hidden is visible elsewhere. The type stays MASC, and this report says so.
4. The faint second figure of 25 in GRÜSZE is disclosed as the one call resting on word sense. Kept.

# HCP 974: a spa patient's health report from Bad Brückenau to Emma Krumbholz, Heidelberg

Human solver: Tomáš Pavuk

**Status: deciphered in full (116 of 116 letter signs: 76 digit cipher signs and 40 plain letters); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 974 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/974), portal name cpc_--27_DE_Bruckenau_DE_Heidelberg_heidelberg-03, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Emma Kr", with no transcription or solution attached.

It is a picture postcard "Bad Brückenau, Kgl. Kurhaus" (the Royal Spa House at Bad Brückenau in Lower Franconia, Bavaria), published by Hans Brust, Brückenau ("Malerische Motive No. 7", print code 09 27113). The address side is written in plain German Kurrent: **Frau Emma Krumbholz, Heidelberg, Mittelstr. 18** (the surname and street are a reading of the handwriting; the portal gives only "Emma Kr"). The stamp has been lost; only the BRÜCKENAU BAD postmark is left, with the day "27" legible but not the month or year. The publisher's print code "09" suggests c. 1909, but that is an estimate only.

The message is written sideways in ten lines on the left half of the address side, in a mixture of digits and Latin cursive letters. A collector's number "3" appears on both sides, and a few faint later pencil letters (an earlier decoding attempt, for example "e u n" above line 3) are not part of the message.

![Picture side: Bad Brückenau, Kgl. Kurhaus (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Frau Emma Krumbholz, Heidelberg, Mittelstr. 18; the cipher message is on the left half (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright, from the high-resolution scan (work/crops/msg_rot.png)](../work/crops/msg_rot.png)

**Stamp box and picture side.** Some postcard series hide a second (plain or enciphered) message under the stamp, so both solver and reviewer looked for one. The stamp is gone; an enhanced crop of the stamp box shows only glue stains and the postmark, with no writing. The picture side carries only the printed caption and the collector's "3". No steganographic part was found, so the cipher type is plain MASC. What was written under the lost stamp, if anything, can no longer be checked.

## Method

The transcription is manual, from the un-converted high-resolution scan of the address side, turned upright and read line by line on enlarged crops. No OCR was used.

The key was found from a crib. The group K23828 at the start of line 7 has the shape of "keinen" (K, then e i n e n), giving 2 = e, 3 = i, 8 = n. Then 30T = "ist", Z50T18D = "Zustand" (5 = u, 0 = s, 1 = a), D29 = "der" (9 = r), 72H9 = "mehr" (7 = m), 749G28 = "Morgen" (4 = o) and H26 = "hel(l)" (6 = l). These ten digits give a regular pattern: the five vowels a e i o u are 1 to 5, and the consonants l m n r s are 6 to 0, in alphabetical order. Every other letter is written plain.

Two pairs of shapes needed care. The digit 7 (= m) and the plain capital F are both crossed long strokes; the F has a curled J-shaped tail at the foot (in "fast" and "findet"), the 7 has none (in "mein", "mehr", "Morgen", "Samstag", "nachmitag"). The sign before H in line 10 is discussed under Uncertainties.

In review, the reviewer rotated the scan itself, wrote down all ten lines from its own reading before comparing, derived the key from the cribs on its own, and decoded with its own script. Its transcription agreed with the solver's sign for sign.

## Key

Partial monoalphabetic substitution: ten letters are replaced by digits, the rest are written as plain Latin letters.

| Digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Plain | a | e | i | o | u | l | m | n | r | s |

All ten digits occur, each always with the same value. The letters a e i o u l m n r s never occur in plain on this card, and the plain letters used are only b c d f g h k t w z, so the split between cipher digits and plain letters holds across the whole message. Frequency of the digits (76 in all): 1:10, 2:20, 3:10, 4:1, 5:2, 6:1, 7:5, 8:10, 9:7, 0:10.

The writer writes doubled letters only once (gebesert, Eiweis, Waser, hel, nachmitag); this is a habit of the writer, visible in the ciphertext itself, not a decoding gap.

## Plaintext

Ciphertext as transcribed, line by line (digits are cipher signs, capitals are plain letters; " is the writer's continuation mark):

```text
L01 7238 Z50T18D 30T
L02 B2D25T28D G2
L03 B2029T. 23W230
L04 30T F10T G18Z
L05 W2G. 23T29 F38"
L06 D2T D29 19ZT
L07 K23828 72H9.
L08 W1029 30T G18Z
L09 H26! 749G28- 0170"
L10 T1G 81CH73T1G-
```

Decoded, line by line:

```text
L01 mein zustand ist
L02 bedeutend ge
L03 besert. eiweis
L04 ist fast ganz
L05 weg. eiter fin"
L06 det der arzt
L07 keinen mehr.
L08 waser ist ganz
L09 hel! morgen- sams"
L10 tag nachmitag-
```

German, normalised: Mein Zustand ist bedeutend gebessert. Eiweiß ist fast ganz weg. Eiter findet der Arzt keinen mehr. Wasser ist ganz hell! Morgen – Samstag Nachmittag –

English: My condition has improved considerably. The albumin is almost completely gone. The doctor finds no more pus. The urine ("water") is quite clear! Tomorrow – Saturday afternoon –

Slovak: Môj stav sa výrazne zlepšil. Bielkovina je takmer úplne preč. Hnis už lekár nenachádza. Moč („voda") je celkom čistý! Zajtra – v sobotu popoludní –

Notes on the reading:

- The text is a patient's report on a cure: albumin (Eiweiß) in the urine almost gone, no more pus, the urine clear. Bad Brückenau was a spa known for treating kidney and bladder complaints, which fits the picture of its Kurhaus.
- "Wasser" here means the urine, as is usual in German medical talk of the time.
- The message ends with a dash after "nachmitag". The sentence, presumably announcing an arrival or visit on Saturday afternoon, was left unfinished by the writer; nothing is lost at the card edge.
- Line 2 ends with "ge" and line 3 continues "besert" without a continuation mark; in lines 5 and 9 the writer uses " for the break.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-974/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two portal images and the two high-resolution originals, then decodes the manual transcription in work/transcription.txt with the key above and prints the ten decoded lines. It does not read the images; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **The C in "nach" (line 10), read from word sense.** The sign after "81" has a small lower-left loop that runs into a C-like body; it could be taken for a 6 joined to something. Read as 6 (= l) it would give "nalh", which is not German. Read as a looped Latin capital C it gives "nach", which fits "Samstag Nachmittag". This one sign is read from sense, not from its shape alone. Solver and reviewer agree on it.
- **7 versus F.** Distinguished on the pixels (F has a J-shaped tail, 7 has none) and consistent with sense in every case.
- **Ink blot in line 8.** A large blot sits on the 0 of "30T"; the 3 and the T are clear and the word "ist" recurs twice elsewhere, so the reading is safe.
- **Date.** Only the day "27" of the postmark is legible. "c. 1909" is an estimate from the publisher's print code "09", not a reading of the postmark.
- **Names.** The sender did not sign. The recipient's surname "Krumbholz" and the street "Mittelstr. 18" are readings of the plain Kurrent address, not ciphertext.
- **The lost stamp.** Nothing is written in the visible stamp box, but whatever may have been under the stamp is lost.
- A web search for the plaintext found no earlier publication of this card, and the portal attaches no solution.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), rotated the high-resolution scan itself, transcribed all ten lines independently and decoded them with its own script; its 116-sign transcription matched the solver's exactly. It confirmed the 7/F distinction on enlargements, the reading of the blotted "ist", the regular key covering every sign, and that the stamp box and the picture side carry no hidden writing. Its three findings were minor:

- **Sign count.** SOLUTION.md said "94 signs"; the correct count is 116 letter signs (76 digits and 40 plain letters). Fixed.
- **C in "nach".** Kept as an uncertainty that rests on word sense, as stated above.
- **Date.** Given only as an estimate (c. 1909), as above.

No decoded letter changed as a result of the review. Transcription, key reconstruction and decipherment were done by Claude Opus 5.5; there was no earlier work on this card.

## Sources

- HC Portal record 974, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/974 (source/metadata.md).
- Picture side and address side images from the portal (source/picture-large.jpg, source/address-large.jpg) and their high-resolution originals (work/hires/), as listed in SOURCES.md.
- Collection reference given on the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.

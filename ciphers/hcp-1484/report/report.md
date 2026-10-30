# HCP 1484 (pc_hcp_165): an English love note to Colwyn Bay in a stroke-and-shape cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (177 of 177 cipher signs; one extra faint sign noted separately); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1484 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1484), portal name pc_hcp_165, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1908-01-30, language Unknown, location Europe, sender Unknown, recipient "J. Willams", with no transcription or solution attached.

The picture side is a printed comic card of the series "Pictorial Comedy" (James Henderson & Sons, London) titled "The turning of the Tide", showing a kissing couple. It carries no cipher writing, only the printed caption and the portal watermark.

The cipher text is on the address side, to the left of the address. The address is in ordinary handwriting and reads, as far as the scan allows, **Miss G. Williams, "Baron Hill", York Road, Colwyn Bay, N. Wales**. (The portal metadata gives "Bowntree" and "Oak Road" as provisional readings; "Baron Hill" and "York Road" fit the scan better. The address was not used as a crib.)

The whole message is written **upside down** relative to the printed card: only after turning the card through 180 degrees do the question marks, commas and quotation marks take their normal shape. In that orientation the text stands in ten lines.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned through 180 degrees: the cipher message in its reading orientation (work/rot180.png)](../work/rot180.png)

## Method

The setup on 2026-10-26 (capturing the three portal tabs, downloading both images, a triage note) was done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), which made no transcription or decipherment. The transcription, identification of the system, key and plaintext are by Claude Opus 5.5 (2026-10-29).

1. **Transcription.** The card was turned 180 degrees and every line cut into enlarged crops (10–16×, nearest-neighbour). Each sign was recorded in a descriptive notation (shape name for vowel signs; side, anchor and bar count for stem signs) in work/transcription.txt. No OCR was used and the portal supplied no transcription.
2. **First break.** A provisional first transcription with rough sign classes was attacked by hill-climbing with English quadgram statistics. It produced fragments such as "…THAN… YOU EVER", "IN THE MORNING" and "TO HEAR EVEN BETTER", which fixed several letters and showed that the text was English.
3. **Structure of the alphabet.** With these letters known, the construction of the sign alphabet became clear (see Key): the consonants follow the alphabet in a strict 6 × 3 grid. The first draft had merged the 2-bar and 3-bar variants of several signs (C/D, N/P, R/S), which is why the hill-climb output was partly garbled. Every stem was then re-read and its bars counted on the enlargements.
4. **Decoding.** The final transcription is decoded mechanically with the key in work/key.json by work/decode.py. Every one of the 177 signs maps to a letter; no sign is left over.

## Key

Monoalphabetic substitution with a home-made, systematically built sign alphabet. Word spaces are not written; ordinary punctuation is kept.

**Consonants** are a vertical stem with one to three short horizontal bars. The side of the bars (left, right, both) and whether they hang from the top of the stem or stand at its bottom give six groups; the number of bars gives the position within the group. Read in order, the eighteen signs are the consonants of the alphabet B C D F G H J K L M N P Q R S T V W:

| Bars on | hang from top: 1 / 2 / 3 bars | stand at bottom: 1 / 2 / 3 bars |
|---|---|---|
| left of stem | B / C / D | F / G / H |
| right of stem | (J) / K / L | M / N / P |
| both sides | (Q) / R / S | T / V / W |

**Vowels** are geometric shapes:

| Shape | Letter |
|---|---|
| circle with a central dot | A |
| triangle | E |
| triangle with an inner vertical stroke | I |
| empty square | O |
| square with a `\` diagonal | U |
| square with a `/` diagonal, often with an extra short stroke from the top-left corner | Y |

A **superscript "2"** after a sign doubles the letter. It occurs seven times, always on an English double letter: LITTLE, BETTER, LLANGOLLEN (twice), SHALL, HAPPY, ALL.

J and Q do not occur on this card; their signs are filled in from the pattern only. No signs for X and Z are attested.

## Plaintext

Literal decoded text, line for line as on the card (the bracketed sign is the faint sign discussed under Uncertainties; word division is editorial):

```text
MY OWN LITTLE DARLING,
THANK YOU EVER SO MUCH
FOR THE POSTCARD. I HOPE
TO HEAR EVEN BETTER NEWS
IN THE MORNING. WHY A
CARD OF LLANGOLLEN? SHALL
WE GO THERE TOGETHER, SOME
HAPPY DAY, [d] DARLING? I LOVE
YOU, "DEAREST-OF-ALL-THE-WORLD,"
YOUR BOY.
```

Normalised English: **My own little darling, thank you ever so much for the postcard. I hope to hear even better news in the morning. Why a card of Llangollen? Shall we go there together, some happy day, darling? I love you, "dearest-of-all-the-world". Your boy.** ("together" is underlined on the card.)

Slovak translation: **Môj vlastný malý miláčik, veľmi pekne ďakujem za pohľadnicu. Dúfam, že ráno sa dozviem ešte lepšie správy. Prečo pohľadnica z Llangollenu? Pôjdeme tam spolu niekedy v šťastný deň, miláčik? Ľúbim ťa, „najdrahšia na celom svete“. Tvoj chlapec.**

Notes on the reading:

- **Llangollen** is a town in the Dee valley in Denbighshire, North Wales, a well-known beauty spot about 50 km from Colwyn Bay; the addressee had evidently sent the writer a picture postcard of it.
- **"better news"** suggests the addressee had written about some worry and the writer hopes for an improvement by the morning; what it was is not known.
- The writer signs only **"your boy"**; his identity is not established.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1484/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the three files in source/, decodes work/transcription.txt with work/key.json (stopping on any unmapped sign), and prints the ten lines above followed by `177 signs, all mapped`. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **One faint sign.** In line 8, after "SOME HAPPY DAY,", there is a sign in much lighter ink, set lower than the line, with a curl below. Its visible strokes are a stem with three bars on the left at the top, i.e. the D-sign, and it is followed by a normal dark "DARLING". It is read as an abandoned start of "DARLING" (the pen ran dry, was re-inked and the word rewritten) and printed as `[d]`. It is too faint to rule out bars on both sides of the stem as well, so another reading is possible; it is **not counted as part of the message** (it is not among the 177 signs), and no reading of it changes the sense.
- **Signs touched by printed text.** The vertical printed line "Pictorial Comedy … James Henderson & Sons, London" crosses a few signs: the M of SOME, the E and V of LOVE and the D of WORLD. Each is still identifiable from its visible strokes (M: stem with one bar at the bottom right; E: a triangle under the printed "&"; D: three left-top bars); none was restored from context alone.
- **Word division and punctuation.** The writer left almost no spaces; word division is editorial. The punctuation, the hyphens in DEAREST-OF-ALL-THE-WORLD and the quotation marks around it are on the card.
- **J, Q, X, Z.** The signs for J and Q are inferred from the pattern; those for X and Z are unknown. None is needed for this text.
- **Address and persons.** The house name ("Baron Hill") and street ("York Road") are readings of ordinary handwriting and are not certain. The sender is not identified.

## Why the solution is believed correct

- All 177 signs on the card are transcribed and decoded; none is unmapped and none is left over.
- The key is a clean, regular design (an alphabetical 6 × 3 consonant grid plus six vowel shapes), not a table fitted sign by sign; the reviewer rebuilt it from the rule alone and got the same text.
- The text is fluent Edwardian English with content that fits the card: a love note to a young woman in Colwyn Bay, mentioning nearby Llangollen, on a card showing a kissing couple.
- Repeated words decode identically (DARLING twice, YOU twice plus YOUR, THE three times), and the doubling mark falls only on genuine English double letters.
- **Sister card.** HCP 1485 (pc_hcp_166), addressed to the same Miss G. Williams at the same address, was deciphered separately in this repository with the identical stroke-and-shape alphabet; it opens "Gwennie darling", which fits the initial G. Its review 1 verdict is ACCEPT, but it had not yet been closed when this report was written. Nothing on this card was derived from it; it is independent support for the key.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), wrote its own decoder that builds every consonant from the structural rule alone without reading the solver's key file (same 177-letter result), rotated the scan itself, cut every line into enlargements and read all signs independently; every word and line break agreed. It paid particular attention to the 2-bar/3-bar pairs (N/P, C/D, R/S, V/W), the separate C and H at the end of MUCH, the seven doubling marks and the signs crossed by printed text, and confirmed that the picture side has no cipher writing and that no published solution was used. Its three findings were minor and are reflected here:

- **Y glyph description.** The solution had described Y as a square "with a V from the two top corners". On the card Y is a square with a `/` diagonal (often with an extra stroke from the top-left corner) and U a square with a `\` diagonal, as on HCP 1485. The description of the key was corrected; the sign classes and the reading were already right.
- **Faint sign.** The report now says that the faint sign is too faint to rule out bars on both sides and that it is not counted as part of the text.
- **Sister-card corroboration.** HCP 1485 and its review status are now cited as independent support.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1484, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1484 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4513/conversions/pc_hcp_165_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4512/conversions/pc_hcp_165_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.

# HCP 1373 (pc_hcp_54): a Caesar-shifted love postcard of 4 November 1907

Human solver: Tomáš Pavuk

**Status: whole message read, 63 of 63 enciphered letters decoded with a single key; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1373 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1373), portal name pc_hcp_54, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-11-04, language Unknown, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a printed view, "Guildford Castle", with no handwriting. The address side carries a halfpenny Edward VII stamp and the postmark WIMBORNE / 10 PM / NO 4 / 07. It is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. The message is written sideways on the same side, so the scan must be turned 90° counter-clockwise to read it. 4 November 1907 was a Monday, which agrees with the plain heading "Monday".

The card belongs to a correspondence between one couple on the neighbouring HC Portal cards (hcp-1374 to 1385 from Wimborne, and hcp-1386 to 1407), in the same hand and with the same cipher. The heading number "No 1" fits "No. 3" on hcp-1376, dated Saturday 9 November. No published solution of this card was found or used.

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned to reading position (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is manual, with no OCR. The un-converted original scan of the address side was turned upright and every row was read from crops enlarged 3 to 6 times. The couple's closing formula, known from sister cards, showed a shift of one letter at once: `Nz Pxo E. L. Cpz ... Gspn Zpvs Pxo E. L. Hjsm` decodes to "My own E. L. boy ... from your own E. L. girl". That is a hypothesis taken from the family, and it was then tested on every enciphered word of this card.

The last word of row 4 resisted longest. THANK, VITAL, TRIAL and other candidates were tried and rejected, because none has a crossed t in second place. The word was settled when the writer's t on hcp-1376 (in `qptufe` and `Nztufsz`) proved to be a tall stroke with a flag running right, the same as the second sign here. This gives V-t-v-b-m, USUAL.

The reproduction command, run from the repository root, checks the source hashes, decodes every token and checks the inverse:

```sh
python3 -I ciphers/hcp-1373/work/decode.py
```

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Not enciphered: the heading "G. H. Monday", "No 1", the word "Friday" in the body, and the "&". The groups `E. L.` (twice) and `N. & L.` are the couple's abbreviations, kept literal as on the sister cards. Their shifted values would be D. K. and M. & K.

## Plaintext and translation

| Row | Ciphertext | Literal plaintext |
|---|---|---|
| heading | G. H. Monday. No 1 | plain writing |
| 1 | Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| 2 | J. bn. hpjoh. po. | I. AM. GOING. ON. |
| 3 | odjfmz. & bcpvu | NCIELY [= NICELY]. & ABOUT |
| 4 | Nz. Sppn. usz. Vtvbm | MY. ROOM. TRY. USUAL |
| 5 | gps. Friday. Nz. N. & | FOR. Friday. MY. [N. & |
| 6 | L. Gspn. Zpvs. Pxo. E. L. | L.] FROM. YOUR. OWN. [E. L.] |
| 7 | Hjsm | GIRL |

The plaintext language is English. Punctuation in the readings below is editorial.

> G. H. Monday. No. 1. My own E. L. boy. I am going on nicely & about my room. Try usual for Friday. My N. & L. from your own E. L. girl.

Slovak translation:

> G. H. pondelok. Č. 1. Môj vlastný E. L. chlapec. Darí sa mi pekne a chodím po svojej izbe. Skús to obvyklé na piatok. Moje N. & L. od tvojho vlastného E. L. dievčaťa.

## What remains uncertain

- **`odjfmz` = NCIELY, read as NICELY.** The signs stand in the order d, j, so the literal decode is NCIELY. This is taken as the writer's slip for `ojdfmz`. The decoder prints the literal form, and NICELY is an emendation.
- **`Vtvbm` = USUAL.** This is the hardest word on the card; the strokes are heavy and run together. A mark lost past the card edge cannot be fully excluded, but nothing suggests one.
- **Sense of "try usual for Friday".** The words are read, but the phrase is elliptical. It presumably refers to an arrangement known to the couple.
- **Sense of "about my room".** It is taken as "up and about in my room", that is, recovering. The card names no illness.
- **`Nz` in row 1.** The z is a short compressed stroke, weaker than on hcp-1376. MY here rests partly on the formula and on the fuller `Nz` of rows 4 and 5.
- **Abbreviations.** E. L., N. & L. and G. H. are not expanded, because nothing on the card proves an expansion.
- **Heading.** The first initial is printed G because of a small foot stroke, but C is not excluded and sister solutions divide. The sign after "No" is read as 1; an exclamation mark is possible.
- **Two deceptive shapes.** The P of `Pxo` (rows 1 and 6) has a very long flat bowl and looks like a T, but `Txo` is no word. The L opening row 6 has a top flag, unlike the plain L of `E. L.`

## Review and what changed

An independent review was made by a separate Claude Opus 5.5 agent. Solver and reviewer are the same model, so this was not a check across vendors. The reviewer re-ran the command, typed its own tokens from its own crops and decoded them with its own script, which gave the same 63 letters. It re-read every row and attempted to break NICELY and USUAL, and found that one shift covers all enciphered tokens. It also computed the weekday and checked the postmark and address. **Verdict: ACCEPT.**

There were four minor findings, all addressed, and no decoded letter changed:

1. The heading initial is now printed G, not C, with the doubt kept.
2. The description of the z in row 1 was weakened to what the scan shows.
3. The two deceptive shapes, P and flagged L, are now described.
4. USUAL is now flagged as the hardest word in the argument for correctness.

## Credits

Transcription, decipherment and this report by Claude Opus 5.5 on 2026-10-30, using the cipher and hand comparisons from accepted sister cards. No earlier work on this number exists.

# HCP 1371 (pc_hcp_52): an English Caesar love postcard from "Girl" to "Boy", 22 July 1907

Human solver: Tomáš Pavuk

**Status: message deciphered in full (46 of 46 shifted letters). Two short initial groups, N. L. and & Lt.., are reported literally and are not expanded. Independent review 1 verdict ACCEPT, with four minor findings and no change to any decoded letter.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1371 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1371), portal name pc_hcp_52. It belongs to the HCPortal collection of cryptographic postcards. When the record was captured on 2026-10-30, the portal listed it as **Not solved**: Postcard, HCPortal collection, category Substitution, date 1907-07-22, language Unknown, location Europe, sender Unknown, recipient "W. Abboú". No transcription or solution was attached. The solver found no published solution of this card; the search covered this repository and the AI Decipherment Register only.

The picture side is a printed view, **Crescent Gardens, Harrogate**, with no handwriting. The publisher's line on the address side reads Boots Cash Chemists, "Pelham" Series.

The cipher is on the address side, and the card is scanned sideways; turned 90° counter-clockwise it reads normally. The plain heading is **G. H. Monday** and the plain side note is **July 22nd -07**. 22 July 1907 was a Monday, so the two agree. The address reads **Mr. W. Abbott, Stokelake Farm, Chudleigh, Devon**. The portal's "Abboú" is kept unchanged in the metadata file. The halfpenny Edward VII stamp is postmarked ...ORNE, 10 PM, 22 JY 07. The start of the town name is worn or hidden; WIMBORNE is known only from sister cards.

The card belongs to the correspondence of one couple, 1907–08, addressed to W. Abbott (HCP 1386 to 1407 and related numbers), who write in the same Caesar shift and sign as "Boy" and "Girl". Several of those cards are deciphered in this repository. The key was taken from them as a hypothesis and then tested on this card. This is a known family key, not a new key recovery.

![Picture side: Crescent Gardens, Harrogate (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned upright: plain heading, five cipher lines, plain date (work/crops/reading.png)](../work/crops/reading.png)

## Method

The transcription is **manual**. The high-resolution address side was rotated, enlarged and read word by word, with no OCR. The portal supplied no transcription. The decoder then subtracts one from each letter, checks the round trip and checks the file hashes.

Two first rough readings were corrected on the enlargements, by rereading the shapes and not by changing the key. The second word of line 3 is `Mpwf`, and the end of the card is `Hjsm`, with a slash j and a flattened m.

To reproduce, run from the repository root:

```sh
python3 -I ciphers/hcp-1371/work/decode.py
```

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading and the side date are ordinary writing. No word on the card needs any adjustment to the shift.

## Plaintext

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| plain | G. H. Monday | (not enciphered) |
| 1 | Nz. Pxo N. L. Cpz | MY OWN [N. L.] BOY |
| 2 | Mfuufs up-Ebz. | LETTER TO-DAY. |
| 3 | "tqmfoeje" Mpwf | "SPLENDID" LOVE |
| 4 | & Lt.. Gspn. Zpvs | [& Lt..] FROM YOUR |
| 5 | Pxo. N. L. Hjsm | OWN [N. L.] GIRL |
| plain | July 22nd -07 | (not enciphered) |

46 enciphered letters are decoded by the one key; 6 letters of initial groups are kept literal.

**English:** G. H. Monday. My own N. L. Boy, letter to-day "splendid". Love & Lt.. from your own N. L. Girl. July 22nd 1907.

**Slovak:** G. H. pondelok. Môj vlastný N. L. chlapec, list dnes „skvelý“. Láska & Lt.. od tvojho vlastného N. L. dievčaťa. 22. júla 1907.

Punctuation in the sentences is editorial. The initial groups are left unexpanded in both versions.

## What remains uncertain

- **N. L. (lines 1 and 5).** An arched N, a short dash, and a slanted stem with a small foot. The closest parallel is the same slot on HCP 1402. It was first transcribed N. h., and h is not excluded because the foot is small. M or E for the first sign is not wholly excluded either. It is not established whether the group is enciphered, and no expansion is claimed.
- **& Lt.. (line 4).** This is the weakest reading on the card. The first sign is an open hooked V, read as an ampersand from its stroke direction and its slot; a plain V or an N is not excluded. The second is a looped L. The third is a small sign read as t, with c or r not excluded. If the group is enciphered it gives & Ks. Together with LOVE before it, and L. & K. on HCP 1395, the likely sense is "love & kisses". That is a hypothesis, not a reading, and the plaintext does not use it.
- **Signs settled partly by the word.** The o of `Pxo` in line 1 is a filled oval with no counter. The final e of `tqmfoeje` has no open eye and looks c-like, but c would give SPLENDIB. The j of the same word has no loop, and f would give SPLENDED. The capitals of `Mfuufs` and `Mpwf` are decided partly by METTER and NOVE not being words. In `Hjsm` the ink is pale and the m is flattened, and it looks like "2u".
- **Wording.** "Letter to-day 'splendid'" has no verb, and nothing is added.
- **Heading.** The initials could be C. H., as on HCP 1386, though the loop here reads as G. They are not part of the cipher.
- **Postmark and people.** The first letters of the town are not legible, and the writers are not identified.

Two hand-drawn lines are not ciphertext: one under "tqmfoeje", which looks like underlining of the quoted word, and one under line 5, running from the flourish of the date.

## Why the solution is believed correct

One fixed shift, with nothing tuned to this card, gives English for all 46 letters. A test of all 26 shifts gives English only at this one, on the whole text. The text includes the 8-letter SPLENDID, which is not one of the couple's stock formulae. The closing is the couple's formula, and the Monday heading agrees with the postmark date and the calendar.

## Review

An independent reviewer, a separate Claude Opus 5.5 agent, tried to refute the solution. It ran the decoder, wrote its own decoder from its own transcription, checked the file hashes, reread every word at 4× and the hardest at 8×, and checked the postmark, address, date and weekday. It reached the same 46 letters and returned **ACCEPT** with four minor findings, none of which changes a decoded letter:

1. The salutation group matches HCP 1402 sign for sign. It was changed from N. h. to N. L., with h still left open.
2. The support for & Lt.. was understated in one way and overstated in another. Only the stroke direction is shared with other ampersands, but the slot parallel is stronger than first stated. Both points were corrected, and r was added as an alternative for the third sign.
3. The c-like final e of `tqmfoeje` was not listed as an uncertainty. It now is.
4. The two pen lines were not recorded. They now are.

The reviewer could not verify the meaning or cipher status of the initial groups, the postmark town, or the writers' identity. It did no web search of its own.

## Credits

The decipherment was done by Claude Opus 5.5 as solver, 2026-10-30. No earlier work on this number exists. The key and comparison shapes come from sister-card work in this repository by an OpenAI GPT solver and by Claude Opus 5.5. Review was by a separate Claude Opus 5.5 agent.

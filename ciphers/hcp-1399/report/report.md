# HCP 1399 (pc_hcp_80): an Edwardian Caesar-shift postcard to Miss Dean

Human solver: Tomáš Pavuk

**Status: the message is deciphered in full (46 of 46 enciphered letters); two short groups of initials are reported literally and not expanded. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1399 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1399), portal name pc_hcp_80, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date and language unknown, location Europe, sender unknown, recipient Dean, with no transcription or solution attached.

The picture side is a printed view, "St. Philips Church & Monument, Birmingham" (Copyright F.F. & Co.), with no handwriting. All the writing is on the address side, which is scanned sideways; turned 90° counter-clockwise it reads, in plain writing, **Miss Dean, Queen's House (?), Wimborne, Dorset**. The house name is uncertain and is not part of the message.

The card carries a green halfpenny Edward VII stamp (in use 1902–1910). The postmark reads **7.30 PM / ?E 2 / 08**, with the lower arc of the office name ending **…N ABBOT** (Newton Abbot, Devon). Only the letter E of the month is clear; "FE" (February) fits, because **2 February 1908 was a Sunday**, and the message is headed in plain writing "S. 7. Sunday." This agreement is a consistency check, not an independent proof of the date.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Address side turned so that the message reads upright: the address at the top right, the message in seven lines at the lower right (work/reading.png)](../work/reading.png)

![Picture side, printed view of St Philip's, Birmingham (source/picture.jpg)](../source/picture.jpg)

The card belongs to a family of English cipher postcards in this repository, HCP 1386–1407, written in 1907–08 between a young woman and Mr W. Abbott of Chudleigh (near Newton Abbot), all in the same simple Caesar cipher and with the same formulas: "Nz Pxo" (MY OWN) at the start, "gspn Zpvs Pxo" (FROM YOUR OWN) at the end, and a group of initials with "&" before FROM. HCP 1400 is a second card to Miss Dean. This card was posted at Newton Abbot to Miss Dean at Wimborne, so it very probably goes from the Abbott side of the correspondence to the young woman (HCP 1407 was posted at Wimborne). This is context only; no letter of this card is read from it.

## Method

The transcription is **manual**, made from enlarged crops of the turned scan. The earlier solver (OpenAI GPT, GPT-6 Astra / GPT-6.1 Sol, 2026-10-26) captured the portal record and both images, took the Caesar −1 hypothesis from the related card HCP 1400, and confirmed it on the body of this card (MANY THANKS, FOR "SWEETS", THIS MORNING), but left the groups of initials undescribed and did not hand the card over. Claude Opus 5.5 (2026-10-29) re-read every word on 4–7× enlargements, transcribed the initial groups literally, read the postmark, and wrote the final transcription file and the decoding script.

All 26 Caesar shifts were tried; only a shift of one back gives language. Each enciphered word was decoded and re-encoded to check the round trip. The plain heading, the address and the two groups of initials were not shifted.

In review a separate Claude Opus 5.5 agent made its own rotation and 3–7× crops of the scan, transcribed the card itself without using the solver's file, and decoded it with its own script under all 26 shifts. It obtained the same 46 letters and the same plaintext.

## Key

Simple Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet (A as B, B as C, …, Z as A). To decrypt, shift every letter back by one:

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Line | Ciphertext (as written) | Plaintext |
|---|---|---|
| heading (plain) | S. 7. Sunday. | S. 7. Sunday. |
| salutation | Nz Pxo **E.h.** | MY OWN [E.h.] |
| 1 | Nboz uibolt | MANY THANKS |
| 2 | gps "Txffut" | FOR "SWEETS" |
| 3 | uijt npsojoh. | THIS MORNING. |
| 4 | **N & Lt** gspn | [N & Lt] FROM |
| 5 | Zpvs Pxo **E.h.** | YOUR OWN [E.h.] |

Groups in bold are initials, reported as written. The quotation marks around "Txffut" and the full stop after "npsojoh" are on the card.

The message is in English: **My own E.h., many thanks for "sweets" this morning. N & Lt from your own E.h.**

English (normalized): **"My own [E.h.], many thanks for the 'sweets' this morning. [N & Lt] from your own [E.h.]."**

Slovak translation: **„Môj vlastný [E.h.], veľká vďaka za ‚sladkosti‘ dnes ráno. [N & Lt] od tvojho vlastného [E.h.].“**

The text is an ordinary short Edwardian thank-you note between sweethearts. The card does not say what the "sweets" in quotation marks were.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1399/work/solve.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the files in source/, decodes the manual transcription in work/transcription-v2.json with the Caesar −1 key, re-encodes each word to check the round trip, and prints the six lines of the table above, the initial groups literally with their Caesar −1 equivalents (`E.h.` → D.g., `N & Lt` → M & Ks), and the line `46 enciphered letters decoded with one key`. It decodes a manual transcription, not image pixels.

## Uncertainties

1. **`E.h.`** (salutation and closing, the same form both times): a looped capital like a cursive E, a dot, a clear h, a dot. It is kept as written. If it were enciphered like the words it would stand for D.g.; what it means (pet name or initials) is not established. The closest parallel is HCP 1400, also to Miss Dean, whose salutation begins "Nz E.h. …"; HCP 1386 has a comparable slot written "E. L.".
2. **`N & Lt` before FROM:** a capital of the same form as the writer's N (M not excluded), a small reversed-c ampersand, a looped capital L, then a small loop with a trailing stroke. The last sign can be a t whose cross is a trailing dash, or a flourish or full stop after L; **`N & Lt` and `N. & L.` are equally possible readings**. Under Caesar −1 they would give M & Ks or M. & K. The same slot is kept literal on HCP 1386 and 1403 (`N. & L.`) and 1407 (`M. & L.`), while HCP 1395 reads its `M. & L.` as cipher, giving L. & K. ("love & kisses"). An expansion such as "[much love] & kisses" is plausible but is **not claimed**.
3. **`gspn` (FROM)** is crossed by the long descender of its own g and by a stroke from the line above, so its s and p are only partly separable. The word is read from its length, the visible shapes and the fixed "… from your own …" formula of the sister cards; it is not fully clear on the scan.
4. The heading **"S. 7."** is ordinary writing; its meaning is unknown and it is not shifted.
5. The **postmark month** is only partly legible (…E); February 1908 rests on the weekday agreement with "Sunday". The upper arc of the office name is not legible.
6. The **house name** in the address (Queen's House?) is uncertain.
7. The identities of the writer and of Miss Dean beyond the address are not established.
8. No search for a published solution was made beyond the portal status (Not solved, no attached solution) and the AI Decipherment Register (no entry for this card on 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), transcribed the card independently from its own enlargements and decoded it with its own script under all 26 shifts; only shift −1 gave English, and its 46 letters agreed with the solver's. It checked every word against the scan, confirmed the postmark reading and that 2 February 1908 was a Sunday, judged the plaintext ordinary Edwardian English, and confirmed that the earlier GPT work and all uncertainties were disclosed. It had no blocker or major findings; its three minor findings are reflected here:

- **`N & Lt`:** the "t" may be a flourish or full stop, so `N. & L.` (as on the sister cards) is now given as an equally possible reading (uncertainty 2).
- **Family practice:** the different treatment of the same closing slot on HCP 1395 (read as cipher, L. & K.) is now mentioned, and HCP 1400 is cited as the closest parallel for `E.h.` (uncertainties 1 and 2). In doing so the solver also corrected its own list of sister cards with this group (1386, 1395, 1403, 1407; not 1402).
- **`gspn`:** kept as a disclosed uncertainty, not presented as fully clear (uncertainty 3).

No decoded letter, key value or transcription changed as a result of the review.

## Sources

- HC Portal record 1399, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1399 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4257/conversions/pc_hcp_80_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4258/conversions/pc_hcp_80_adr-large.jpg (source/address.jpg).
- Related cards in this repository: HCP 1386–1407 (the Abbott correspondence) and HCP 1400 (the other card to Miss Dean).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

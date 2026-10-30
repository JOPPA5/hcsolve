# HCP 1380 (pc_hcp_61): a Caesar-shift love postcard, 6 April 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (97 of 97 enciphered letters); independent review 1 verdict ACCEPT. The review changed how one sign is transcribed, not the words read.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1380 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1380), portal name pc_hcp_61, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-04-06, language Unknown, location Europe, sender Unknown, recipient W. Abboú (a catalogue spelling), with no transcription or solution attached.

The picture side shows "Margate, Lifeboat Memorial" and carries no cipher. The address side has a halfpenny Edward VII stamp and a postmark read as WIM[BORNE], 10 PM, AP 6, 07. The 6 and 07 fall on the stamp but are legible. 6 April 1907 was a Saturday, which matches the plain heading "Sat: afternoon". The card is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.

The message fills the left half of the address side, written sideways, so the scan must be turned 90° counter-clockwise to read it. The pencil "(10)" at the top is not message text. The heading "Sat: afternoon" and the address are ordinary writing.

The card belongs to a correspondence of Caesar-shift postcards to the same recipient in the same hand, many of them already read in this repository (for example HCP 1379, posted at Wimborne three days later, and HCP 1386–1407). Those cards pointed to the key, but the key was tested on this card and not assumed: the shift decodes every enciphered letter here.

![Address side as scanned, with the message in the left half (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright (work/crops/msg.jpg)](../work/crops/msg.jpg)

## Method

The transcription is **manual**. The solver turned the un-converted original scan upright, cut enlarged crops of each line and of the difficult signs, and read the card sign by sign. No OCR was used. The result is in work/transcription.json. A short script then applies the shift, checks the inverse, and checks the hashes of the scans.

First readings that were corrected on the enlargements, all by rereading shapes and never by changing the key:

- `Gps.z` was rejected, because the capital is the barred form of `t` seen in `ofxt` and `tqfdjbm`. This gives `Tpssz`, SORRY.
- `dbtf` (CASE) was rejected, because the second letter is the writer's looped `p`. This gives `dpef`, CODE.
- `Up` (TO) was rejected, because the faded capital is the same `J` as in line 1. This gives `Jo`, IN.
- The tall sign in `ublf` was first misidentified. It is the looped `l`, so the word is TAKE.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one, with A becoming Z.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

All 97 letters use this one shift. The "&" is left unshifted, as on sister cards.

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| Nz. Efbsftu. J. bn. | MY. DEAREST. I. AM. |
| wfsz. Tpssz bcpvu | VERY. SORRY ABOUT |
| ofxt. Jo. dpef. &. | NEWS. IN. CODE. &. |
| ipqf Zpv. xjmm | HOPE YOU. WILL |
| ublf. hsfbu dbsf | TAKE. GREAT CARE |
| "Cz. wfsz. tqfdjbm | "BY. VERY. SPECIAL |
| Sfrvftu." Zpvs. pxo | REQUEST." YOUR. OWN |
| mpwjoh. Hjsm. | LOVING. GIRL. |

The writer's dots are approximate separators. "Cz wfsz tqfdjbm Sfrvftu" is in quotation marks and underlined on the card.

**English:** Sat: afternoon. My dearest, I am very sorry about news in code & hope you will take great care, "by very special request". Your own loving girl.

**Slovak:** Sobota popoludní. Môj najdrahší, veľmi ma mrzí tá správa v šifre a dúfam, že si budeš veľmi dávať pozor, „na veľmi zvláštnu žiadosť". Tvoje vlastné milujúce dievča.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1380/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans in source/ and the two originals in work/hires/, decodes every token of work/transcription.json, checks the inverse round trip, and prints the table and the reading. It does not read the image: the transcription step is manual, and it was confirmed independently in review.

## Uncertainties

- **The `c` of `bcpvu`.** The sign is the only lowercase `c` on this card and is close in form to the card's `e`. Its upper part is a solid wedge with no visible counter, and it matches the flagged `c` in the same word on HCP 1359. The word ABOUT is not in doubt.
- **The `n` of `bn`.** It is angular, close to an `x` or `z` shape, and is the only lowercase `n` on the card. AM rests on the context and on `J. bn` on sister cards, not on the shape.
- **Faded letters.** The `s` of `Zpvs`, the `x` and `o` of `pxo`, the `w` of `mpwjoh`, the `m` of `Hjsm`, the `J` and `o` of `Jo` and the second `s` of `Tpssz` are thin but readable at 5–6×. No letter is restored from context. The portal's wheel watermark overlies parts of lines 2–5.
- **Separators.** Dots and ink pools cannot always be told apart. No word depends on them.
- **Sense.** The meaning of "news in code", and of the quoted "by very special request", cannot be tested from this card. Taking the first as news the couple exchanged in this cipher is an interpretation.
- **People.** The sender is known only as "your own loving girl". Her identity is not established, and neither is that of W. Abbott beyond the address.
- **Prior publication.** The check covered the portal status (Not solved), the absence of any attached solution, and the AI Decipherment Register on 2026-10-30, which has no record for this card. No wider search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, typed its own transcription from its own crops, and decrypted it with its own code. It obtained the same 97 letters and 25 tokens, with one sign read differently (finding 1 below). It also divided the card by the median of 25 other address sides to remove the portal's wheel watermark, which made the pale letters easier to read. It checked every word on that view and on the raw scan, and confirmed the postmark, the weekday, the address and the closing formula.

Its four findings were minor, and all were accepted:

- **`bepvu` became `bcpvu`.** The solver had described an e-like closed loop and printed ADOUT as the literal decode. The loop is not visible, and the sign matches the writer's `c` on HCP 1359. The literal decode is now ABOUT, and the suggestion of a writer's slip was withdrawn. This is the only change to a decoded letter.
- **`Tpss.z` became `Tpssz`.** The supposed dot inside the word is most likely the pooled foot of the faint `s`. Separators are now described as approximate.
- **The `n` of `bn`** is now described as angular and unconfirmed by its shape.
- **The ampersand.** The pointer to a sister crop was corrected. The sign is ink on this card and not part of the watermark, so that doubt is closed.

## Credits

Download and capture by the orchestrator. Transcription, key test, decoder and this report by Claude Opus 5.5 as solver, 2026-10-30. Independent review by a separate Claude Opus 5.5 agent. There was no earlier work on this number.

## Sources

- HC Portal record 1380, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1380 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4200/pc_hcp_61_pic.JPG (work/hires/) and its conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4201/pc_hcp_61_adr.JPG (work/hires/) and its conversion (source/address-large.jpg).
- Sister cards in this repository: ciphers/hcp-1359, hcp-1373, hcp-1379, hcp-1386 to hcp-1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.

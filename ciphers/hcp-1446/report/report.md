# HCP 1446 (pc_hcp_127): a Caesar-shifted thank-you postcard to Nayland

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1446 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1446), part of the HCPortal cryptographic postcards collection (private collection), portal name pc_hcp_127. When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard HCPortal collection, category Substitution / Monoalphabetic, date 1907-01-30, language Unknown, location Europe, sender Unknown, recipient N. F. Sawdy, with no transcription or solution attached.

It is a British picture postcard printed by P.P. & P. Co., Croydon. The picture side shows the Great Wheel at Earls Court, London, with only the printed caption and no cipher. The address side is addressed in plain writing to **Miss N. J. Sawdy, The Manse, Nayland** (the portal reads the second initial as F; in this copperplate F and J are close, and the card looks more like J). The halfpenny Edward VII stamp is cancelled **NAYLAND B JA 30 07**, and a plain cursive date along the lower left edge reads "Jan 30th 07". Both agree with the portal date, Wednesday 30 January 1907. Nayland is a village in Suffolk, England. The cipher is six lines of capital letters written across the left half of the card, read with the card turned 90° clockwise.

![Address side: six lines of shifted capitals on the left, the plain address on the right (source/address.jpg)](../source/address.jpg)

## Method

The cipher consists of 64 ordinary capital letters in six lines, with normal word spacing and two commas. The transcription is **manual**, from a rotated copy of the scan (work/transcription.txt); the portal supplied no transcription and no OCR was used.

Short repeated words give the key at once: SGD → THE and XNT → YOU both mean that every letter is written one place earlier in the alphabet. The same single shift turns all 64 letters into an idiomatic English thank-you note, with no exceptions. Shift 0 (the letters as written) and all other shifts give no English.

In review the transcription was checked independently, line by line, against the reviewer's own crops of the scan, with particular attention to the decorated initial S, the tailed Q's (which cannot be O) and C against G (G has a bar). The reviewer's own reading, decoded with its own script, agrees with the solver's for all 64 letters.

## Key

A Caesar shift of −1 for encryption (+1 for decryption): each plaintext letter is written as the letter before it, and A wraps round to Z.

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | Z | A | B | C | D | E | F | G | H | I | J | K | L |

| Plaintext | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | M | N | O | P | Q | R | S | T | U | V | W | X | Y |

Letters actually observed on the card: B, C, D, E, F, G, H, I, J, K, L, M, N, Q, R, S, T, U, V, X, Z (plaintext C, D, E, F, G, H, I, J, K, L, M, N, O, R, S, T, U, V, W, Y, A).

## Plaintext

Ciphertext as written on the card (commas and the final full stop are on the card):

```text
SGZMJR UDQX LTBG ENQ
SGD BZQC XNT, RDMS LD,
ZMC FNNC VHRGDR
XNTQR
RHMBDQDKX
INGM.
```

Decrypted, line for line:

```text
THANKS VERY MUCH FOR
THE CARD YOU, SENT ME,
AND GOOD WISHES
YOURS
SINCERELY
JOHN.
```

Normalized English (capitals and punctuation editorial): **Thanks very much for the card you sent me, and good wishes. Yours sincerely, John.**

Slovak translation: **Ďakujem veľmi pekne za pohľadnicu, ktorú si mi poslala, a veľa dobrých želaní. S úctou, John.** (The feminine "poslala" follows "Miss" in the plain address, not the cipher.)

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1446/work/decode.py
```

The script checks the SHA-256 hashes of the source files and decodes the manual transcription in work/transcription.txt with the shift above. It does not read the image; the transcription step is manual (and was confirmed independently in review). Its transcription contains two spaces that are not on the card ("L TBG", "RHMB DQDKX"), so the output prints "M UCH" and "SINC ERELY"; the letters are the same as above.

## Uncertainties

- The identity of John is not established, nor is the recipient's second initial (F or J).
- The signature was at first read either as JOHN or, if its first sign were L, as MOHN. The dot above the sign and its left-turning foot show it is I, so JOHN is the reading; MOHN is rejected.
- The commas after YOU and ME are kept as written; their placement is the writer's.
- No search for a prior publication was made beyond the portal status (Not solved), skip.txt and a same-day snapshot of the AI Decipherment Register, none of which lists this card.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 64 letters from the scan before comparing, decoded them with an independently written script, and found no letter-level differences. It checked that one shift covers every letter, searched both sides of the card for untranscribed cipher (none), and checked the postmark and dates. Its four findings were minor and are reflected here:

- The signature uncertainty JOHN / MOHN is settled in favour of JOHN by the dot over the first sign and the shape of its foot.
- Two word gaps in the solver's transcription (inside LTBG and RHMBDQDKX) are not visible on the card; this report gives MUCH and SINCERELY as continuous words.
- The plain address, postmark and handwritten date (Miss N. J. Sawdy, The Manse, Nayland; NAYLAND JA 30 07; "Jan 30th 07") are now recorded.
- A protocol note (directories changed after the hand-over marker) has no effect: the source image hashes still match.

No change to the decoded letters resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1446, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1446 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4399/conversions/pc_hcp_127_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4398/conversions/pc_hcp_127_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register, public JSON snapshot of 2026-10-26 (ciphers/hcp-1450/work/register-snapshot.json), checked in review.

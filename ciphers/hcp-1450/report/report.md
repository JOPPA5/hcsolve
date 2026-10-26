# HCP 1450 (pc_hcp_131): a dotted Pigpen postcard from Warrenton to Emma Alwin

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1450 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1450), part of the HCPortal cryptographic postcards collection (private collection), portal name pc_hcp_131. When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard HCPortal collection and Pigpen, category Substitution / Monoalphabetic, date 1905-05-26, language Unknown, location North America, sender Unknown, recipient Ema Alwin, with no transcription or solution attached.

It is an American picture postcard showing four kittens in bed. The cipher is written on the picture side: a plain handwritten heading "Warrenton, Mo. May. 26, '05." and seven rows of Pigpen signs, with words separated by slashes. The address side, with a one-cent Franklin stamp, is addressed in plain writing to **Miss Emma Alwin, New Ulm, Minn.** (the portal spells the name Ema). It carries the cancel **WARRENTON MAY 26 … PM 1905 MO.**, a machine RECEIVED cancel and the receiving mark **NEW ULM MINN. MAY 2? 1905** (day not legible). Heading and postmark give Friday 26 May 1905. A few faint pencil strokes at the left of the address side contain no grid signs or dots and are not cipher.

![Picture side: heading and seven rows of dotted Pigpen (source/picture.jpg)](../source/picture.jpg)

## Method

The cipher consists of 118 Pigpen outlines in seven rows, each outline with one, two or three dots inside, plus two plain question marks and one plain cursive word, "won't", in row 5. The transcription is **manual**: each sign was recorded as the sides of the cell that are drawn plus its dot count in work/transcription.txt, from enlarged row crops. The portal supplied no transcription and no OCR was used.

The conventional three-count Pigpen layout, applied with one fixed key, gives continuous English across all seven rows. Repeated letters are drawn the same way each time (E ×19, T ×10, A ×9, S ×9, I ×8, N ×8, O ×8, D ×6), no sign needs two values, and the decoded salutation DEAREST EMMA matches the plain address. Some signs are overdrawn and several dots merge into blots. For those (the X's of EXAMINATIONS and EXCUSE, both A's of EXAMINATIONS, the E of EDW) the outline is clear but the dots cannot be counted; every other dot count would give a non-word, except for the E of EDW (see Uncertainties). During solving a second solver helper read the hardest row and the signature from separate crops; that was visual assistance, not a review.

In review the transcription was checked independently, sign by sign, against the reviewer's own crops at 4× and, for the hard signs, at 7–14×, and decoded with the reviewer's own script. The two readings agree for all 118 signs, including the word divisions.

## Key

A dotted three-block Pigpen variant. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right (┘) | A | J | S |
| bottom + left + right (⊔) | B | K | T |
| bottom + left (└) | C | L | U |
| top + bottom + right (]) | D | M | V |
| all four sides (□) | E | N | W |
| top + bottom + left ([) | F | O | X |
| top + right (┐) | G | P | Y |
| top + left + right (⊓) | H | Q | Z |
| top + left (┌) | I | R | (unused) |

## Plaintext

Row by row as written on the card, with the slashes between words shown as spaces; the two question marks and the cursive "won't" (in braces) are in plain writing:

```text
DEAREST EMMA
WELL SWEETNESS
HOW BE YOU? I DONT THINK
I CAN COME HOME UNTIL
AFTER EXAMINATIONS DR {won't}
EXCUSE US CAN YOU READ
THIS? WITH LOVE DEAREST EDW.
```

HOW BE YOU, DONT (without an apostrophe), DR and EDW. are kept as written.

Normalized English (punctuation and sentence division editorial): **Dearest Emma, well, sweetness, how be you? I don't think I can come home until after examinations. Dr won't excuse us. Can you read this? With love, dearest, Edw.**

Slovak translation: **Najdrahšia Emma, nuž, miláčik, ako sa máš? Nemyslím, že budem môcť prísť domov skôr než po skúškach. Dr nás neospravedlní. Vieš si toto prečítať? S láskou, najdrahšia, Edw.**

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1450/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes all 118 manual outline/dot tokens in work/transcription.txt with the key above and checks the inverse-key round trip. It does not read the image; the transcription step is manual (and was confirmed independently in review).

## Uncertainties

- DR in row 5: the dot of the D is one elongated blob, laid diagonally like the two dots of M, so MR (]2) cannot be excluded from the pixels. DR is kept because a bare title is natural for a school's head and a bare "Mr" is not. An earlier alternative, IS, was rejected during solving.
- The heavy blotted signs (X of EXAMINATIONS and EXCUSE, both A's of EXAMINATIONS) have uncountable dots; their readings rest on the clear outlines and on the fact that all other dot counts give non-words.
- The E of EDW is a blot; N (NDW) or W (WDW) are possible in principle, but EDW. with its full stop is the usual abbreviation of Edward. No full name is asserted.
- Who Edw. and the Dr were is not established. Warrenton, Mo. had a college at the time, which would fit "examinations"; this was not checked and the solution does not rely on it.
- The day on the New Ulm receiving mark is not legible.
- A same-day snapshot of the AI Decipherment Register (110 records) has no entry for this card, the portal status is Not solved and the card is not in skip.txt; this is not proof that no decipherment was published elsewhere.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 118 signs from the scan before comparing, decoded them with an independently written decoder that builds the key from the grid geometry, and found no differences. It checked key consistency, searched both sides of the card for untranscribed Pigpen (none) and checked the postmarks and the date. Its three findings were minor and are reflected here:

- The dot of the D in DR is oversized and may be two merged dots; MR is now listed as a visual alternative, while DR is kept as the reading.
- The other flagged blotted signs were confirmed: their outlines are clear and every other dot count gives a non-word; for the E of EDW, N or W are possible only in principle.
- The postmarks (Warrenton MAY 26 1905; New Ulm MAY 2? 1905) and the weekday (Friday) are now recorded.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1450, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1450 (source/metadata.md).
- Picture side (with the cipher): https://api.hcportal.eu/media/4410/conversions/pc_hcp_131_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4411/conversions/pc_hcp_131_adr-large.jpg (source/address.jpg).
- AI Decipherment Register, public JSON snapshot of 2026-10-26: https://ai.hcportal.eu/register/?format=json (work/register-snapshot.json).

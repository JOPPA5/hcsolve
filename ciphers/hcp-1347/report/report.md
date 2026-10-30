# HCP 1347 (pc_hcp_28): an English Caesar sweetheart postcard, 9 August 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (58 enciphered letters: 57 read, 1 restored under a smear); one group of initials kept literal. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1347 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1347), portal name pc_hcp_28, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and HCPortal collection, category Substitution, date 1907-08-09, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. The catalogue spelling is a misreading of the writer's barred double t: the address says Abbott.

The picture side is a printed view, "Lady Chapel, Wimborne Minster", series number 14276, with no handwriting. The address side (The Wrench Series No. 14276) has a halfpenny Edward VII stamp cancelled **WIMBORNE, 10 PM, AU 9 07**, and is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The message stands on the left half, written along the card, so the card must be turned 90 degrees anticlockwise to read it. The large disc with alphabet rings and the small building logo are a scanner overlay, not part of the card.

9 August 1907 was a Friday, which agrees with the plain heading "G. H. Friday." The card belongs to a correspondence of a couple, addressed to W. Abbott, that is deciphered elsewhere in this repository (for example HCP 1355, 1365, 1368 and 1386–1407). The writer signs with a closing formula of the form "your own … girl". Her identity is not known.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the cipher text is at the left (source/address-large.jpg)](../source/address-large.jpg)

![The message turned to reading position (work/crops/msg.png)](../work/crops/msg.png)

## Method

The transcription is manual: the original scan was rotated and read sign by sign from enlargements of 3 to 8 times. No OCR was used, and the portal supplied no transcription.

The cipher was not recovered blind. Caesar −1 was taken as a hypothesis from the sister cards to W. Abbott and then tested on this card's own signs. Every word resolved with that one shift and no adjustment for this card. In review, all 26 shifts were tried on an independently typed ciphertext, and only this shift gives English.

The ciphertext word `Njotufs` occurs in no other SOLUTION.md in this repository, so MINSTER was not carried over from a sister card. It comes out of the cipher and agrees independently with the picture and the Wimborne postmark.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet (A as B, B as C, … Z as A). To decipher, subtract one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading and address are in clear. The initials `M. L.` are kept literal, as on the sister cards; they are not known to be enciphered (shifted they would be L. K.).

## Plaintext

Brackets inside a word mark a restored letter. Whole bracketed groups are initials kept literal. The writer's dots between words carry no meaning. The quotation marks in line 6 are on the card.

| Line | On the card | Literal reading |
|---|---|---|
| 1 (clear) | G. H. Friday. | G. H. Friday. |
| 2 | Nz. Pxo M- L Cpz. | MY. OWN [M-] [L] BOY. |
| 3 | J. bn. hpjoh up | I. AM. GOING TO |
| 4 | uif Njotufs | THE MINSTER |
| 5 | Tvoebz. Ojhiu | SUNDAY. NIGHT |
| 6 | "Opu. bmpof" | "NOT. ALONE" |
| 7 | Zpvs. Pxo. M. L. Hjs[m] | YOUR. OWN. [M.] [L.] GIR[L] |

English (the original language; the portal says Unknown): **G. H. Friday. My own M. L. boy, I am going to the Minster Sunday night, "not alone". Your own M. L. girl.**

Slovak translation: **G. H., piatok. Môj vlastný M. L. chlapec, v nedeľu večer idem do Minsteru, „nie sama". Tvoje vlastné M. L. dievča.**

Notes on the reading:

- **The Minster** is Wimborne Minster, the church on the picture side and the town of the postmark. The writer chose a card of the place she mentions.
- **"Not alone"** is in quotation marks on the card. The card does not say who goes with her, or why the words are quoted.
- **Sunday night** was presumably 11 August 1907, an inference from the Friday postmark.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1347/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four image files, decodes the manual transcription in `work/transcription.json`, re-encodes each word as a check, and prints the table above with the count: 58 enciphered letters (57 read, 1 restored), 4 initial tokens kept literal. It does not read the image: the transcription step is manual and was checked independently in review.

## Uncertainties

- **Final letter of GIRL is a restoration.** `Hjs` is clear; the last sign is largely covered by a smear. A doubled stem and further dark masses are visible, compatible with a smeared m, but the stem is taller than a normal minim of this hand, so the pixels alone neither show nor confirm an m. GIR[L] rests on the visible letters and on the same closing formula on sister cards.
- **The e of SUNDAY.** It has no visible loop and looks like a c with a thick head. As c it would give SUNBAY, so it is read as e with the loop filled. It is the only e in the ciphertext, so this card offers no comparison; the same word is on HCP 1355.
- **The initials `M. L.`** are unexplained, and it is not proved whether they are shifted. The first sign has a hook, a stem and two further strokes, against one in the N of `Nz`, so it is read M here; N remains possible. Sister cards print this slot variously as `M. L.`, `N. L.`, `M. h` and `M-h`, and these are probably one group, not different pairs of initials. The second sign on this card is a stem with a small foot, so h is possible as well as L. In line 7 it also shares its stem with a descender from the line above. The form printed here is a choice.
- **GOING is blotted.** The stem of the p is heavily blotted, the arch of the final h is swallowed by a blot, and the j has no visible dot. The word is not in doubt.
- **NIGHT:** after h the card has three small minims and one dot set slightly right of its place. That count fits i + u of `Ojhiu`.
- **OWN in line 7:** the arc of the P runs into a blotted descender from the line above; the form matches line 2.
- **Heading initials:** read `G. H.`, but the G could be a C, as discussed on sister cards.
- **No published solution** of this card was met, but no web search was run. The checks made were the portal status (Not solved) and the AI Decipherment Register (no entry for this card, checked 2026-10-30 by the orchestrator).
- **The review was not cross-provider:** solver and reviewer were separate Claude Opus 5.5 agents.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate session, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, checked the file hashes, retyped the ciphertext from its own crops, and tried all 26 shifts with its own script. It compared every token with the scan at 3 times, and the doubtful signs at 6 to 10 times; every token matched. It confirmed that 9 August 1907 was a Friday, and it confirmed the claims about sister cards. It could not verify the meaning of the initials or whether a published solution exists.

Its four findings were minor. All were addressed, and no decoded letter changed:

- **GIRL printed as fully read.** The restored letter is now marked as GIR[L] in the table, the transcription and the decoder output, and the count is split into 57 read and 1 restored.
- **Smudged signs in GOING.** Now listed under uncertainties.
- **`M. L.` against `N. L.`** The report now says that these are probably one group. In responding, the solver also noted the `M. h` reading of the same slot, which the review had not raised.
- **Height of the restored m.** The uncertainty now says that the stem is taller than a normal minim, and that the pixels do not settle the letter.

## Credit

Download of the portal record: Claude Opus 5.5 (orchestrator). Transcription, decipherment, closing and report: Claude Opus 5.5 as solver, 2026-10-30. There is no earlier work on this number. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1347, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1347 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4101/pc_hcp_28_pic.JPG and its conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4102/pc_hcp_28_adr.JPG and its conversion (source/address-large.jpg).
- Sister cards in this repository: ciphers/hcp-1355, 1365, 1368, 1386–1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.

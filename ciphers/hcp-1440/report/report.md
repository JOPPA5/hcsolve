# HCP 1440 (pc_hcp_121): a Good Friday Pigpen tease to Ray Bartley

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1440 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1440), portal name pc_hcp_121, part of the HCPortal cryptographic postcards collection (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard and Pigpen, main category Substitution (monoalphabetic), language Unknown, date 1908-04-17, sender Unknown, recipient Ray Bartley, with no transcription or solution attached.

The picture side is a printed "Easter Greetings" card (lambs, a church, Easter eggs and lilies of the valley) and carries no handwriting. 17 April 1908 was Good Friday (Easter Sunday was 19 April 1908). On the address side the postmark reads RUT[LAND] APR 1? … PM 1908 IOWA; the day digit and the hour are covered by the printed "POST CARD" ornament. The card is addressed to Mr Ray Bartley, Laurens, Iowa.

The writer dated the card 4-17-08 at the top left and wrote two short lines of Pigpen (19 signs) next to the date, followed directly by a plain "Ha Ha." The rest of the address side is a plain cursive letter: the writer is sitting up front and expects to stay the rest of the term, went to Lodge and danced although someone "didn't want us to dance but we did it anyway", sat up all night, and wanted to go to a play in Humboldt that night. It is signed with the plain initials **R.E.B.**, which are not expanded to an identified person. The related card HCP 1438, to the same addressee and also postmarked Rutland, uses the same Pigpen key.

![Address side; the two Pigpen lines are at the top, after the date 4-17-08 (source/address.jpg)](../source/address.jpg)

## Method

The solver traced each sign manually from the scan and an enlarged crop of the header (work/header-large.jpg) into work/transcription.txt as an outline (which sides of the cell are drawn) plus a dot count. The signs use nine tic-tac-toe outlines with one, two or three dots. Reading the plain 3×3 grid A–I with the dot count selecting the block decodes all 19 signs to English under one fixed table. YOU is written twice with identical signs, and O and U recur with the same signs in COULD.

In review both lines were transcribed again from the scan, independently, by the strokes seen plus dot count (9× crops of each line, 12–18× details of the doubtful signs), and decoded with an independently written script. The comparison gives 0 differences out of 19. The reviewer described three imperfect signs the solver had not named; they are listed under Uncertainties.

## Key

A dotted three-block Pigpen, the same key as on HCP 1438. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused. Solver labels from work/transcription.txt are given in brackets.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right (BR) | A | J | S |
| bottom + left + right (B) | B | K | T |
| bottom + left (BL) | C | L | U |
| top + bottom + right (R) | D | M | V |
| all four sides (C) | E | N | W |
| top + bottom + left (L) | F | O | X |
| top + right (TR) | G | P | Y |
| top + left + right (T) | H | Q | Z |
| top + left (TL) | I | R | (unused) |

## Plaintext

Transcription (work/transcription.txt; label = outline, digit = dot count, | = word gap):

```text
R1 L2 C2 B3 | TR3 L2 BL3 | C3 TL1 BR3 T1
TR3 L2 BL3 | BL1 L2 BL3 BL2 R1
```

As written, decoded:

```text
DONT YOU WISH
YOU COULD
```

Normalized English (apostrophe and question mark editorial; the plain "Ha Ha." follows on the card): **Don't you wish you could? Ha Ha.**

Slovak translation (contextual; "to tiež" is not decoded text): **Neprial by si si, aby si to tiež mohol? Cha cha.**

The cipher does not say what "could" refers to, and no object is supplied. In the setting of the plain letter, with its Lodge dance and sleepless night, the line reads naturally as a tease.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1440/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the 19 manual tokens in work/transcription.txt with the key above and checks the inverse-key round trip. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **N of DONT.** The closed box has one clear dot inside at the left; the second "dot" is a dark mark merged into the right-hand side of the box. Read strictly as one dot the sign is E (DOET). The two-dot reading N is adopted because only it gives a word.
- **D of COULD.** The final sign (top + bottom + right, one dot inside) has two small specks just above its top stroke, outside the outline. Counted as dots they would make it V (COULV). They are not counted: every other dot sits inside its outline and the specks are smaller than real dots. Whether they are ink or paper defects is not known.
- **I of WISH.** The left stroke of the top-left corner runs down into the printed caption "This Space for Writing Messages". No bottom stroke is visible, so it is not the top + bottom + left outline (F, which would give WFSH).
- Some other small dots touch their outlines, especially in the three-dot W and U; solver and reviewer counted them the same way.
- The day digit and hour of the postmark are hidden; the date rests on the writer's 4-17-08 and the portal.
- R.E.B. and Ray Bartley are not identified further.
- No published decipherment was found: the portal showed Not solved with no attachment, and a same-day snapshot of the AI Decipherment Register (work/register-snapshot.json) has no entry for this card. No wider search was made.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output byte-identical to the solver's saved check), transcribed both lines from the scan in its own notation before comparing, decoded them with an independent script (0 differences out of 19), checked key consistency and coverage, decoded the strict alternatives (DOET, COULV) for comparison, checked the rest of the card for missed ciphertext and checked the context. Its four findings were minor and are reflected here:

- The N of DONT is a one-dot box plus an edge blob: listed under Uncertainties.
- Two specks above the D of COULD: listed under Uncertainties.
- The I of WISH runs into the printed caption: listed under Uncertainties.
- Context was left out: the Good Friday date and Easter card, the plain "Ha Ha." and the dancing story, the Rutland postmark and the initials R.E.B. are now given under Origin and context.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1440, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1440 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4381/conversions/pc_hcp_121_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4380/conversions/pc_hcp_121_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register snapshot, 2026-10-26: https://ai.hcportal.eu/register/?format=json (work/register-snapshot.json).
- Related card: ciphers/hcp-1438/ (HCP 1438, also to Ray Bartley), consulted for context only.

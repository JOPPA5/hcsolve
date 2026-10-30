# HCP 1490 (pc_hcp_171): Pigpen fragments on a postcard to Annie Kepler, 1911

Human solver: Tomáš Pavuk

**Status: cipher passages solved, with the first letter of the greeting unresolved and the script initial of the signature unidentified; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1490 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1490), portal name pc_hcp_171, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, Pigpen, category Substitution / Monoalphabetic, used around 1911, language Unknown, location North America, sender Unknown, recipient Annie Kepler, with no transcription or solution attached.

The address side is addressed to **Miss Annie Kepler, Middletown, Frederick Co., Md.** and carries a 1911 postmark. The picture side shows the War Correspondents' Memorial Arch at Gapland, Maryland, about 10 km from Middletown; it has no cipher text. The message on the address side is mostly in plain English and invites the recipient to a party; three short passages are written in Pigpen signs: the word after "Hello", two words after "to-morrow night not", and the signature after "from a friend".

![Address side: plain-text invitation with three Pigpen passages (source/address-large.jpg)](../source/address-large.jpg)

![Greeting, enlarged 4x: blotted square, then O N E Y (work/greeting-4x.jpg)](../work/greeting-4x.jpg)

![Body, enlarged 3x: "not" followed by SUNDAY NIGHT; the final T is written below the line (work/body-3x.jpg)](../work/body-3x.jpg)

![Signature, enlarged 4x: script b-shaped sign, then D K (work/signature-4x.jpg)](../work/signature-4x.jpg)

## Method

The transcription is **manual**: each Pigpen sign was read on enlarged crops of the address-side scan and recorded as a token, the cell outline (which sides of the tic-tac-toe cell are drawn) plus the number of dots inside (work/transcription.txt). No OCR was used and the portal supplied no transcription. The 19 signs were then decoded by script against the standard Pigpen grid with dot count as the block selector.

The card follows the same cell order as the dot-count Pigpen cards HCP 1131, 1189 and 1190 in this repository, except that here the first block (A–I) has no dot, the second (J–R) one dot and the third (S–Z) two dots. No X-shaped cells occur.

In review the reviewer made its own crops at 6x and 12x, wrote its own token list without using the solver's file, and decoded it with its own script; its token list agrees with the solver's on every sign.

## Key

| Outline (strokes) | Token | 0 dots | 1 dot | 2 dots |
|---|---|---|---|---|
| bottom + right | BR | **A** | J | **S** |
| bottom + left + right | B | B | **K** | T (std) / **U** on this card |
| bottom + left | BL | C | L | U (std) / **T** on this card |
| top + bottom + right | R | **D** | M | V |
| four sides | C | **E** | **N** | W |
| top + bottom + left | L | F | **O** | X |
| top + right | TR | **G** | P | **Y** |
| top + left + right | T | **H** | Q | Z |
| top + left | TL | **I** | R | (none) |

Bold letters occur on this card. The two-dot B and BL cells occur once each, exactly where the text needs U and T; the standard layout has them the other way round. Either the writer's grid had T and U exchanged or he slipped twice; with one occurrence each this cannot be decided.

## Plaintext

Transcription (tokens; `|` = word gap):

```text
greeting:  C* L1 C1 C0 TR2
body:      BR2 B2 C1 R0 BR0 TR2 | C1 TL2x TR0 T0 BL2
signature: [b] R0 B1
```

Decoded (standard layout literally, then with the card's T/U exchange):

```text
greeting   ?ONEY
body       STNDAY N(I)GHU   ->   SUNDAY N(I)GHT
signature  [b]DK
```

Full message, cipher passages in capitals, clear text as written on the card:

> Hello **[?]ONEY** / how is times with you – they are fine with me. / I want to see you at the Party to-morrow night not **SUNDAY NIGHT** / be sure and come. I must stop from a friend / **[b]DK**

English (normalised): **Hello [Honey?], how are things with you? They are fine with me. I want to see you at the party tomorrow night – not Sunday night. Be sure and come. I must stop. From a friend, [b]DK.**

Slovak: **Ahoj [zlato?], ako sa máš? U mňa je všetko v poriadku. Chcem ťa vidieť zajtra večer na večierku – nie v nedeľu večer. Určite príď. Musím končiť. Od priateľa, [b]DK.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1490/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 of the three files in source/, decodes work/transcription.txt with the standard layout and with the card key, and prints both. The full message it prints at the end is a manual transcription of the clear text; only the capital cipher passages come from the decoder. The pixel-to-token step is manual.

## Uncertainties

- **First sign of the greeting.** A full square with a dark 4- or x-shaped blot inside; the dots cannot be counted. A square stands for E, N or W in this key, none of which gives a word with -ONEY. HONEY (top+left+right, no dot) is the obvious greeting after "Hello", but it is a contextual guess, not a reading; the sign may be an overwrite.
- **T/U exchange.** The two-dot B and BL cells are read U and T against the standard layout (see Key). Without the exchange the body reads STNDAY NIGHU.
- **The I of NIGHT is restored, not read.** The sign has the top+left outline (the I/R cell) but carries two dots, which would be the 27th cell of the grid and has no letter; a small x- or inverted-V mark stands below it, perhaps a correction. The I is supplied from the outline and the word NIGHT, a contextual restoration of one letter like the T/U exchange. R (one dot) gives no word.
- **Signature.** The first sign is a b- or 6-shaped stroke in ordinary script (perhaps an initial) and is reported literally as [b]; D and K are clear. The sender is not identified.
- **Coverage.** 14 of the 19 signs (14 of 18 Pigpen outlines) decode under the standard layout with no adjustment; the other five are the four points above (blotted square, the U and T, the two-dot I, the script b).
- The clear-text words ("how is times", "stop from a friend") are transcribed as written.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, wrote its own token list from its own 6x–12x crops and decoded it with an independent script; the token list agreed with the solver's on every sign. It confirmed that every sign is accounted for, that SUNDAY NIGHT fits the clear sentence (word gap, repeated N, Y and G sharing the top+right cell with two and no dots), that address, postmark and picture agree, and that no published solution was used. Its five findings were all minor and are reflected here:

- **Count of clean signs.** SOLUTION.md said 16 of 19; corrected to 14 of 19.
- **HONEY in the translations.** Now marked as conjectural, "[Honey?]" / "[zlato?]".
- **The I of NIGHT.** Now stated plainly as a contextual restoration of an unassigned cell.
- **Hard-coded full message.** The decoder output now says the clear text is a manual transcription.
- **Partial character.** The status line now says the first greeting letter is unresolved.

No decoded letter changed as a result of the review.

**Credit.** Source capture and a first triage (three fragments, greeting shapes, HONEY noted as speculative) were done by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26. The full transcription, the key, the decipherment, the response to review and this report are by Claude Opus 5.5; the review was by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1490, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1490 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4531/conversions/pc_hcp_171_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4530/conversions/pc_hcp_171_pic-large.jpg (source/picture-large.jpg).
- Sister dot-count Pigpen cards in this repository: HCP 1131, 1189, 1190.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.

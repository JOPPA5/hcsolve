# HCP 1475 (pc_hcp_156): an English initial-message on a 1910 postcard

Human solver: Tomáš Pavuk

**Status: the only ciphertext on the card (9 of 9 letters) is read and expanded; independent review 1 verdict ACCEPT, no change to the reading.** The expansion of an initialism is an interpretation, not a proof (see Uncertainties). Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1475 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1475), portal name pc_hcp_156, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Unknown, date 1910-07-11, language Unknown, location Europe, sender Unknown, recipient P. H. Ellis, with no transcription or solution attached.

It is a picture postcard with a windmill on the picture side (no writing there) and the publisher's imprint "Photochromie, Serie 80, Nr. 1956" on the address side. The address is in plain handwriting: **Mrs P. H. Ellis, 50 Eversley Road, Charlton S.E.** (Charlton, south-east London). The card carries a purple date hand stamp **11 JUL 1910**, but no postage stamp and no postal cancellation, so it cannot be shown that it went through the post. A pencil "£4 50" at the top is a later dealer's price.

The only coded text is one line of nine capitals written in ink up the left margin of the address side (read after turning the card 90° counter-clockwise), ending in a full stop. The large grey letter wheel across the card is the portal's watermark, not part of the cryptogram.

![Address side turned so that the cipher line reads left to right; the wheel is the HCPortal watermark (work/reading.jpg)](../work/reading.jpg)

![The cipher line, enlarged 3x with contrast stretched (work/line.png)](../work/line.png)

## Method

The line was transcribed **manually** from the portal scan (source/address-large.jpg), enlarged 4–8x with contrast stretched; no OCR was used and the portal supplied no transcription. An earlier provisional reading by an OpenAI GPT solver, "ILYMAMWLM", misread letters 3–4: on the enlargement they are clearly M (/\/\) and W (\/\/). The reading is **ILMWAMWLM.**

The string uses only five distinct letters (I, L, M, W, A) in nine places, with the mirror pattern I-L-M-W-A-M-W-L-M. Shifting it by any Caesar shift, or reversing the alphabet (Atbash), gives nothing readable (e.g. shift −1 HKLVZLVKL, Atbash RONDZNDON), so a letter substitution is not indicated. The pattern fits an **initial-message**: each capital is the first letter of one English word, and the sentence turns round on "and" (X loves Y and Y loves X). Such initial-messages were a common sweetheart game on Edwardian postcards.

## Key

Initialism (acronym code); no substitution, the letters are the initials of the plaintext words.

| Initial | Word |
|---|---|
| I | I |
| L | love / loves |
| M | my / me |
| W | wife |
| A | and |

## Plaintext

Ciphertext: `ILMWAMWLM.`

English (original): **I love my wife and my wife loves me.**

Slovak translation: **Ľúbim svoju ženu a moja žena ľúbi mňa.**

The sentence is grammatical, idiomatic English of the period, and it suits a card addressed to a married woman: it is most naturally a husband's message to his wife, written in a form a casual reader of the card would not understand.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1475/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both scans, reads the transcription from work/transcription.txt, checks that every word of the proposed expansion begins with the transcribed letter in the same position, and prints `plaintext : I love my wife and my wife loves me.` For an initialism the words cannot be derived mechanically: the script verifies the proposed expansion, it does not produce it.

## Uncertainties

- **The expansion is an interpretation.** An initialism has no key that proves its words. "I love my wife and my wife loves me" fits all nine letters, uses the same word (or a form of the same pronoun) for each repeated letter, and is coherent; no equally coherent alternative was found by solver or reviewer. Variants such as "I like my wife …" would change single words but not the sense.
- **Transcription.** All nine letters are clear on the scan. Letter 6 has a shorter last stroke than letters 3 and 9 but the same M form; there is no break that would make it "MI" or "N". No sign is restored.
- **Writer and posting.** The card is unsigned; that the writer was Mrs Ellis's husband is an inference from the text. The 11 JUL 1910 is a date hand stamp, not a postmark, and with no stamp or cancellation it cannot be shown that the card was posted. Mrs P. H. Ellis was not identified in 1910 records.
- Only the 1024×674 portal scan was available, not the physical card.
- No published solution of this card was found: portal status Not solved, no solution attachment, and no entry in the AI Decipherment Register (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, made its own rotated and enlarged crops of the scan (up to 7–8x), read all nine letters itself and got the same `ILMWAMWLM.`, confirmed that no other cipher text is on either side, ran all 26 Caesar shifts and Atbash (nothing readable) and expanded the initials independently to the same sentence. Its three minor findings were addressed without changing the reading:

- **The command verifies rather than derives the words.** The script and SOLUTION.md now say so explicitly, and a misleading "stem" printout was replaced by a plain list of the words used per initial.
- **Overstated wording.** "The same word for every repeated letter" became "the same word or a form of the same pronoun" (M is "my" twice and "me" once).
- **Postmark and husband.** The purple 11 JUL 1910 is now described as a date hand stamp, not a postmark, and the husband as a likely, not a certain, writer.

## Credits

Source capture (metadata, scans) and the first provisional reading "ILYMAMWLM", with the suggestion of an "I love you"-type initialism, by the earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). Re-transcription from the pixels, the expansion, the script, the response to review and this report by Claude Opus 5.5 (2026-10-30); independent review by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1475, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1475 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4486/conversions/pc_hcp_156_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4485/conversions/pc_hcp_156_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

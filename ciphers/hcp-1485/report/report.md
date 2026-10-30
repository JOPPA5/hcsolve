# HCP 1485 (pc_hcp_166): Arthur's golfing love note to Gwennie, Colwyn Bay 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 172 cipher letters of 10 lines plus the closing initials); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1485 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1485), portal name pc_hcp_166, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, used around 3.1908, language Unknown, location Europe, sender Unknown, recipient "J. Willams", with no transcription or solution attached. No published solution of this card was found.

The picture side is a "Pictorial Comedy" comic card (James Henderson & Sons, London) captioned **"A good game for two"**: a courting couple on a golf course, with a golf bag. It carries no cipher text.

The address side, in ordinary handwriting, reads **Miss G. Williams, "Baronhill", York Road, Colwyn Bay, N. Wales**, with a ½d Edward VII stamp and a 1908 postmark. The message area is filled with ten lines of geometric signs followed by four signs separated by dots, and the plain signature **Arthur**. The cipher text is written upside down relative to the printed card: the question marks, commas, apostrophes and brackets only read correctly after turning the card 180°.

A sister card, HCP 1484 (pc_hcp_165, same addressee and address, same publisher series, dated 30 January 1908, signed "your boy"), was deciphered independently in this repository with the same sign system (see Key).

![Picture side: "A good game for two" (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned 180°, the orientation in which the cipher was written and read (work/upright.jpg)](../work/upright.jpg)

## Method

The earlier triage of 2026-10-26 by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal record and the two images, made the 180° working image and noted the geometric sign set; it established no key or plaintext. The transcription and decipherment were made by Claude Opus 5.5 on 2026-10-29.

The transcription is manual: every sign was read on 9–16× enlargements of the upright image and recorded in a descriptive notation (work/transcription.txt), for example `L2b` = a vertical stem with two ticks on its left side, low on the stem, or `SQB` = a square with a `\` diagonal. A superscript "2" written after a sign marks a doubled letter.

The entry point was the first line: the pattern `G W E N² I E` against the addressee "Miss G. Williams" gave GWENNIE, followed by DARLING; the picture caption then suggested the second line, GOLF IS A GOOD GAME FOR TWO. With these letters placed, the consonant signs turned out to follow a strict alphabetical grid (below), which then predicted every remaining sign. An earlier idea, reading the signs as look-alikes of Latin letters, was a dead end.

The reviewer built the key independently from the stated construction rule alone, decoded the transcription with its own script and obtained identical text; it also checked the transcription against its own enlargements of the scan, line by line, with close-ups of every unusual sign.

## Key

Monoalphabetic substitution with a home-made, systematic **stroke alphabet**. Word spaces and ordinary punctuation are kept.

Consonants are a vertical stem with 1–3 short ticks. The side of the ticks (left, right, or bars crossing the stem), their number, and their position (upper or lower part of the stem) give the letter; the consonants run in alphabetical order in groups of three:

| Ticks | 1 high | 2 high | 3 high | 1 low | 2 low | 3 low |
|---|---|---|---|---|---|---|
| left | B | C | D | F | G | H |
| right | J* | K | L | M | N | P* |
| crossing | Q* | R | S | T | V | W |

(* not attested on this card; filled in from the pattern.)

Vowels and Y are shapes:

| Shape | Letter |
|---|---|
| circle with a central dot | A |
| triangle | E |
| triangle with an inner vertical stroke | I |
| plain square | O |
| square with a `\` diagonal | U |
| square with a `/` stroke | Y |

X and Z do not occur. The sister card HCP 1484, deciphered independently, uses the same construction and the same letter for every sign; its description of the Y-sign ("a V from the two top corners") differs slightly in wording, but on both cards the Y-square is distinct from the U-square.

## Plaintext

Literal decipherment, line by line as on the card (upright orientation):

```text
GWENNIE DARLING.
GOLF IS A GOOD GAME FOR
TWO BOT I DON'T THINK
IT BEATS OUR CAME OF
"IN THE GLOAMING" (ALSO
FOR TWO!) WHAT DO YOO
THINK DEAREST? AREN'T
YOU ALSO RATHER STRUCK
WITH THE "GAME"? CARIAD!!!
I LOVE YOU GWENNIE DEAR,
A.M.H.L.
Arthur            [plain script]
```

Reading (three writer's slips corrected; the literal form is in braces):

```text
GWENNIE DARLING.
GOLF IS A GOOD GAME FOR
TWO BUT{BOT} I DON'T THINK
IT BEATS OUR GAME{CAME} OF
"IN THE GLOAMING" (ALSO
FOR TWO!) WHAT DO YOU{YOO}
THINK DEAREST? AREN'T
YOU ALSO RATHER STRUCK
WITH THE "GAME"? CARIAD!!!
I LOVE YOU GWENNIE DEAR,
A.M.H.L.
```

Normalized English: **Gwennie darling. Golf is a good game for two, but I don't think it beats our game of "In the Gloaming" (also for two!). What do you think, dearest? Aren't you also rather struck with the "game"? Cariad!!! I love you, Gwennie dear. A.M.H.L. Arthur.**

The text is English; the only foreign word is Welsh **cariad**, "darling, love", natural on a card to Colwyn Bay in North Wales. "In the Gloaming" is a popular Victorian love song (1877); the writer uses it as a playful name for courting at dusk, set against the golf of the picture.

Slovak translation: **Gwennie, miláčik. Golf je dobrá hra pre dvoch, ale nemyslím si, že prekoná našu hru „V súmraku“ (tiež pre dvoch!). Čo si o tom myslíš, najdrahšia? Nie si aj ty tou „hrou“ dosť uchvátená? Cariad (miláčik)!!! Ľúbim ťa, Gwennie drahá. A.M.H.L. Arthur.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1485/work/decode.py
```

The script checks the SHA-256 of the three files in source/, decodes work/transcription.txt with work/key.json, and prints the literal decipherment and the reading with the slips marked. Exit code 0 means the hashes matched. The transcription itself is manual and was confirmed independently in review.

## Uncertainties

- **Three writer's slips.** The glyphs are clear on the scan; the reading corrects them. In "BOT" (line 3) and "YOO" (line 6) the U is written as a plain square without its diagonal (compare YOU on lines 8 and 10, OUR, STRUCK). In "CAME" (line 4) the first sign has its two left ticks high on the stem (C) instead of low (G, as in GAME on lines 2 and 9). The reviewer confirmed all three literal forms at 8–10× enlargement. The sister card HCP 1484 shows none of these slips.
- **Initials A.M.H.L.** Deciphered literally (A = dotted circle, M = one low right tick, H = three low left ticks, L = three high right ticks). Their meaning is not established. They might be a lovers' formula (a guess such as "all my heart's love") or initials; neither is asserted.
- **Small scan.** The image is only 1024 px wide, so ticks are 2–4 px features. Each count was checked on enlargements, and every one agrees with the key except the C/G slip above.
- **Word division** is partly editorial where the spacing on the card is tight; it does not affect any letter.
- **Inferred key letters.** J, P and Q are filled in from the grid; X and Z are unknown.
- **People and date.** Arthur and Gwennie (Miss G. Williams) are not otherwise identified. The postmark is not fully legible on the scan; the date "around 3.1908" is portal metadata.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (all hashes OK, output identical to the claimed plaintext), decoded the transcription with its own script built from the construction rule alone (172 letters, 21 sign types, nothing unmapped), compared all ten lines and the initials with its own enlargements of the scan, confirmed the three slips as genuine literal forms, and checked the language and context. Its four minor findings and what changed:

- **Address misread.** The house and street had been read provisionally as "Bowntree", Oak Road; the scan shows **"Baronhill", York Road**, as also read on HCP 1484. Corrected in SOLUTION.md and this report. The cipher is unaffected.
- **Sister card.** HCP 1484, deciphered independently with the same construction, is now cited as support for the key; it shows none of the slips found here.
- **Slips.** Kept as literal glyphs corrected in the reading, with the literal forms shown above.
- **Initials.** Left unexplained; any expansion is marked as a guess.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1485, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1485 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4516/conversions/pc_hcp_166_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4515/conversions/pc_hcp_166_pic-large.jpg (source/picture-large.jpg).
- Sister card: ciphers/hcp-1484 in this repository (pc_hcp_165).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.

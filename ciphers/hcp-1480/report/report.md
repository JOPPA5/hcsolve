# HCP 1480 (pc_hcp_161): an English love note to "Idie", Swanage 1910

Human solver: Tomáš Pavuk

**Status: deciphered in full (61 of 61 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1480 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1480), portal name pc_hcp_161, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution / Monoalphabetic, date 1910-07-17, language **Unknown**, location Europe, sender **Unknown**, recipient Light, with no transcription or solution attached.

It is a British "Valentine's Series" picture postcard showing the *Depot Gateway, Dorchester*. The picture side carries no writing. The address side is addressed in plain writing to **Mrs Light, Police Station, Swanage, Dorset, Local**. It has a green halfpenny King Edward VII stamp cancelled **SWANAGE / DORSET, 4.30 PM, 17 JY 10** (17 July 1910). "Local" means that the card was posted inside Swanage.

The message is written on the left half of the address side, in seven short lines of small geometric signs: triangles, squares, crosses, circles, bars and similar shapes. Word spaces are kept. The pencil notes at the top left ("CODED MESSAGE TO POLICE STATION", "13.50", "AR38") were added later, probably by a dealer or collector. They are not part of the cipher. The large wheel and the letters behind the text are the HCPortal watermark.

![Address side: the seven cipher lines at left, the address of Mrs Light at Swanage Police Station at right, the Swanage postmark of 17 July 1910 (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Depot Gateway, Dorchester; no cipher writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The signs were transcribed **by hand** from enlarged crops of the address scan. Each distinct shape got a conventional label (for example TRI for an upright triangle, BOX for a square, CROSS for ×). Every word was written as a sequence of labels, with word spaces and line breaks kept as on the card (work/transcription.txt, 61 signs). No OCR was used, and the portal supplied no transcription.

Since the word spaces are kept, the cipher could be attacked through word patterns. The two-sign word in line 1 and the four-sign word IDIE in line 6 use the same two signs (× and △), which suggests a name. The repeated seven-sign word in lines 1 and 5 gave DEAREST, and the familiar postcard formula followed: "just a card with love and kisses, ever yours". Every value was then checked against every occurrence of its sign. The vowels turn out to be simple shapes (A circle, E square, I cross, O angle, U cup). That points to an ad-hoc private alphabet, not Pigpen or any other published scheme.

The first pass (OpenAI GPT, 2026-10-26) left four positions open, all in line 5. On 2026-10-29 Claude Opus 5.5 re-examined them at 8–9× enlargement:

- The second sign of the two-sign word, first read as a "hook", is the same rounded arch on a flat base with a ticked right leg as the first sign of YOURS. Its upper arc is in faded, dry-pen ink. It is therefore Y.
- The first sign of that word, first read as "bar with a lower mark", is one T-shaped sign: a bar with a faint stem and a small foot. In context (?Y before "dearest") it is M, giving MY.
- The second sign of YOURS is the pointed-C sign of the O in LOVE, with one small extra dot above it. It is read as O.

![Left: first sign of YOURS; right: the former "hook", the same arch sign with a faded upper arc (work/arch-vs-hook-claude.png)](../work/arch-vs-hook-claude.png)

![The two-sign word MY in line 5: T-shaped sign (M) and arch (Y) (work/my-group-claude.png)](../work/my-group-claude.png)

In review, a separate Claude Opus 5.5 agent made its own crops (4× per line, 8× for the critical groups), wrote its own transcription with its own labels and decoded it with its own script. Its output is identical to the solver's in all 61 positions.

## Key

Monoalphabetic substitution with a home-made set of geometric symbols. The descriptions below are conventional names for hand-drawn shapes. Four pairs of labels are hand-drawn variants of one sign: BOX/BOX_BAR, BAR/SLANT_BAR, DIV/CURVED_BAR_TWO_DOTS, C_SHAPE/DOTTED_C.

| Sign (label) | Letter | Sign (label) | Letter |
|---|---|---|---|
| ○ open circle (CIRCLE) | A | ⊠ square with cross (BOX_CROSS) | K |
| low stroke with left upturn (UNDER) | C | — horizontal bar (BAR, SLANT_BAR) | L |
| △ upright triangle (TRI) | D | ⊤ bar with stem and foot (T_STEM) | M |
| □ square (BOX, BOX_BAR) | E | curl like a cursive 2 (CURL_N) | N |
| ▷ right-pointing triangle (RIGHT_TRI) | H | pointed C / < (C_SHAPE, DOTTED_C) | O |
| × cross (CROSS) | I | ÷ bar with dots (DIV, CURVED_BAR_TWO_DOTS) | R |
| ⊕ circle with cross (CROSS_CIRCLE) | J | ▽ with central stroke (DOWN) | S |
| ▯ tall narrow rectangle (RECT) | T | stem between curved strokes (CUP) | U |
| ∧ caret (CARET) | V | wave (WAVE) | W |
| rounded arch on base, right leg ticked (ARCH) | Y | | |

Nineteen letters occur. B, F, G, P, Q, X and Z do not occur, so their signs (if the writer had any) are unknown. Sign counts: E 9, S 7, D 6, I 6, A 5, R 5, T 4, L 3, O 2, U 2, V 2, W 2, Y 2, and C, H, J, K, M, N once each (61 in all).

## Plaintext

Transcription, line by line (labels; `/` = word space):

```text
TRI BOX_BAR CIRCLE DIV BOX DOWN RECT / CROSS TRI
CROSS_CIRCLE CUP DOWN RECT / CIRCLE / UNDER CIRCLE DIV TRI
WAVE CROSS RECT RIGHT_TRI / BAR C_SHAPE CARET BOX / CIRCLE CURL_N TRI
BOX_CROSS CROSS DOWN DOWN BOX_BAR DOWN / BOX CARET BOX CURVED_BAR_TWO_DOTS
ARCH DOTTED_C CUP DIV DOWN / T_STEM ARCH / TRI BOX CIRCLE DIV BOX_BAR DOWN RECT
CROSS TRI CROSS BOX
WAVE CROSS BAR SLANT_BAR
```

Decoded English, as on the card:

```text
DEAREST ID
JUST A CARD
WITH LOVE AND
KISSES EVER
YOURS MY DEAREST
IDIE
WILL
```

Normalised (punctuation editorial): **Dearest Id, just a card with love and kisses. Ever yours, my dearest Idie — Will.**

English translation: the plaintext is already English; in modern wording, **"Dearest Id, just a card with love and kisses. Ever yours, my dearest Idie — Will."**

The language is **English**, replacing the portal's "Unknown". The phrasing ("just a card with love and kisses, ever yours") is a common Edwardian postcard formula, and it fits a card posted in Swanage, Dorset, in 1910.

Slovak translation: **Najdrahšia Id, len pohľadnica s láskou a bozkami. Navždy tvoj, moja najdrahšia Idie — Will.**

Notes on the reading:

- **Id / Idie** are kept exactly as enciphered. They are evidently the same pet name in two forms (perhaps for Ida or Edith), used in the greeting and again before the signature. The person is not identified.
- **Will** is the signature. The portal records the sender as Unknown, and his identity remains unknown. The card is addressed to Mrs Light at Swanage Police Station. Whether she is "Id" herself, or the card was sent to her address for someone else, cannot be decided from the card.
- The pencilled "Coded message to police station" is a later collector's remark. The message itself is a private love note with nothing to do with police work.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1480/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the three files in source/, decodes the manual transcription work/transcription.txt with the key work/key.json, asserts that every sign is mapped, and prints the seven plaintext lines followed by `-- 61 signs, all mapped; source hashes OK`. It does not read the image. The transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Context-only letters.** C, H, J, K, M and N each occur once, and Y twice, so their values rest on the words they make (CARD, WITH, JUST, KISSES, MY, AND, YOURS), not on repeats. In each case no other letter gives an English word.
- **Faint strokes in line 5.** The upper arc of the second ARCH (Y) and the stem of the T_STEM (M) are in faded ink at the limit of the 1024-pixel scan. Both solver and reviewer see them, but a higher-resolution scan would make them firmer.
- **The dotted O.** The O of YOURS carries one small dot above it. It is treated as a stray or decorative dot; it does not affect the reading.
- **Variant merges.** Four pairs of slightly different shapes are taken as hand-drawn variants of one sign (E, L, R, O). Each merge is consistent with every occurrence.
- The identities of Will, of Id/Idie and of Mrs Light are not established. Line 5 is read left to right and then on to line 6, following the layout.
- No prior publication of this card was found: the portal shows Not solved with no attached solution, and the AI Decipherment Register had no entry for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, wrote an independent transcription and decoder, and got identical output in all 61 positions. It checked every sign of every line on 4× and 8× autocontrast crops, including the three line-5 signs restored in the second solving round, and recomputed the sign counts. It confirmed that the text is natural period English and that no published solution was used. Its four findings were minor:

- **Context-only singletons.** Already disclosed; repeated in the uncertainties above.
- **Stale legend.** work/transcription-legend.md now begins with the current label set and marks the old labels HOOK, CURVED_DIV and BAR_LOWER_MARK as superseded.
- **Language and sender.** This report states that the language is English and that the sender signs as Will, identity unknown.
- **Type.** Recorded as MASC (ad-hoc geometric symbols, not Pigpen).

No decoded letter changed as a result of the review.

## Credits

The source capture, transcription, shape labels, most of the key and the main reading were made on 2026-10-26 by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), with four positions left open. On 2026-10-29 Claude Opus 5.5 re-checked all signs, resolved the four open positions and completed the decipherment. The review, the response to it and this report are by Claude Opus 5.5 agents.

## Sources

- HC Portal record 1480, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1480 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4501/conversions/pc_hcp_161_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4500/conversions/pc_hcp_161_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

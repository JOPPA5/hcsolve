# HCP 1800 (pc_hcp_481): a numbered-Pigpen postcard to William S. Wilson, Highrock, Pa.

Human solver: Tomáš Pavuk

**Status: deciphered in full (48 of 48 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1800 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1800), portal name pc_hcp_481, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, Pigpen, category Substitution / Monoalphabetic, location North America, language and date unknown, sender Unknown, recipient William S. Wilson, with no transcription or solution attached.

The picture side is a comic photographic card: a young man and a young woman kissing on top of a tall step-ladder, with the printed caption **LOVE AT IT'S HEIGHT.** Directly under the caption the sender wrote two lines of small square signs, each a Pigpen-like outline with a numeral 1, 2 or 3 inside it. The scan is delivered sideways; the images below are turned upright.

The address side is in plain writing: **Mr. William S. Wilson / Highrock, / Pa.** It is a divided back ("This space may be used for correspondence"), printed by the Douglass Post-Card Co., 27 N. 10th St., Philadelphia, and franked with a red 2-cent George Washington stamp of the US 1903 series. A faint circular postmark left of the stamp shows only "...ORK"; the town and the date cannot be read. Divided backs were allowed in US mail from 1 March 1907, and the 1903 Washington stamp was replaced in 1908–09, so the card was most likely sent **c. 1907–1910**. A pencil note "30- SECRET CODE" in the top left corner is a later dealer or collector mark. The sender is not named.

![Picture side turned upright: couple on a step-ladder, caption "LOVE AT IT'S HEIGHT." and two cipher lines below it (work/upright.jpg)](../work/upright.jpg)

![The two cipher lines, enlarged (work/text-large.jpg)](../work/text-large.jpg)

![Address side: Mr. William S. Wilson, Highrock, Pa.; divided back, 2-cent Washington stamp (source/address-large.jpg)](../source/address-large.jpg)

No other cipher text was found on either side. The large circular watermark crossing both images is the HC Portal's own.

## Method

The sources (both portal scans and the rendered portal record) were captured by an OpenAI GPT solver session (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26), which also made rotated and enlarged working images but reached no stable transcription. On 2026-10-30 Claude Opus 5.5 completed the work.

The signs are clearly a Pigpen variant: each is one of the nine cell outlines of a 3×3 grid (some combination of top, bottom, left and right strokes), with a small handwritten numeral inside. The same system, with numerals 1–3 selecting one of three blocks of the alphabet, occurs on the sister card HCP 1193; closely related cards (HCP 1131, 1189, 1190) use one, two or three dots instead of numerals. That key was taken over as a hypothesis and tested on this card.

The transcription is **manual**. Each of the 48 signs was read from 2–6× enlarged, contrast-stretched crops of the 1024-pixel portal scan (each sign is only about 10 pixels high) and written down as outline + numeral, e.g. `TL2` = strokes top and left, numeral 2. The token list is kept in work/transcription.txt and decoded by a short script (work/decode.py), which also checks the SHA-256 hashes of the source scans. No OCR was used, and the portal supplied no transcription. The key decodes every sign of the card into nine ordinary English words, with no unknown or leftover sign.

## Key

Monoalphabetic substitution (MASC), Pigpen family. The outline selects the position in a 3×3 grid; the numeral selects the block: 1 = A–I, 2 = J–R, 3 = S–Z.

| Outline (strokes present) | Token | 1 | 2 | 3 |
|---|---|---|---|---|
| bottom + right | BR | A | J | S |
| bottom + left + right | B | B | K | T |
| bottom + left | BL | C | L | U |
| top + bottom + right | R | D | M | V |
| all four sides | C | E | N | W |
| top + bottom + left | L | F | O | X |
| top + right | TR | G | P | Y |
| top + left + right | T | H | Q | Z |
| top + left | TL | I | R | — |

Twenty letters occur on the card: A B C D E F G H I K L M N O P R S T U Y. There are no word dividers other than blank space, and no punctuation.

## Plaintext

Transcription, word by word (outline + numeral):

```text
Line 1
TR3 L2 BL3 TL2                       YOUR
TL2 L2 BL1 B2 TL1 C2 TR1             ROCKING
BL1 T1 BR1 TL1 TL2                   CHAIR
TR2 BL2 BR1 C2                       PLAN
BL2 L2 L2 B2 BR3                     LOOKS
Line 2
BR3 BR1 L1 C1 TL2                    SAFER
BR1 C2 R1                            AND
R2 L2 TL2 C1                         MORE
BL1 L2 R2 L1 L2 TL2 B3 BR1 B1 BL2 C1 COMFORTABLE
```

English, as on the card:

```text
YOUR ROCKING CHAIR PLAN LOOKS
SAFER AND MORE COMFORTABLE
```

Punctuated: *"Your rocking-chair plan looks safer and more comfortable."*

The message is a joke on the printed picture: compared with kissing on top of a tall step-ladder ("love at its height"), the recipient's plan of courting in a rocking chair looks safer and more comfortable.

Slovak: *„Tvoj plán s hojdacím kreslom vyzerá bezpečnejšie a pohodlnejšie."*

The full plaintext is reproduced from the repository root with:

```sh
python3 -I ciphers/hcp-1800/work/decode.py
```

which prints `source hashes OK` followed by the two lines above.

## Why the reading is believed correct

- One fixed key, already attested on sister cards, decodes all 48 signs; nothing is left over and no sign was guessed or restored.
- Repeated letters keep their sign throughout: O = L2 seven times, R = TL2 six times, A = BR1 five times, C = BL1, E = C1, L = BL2 and N = C2 three times each.
- The result is a single grammatical English sentence, idiomatic for American English of the 1900s, and it fits the printed picture exactly. Fitting a known key to noise would not produce this.

## Uncertainties

1. **Low resolution.** Only the portal's 1024-pixel scans exist; signs are about 10 pixels high and the watermark crosses the text.
2. **R in MORE**: the left stroke and numeral 2 are clear, the top stroke is faint or invisible. Read as R from the word.
3. **M in COMFORTABLE**: the outline (top + bottom + right) is certain, but the numeral looks closer to a 3 than a 2 (3 would give V, "COVFORTABLE"). M is fixed by context, not by the pixels.
4. **K and S in LOOKS**: outlines clear; K's numeral is indistinct and the final S's numeral is faint against the right edge. Context-supported.
5. **First R of ROCKING and P of PLAN**: the base of the numeral 2 sits low and can look like a bottom stroke; read from the stroke ends. The alternatives make no words.
6. **Date and sender**: unknown; c. 1907–1910 from the divided back and the stamp. The identity of William S. Wilson of Highrock (High Rock), Pennsylvania, was not researched.

None of these affects the sense of the message.

## Review and what changed

An independent Claude Opus 5.5 reviewer re-ran the reproduction command, wrote its own decoder that builds the key from the grid geometry (review/work/indep.py) and obtained the same two lines; it re-read every word on its own 5–12× crops of the scan and confirmed the outlines, in particular the closed boxes of N and E against the open boxes of O and F, and the G of ROCKING. Verdict: **ACCEPT**, with four minor findings, all accepted:

1. The sign count was misstated as 47; it is 48. Corrected.
2. Repetition counts (R six times, A five times) and the list of attested letters (U was missing; 20 letters) were corrected.
3. The M of COMFORTABLE, the R of MORE and the numerals of K and S in LOOKS are now stated explicitly as fixed by context rather than by the pixels.
4. The dating was refined to c. 1907–1910 from the divided back, and the partial postmark was noted.

No letter of the decipherment changed.

## Credits

Source capture and first examination: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Transcription, identification of the key and decipherment: Claude Opus 5.5, 2026-10-30. Independent review: a separate Claude Opus 5.5 agent. No previously published solution of this card was found or used.

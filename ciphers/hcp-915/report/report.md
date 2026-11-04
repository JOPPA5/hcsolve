# HCP 915 (cpc_--_IE____): "Give me a kiss" in Ogham on an Irish postcard

Human solver: Tomáš Pavuk

**Status: deciphered in full (12 of 12 Ogham letter groups); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 915 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/915), portal name cpc_--_IE____, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender and recipient Unknown, with no transcription or solution attached.

It is an Irish comic picture postcard printed by "Lawrence, Publisher, Dublin". The picture shows a young man in a hat kissing a girl; the printed caption reads, in green Gaelic type, "Arrah na Pogue" (the title of Dion Boucicault's Irish play of 1864, "Arrah of the Kiss") and below it in English "Give me a Kiss". The back is an undivided "Post Card" back ("The address to be written on this side") with an empty printed STAMP box; such Lawrence cards date from about 1900–1905. The card was never posted: there is no address, no message, no stamp and no postmark.

All handwriting is in pencil on the picture side, in the blank margin left of the picture, written with the card turned 90 degrees:

1. an **Ogham** inscription on a hand-drawn stem line (the cipher);
2. beside it, the same words in Irish written in Gaelic (insular) script, unenciphered.

![Picture side as scanned (work/picture_small.jpg)](../work/picture_small.jpg)

![The pencil lines turned so that they read left to right: the Gaelic-script line above, the Ogham below (work/strip_upright.jpg, from the high-resolution scan)](../work/strip_upright.jpg)

![Address side: unused, no address, the printed STAMP box empty (work/address_small.jpg)](../work/address_small.jpg)

Hidden writing was looked for on purpose, because many cards in this collection carry a message under the stamp, inside the picture or along the edges. This card has no stamp (and no trace of one having been stuck on and removed), the address side is blank, and neither side shows further writing at the resolution of the scan. The only other marks are the printed texts and the HCPortal watermark.

## Method

The transcription is **manual**: the solver cropped the pencil strip from the un-converted high-resolution scan (3410 x 2265 pixels), turned it upright and read every stroke group on 3–5x enlargements. Each group was recorded by its shape: strokes above the stem only, below only, straight across, slanted across, plus the extra marks (a bar, a dot, an acute, the separators). The recorded groups were then decoded with the standard Ogham table by a short script, and the result was compared with the unenciphered Gaelic-script line.

The Gaelic-script line was read by eye; it is plain writing and is not produced by the script. The reproduction command (from the repository root) is

    python3 -I ciphers/hcp-915/work/decode.py

It checks the SHA-256 hashes of the four scans, decodes work/transcription.txt and prints the literal reading, the reading with diacritics, the counts (12 letters, 2 separators, 1 final dot) and, labelled as a manual reading, the plain line.

## Key

Ogham is the early medieval Irish alphabet of notches and strokes along a stem line. Used as here, it is a fixed-script letter-for-letter (monoalphabetic) substitution; the writer added Irish diacritics on top. With the stem horizontal and read left to right:

| Group | 1 stroke | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| below the stem only (B-aicme) | b | l | f | s | n |
| above the stem only (H-aicme) | h | d | t | c | q |
| slanted across (M-aicme) | m | g | ng | z | r |
| straight across (vowels) | a | o | u | e | i |

Extra signs on this card: a horizontal bar above the stem = p; a dot above = lenition (séimhiú, written today as h after the letter); an acute above = length mark (fada); two dots (:) = word separator; a dot below the stem at the end = full stop.

## Ciphertext and plaintext

Transcription (H = above, B = below, X = straight across, M = slanted across, number = strokes; ^ = lenition dot, ' = acute, P = bar):

    H2 X1 B1^ X1 X5 M5 : H2 X2 M1 : P X2' M2 .

| Word | Groups | Letters |
|---|---|---|
| 1 | H2 X1 B1 X1 X5 M5 + dot | d a b(h) a i r |
| 2 | H2 X2 M1 | d o m |
| 3 | bar, X2 + acute, M2, final dot | p ó g . |

Ogham, letter for letter: **dabair dom pog.** With its marks: **dabhair dom póg.**

Plain Gaelic-script line (manual reading): Taḃair ḋom póg (the g written in its insular form), in modern spelling **Tabhair dom póg**.

Irish: **Tabhair dom póg.**

English: **Give me a kiss.**

Slovak: **Daj mi bozk. (Pobozkaj ma.)**

The writer has put the printed English caption "Give me a Kiss" into Irish twice: once in Ogham and once in Gaelic script. "Tabhair" is the imperative of "give", "dom" is "to me" (the older spelling with lenition, ḋom, appears in the script line), "póg" is "kiss", the same word as "pogue" in the printed play title.

## Uncertainties

- **First letter D, not T.** The first Ogham group clearly has two strokes above the stem, which is D; T would have three. Both solver and reviewer checked this at 4x and found no trace of a third stroke. The literal reading is therefore "dabhair"; the T of "tabhair" rests on the parallel plain line and on word sense. It is a slip of the writer (or, less likely, a deliberate voiced spelling); with one such letter it cannot be decided.
- **P as a bar.** Classical Ogham has no fixed common sign for p; here a horizontal bar above the stem, not touching it, is used. Reading it as p rests only on word sense ("póg") and on the plain line.
- **Position of the lenition dot.** In the Ogham the dot stands after the b-stroke, slightly right of the second a-stroke, not directly over the b; in the Gaelic-script line it sits between b and a. It is assigned to b (bh) from the spelling of "tabhair", not from its position.
- **No dot on "dom" in the Ogham**, while the script line has ḋom. Both spellings are acceptable Irish.
- **Final dot** below the stem is read as a full stop.
- **Writer, date and recipient** are unknown; the card is unused, and the date range c. 1900–1905 rests only on the printed card (Lawrence, Dublin, undivided back). Faint writing below the resolution of the scan cannot be ruled out, but none is visible.
- No published solution of this card was found; the portal attaches none.

## Review summary

Reviewer: a separate Claude Opus 5.5 (Anthropic) agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), cut and enlarged the Ogham strip from the high-resolution scan itself, read every stroke group independently and decoded its own transcription with its own script; its transcription matched the solver's group for group. It confirmed the Gaelic-script line, the Irish grammar and both translations, the blank address side and the empty stamp box. Its findings were minor and are reflected here:

- **D vs T** and **P as a bar**: agreed as disclosed uncertainties; nothing changed.
- **Dot position**: the description was corrected to "after b, not directly over it".
- **Count**: the solution had said "17 groups"; it now says 12 letter groups, 2 separators and 1 final dot, plus 2 diacritics, and the script prints these counts.
- **Script line**: the decoding script now labels the Gaelic-script reading as manual, not computed.
- **Register type**: MASC; there is no stamp and no hidden writing, so "MASC + Steganography" does not apply to this card.

No letter of the reading changed as a result of the review.

## Sources

- HC Portal record 915, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/915 (source/metadata.md). The portal links the Schrödel postcard collection paper in HistoCrypt: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Picture side: https://api.hcportal.eu/media/2805/cpc_--_IE_____pic.jpg (high resolution, work/hires/) and its large conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/2806/cpc_--_IE_____adr.jpg (work/hires/) and its large conversion (source/address-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03 by the orchestrator: no entry for this card.

Transcription, decipherment and report by Claude Opus 5.5 (Anthropic); no earlier solver worked on this card.

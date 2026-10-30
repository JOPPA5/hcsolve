# HCP 1189 (cpc_--_USA_Hanford_USA_Hanford, California_): a dotted Pigpen postcard to Velma

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1189 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1189), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was acquired on 2026-10-25 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection and Pigpen, category Substitution / Monoalphabetic, date and language Unknown, sender Unknown, recipient Velma Cornel, with no transcription or solution attached.

The picture side is a printed comic card signed "Dwig": a lady buying violets at "$4.00 per bunch" and a fur-coated man, captioned "How can you do it on 9.50 per?". It carries no cipher. The address side is printed "POST CARD", with "Germany" and "Serie No 49" at the foot, and bears a green 1-cent Washington stamp of the 1908–1914 design type under a machine cancel; the cancel shows a day "30" but no legible year, and its town is not securely read. The card is addressed in plain writing to "Miss Velma Cornel, Hanford, Calif."; the forename is clear, the surname less so. The two lines of cipher stand on the left half of the address side. The stamp type suggests roughly 1909–1915, but no date is claimed.

![Address side with the two cipher lines at upper left (source/address-large.jpg)](../source/address-large.jpg)

## Method

The cipher consists of 17 Pigpen-type outlines in two lines, each carrying one, two or three dots, with spaces between words and a full stop at the end. The transcription is **manual**: each sign was recorded as an outline (which sides of the cell are drawn) plus a dot count in work/transcription.txt. The portal supplied no transcription.

The alphabet was not derived from this card alone. The solver carried over the dotted grid alphabet it had established for the related Schrödel cards HCP 1193 and HCP 1190. Applied here it gave English at once over all 17 signs. 11 distinct signs occur; repeated letters (E ×3, A ×2, L ×2, O ×2, V ×2) are drawn the same way each time, and no sign has two values. The text is short, so the confirmation rests on the coherent words and on the match with the addressee's name rather than on statistics.

In review the transcription was checked independently, sign by sign, against enlarged and contrast-enhanced crops of the scan. The reviewer's own reading, decoded with its own script, agrees with the solver's for all 17 signs. Two signs in VELMA are not decidable by dot count alone (see Uncertainties); for them the plain-written name of the addressee on the same card is the deciding evidence.

## Key

A dotted three-block Pigpen variant. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right | A | J | S |
| bottom + left + right | B | K | T |
| bottom + left | C | L | U |
| top + bottom + right | D | M | V |
| all four sides | E | N | W |
| top + bottom + left | F | O | X |
| top + right | G | P | Y |
| top + left + right | H | Q | Z |
| top + left | I | R | (unused) |

Signs used on this card: D, E, A, R, V, L, M, I, O, Y, U.

## Plaintext

As written on the card (word spaces and the final full stop are on the card):

```text
DEAR VELMA
I LOVE YOU.
```

Normalized English (comma and capitals editorial): **Dear Velma, I love you.**

Slovak translation: **Milá Velma, ľúbim ťa.**

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1189/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/transcription.txt with the key above and checks an exact sign-to-letter round trip. It does not read the image; the transcription step is manual and was confirmed independently in review. The round trip only shows that the key is internally consistent, not that the reading is right. The script's final line ("Independent visual review is still pending") predates review 1 and is superseded by it.

## Uncertainties

- **V of VELMA.** The outline is top + bottom + right, but only **two** dots are clearly separable (the right-hand one is elongated and may be two merged dots). Read strictly by visible dots it would be M, giving MELMA. It is read as V (three dots) because the card is addressed to "Miss Velma", and because the V of LOVE has the same outline with three clearly separate dots.
- **E of VELMA.** The closed square carries one wide blob about twice the width of a single dot, which in isolation could be two merged dots (N). It is read as E for the same reason; E occurs twice more on the card with a single dot.
- The other 15 signs are unambiguous and were read identically by solver and reviewer.
- No date is claimed: the cancel shows the day "30" without a legible year, and the stamp only suggests c. 1909–1915. The postmark town is not securely read.
- The recipient's surname (catalogue "Cornel") is less secure than the forename; the sender is unknown.
- The alphabet was transferred from HCP 1193/1190 rather than derived independently; with only 17 signs, this card on its own gives little statistical support for it.
- No published plaintext for this card was found or used; this does not prove that no earlier decipherment exists.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and checked the source hashes, decoded with an independently written decoder, read all 17 signs from enlarged crops of the scan (up to 20× and contrast-enhanced), and compared its reading with the solver's: no sign-level differences. It also checked the context (addressee Velma, the stamp type, the picture side) and found no indication that a published solution had been used. Its two findings were minor and are reflected here:

- The V and E of VELMA are decided by the addressee's name, not by counting dots: this report states the visible counts (two dots on the V, one wide blob on the E) and that the name is the deciding evidence for these two signs.
- The reproduction only round-trips a manual token list: this report states that the round trip is not evidence for the reading and that the transcription was verified sign by sign in review.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1189, General, Description and Attachments tabs, captured 2026-10-25: https://crypto.hcportal.eu/dashboard/cryptograms/1189 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/3628/conversions/cpc_--_USA_Hanford_USA_Hanford,-California__adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/3627/conversions/cpc_--_USA_Hanford_USA_Hanford,-California__pic-large.jpg (source/picture-large.jpg).
- Tobias Schrödel, "Cryptographic postcards", HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (collection context; captured during the HCP 1190 work as ciphers/hcp-1190/source/schroedel-2021.pdf). No published plaintext for this card was used.
- Internal: the dotted grid alphabet of ciphers/hcp-1193/ and ciphers/hcp-1190/, applied here as a hypothesis.

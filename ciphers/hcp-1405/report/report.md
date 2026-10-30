# HCP 1405 (pc_hcp_86): a Caesar-shifted English love postcard to W. Abbott, 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (43 of 43 enciphered letters; three short abbreviation groups kept literal, 6 letters); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1405 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1405), portal name pc_hcp_86, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1908-02-07, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a misreading of Abbott), with no transcription or solution attached.

It is a Raphael Tuck & Sons "Oilette" postcard from the series "Scottish Lochs" (Loch Awe with Kilchurn Castle). The picture side carries no handwriting. The address side, scanned sideways, is addressed in plain writing to **W. Abbott, … Chudleigh, S. Devon** and carries a green halfpenny Edward VII stamp cancelled **WIMBORNE / FE 7 / 08**. The message is written in the left half of the address side: a plain heading **G. H. Friday** (7 February 1908 was a Friday, agreeing with the postmark), followed by six short lines of cipher. The last line is crossed by the upside-down printed publisher's line "Art Publishers to Their Majesties the King & Queen".

The card belongs to a run of cipher postcards in the HC Portal collection sent to W. Abbott in 1907–1908 by one couple (HCP 1386 to 1407), all in the same hand and the same cipher; several are deciphered in this repository (for example HCP 1386, 1390, 1393, 1397 and 1403). The cipher and the couple's recurring formulas were therefore known from those cards; this card was read with a **known key**, not a new key recovery. No published reading of this card was found.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Address side turned upright: heading G. H. Friday and the six cipher lines; WIMBORNE FE 7 08 postmark at the top (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is **manual**: the address side was turned upright and every line was read letter by letter from 3–8× enlarged crops (work/v2/crops/). No OCR was used and the portal supplied no transcription. The reading was then decrypted with a single fixed shift by a script that also checks the hashes of the source files and the round trip (re-encryption gives back the transcript).

The cipher is the simplest kind of substitution: each plaintext letter is replaced by the **next** letter of the alphabet (A→B, …, Z→A); dots between words are kept. Three short groups — `El`, `N. & L.` and `Mu` — recur on the sister cards in the same positions (after "my own" in the greeting, after "my" in the closing, before "girl") and are the couple's private abbreviations. Whether they are plain initials or themselves shifted is not established, so they are kept literal; their shifted values (Dk, M. & K., Lt) are printed alongside for reference.

In review a separate agent rotated and cropped the scan itself, read all six lines independently and decrypted them with its own script (review/work/mydecode.py); it obtained the same six lines and the same count of 43 enciphered letters.

## Key

Caesar shift by one (cipher letter = plain letter + 1). To decrypt, move each letter one place back:

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Line | Ciphertext (as written) | Literal plaintext |
|---|---|---|
| 1 | Nz. Pxo. El Cpz. | MY. OWN. [El] BOY. |
| 2 | J. ibwf. Cffo. | I. HAVE. BEEN. |
| 3 | wfsz. cvtz. | VERY. BUSY. |
| 4 | up-Ebz. | TO-DAY. |
| 5 | Nz. N. & L. Zpvs | MY. [N. & L.] YOUR |
| 6 | Pxo. Mu Hjsm | OWN. [Mu] GIRL |

The heading "G. H. Friday" is plain writing and is not enciphered.

English: **"My own El. boy, I have been very busy to-day. My N. & L. — your own Mu. girl."**

Slovak translation: **„Môj vlastný El. chlapec, dnes som mala veľa práce. Moje N. & L. — tvoje vlastné Mu. dievča."**

The text is a short, natural Edwardian lovers' note. The formulas repeat exactly those of the sister cards: "My own E. L. boy" (HCP 1386, 1403), "my N. & L. … your own … girl" (HCP 1386) and "Mu. girl" (HCP 1390, 1393).

![Line 6 enlarged: Pxo. Mu Hjsm (OWN [Mu] GIRL), crossed by the upside-down printed publisher's line (work/v2/crops/l6e.png)](../work/v2/crops/l6e.png)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1405/work/v2/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, reads the manual transcript work/v2/transcription.json, decrypts every enciphered token with the shift, verifies the round trip, and prints the six literal lines with the summary "43 enciphered letters decoded + 6 abbreviation letters kept literal; hashes OK". It does not read the image; the transcription is manual and was confirmed independently in review.

## Uncertainties

- **Abbreviations not expanded.** `El`, `N. & L.` and `Mu` are kept literal. On this card the greeting group is written `El` without an inner dot, while sister cards write `E. L.`; it is treated as the same group. Their meaning (pet names, initials, or shifted letters) is not established and no expansion is claimed.
- **`Mu`.** A capital M followed by small strokes, crossed by the printed line; the second sign could be u or h. The group is identified by shape and position with the sister cards.
- **`Hjsm` (GIRL).** The second letter is cramped under the printed line and is not individually secure; it is read from the word shape and the series formula. No other letter gives an English word in the slot.
- **Small z forms.** In `Cpz` and `wfsz` the z is a small 1/2-like sign; the z of `wfsz` lies partly under the grey portal watermark. Line 4 `up-Ebz` is faint but all letters are visible.
- **Heading initial** G or C (sister card HCP 1403 has "C. H."); this is plain writing and not part of the cipher.
- The writer's and the recipient's identities beyond "W. Abbott, Chudleigh" are not established. Punctuation and capitals of the English sentence are editorial.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decrypted its own independent transcription with its own script (same result, 43 letters), checked each line against its own enlargements of the scan, confirmed the single key covers every enciphered token, that the heading Friday agrees with the postmark of 7 Feb 1908, and that earlier work was credited. Its four findings were minor:

- **The j of Hjsm** is not individually visible as a distinct letter; this is now listed among the uncertainties.
- **`El` vs `E. L.`** — already disclosed; no change.
- **Same-provider review** — the round-1 completion and the review were both by Claude Opus 5.5 (separate agents); this report and the register entry say so.
- **Heading initial G/C** — already disclosed; no change.

No letter of the reading changed as a result of the review.

## Credit

Earlier partial work in this directory (OpenAI GPT-6 Astra, 2026-10-26) captured the portal record, found the shift and read I HAVE BEEN and TO-DAY, but misread the greeting as MY OWN DEAR and left the rest unresolved. Claude Opus 5.5 (2026-10-29) re-read every line, corrected the greeting (El BOY), read VERY BUSY, TO-DAY and the closing, and wrote the decoder; a separate Claude Opus 5.5 agent reviewed it.

## Sources

- HC Portal record 1405, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1405 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4275/conversions/pc_hcp_86_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4276/conversions/pc_hcp_86_adr-large.jpg (source/address.jpg).
- Sister cards in this repository: ciphers/hcp-1386, 1390, 1393, 1397, 1403, 1406, 1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.

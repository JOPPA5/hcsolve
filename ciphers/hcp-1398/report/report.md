# HCP 1398 (pc_hcp_79): an English love note in Caesar cipher, signed "Loo"

Human solver: Tomáš Pavuk

**Status: deciphered in full (51 of 51 cipher letters); independent review 1 verdict REVISE, all findings addressed, reading unchanged except that the literal DEARST is now reported as written.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1398 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1398), portal name pc_hcp_79, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date and language unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed scene with no handwriting. Everything written is on the address side. Turned 90° counter-clockwise, it reads **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The card carries a green halfpenny stamp of Edward VII, which places it between 1902 and 1910, and a postmark whose visible part reads "…MBORNE" and "10 PM" (perhaps Wimborne; the town and date are not securely legible). Below the address, under the plain heading **Thursday**, stand five short lines of cipher. The heading also has some overwritten initial-like marks and a word that looks like "Today"; none of these is cipher.

The recipient, the hand and the cipher match a group of Caesar cards to W. Abbott at Stokelake Farm deciphered in this repository (HCP 1388, 1395, 1397, and the wider series 1386–1407, dated 1907–08 where a date is legible). This card very probably belongs to the same correspondence. That is supported by the shared address and cipher but not proven, since this card carries no date.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Address side turned 90° counter-clockwise: address at the top, cipher message below "Thursday" (work/reading.png)](../work/reading.png)

![The cipher message enlarged (work/message.png)](../work/message.png)

![Picture side (source/picture.jpg)](../source/picture.jpg)

## Method

The transcription is **manual**: the scan was turned upright and each word read letter by letter on enlarged crops (no OCR; the portal supplied no transcription). The ciphertext is in ordinary Latin cursive. Groups like `ibwf`, `wjfx` and `bmcvn` are recognisable English words shifted by one letter (HAVE, VIEW, ALBUM), as on the sister cards, so a Caesar shift of −1 was tested and decodes every word.

The work was done in stages. The OpenAI GPT solver (GPT-6 Astra) made the transcription and the reading on 2026-10-26 but left the first letter of the signature open between M and N. Claude Opus 5.5, acting as solver, read it as a capital M on 2026-10-29. In review a separate Claude Opus 5.5 agent re-read every word on its own 3–8× crops (thresholded to remove the grey printed watermark wheel) and decoded its own transcription with its own script. It found one transcription error, corrected here (see the review summary).

## Key

Caesar cipher: each cipher letter stands one place after its plaintext letter in the alphabet. To decipher, shift each letter back by one.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The plain heading "Thursday" is not enciphered and is not shifted.

## Ciphertext and plaintext

Ciphertext as transcribed (case and dots as on the card):

```text
Nz. pxo. efbstu Cpz.
J. pomz. ibwf uijt
wjfx Jo. nz bmcvn
Zpvs. hjsm
Mpp
```

Literal plaintext:

```text
MY. OWN. DEARST BOY.
I. ONLY. HAVE THIS
VIEW IN. MY ALBUM
YOUR. GIRL
LOO
```

Normalized English (the E of "dearest" is an editorial restoration; the card writes DEARST):

**My own dearest boy, I only have this view in my album. Your girl, Loo.**

Slovak translation: **Môj vlastný najdrahší chlapec, mám v albume len tento pohľad. Tvoje dievča, Loo.**

Notes on the reading:

- **DEARST.** The word is written `efbstu`, six letters: e, one looped f, b (written like a 6), s, a crossed t and u. This writer's f always descends well below the line, and nothing between s and t does, so there is no second f. The card literally says DEARST, a slip (or skipped letter) for DEAREST.
- **The dots** after many words (MY. OWN. … I. ONLY.) are the writer's habit and are kept in the literal text.
- **"This view in my album"** suits a picture postcard: she is sending a view she has only one copy of.
- **The signature** `Mpp` begins with a copybook capital M (a lead-in curl, then three downstrokes joined by two arches; a capital N would have only one arch), followed by two descending p's. It decodes to **LOO**, probably a pet name (perhaps for Louie or Louisa; that is a guess, not established). The closing "Your girl" matches "Your own girl" on the sister card HCP 1388.

![The signature Mpp → LOO, enlarged (work/closing.png)](../work/closing.png)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1398/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the scans, decodes the manual transcription in work/transcription.json with Caesar −1, and prints the five literal rows, a normalized line with DEAR[E]ST, and `51 cipher letters, all decoded with one key (Caesar -1); 0 alternatives.` It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **DEARST** is what the card says; whether the missing E is a slip of the pen or a deliberate shortening cannot be told.
- **The signature initial** is read as M (giving LOO); the solver and the reviewer agree on the enlarged crop, but it is a single cursive capital. "Loo" as a pet form of Louie or Louisa is conjecture.
- **Plain marks** in the heading (overwritten initials, the word after "Thursday") and the postmark town and date are not securely read. No date is recovered; the stamp gives 1902–1910.
- **The sender's identity** is unknown. The link to the 1907–08 Abbott cards rests on the shared address, hand and cipher.
- No published solution of this card was found: the portal shows Not solved with nothing attached, and the AI Decipherment Register had no record for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic, a separate agent), round 1, verdict **REVISE**. The reviewer ran the reproduction command, made its own enlarged and thresholded crops, transcribed the card itself and decoded it with its own script. It confirmed the Caesar −1 key over every letter, every word, and the M of the signature. Its findings and what changed:

1. **major: one word mistranscribed.** The transcription had `efbsftu` (DEAREST) where the card has `efbstu` (DEARST); the earlier transcription had silently supplied the missing letter. Corrected: the literal text now reads DEARST, the restoration of E is marked as editorial, and the letter count is 51 (not 51 + 1).
2. **minor: the command did not print the final reading.** The decoder still printed [L/M]OO. Now the signature is fixed as `Mpp` and the command prints LOO with no alternatives.
3. **minor: SOLUTION.md contradicted itself** (an old "partial" header next to the completion note). Rewritten to state the current claim.
4. **minor: context missing.** The full address, the Edward VII stamp and the postmark are now described, with the link to the sister cards stated as probable only.

The meaning of the message did not change as a result of the review.

## Sources

- HC Portal record 1398, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1398 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4254/conversions/pc_hcp_79_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4255/conversions/pc_hcp_79_adr-large.jpg (source/address.jpg).
- Sister cards to W. Abbott in this repository: ciphers/hcp-1388, hcp-1395, hcp-1397.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

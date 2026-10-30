# HCP 1393 (pc_hcp_74): an Edwardian love note in a Caesar shift, 1907

Human solver: Tomáš Pavuk

**Status: enciphered message deciphered in full (73 of 73 enciphered letters); two short shorthand fields kept literal and unread; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1393 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1393), portal name pc_hcp_74, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1907-04-29, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed colour view, **"Church Parade. Southsea."**, with no handwriting. All the writing is on the address side. It carries a halfpenny Edward VII stamp cancelled **WIMBORNE / 10 PM / AP 29 / 07**, and the address reads Mr W. Abbott, [a farm, probably Stokelake Farm as on the sister card HCP 1397], Chudleigh, S. Devon. The portal's "W. Abboú" is a machine misreading of "Abbott". The message, written to the left of the address, opens with a plain heading **G. H. Monday.** 29 April 1907 was a Monday, so the heading agrees with the postmark.

The card belongs to a run of postcards sent in 1907–08 to Mr W. Abbott of Chudleigh (HC Portal 1386–1407), all written by one woman in the same simple Caesar shift. Several of them are deciphered in this repository (for example HCP 1390 and 1397). The circular A–Z disc that appears on the scans is an overlay added to the scans, not part of the card.

![Picture side: "Church Parade. Southsea." (source/picture.jpg)](../source/picture.jpg)

![Address side turned upright: the enciphered message on the left, the address and the WIMBORNE postmark on the right (work/address-rotated.jpg)](../work/address-rotated.jpg)

## Method

The transcription is **manual**. The portal supplied none, and no OCR was used. The address side was rotated upright, and each line was read sign by sign from 3–6× enlarged crops (work/crops/). A first, partial reading was made on 2026-10-26 by an earlier OpenAI GPT solver. It identified the cipher as a Caesar shift and read the salutation and several phrases. On 2026-10-29 Claude Opus 5.5 re-read the whole card from the pixels. It completed line 2 (GLAD THERE IS ONE), corrected an earlier `mfuufst` to `mfuufs` (LETTER; the scan has no extra t), and read the end of line 4, line 6 and the word in the drawn cloud.

The key follows from the card itself. Long words such as `Efbsftu`, `uifsf`, `mfuufs` and `gspn zpvs pxo` become DEAREST, THERE, LETTER and FROM YOUR OWN when every letter is moved one place back in the alphabet. The same shift is used on all the sister cards. Every one of the 73 enciphered letters decodes under this single shift; no enciphered group is left unread.

In review a separate Claude Opus 5.5 agent rotated the scan itself, made its own enlarged crops, transcribed the letters independently and decoded them with its own script. Its plaintext is identical to the solver's.

## Key

Caesar substitution. Each plaintext letter is written as the **next** letter of the alphabet (encryption +1, decryption −1). Upper and lower case are kept.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Ciphertext as transcribed and its decryption, line by line (punctuation as written on the card). Shorthand fields are not enciphered text and are kept as written.

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading | G. H. Monday. *(plain)* | G. H. Monday. |
| 1 | Nz. Pxo. Efbsftu. J. bn | MY. OWN. DEAREST. I. AM |
| 2 | hmbe. uifsf. jt. pof. | GLAD. THERE. IS. ONE. |
| 3 | npsf. mfuufs. gps. | MORE. LETTER. FOR. |
| 4 | nf. uijt xffl! x  M ? L *(shorthand)* | ME. THIS WEEK! x  M ? L |
| 5 | gspn. zpvs. pxo. | FROM. YOUR. OWN. |
| 6 | M[h] *(shorthand)* "Hjsm" | M[h] "GIRL" |
| 7 | "Ivssbi" *(in a drawn cloud)* | "HURRAH" |

English (punctuation editorial):

**G. H., Monday. My own dearest, I am glad there is one more letter for me this week! x M ? L. From your own M[h] "Girl". "Hurrah"**

Slovak translation:

**G. H., pondelok. Môj najdrahší, som rada, že je tento týždeň pre mňa ešte jeden list! x M ? L. Od tvojho vlastného M[h] „dievčaťa“. „Hurá!“**

Notes on the reading:

- **x** after "week!" is a cross written slightly below the line, read as a kiss. It is not a cipher letter.
- **M ? L** (end of line 4) is a cursive capital M (or N), a small middle sign that looks like r, & or +, and a capital L with a raised mark and an underline. Similar groups occur on sister cards (HCP 1403 has "N. & L."). An expansion such as "much love" is possible but is not claimed. Decoded through the shift, the letters would give L ? K, which makes no better sense.
- **M[h]** (line 6) is a capital M with a raised tall letter that looks like h (b or k not excluded) and dots below. It is unread and unexpanded. Sister HCP 1390 has a comparable closing, which is also recorded there as unread.
- The quotation marks around "Girl" and "Hurrah" are as written. "Hurrah" stands inside a small cloud drawn at the end of the message.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1393/work/decode2.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, reads the manual transcription in work/transcription2.json, decrypts it with Caesar −1, re-encrypts every line to check the round trip, and prints the seven lines above with `enciphered letters decoded: 73`. It does not read the image. The transcription step is manual and was checked independently in review.

## Uncertainties

- **Two shorthand fields** (M ? L and M[h]) are unread. They are probably private abbreviations shared by the couple. The sender is known only by them and as "Girl"; her identity, and the meaning of the heading initials G. H., are not established.
- **Letters read with effort.** The first letter of `jt` (line 2) has the shape of a g (a closed upper loop, a descender, no dot). It is read as j **by context only**: g would give "FS", while IS is required by "glad there is one more letter". A slip by the writer is assumed. The u and i of `uifsf` (line 2) are faint, partly overlaid strokes; f-s-f is firm, and THERE is the only sensible reading. The third letter of `Efbsftu` is a closed loop read as b (o would give "DENREST"). `hmbe` (GLAD) is faint, but each letter is visible. No letter was restored or invented.
- The farm name in the address is outside the cipher and is not securely read.
- No published solution of this card was found. The portal status was Not solved, with no attached solution, and the AI Decipherment Register had no entry for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (its output matched the claimed plaintext) and decoded its own independent transcription with its own script, with the same result: 73 letters under one shift and no unread group. It checked every sign against its own enlarged crops of the scan and confirmed the corrected `mfuufs`. It also confirmed that 29 April 1907 was a Monday and that the addressee and the shift agree with the sister cards. It raised four minor findings, all accepted:

- **Signature abbreviation.** The raised letter after M had been read as a small u ("Mᵘ") and linked to a "Mu." on HCP 1390. The reviewer showed it is an h-like letter, and that HCP 1390 had itself withdrawn "Mu.". It is now recorded as M + raised h-like letter, unread.
- **`jt`.** The first letter is g-shaped. The report now says plainly that it is read as j from context.
- **`uifsf`.** Its faint u and i are now listed among the letters read with effort.
- **M ? L.** The middle sign is no longer asserted to be "&"; it is described as r-, &- or +-like.

No decoded letter changed as a result of the review.

## Credit

Source capture, the Caesar −1 identification and a partial reading were made on 2026-10-26 by an earlier OpenAI GPT solver (model version not recorded in the working files). The complete transcription and decipherment, the response to review and this report were made by Claude Opus 5.5 on 2026-10-29/30. The independent review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1393, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1393 (source/metadata.md, SOURCES.md).
- Picture side and address side scans from the portal (source/picture.jpg, source/address.jpg).
- Sister cards to W. Abbott, Chudleigh, in this repository: ciphers/hcp-1390, ciphers/hcp-1397, ciphers/hcp-1403.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

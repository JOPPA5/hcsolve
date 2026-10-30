# HCP 1384 (pc_hcp_65): a Caesar-shifted love postcard to W. Abbott

Human solver: Tomáš Pavuk

**Status: whole enciphered message read (48 of 48 cipher letters, one of them a disclosed restoration); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1384 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1384), portal name pc_hcp_65, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient W. Abbott (spelled "W. Abboú" in the catalogue), with no transcription or solution attached.

The picture side is a printed view, "Promenade Gardens, Malvern" (Tilley & Son, Ledbury, with the Great Malvern arms), and carries no handwriting. The address side has a plain address, **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**, a halfpenny Edward VII stamp, and a postmark reading WIMB… 10 PM. The date on the postmark is not legible, so this card itself does not establish a year. The disc and building logo across both scans are a scanning overlay, not part of the card.

The message is written across the left half of the address side, under the plain heading **"G. H. Sunday"** (G preferred, as on HCP 1388). The recipient, hand, key and formulas match the cards HCP 1386, 1388, 1395, 1402 and 1403 in this repository, a run of cards from one couple dated on other cards to 1907–08. That the writer of this card is the same woman is an inference from those matches, and her identity is not established.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side rotated for reading (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is **manual**, made from the un-converted original scan of the address side, rotated and enlarged line by line. No OCR was used. The key was taken as a hypothesis from the sister cards and then tested on this card: all 48 letters decode under it with no exception, no nulls and nothing skipped. The reviewer's trial of all 26 shifts found that only this one gives English.

The one difficult word was `Mfuufs`, which at first looked like "M b r u u f". The second sign has an ascender and a descending loop, unlike the b of `mbuf` on the next line, so it is f.

## Key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Ciphertext and plaintext line by line. `[n]` and `[M]` mark the restored letter; the groups in square brackets on the plaintext side are abbreviations kept as written; dots are as on the card.

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. E L. Cpz. | MY. OWN. [E L.] BOY. |
| J. b[n]. Tpssz Nz. | I. A[M]. SORRY MY. |
| Mfuufs xbt. | LETTER WAS. |
| mbuf. | LATE. |
| Nz. N. & L. Gspn | MY. [N. & L.] FROM |
| zpvs Pxo E. L Hjsm | YOUR OWN [E. L] GIRL |

English: **"My own E. L. boy. I a[m] sorry my letter was late. My N. & L. from your own E. L. girl."**

Slovak: **„Môj vlastný E. L. chlapec. Je mi ľúto, že môj list prišiel neskoro. Moje N. & L. od tvojho vlastného E. L. dievčaťa."** (The Slovak sentence does not show the restored M of "am"; see below.)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1384/work/decode.py
```

The script checks the SHA-256 of the two source scans and the two original scans, decodes the manual transcription in work/transcription.json and prints the lines above, ending with `48 cipher letters decoded; abbreviation groups kept literal`. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **`b[n].` (AM), line 2: restoration.** The second letter sits in an ink blot. What shows through is a closed oval with a flat top, closer to o than n. Read literally, `bo` gives AN, which makes no sentence, so n rests on sense and on the formula `J. bn` of HCP 1393, 1395, 1403 and 1406, not on pixels. The writer may have written o by slip; the blot prevents deciding.
- **`xbt.` (WAS), line 3.** The final sign is one plain slanted stroke with no visible cross, and it is the only lower-case cipher t on this card. Only t gives a word here (`xbt` also occurs on HCP 1402, where it is recorded with a tall upstroke; the reviewer did not compare the pixels of that card).
- **`E. L.` and `N. & L.`** Kept literal, as on the sister cards. Their meaning is not established, nor whether they are enciphered; shifted, they would be D. K. and M. & K.
- **Form of these initials.** The second letter of `E. L.` differs between its two occurrences (a 4-like and a k-like shape). The L after `&` has a hook at the top and a foot at the base and differs from both; T or J are not excluded in isolation. The N has the same hook, stem and second leg as the N of `Nz`, so N is preferred, but a blot lies where a third leg of M would be, so M is not fully excluded. HCP 1395 reads this group as `M. & L.`, ciphertext for L. & K. None of this affects the message.
- **Flourish and dots.** After `mbuf.` a long thin curved stroke with a hook runs to the end of the line. It is read as a closing flourish, not a letter. Dots are not significant.
- **Date.** Not established. Below 10 PM on the postmark the top of one more line survives, a D-like sign and a flat-topped sign. A month DE is only a tentative reading; day and year are lost. The sense of G. H. and the writer's identity are also not established.
- **Prior publication.** The portal status (Not solved) and the AI Decipherment Register (checked 2026-10-30, no record of this number) show no earlier solution; no wider search was run.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**, with no blocker or major finding. The reviewer ran the reproduction command, read the card itself from its own enlargements, decoded its own transcription (the same words, 48 letters), and tried all 26 shifts. It confirmed the card's words against the sister cards, and that `mbuf` is a new word for the family, read from clear pixels. Its four minor findings changed the following:

- **Restoration not marked.** The restored letter is now shown as `[n]` and `[M]` in the data, the command output and this report.
- **Unmentioned stroke and inexact dots.** The flourish after `mbuf.` is now recorded, and the dots were corrected to the card.
- **First initial of N. & L.** The possibility of M under the blot, and the treatment on HCP 1395, are now stated.
- **Postmark.** The remains of a further line are now noted, as tentative only.

No decoded letter changed as a result of the review.

## Credit

Transcription, decipherment and this report by Claude Opus 5.5, 2026-10-30, with no earlier work on this number. The key comes from the finished sister cards; their own files record their credits. Independent review by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1384, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1384 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4212/conversions/pc_hcp_65_pic-large.jpg and original https://api.hcportal.eu/media/4212/pc_hcp_65_pic.JPG
- Address side: https://api.hcportal.eu/media/4213/conversions/pc_hcp_65_adr-large.jpg and original https://api.hcportal.eu/media/4213/pc_hcp_65_adr.JPG
- Sister cards in this repository: ciphers/hcp-1386, 1388, 1393, 1395, 1402, 1403, 1406.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.

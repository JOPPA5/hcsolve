# HCP 1397 (pc_hcp_78): a shift-by-one "Scotch view" postcard to Chudleigh

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-27.

## Origin and context

The cryptogram is record 1397 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1397), part of the HCPortal cryptographic postcards collection (private collection), portal name pc_hcp_78. When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard HCPortal collection, category Substitution, date 1907-04-10, language Unknown, location Europe, sender Unknown, recipient W. Abboú, with no transcription or solution attached.

It is a British picture postcard of Frith's Series. The picture side shows **"Trossachs Hotel & Loch Achray"**, a view in the Trossachs in Scotland, with only the printed caption and no handwriting. The address side is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon** (the portal's "W. Abboú" is a misreading of Abbott). The halfpenny Edward VII stamp is cancelled **…ORNE / 7 PM / AP 10 / 07**; only the end of the office name is legible, but it is an English office. A plain date beneath the message reads "April 10th 1907", agreeing with the postmark and with the portal date, Wednesday 10 April 1907. The message is signed with circled initials, most probably **G. H.** (C. H. is not excluded).

The cipher is four short lines of cursive Latin letters on the left half of the card, read with the card turned 90° anticlockwise. The plaintext language is **English** (the portal gives Unknown). The circular alphabet disc that appears across both scans, in the same position on each side, is an overlay on the images, not part of the card, and is not cipher text.

The portal holds a long run of cards to the same recipient (records 1386–1398 and 1401–1407, pc_hcp_67 to pc_hcp_88, dated 1907–1908). A shift-by-one hypothesis suggested by that correspondence was given to the solver at the start, and was then tested on every letter of this card.

![Address side: four cipher lines, the plain date and the circled initials on the left, the plain address on the right (source/address.jpg)](../source/address.jpg)

![Picture side: Trossachs Hotel & Loch Achray, Frith's Series (source/picture.jpg)](../source/picture.jpg)

## Method

The cipher consists of 48 ordinary cursive letters in thirteen words, with the writer's dots between some words. The transcription is **manual**, from a rotated copy of the scan (work/transcript.json); the portal supplied no transcription and no OCR was used.

Subtracting one from every letter turns the whole message into ordinary English, with no exceptions: Efbsftu → DEAREST, tdpudi → SCOTCH, wjfx → VIEW, Mpwf → LOVE, gspn → FROM. The long words make a chance fit impossible. Nothing is left over and no letter is supplied.

In review the transcription was checked independently against the reviewer's own crops of the scan, with particular attention to the capital N of Nz (two downstrokes, so N and not M), the faint "tu" at the end of Efbsftu, the ornate capital M of Mpwf, and the looped x of Pxo. The reviewer's own reading, decoded with its own script, agrees with the solver's for all 48 letters.

## Key

A Caesar shift of +1 for encryption (−1 for decryption): each plaintext letter is written as the letter after it, and Z would wrap round to A.

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | B | C | D | E | F | G | H | I | J | K | L | M | N |

| Plaintext | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |

Letters actually observed on the card: B, D, E, F, G, H, I, J, M, N, O, P, S, T, U, V, W, X, Z (plaintext A, C, D, E, F, G, H, I, L, M, N, O, R, S, T, U, V, W, Y).

## Plaintext

Ciphertext as written on the card (dots and capitals as read in review):

```text
Nz. Efbsftu uijt
pof. jt.b. tdpudi
wjfx Mpwf gspn
zpvs. Pxo. Hjsm.
```

Decrypted, line for line:

```text
MY. DEAREST THIS
ONE. IS.A. SCOTCH
VIEW LOVE FROM
YOUR. OWN. GIRL.
```

Normalized English (capitals and punctuation editorial): **My dearest, this one is a Scotch view. Love from your own girl.** It is followed by the plain date "April 10th 1907" and the circled initials G. H.

"This one is a Scotch view" describes the picture on the card (the Trossachs), not where the writer was: the card was posted in England.

Slovak translation: **Môj najdrahší, táto pohľadnica zobrazuje Škótsko. S láskou, tvoje dievča.** ("pohľadnica" explains "this one"; the feminine closing follows GIRL.)

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1397/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/transcript.json with the shift above, and checks that re-enciphering gives back the transcription. It does not read the image; the transcription step is manual (and was confirmed independently in review). Its transcription splits the line-2 word as "Tdpu di", so the output prints "SCOT CH"; the card has one continuous word, and the letters are the same as above. Its punctuation also differs slightly from the reading given here, which does not affect any letter.

## Uncertainties

- The sender's identity is not established. The circled initials are read G. H. by preference (the first has the tail of this writer's G); C. H. is not excluded. They are not expanded and were not shifted.
- Only the end of the postmark office name (…ORNE) is legible.
- Dots and capitals are manual readings and do not affect the decipherment.
- Which records of the related correspondence suggested the shift was not recorded; the key is verified on this card alone.
- No search for a prior publication was made beyond the portal status (Not solved) and skip.txt; no solution is attached on the portal.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 48 letters from the scan independently, decoded them with an independently written script, and found no letter-level differences. It checked that one shift covers every letter, searched both sides of the card for untranscribed cipher (none), and checked the postmark against the dates. Its four findings were minor and are reflected here:

- The line-2 word is one continuous word, tdpudi / SCOTCH, not "Tdpu di"; the dots and capitals follow the reviewer's reading.
- The circled initials are more likely G. H. than C. H.; this report states that preference.
- The postmark (AP 10 07, an English office ending -ORNE), its agreement with the written date, and the related correspondence are now recorded.
- The plaintext language is stated as English, and the English sentence is given beside the Slovak translation.

No change to the decoded letters resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1397, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1397 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4252/conversions/pc_hcp_78_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4251/conversions/pc_hcp_78_pic-large.jpg (source/picture.jpg).
- Related cards to the same recipient: HC Portal records 1386–1398 and 1401–1407 (context only).

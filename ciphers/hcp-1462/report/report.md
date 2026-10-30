# HCP 1462 (pc_hcp_143): Sadie's postcard to Ralph from Prittlewell

Human solver: Tomáš Pavuk

**Status: deciphered in full (110 of 110 cipher letters, 9 of 9 lines); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1462 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1462), portal name pc_hcp_143, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Unknown, language Unknown, location Europe, sender Unknown, recipient R. E. Holmes, with no transcription or solution attached.

The picture side is a printed view of **Prittlewell Church** (St Mary's, Prittlewell, now part of Southend-on-Sea, Essex). Its bottom margin carries a faint plain-English pencil note. The address side is written to **R. E. Holmes Esq, 12 Bedford Rd, West Green Rd, Tottenham** (north London) and carries a ½d stamp of Edward VII, so the card dates from 1902–1910; the cancellation is not legible in the scan. The message area of the address side holds nine short pencil lines of apparent gibberish (for example "DaRlhpare", "Tiitehrhcuchssh") and one clear "P.S.".

Both scans also carry a large grey alphabet ring with a building-and-padlock emblem. It is the **HCPortal watermark**, which appears on the picture side as well (across the photograph of the church); it is not part of the card and has nothing to do with the cipher.

![Picture side: Prittlewell Church, with the faint pencil note in the bottom margin; the grey alphabet ring is the HCPortal watermark (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: R. E. Holmes Esq, Tottenham; Edward VII ½d stamp; nine cipher lines with a plain "P.S." (source/address-large.jpg)](../source/address-large.jpg)

A sister card, HCP 1460 (pc_hcp_141), uses exactly the same scheme. It is addressed to Miss Ovington, South Tottenham (postmarked 7 March 1905), opens "Dear Sadie" and is signed by another writer. The shared scheme and the Tottenham addresses suggest the two cards come from one circle of correspondents; that is an inference, not established.

## Method

The transcription is **manual**, made from enlarged and contrast-stretched crops of the address side (3–8x); the portal supplied none and no OCR was used. Each physical line was written down as one row (work/transcription.txt); word gaps in the cipher are ignored, and the plain "P.S." is kept outside the cipher.

The letters are ordinary Latin cursive and their frequencies look like English, so a transposition was suspected. The first line, "DaRlhpare", shows the rule at once: reading first, last, second, second-from-last, … inward gives D-e-a-r-R-a-l-p-h, "Dear Ralph". The same rule, restarted on each line, turns every one of the nine lines into English. There is no substitution and no key word.

The earlier OpenAI GPT solver (GPT-6 Astra, 2026-10-26) captured the portal record, downloaded the scans, found the route rule and read lines 1, 3, 4, 5, 7 and 9, some of them provisionally. Claude Opus 5.5 (2026-10-29/30) re-read every line on enlarged crops, newly read lines 2, 6 and the postscript line 8, settled the open letters in lines 3, 5 and 9, and wrote the full transcription and decoding script.

## Key

**Line-by-line route transposition.** For each written line of plaintext letters p1 p2 … pn the writer put the odd-position letters first, left to right, then the even-position letters in reverse order:

cipher = p1 p3 p5 … then … p6 p4 p2

To decipher a line, read its letters alternately from the two ends: first, last, second, second-from-last, and so on to the middle. The route restarts on every line. Example:

```text
cipher   D a R l h p a r e
order    1 3 5 7 9 8 6 4 2
plain    D e a r R a l p h   -> Dear Ralph
```

## Plaintext

| # | Cipher (as transcribed) | Decrypted |
|---|---|---|
| 1 | DaRlhpare | Dear Ralph |
| 2 | Tiitehrhcuchssh | This is the church |
| 3 | Imonttishogiga | I am going to this |
| 4 | eeignnv | evening. |
| 5 | Peswieonostreal | Please write soon. |
| 6 | Iiloooorwormtsdlw | I will do so tomorrow. |
| 7 | YsaiedSr | Yrs Sadie |
| 8 | P.S. WntEswodotaote | P.S. Went to Eastwood |
| 9 | timrignnosh | this morning. |

All 110 cipher letters decrypt under the one rule; none is left over or moved by hand.

**English (original):** "Dear Ralph, This is the church I am going to this evening. Please write soon. I will do so tomorrow. Yrs Sadie. P.S. Went to Eastwood this morning."

**Slovak:** „Milý Ralph, toto je kostol, do ktorého idem dnes večer. Prosím, napíš čoskoro. Ja tak urobím zajtra. Tvoja Sadie. P.S. Dnes ráno som bola v Eastwoode."

The plain pencil note on the picture side reads, tentatively, **"I hope you will u[nderstand?] … message. Sadie"**, probably a hint to the recipient that the address side holds a ciphered message.

![Picture-side pencil note, contrast-enhanced (work/pic-note-2x.png)](../work/pic-note-2x.png)

The text fits the card closely: the picture is Prittlewell Church ("This is the church I am going to this evening"), and **Eastwood** is the neighbouring parish to Prittlewell, on the west side of Southend. "Ralph" fits the initial R. of the addressee, R. E. Holmes. "Yrs" is the usual abbreviation of "yours".

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1462/work/decode-full.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, decrypts each line of work/transcription.txt by the route rule, re-encrypts each result to confirm the round trip, and prints the nine plaintext lines with the summary `9 lines, 110 cipher letters, all decrypted; source hashes OK.` The transcription step itself is manual and was checked independently in review.

## Uncertainties

- **Line 6, 7th letter (weakest point).** The fourth `o` of the run "oooo" lies on the large watermark letter S. On the blue channel the lower bowl of that S is as dark as the pencil while its upper part stays watermark-grey, so a pencil `o` is read over it. It is the only letter that completes "tomorrow" and gives the 17 letters the route needs. A stray dot after the first `o` is ignored.
- **Line 9, 8th letter: n or m.** The sign is narrower and more cramped than the preceding `n` and has a small extra stroke; a literal `m` ("morming") cannot be excluded. `n` is preferred on sense; if the writer wrote `m`, it was a slip. "this morning" stands either way.
- **Line 2.** The first sign is a cursive capital T (loop with descending stem), unlike the Y of the signature, which earlier work had read here. The 10th sign is a heavy, apparently retraced `u`, read as one letter (two would leave the line one letter too long for the route). The 9th sign `c` has a curled top that resembles `e`.
- **Line 1.** The final letters "are" are faint and partly under the watermark W; the 4th sign `l` is a short loop.
- **Line 3.** The 12th sign `i` merges with a watermark arc; its dot sits to the right.
- **Line 5.** The final `l` is crossed by a stroke that belongs to the watermark's symbol row, not to the pencil (earlier work had considered `f`).
- **Line 7.** The last sign has a tall stem but matches this writer's `r` in line 9; reading `h` would give "YhsSadie".
- **Line 8.** The 4th sign is read as a cursive capital E (it could be taken for b); the end "taote" is faint, and its `a` has a dark closing stroke that could be mistaken for `a`+`o`.
- **Picture-side note** is read only in part; the word after "will" and the short word after it are under the watermark ring.
- **A pencil mark "Bssn"/"Bran"(?)** above POST CARD at the top left of the address side is not needed for any line and is probably not part of the message; it is uninterpreted.
- **People and date.** Sadie and R. E. Holmes are not identified further; the postmark is illegible, so the date rests on the Edward VII stamp (1902–1910).
- No published solution of this card was found: the portal status was Not solved, and the AI Decipherment Register had no entry for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), wrote its own independent outside-in decoder (review/work/mydecode.py), which gave the same nine lines and 110 letters, and checked the transcription against its own 4–8x enlargements of the scan, line by line. It judged the plaintext natural Edwardian English and the context (Prittlewell Church, Eastwood, "Ralph" = R. E. Holmes, Edward VII stamp) consistent. Its four findings were minor and are reflected here:

- **Line 9 n/m.** The claim that the 8th sign is "the same as the 7th" overstated the evidence; it is now stated that `n` is preferred on sense and `m` is possible as a slip.
- **Watermark, not printed wheel.** The alphabet ring was earlier called "printed"; it is the HCPortal watermark, present on both scans, and is now described as such.
- **Picture-side note.** A tentative fuller reading, "I hope you will u[nderstand?] … message. Sadie", has been added.
- **Link to HCP 1460.** The shared correspondence is now presented as an inference.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1462, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1462 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4446/conversions/pc_hcp_143_pic-large.jpg (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4447/conversions/pc_hcp_143_adr-large.jpg (source/address-large.jpg).
- Sister card with the same scheme: HCP 1460 (pc_hcp_141) in this repository, ciphers/hcp-1460/.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

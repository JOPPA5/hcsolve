# HCP 1460 (pc_hcp_141): an English concert note to Sadie Ovington, 1905

Human solver: Tomáš Pavuk

**Status: deciphered in full (89 of 89 letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1460 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1460), portal name pc_hcp_141, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Transposition, date 1905-03-07, language Unknown, location Europe, sender Unknown, recipient Ovington, with no transcription or solution attached.

The picture side is a printed view captioned "Westminster Abbey. Coronation Chairs." and carries no cipher text. The address side is a British "POST CARD" (printer: The Photochrom Co. Ltd., London) with a green halfpenny Edward VII stamp cancelled **SOUTH TOTTENHAM, 8 PM, 7 MR 05** (7 March 1905). The address is in plain writing: **Miss Ovington / 23 Gloucester Rd / Sth Tottenham** (with "London" added in pencil). The left half carries six lines of scrambled letters and a plain closing "Ys H.A.r".

![Address side with the six cipher lines at the left (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Westminster Abbey, Coronation Chairs (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The six lines were transcribed by hand from enlarged crops (4–12×) of the address-side scan; no OCR was used and the portal supplied no transcription. The letters are ordinary Latin cursive, so this is not a substitution: the letters of "Dear Sadie" are visibly present in the first line `DaSdeiare`, only in another order.

Reading the first line alternately from the left end and the right end (1st letter, last letter, 2nd letter, second-to-last letter, …) gives `DearSadie`. The same route applied to each following line, restarted at every line, gives `Fatherwasdelight`, `edwiththeConcert`, `lastnightandhas`. These first four lines were found by the earlier solver (OpenAI GPT, 2026-10-26), who left the last two lines unread. Claude Opus 5.5 (2026-10-29) re-read every line from the scan, read the last two lines, and found that the same route decodes them too.

The reviewer wrote its own decoder, typed its own transcription from its own crops, and obtained identical output; it also checked the inverse (encryption) of every line.

## Key

Per-line **transposition** (zig-zag from both ends). For a line of *n* plaintext letters p1 … pn, the writer wrote

p1 p3 p5 … (odd-numbered letters, left to right), then … p6 p4 p2 (even-numbered letters, right to left).

To decrypt, take the written letters alternately from the front and the back of the line. There is no keyword and no substitution; word spaces are removed; each written line is an independent unit.

## Plaintext

Ciphertext as transcribed (89 letters; the small `s` written below the last line between `n` and `o` is the writer's own insertion and is included there):

```text
DaSdeiare
Ftewseihtgldarha
ewtteocrtenChhid
lsngtnhsadahita
akdegveouyitmes
hsogauainsotltrnci
```

Strict route output, line by line:

```text
DearSadie
Fatherwasdelight
edwiththeConcert
lastnightandhas
askedmetgivyeuo
hiscongratulations
```

English (original language, normalized; "t[o]" is editorial, see Uncertainties):

**Dear Sadie, Father was delighted with the Concert last night and has asked me t[o] give you his congratulations. Ys H.A.r**

Slovak translation: **Milá Sadie, otec bol nadšený včerajším koncertom a požiadal ma, aby som Ti odovzdal(a) jeho blahoželanie. Tvoj(a) H. A. r.**

The closing "Ys" (= Yours) and the initials are written in plain text. The content – a concert the evening before, a father's congratulations to a young woman – fits a local card posted in South Tottenham to a South Tottenham address.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1460/work/decode_full.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, decodes every line of work/transcription.txt with the route above, re-encrypts every decoded line and checks it against the transcription, checks that line 5 is an exact anagram of `askedmetgiveyou`, and prints the six decoded lines, the line `6 lines, 89 letters; source hashes and roundtrips OK.` and the editorial reading. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **A writer's slip in line 5.** The written line `akdegveouyitmes` decodes strictly to `askedmetgivyeuo`. Its 15 letters are exactly those of "asked me t give you" (the `o` of "to" was never written). Correct encryption of `askedmetgiveyou` would be `akdegv yuoe itmes`; the card has `akdegv eouy itmes`, i.e. the four letters of the joined middle cluster stand in reverse order. No letter is added or changed in the transcription; only this order slip is interpreted, and "t[o]" is marked as editorial. The reviewer checked that no alternative wording reproduces the card either.
- **The inserted `s` in line 6.** The writer first omitted the final `s` of "congratulations" and added it himself below the line; included at the marked position, it makes the line decode without any deviation. This self-corrected omission is a different kind of error from the uncorrected reversal in line 5.
- **Signs decided by the route rather than by the pixels.** Line 6, the second sign of the joined cluster, is ambiguous between cursive `u` and `n` on the scan; it is read `u` because the route requires it (congrat-u-lations). Line 5, second sign, is an `h`-like form with a small knot and is read `k` (as-k-ed), again largely route-driven. In line 3, `ewtt…` is a plain `t` followed by a separate hooked sign that is given the value `t` from context (wi-t-h t-he). Line 2 opens with a cursive `F` that resembles `I`; line 4 opens with a cursive `l`.
- **The closing initials** "H.A.r" are uncertain in form; the writer, Sadie Ovington and the concert are not identified, and no external records were searched.
- Only the portal's 1024-pixel JPEG conversion of the scan was available; finer stroke details cannot be settled at this resolution.
- No published solution of this card was found; the portal status was Not solved and the AI Decipherment Register had no record for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded its own independent transcription with its own implementation of the route (identical result), checked the inverse encryption of every line, confirmed that the route consumes all 89 letters with no unused or added letter, read every line sign by sign from enlarged crops (5–20×), and confirmed that the picture side has no cipher text and that the credit split between the earlier GPT work and Claude's completion matches the notes. Its four findings were minor wording issues, all accepted:

- **`u`/`n` in line 6:** the visual evidence had been overstated; now described as ambiguous, read `u` as the route requires.
- **`k` in line 5:** now described as an `h`-like knotted form, read `k` largely from the route.
- **`tt` in line 3:** had been wrongly described as a crossed double `t`; it is a plain `t` plus a hooked sign valued `t` from context.
- **Analogy:** the line-5 order reversal and the self-corrected line-6 omission are no longer called "similar slips".

No transcribed or decoded letter changed as a result of the review.

## Credit

Transcription of the first four lines and discovery of the route: earlier solver, OpenAI GPT (2026-10-26). Re-reading of all lines, decipherment of the last two lines, documentation of the line-5 slip, response to review and this report: Claude Opus 5.5 (2026-10-29). Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1460, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1460 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4441/conversions/pc_hcp_141_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4440/conversions/pc_hcp_141_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.

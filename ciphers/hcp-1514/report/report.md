# HCP 1514 (pc_hcp_195): A1Z26 greeting and rotated words from Jack, Alton 1906

**Status: accepted in independent review 1 (ACCEPT); final edition, 2026-10-26.**

## Origin and context

The card is record 1514 of the HCPortal cryptographic postcards collection (https://crypto.hcportal.eu/dashboard/cryptograms/1514), portal name pc_hcp_195, held in a private collection. The portal lists the main category as Transposition, the date as 1906-02-12, the location as Europe, the sender as Unknown and the recipient as "S. Bauks", and its description says "There is transposition and also substitution." When the solver acquired it on 2026-10-26 the record was marked **Not solved**, with no attached transcription or solution.

The address side is addressed to "Mrs S. Bauks (possibly Banks), 12 Grove Rd, Alton, Hants, Local". The catalogue's "Bauks" follows the visible letters, but n/u are easily confused in this script, and Banks is a common surname while Bauks is very rare. The halfpenny stamp is postmarked ALTON HANTS, 5.15 PM (minute uncertain), FE 12 06. 12 February 1906 was a Monday. The picture side is a Frith's Series view, "Farnham Castle Entrance" (No. 36124), with no cipher. The message is written sideways in the communication half. The large lettered disk over the scan is the portal's watermark, not part of the card.

![Address side; the message is written sideways in the left half (portal scan)](../source/address-large.jpg)

## Method

There is no attached transcription. The solver read the card by hand from the scan rotated 270° clockwise and enlarged (`work/numbers.txt`, `work/transcription.txt`). The card uses two systems, matching the portal description:

- The greeting is written as numbers: `13.25 / 19.23.5.5.20.5.19.20 / 4.1.18.12.9.14.7 / 19`. All are in 1–26 and decode directly as A1Z26 (1=A … 26=Z) to MY SWEETEST DARLING S.
- The body is in cursive letters, each word rotated by one place. Short words such as `opeh`, `rea` and `ot` show the rule at once (hope, are, to). To encrypt, the first letter of each word was moved to the end; to decrypt, the last letter is moved back to the front. Punctuation stays where it is.

The same rule decodes all 22 body words, including the signature `ackJ` = Jack, with no exceptions and no leftover letters. Word order is unchanged.

## Key

- Greeting: A1Z26 substitution, number n = n-th letter of the alphabet.
- Body: cyclic rotation within each word. Decrypt by moving the final letter to the front (`uiteq` → quite, `ackJ` → Jack).

## Plaintext

Literal decoded text, line by line as on the card:

```
MY SWEETEST DARLING S
shall not be. up untill
tuesday to night. hope
you are well. quite a
treat to have it fine
with best love.
from. Jack.
```

Normalized reading: "My sweetest darling S, shall not be up until Tuesday tonight. Hope you are well. Quite a treat to have it fine. With best love, from Jack."

Slovak translation: „Moja najdrahšia S, prídem až v utorok večer. Dúfam, že sa máš dobre. Je príjemné, že je pekne. S vrúcnou láskou, Jack."

The translation takes "be up" as coming up (to visit) and "fine" as fine weather. Since the card was posted on a Monday, "Tuesday to night" is the following evening. S is an initial and is not expanded.

## Reproduction

From the repository root:

```
python3 ciphers/hcp-1514/work/decode.py
```

It checks the SHA-256 hashes of the scans and metadata, decodes the 18 numbers and 89 cursive letters of the manual transcription, and checks that re-encrypting the result gives back the transcription exactly. It does not read the image; the transcription is manual.

## Uncertainties

- `untill` or `until`: the solver read `ntillu` (two l's), the reviewer `ntilu` (one looped l, a short second one not excluded). The command prints `untill` because it decodes the solver's transcription. The letter count is uncertain; the meaning is the same.
- The first letter of `ouy` (you, line 3) is partly covered by an ink blot.
- In `uesdayt` (Tuesday) the e/s and d are cramped and the t-cross stands over the a. In `ightn` (night) the final n is a weak, e-like stroke. Both words are secure from the rotation rule and the date.
- The terminal s of `halls` (shall) and the rounded w of `ellw` (well) are cursive forms that needed close inspection.
- The recipient's surname is Bauks in the catalogue, possibly Banks. The identities of S and Jack are unknown.

## Review summary

The reviewer was Claude Opus 5.5 (Anthropic) and the verdict was **ACCEPT**. The reviewer transcribed the whole card independently from 4–9× crops and decoded it with an independent script. The readings agree except for one letter count (untill/until), and all 18 numbers and 22 words obey the stated rule. The reviewer also checked the context (postmark date a Monday, "Local" delivery in Alton, the initial S matching the addressee). Four minor findings, all incorporated as disclosures:

- untill/until: now stated as an uncertain letter count rather than a certain misspelling.
- The ink blot over the first letter of `ouy`: now disclosed.
- Letters read with help from context in `uesdayt` and `ightn`: now listed.
- Recipient surname: given as "Bauks (possibly Banks)". This is recorded here and in `SOLUTION.md`; the captured metadata file is unchanged.

The key and plaintext did not change as a result of the review. The closing steps (response to review, this report, register entry) were prepared by Claude Opus 5.5 on behalf of the solver (OpenAI GPT-6 Astra) at the human's request.

## Sources

- Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1514 (General, Description and Attachments tabs, read 2026-10-26).
- Address side: https://api.hcportal.eu/media/4603/conversions/pc_hcp_195_adr-large.jpg
- Picture side: https://api.hcportal.eu/media/4602/conversions/pc_hcp_195_pic-large.jpg
- AI Decipherment Register snapshot (https://ai.hcportal.eu/register/?format=json, 110 records): no entry for this card. This is not proof that no solution was ever published.
- No published solution was used.

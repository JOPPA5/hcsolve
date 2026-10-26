# HCP 1514 / pc_hcp_195 — complete message candidate

Portal freshly showed Not solved on2026-10-26. Complete current reading:
18 numeric positions plus89 cursive letters. Independent review pending.

## Type and key

Mixed A1Z26 substitution and cyclic transposition within each word.
Numeric greeting:1=A,...,26=Z. Cursive body: move each word's final
letter to its beginning. Encryption moved the first letter to the end.
Examples: opeh → hope, uiteq → quite, ackJ → Jack.
Punctuation stays outside the rotation; it is not used as a letter.

## Literal decoded text

```text
MY SWEETEST DARLING S
shall not be. up untill
tuesday to night. hope
you are well. quite a
treat to have it fine
with best love.
from. Jack.
```

Editorial reading, with punctuation and capitalization regularized:
“My sweetest darling S, shall not be up untill Tuesday to night. Hope
you are well. Quite a treat to have it fine. With best love, from Jack.”
UNTILL is the spelling actually produced; no initial I is added to the
literal text. S is an initial, not an expanded name. TO NIGHT is two words.

Slovak translation: „Moja najdrahšia S, prídem až v utorok večer.
Dúfam, že sa máš dobre. Je príjemné, že je pekne. S vrúcnou láskou,
Jack.“ Translation interprets UP as coming over and FINE as fine weather;
these contextual senses are not additional deciphered words.

## Reproduce

From repository root:
`python3 ciphers/hcp-1514/work/decode.py`

No transcription was supplied. work/numbers.txt and work/transcription.txt
are own manual readings of source/address-large.jpg viewed after270-degree
clockwise rotation. Working crops/enlargements are supplied. The script
verifies hashes of both source images and metadata, then decodes these
manual transcripts and asserts exact re-encryption. It does not perform
OCR; transcript/key roundtrips are not independent pixel validation.

## Evidence and limitations

One numerical alphabet and one fixed word permutation cover the entire
message, including greeting and signature. Word order stays unchanged.
The numeric final19 gives S, agreeing with the recipient's catalogue initial.
Cursive rounded terminal s in halls and rounded w in ellw need particular
attention in independent scan review; current readings give SHALL and WELL.
The short single-letter a is retained. There is no remaining unassigned
cipher token in the current reading. Address, postmark, printed captions,
collector marks and watermark are outside the encrypted-message count.
No historical identity for Jack is asserted. No cipher observed on picture.

All three rendered portal tabs inspected; no attached solution encountered.
Register snapshot110 entries has no exact source1514/name pc_hcp_195 match;
absence establishes no priority. No published plaintext was used.
No accepted review, FINAL, PDF report or register entry is claimed.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT, 2026-10-26. The reviewer
re-transcribed the whole card independently and decoded it with an
independent script. The readings agree except for one letter count
(`ntillu` vs `ntilu`). The key (A1Z26 for the greeting, one-letter word
rotation for the body) covers every token with no exceptions.

1. **`untill` may be `until` (minor).** Accepted as an uncertainty. The
   reviewer sees one looped `l` at 8× and cannot rule out a short second one;
   the solver read two. The literal output of the documented command remains
   `untill` (it decodes `work/transcription.txt`, which is not changed). The
   report now states the letter count as uncertain (`untill` or `until`)
   instead of asserting the misspelling. The meaning is the same either way.
2. **Obscured letter (minor).** Disclosed. The first letter of `ouy` (line 3)
   is partly covered by an ink blot; `you` follows from context and the
   rotation rule.
3. **Letters read from context (minor).** Disclosed. In `uesdayt` the `e`/`s`
   and `d` are cramped and the t-cross stands above the `a`. In `ightn` the
   final `n` is a weak, e-like stroke. The rotation rule and the date make
   TUESDAY and NIGHT secure, but these are listed in the report alongside
   `halls`/`ellw`.
4. **Recipient name (minor, metadata).** Correction recorded here and in the
   report, without editing `source/metadata.md`: the catalogue's surname
   "Bauks" is given as "Bauks (possibly Banks)". The third letter of the
   address looks like `u`, but n/u confusion is common in this script, and
   Banks is a common surname while Bauks is very rare. The solution relies
   only on the initial S.

Context added from the review: the postmark reads ALTON HANTS, 5.15 PM (minute
uncertain), FE 12 06. 12 February 1906 was a Monday, so "not ... up until
Tuesday to night" refers to the next evening. The picture side is Frith's
"Farnham Castle Entrance" (No. 36124), with no cipher.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.

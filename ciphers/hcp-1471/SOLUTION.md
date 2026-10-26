# HCP1471 / pc_hcp_152 — full question candidate, review pending

Portal freshly Not solved on2026-10-26. Current full16-letter reading:

```text
ARE WE DOWNHEARTED?
```

Slovak: „Sme skľúčení?“ This is a reading of the short question, not a claim
about its author or connection to a particular historical quotation.

## Type and exact key

Caesar+1 for ordinary lowercase cipher letters, with an explicit marked-A
exception. The two source a-shaped glyphs with a small upward-pointing caret
underneath both decode A. They are normalized A^, not silently transcribed z.
This is not claimed to be pure uniform Caesar with ordinary wraparound.

```text
source IDs: A^ q d / v d / c n v m g d A^ q s d c ?
plaintext:  A  R E / W E / D O W N H E A  R T E D ?
```

Observed mappings: A^→A,c→D,d→E,g→H,m→N,n→O,q→R,s→T,v→W.
The marks' historical intention is not established. Treating the same marked
glyph identically is sufficient for this disclosed candidate key.

## Reproduce

From repository root:
`python3 ciphers/hcp-1471/work/decode.py`

No supplied transcription. work/transcription.txt is own manual reading of
source/address-large.jpg; working rotation45degrees clockwise and crop make
the diagonal writing easier to inspect. Original unchanged. Script verifies
hashes of original images/metadata, covers all16letters and checks exact
inverse mapping on the observed symbols. It explicitly checks both marked
exceptions. This validates the mapping, not OCR or independent pixel reading.

## Evidence and uncertainties for review

One ordinary shift handles14letters and one repeated marked-glyph assignment
handles the other2. The complete short text is coherent and uses every
currently transcribed letter; no missing words supplied.

- Third letter of the final cipher word is currently v. Joined cursive nv
  can resemble nw; compare the v in preceding vd. Reading w instead gives
  DOXNHEARTED. Independent review must check the source, not pick v just
  because it makes a word.
- Final cipher letter is currently c. Its loop resembles e; e would give
  finalF, DOWNHEARTEF. Currentc reading needs scan comparison too.
- Both a-shaped glyphs and their caret marks are visible. Assigning A to
  them is an exception in the proposed key, not evidence of the writer's
  intended alphabet convention or a secretly corrected z.

All encrypted text is on address side. Picture contains no observed cipher.
Postal address, postmark, pencil price/collector marks and red9 are excluded
from16-letter count. Catalogue language was Unknown; candidate is English.
All three rendered portal tabs inspected; no attached/published solution used.
Register snapshot110entries has no exact URL1471/name pc_hcp_152 match;
absence proves no priority. Independent review pending, no FINAL/report or
register entry claimed.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read all 16 letters and both carets from source/address-large.jpg before comparing and obtained exactly work/transcription.txt; its own decoder gives ARE WE DOWNHEARTED?. It resolved the two flagged places in favour of the current reading: the third letter of the last word is a single v of the same form as in "vd" (no second stroke, so not w), and the final letter, blurred by the overprinted word UNION, must be the same c as the clear initial c of that word (D…D), not e. The plaintext is unchanged.

1. Describe the key more simply (minor). Accepted. The system is: write each letter as the one before it in the alphabet (B as a, D as c, E as d, …), i.e. a Caesar shift of −1 for encryption, +1 for decryption. The only letter that would wrap round is A (to z); the writer instead wrote a with a small caret beneath it. The caret therefore marks exactly the one letter for which the shift is not applied, which explains the exception; it is not an ad-hoc rule fitted to the text. The writer's own intention behind the mark is inferred, not documented.
2. Catchphrase not mentioned (minor). Accepted as context only. "Are we downhearted? – No!" was a well-known British catchphrase of the period, associated with Joseph Chamberlain around 1906 and later a familiar soldiers' chant. The card is postmarked 5.30 PM, MY 16 06 (Wednesday 16 May 1906). The report mentions this as supporting context; it was not used to obtain the reading, and no external lookup was made to confirm the attribution.
3. Recipient name (minor). Accepted; source/metadata.md is not edited. The card reads Miss Puplett, Beulah, Birchwood Avenue, Swanley Junct., Local; the portal gives "Puklett". The report records the card's reading.
4. Text quality of SOLUTION.md and NOTES.md (minor). Accepted. The missing spaces ("full16-letter", "Finalc", "markedA") are a formatting defect of the solver's text; the earlier sections are not rewritten here, and the report is written with normal spacing. Where they differ, this section and the report supersede the earlier wording.

Remaining uncertainties carried into the report: the last letter under the overprint rests on its identity with the initial c; the writer's identity, and whether the question refers to the slogan, a private matter or both, are unknown; the prior-solution check was limited to the portal attachments and the register snapshot.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.

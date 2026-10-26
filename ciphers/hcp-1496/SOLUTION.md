# Portal1496 / pc_hcp_177 — full numeric-message candidate

Rendered portal Not solved on2026-10-26. A1Z26 number substitution:
1=A,2=B,...,26=Z. Entire manual numeric transcript uses this single key.
Independent review pending.

## Literal plaintext
```
HELLO RICA HOW ARE YOU I WOULD LIKE TO SEE YOU
I SAW SIMON AND HE ASK ME IF I HAD BEEN UP HOME
THAT LOOKS BAD ANS SOON FMS
```

Punctuation and spacing interpretation:
“Hello Rica, how are you? I would like to see you. I saw Simon and he ask me
if I had been up home. That looks bad. Ans soon. FMS.”

ASK is literal, not silently changed to ASKED. ANS is literal, probably
an abbreviation of answer. FMS are decoded initials, not an identified person.
No additional missing words supplied.

Slovak: „Ahoj Rica, ako sa máš? Rád/rada by som ťa videl/videla. Videl/videla
som Simona a pýtal sa ma, či som bol/bola doma. To vyzerá zle. Čoskoro
odpíš. FMS.“ This interprets ASK and ANS in ordinary grammar and preserves
unknown writer gender; UP HOME has no more precise destination established.

## Reproduction
Run from repository root:
`python3 ciphers/hcp-1496/work/decode.py`

There is no attached transcription. work/transcription.txt is an own
line-preserving number reading of source/address-large.jpg. Decoder verifies
immutable source hashes and maps numbers directly; work/words.txt supplies
only spacing, with exact full ordered-letter equality asserted. Inverse-key
roundtrip also passes. These checks are not OCR or independent pixel validation.
There are93 encrypted numeric positions, all mapped. Fresh register snapshot
contains110 entries with no exact URL1496/name pc_hcp_177 match; no priority
claim follows from absence.

## Scope, evidence and uncertainty
All numbers in the correspondence, including initials, are included; address,
postmark and picture caption are excluded. Long coherent English with a
single direct alphabet and no per-word fixes supports the reading.
Reviewer should inspect handwritten15/10 and14/19, especially LOOKS, and
2/3 in BEEN. No undeciphered numeric position in the current transcription.
RICA may relate to Frederica in the address, but the cipher reading does not
depend on that identification. SIMON is mechanically decoded, no biography
or identity claim. Image address Clark and catalogue Celark kept separate.
No published solution used; no accepted FINAL or register entry claimed.

## Response to review 1

Review 1 by Claude Opus 5.5 (2026-10-26), verdict ACCEPT. The reviewer read all
nine rows of numbers independently; the 93-number transcription is identical to
work/transcription.txt and decodes to the same plaintext. No finding changes it.

1. Doubtful glyphs (minor) – accepted and added to the uncertainty list in the
   report: row 6 `4` of AND written over another digit (4 is the final form);
   row 6 last `11` (K of ASK) looks like `13` at normal size but is two plain
   strokes at 20x; row 5 `1` of SAW is a bare stroke squeezed between `19,` and
   `23` that could be taken for a comma; row 8 first `15` of LOOKS could
   graphically be `10` (already flagged); the last number of row 8 is a looped
   `19`. In each case the alternative gives a non-word.
2. Underline strokes (minor) – accepted. The report states plainly that the card
   has no word dividers: numbers are separated by hooked commas, and the long
   underline strokes do not coincide with word boundaries (row 1 underlines LO
   inside HELLO). Word division in work/words.txt is editorial.
3. Addressee spelling (minor) – accepted. The card reads "Miss Friderica Clark,
   Highland Park, Ky." (first name with i after r; surname Clark with a looped
   capital C). The portal's "Frederica Celark" and the earlier image note
   "Frederica Clark" in source/metadata.md are recorded as differing; the first
   name is not normalised in the report. source/ is unchanged.
4. Dating (minor) – accepted. The report adds the terminus post quem from the
   card itself: Bamforth & Co. card "Copyright 1910" and a U.S. 1-cent Franklin
   stamp (Washington–Franklin series), so 1910 or later. The postmark shows only
   fragments (…AND, A…, 18) and gives no reliable date.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.

# HCP 1506 / pc_hcp_187

## A postcard in numeric substitution, Pennsylvania, May 1913

The portal showed **Not solved** on 2026-10-26. Independent review 1 by
Claude Opus 5.5 found the decipherment correct and requested corrections to
the transcription and its scope (REVISE). Those corrections are addressed
below. One raw token remains unmapped, and several handwritten signs have
explicit alternatives. This is a deciphered message with disclosed defects,
not a claim that every mark or identity is certain.

## Origin and reproduction

A private-collection postcard addressed to Miss Leah Doane, Little Marsh,
Pennsylvania, postmarked Knoxville, PA, in May 1913. The portal's recipient
is spelled “Leeah Doane” and sender “Egna”; the cursive signature may read
“Ezra”, but neither that reading nor an identity is established. The exact
date is uncertain: handwriting approximately “May 2[?], 13”, postmark day
possibly 7 or 2. Rendered General, Description and Attachments supplied no
transcription or solution. No supplied or published solution was used.

Run from repository root:

`python3 ciphers/hcp-1506/work/decode.py`

The command verifies hashes of the immutable scans and metadata, decodes
our manual transcription, and regenerates `work/token-trace.tsv`. It does
not OCR the source or independently prove the reading of the image.
`work/plaintext.txt` records its complete output. A reverse-key check tests
mapped tokens only; it cannot validate the handwritten transcription.

## Key and scope

Monoalphabetic number-to-letter substitution:

| Number | 1 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Letter | M | E | R | V | L | O | T | P | S | F | A | G |

| Number | 14 | 15 | 16 | 17 | 18 | 20 | 21 | 22 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Letter | K | B | U | I | D | C | W | H | X | N | Y |

The same key is used on companion HCP 1507. Entries 9=P and 14=K are
inherited unused entries, not evidence from this postcard. Number 24=X,
also supplied by the companion, decodes the peripheral marks here.
**Number 2 has no established value.** It remains `[2]` in the output;
no entry 2=Y is invented to repair one word.

The main message has 161 numeric positions (160 mapped, one unmapped).
Eight peripheral numeric positions give XXX, ENA and two X's. Thus the
record covers 169 transcribed numeric positions, of which 168 map through
the key. Plain cursive “Sat night”, the date, address, signature, printed
caption, punctuation and underlining are not numeric cipher positions.

## Literal plaintext

Main text, retaining source line breaks and uncorrected wording:

```
OH MY DEAR
GIRL WHAT ID
THE MATTER HAVE
I DONE SOMETHIHG
WRONG OR ARENT Y
OU FEELING WELL
HONEY I HAVE W
ORRIED VERY MUCH
ARE YOU TIED OF ME
IF SO [2]OU OUGHT TO G
YOUR REASON YOU
BETTER COME DOWN
Sat night YOUR
FRIEY
```

Peripheral text, in `work/peripheral-transcription.txt`:

- Under the uncertain handwritten date: `24.24.24` → **XXX**,
  conventionally kisses.
- Picture panel (read after rotating the inscription 180 degrees):
  `3.25.12` → **ENA**, with meaning unknown; name or initials are possible.
- Beside the picture caption, two separate `24` marks → **X**, **X**.

The printed caption reads “I ISS VAITING YET. VHYFORE SUCH SILENCE”; it is
contextual printed text, not output from the cipher. Its waiting/silence
theme agrees with the letter but does not establish any uncertain digit.

## Interpretation and Slovak translation

Proposed English sense, **with editorial repairs, not exact decryption**:

“Oh my dear girl, what [is] the matter? Have I done [something] wrong, or
aren't you feeling well? Honey, I have worried very much. Are you [tired]
of me? If so, [you] ought to [give?] your reason. You better come down
Saturday night. Your [friend?].”

Slovak translation of that repaired sense:

„Ach, moje drahé dievča, čo sa deje? Urobil som niečo zlé, alebo sa necítiš
dobre? Miláčik, veľmi som sa trápil. Už ťa omrzelo byť so mnou? Ak áno,
mala by si povedať prečo. Radšej príď dolu v sobotu večer. Tvoj [priateľ?].“

“Dolu” renders DOWN without adding an unsupported destination. The intended
YOU at `[2]OU`, GIVE at G, and FRIEND at the closing are editorial hypotheses,
not extra decoded letters. XXX / X / X conventionally express kisses;
ENA has no established translation.

## Uncertainties and evidence

- Line 2 is `17.18` = **ID**, not IS (`17.10`).
- Line 4 **SOMETHIHG** contains 22=H where English suggests N. In **DONE**,
  the 25 has no visible detached flag and resembles 26. The working reading
  uses 25=N; the sign-level alternative is **DOYE**. Context supports DONE,
  but the missing flag is not reconstructed as visible ink.
- Line 7 **HONEY** contains a heavily overwritten 5 in 25. In line 8
  **VERY**, 26 is retraced. Both working readings are disclosed image readings.
- **TIED** has no R; TIRED is a repair. The isolated 13 is just **G**;
  GIVE is conjectural expansion.
- Line 10 visibly has a lone **2**, not 26, before `.7.16`. It yields
  **[2]OU**. YOU is the likely intended word, but the missing 6 is not added.
- Line 12 starts the last word with **18**, a separate 1 followed by 8:
  `18.7.21.25` = **DOWN**. The former TOWN reading omitted the leading 1.
- Closing `11.4.17.3.26` gives **FRIEY**. The final flagless b-shaped sign
  could instead be 25, giving **FRIEN**. Neither is silently expanded to FRIEND.
- The picture panel's middle sign is read as 25 with a detached flag,
  giving ENA. Its shape without that flag resembles 26 (EYA); the chosen
  reading follows the visible flag and the independent review. Meaning is unknown.
- Exact date, postmark day, signature and sender identity remain unresolved.

Extensive continuous English, repeated key values and the companion-card
key support the decipherment. These do not make the doubtful signs certain.
The register snapshot (110 records, no exact source/name match) establishes
only that the captured list lacked this entry, not priority or novelty.

## Response to review 1

The independent review by Claude Opus 5.5 concluded REVISE and explicitly
stated that the following record corrections require no further review
round. All original source and reviewer files were left unchanged.

1. **DOWN, not TOWN:** corrected body line 12 in `work/transcription.txt`
   from `8.7.21.25` to `18.7.21.25`. I inspected the original scan and
   `review/work/l12down.jpg`, comparing the leading 18 with DEAR.
   Regenerated decoder output and corrected English sense and Slovak translation.
2. **Raw 2 preserved:** corrected line 10 from `26.7.16` to `2.7.16`.
   `review/work/l10you2.jpg` shows the lone 2 followed by a separator.
   The decoder now retains unknown numbers in brackets, outputs `[2]OU`,
   and traces raw 2 as unknown rather than adding 2=Y. YOU is interpretation only.
3. **Peripheral numbers included:** added `work/peripheral-transcription.txt`
   and decoder coverage of header XXX, picture ENA and X / X. I inspected
   the original sides and `review/work/date.jpg` / `pic_nums180.jpg`.
   Counts now distinguish 161 main and eight peripheral numeric positions.
4. **Sign-level uncertainties:** added flagless 25/26 in DONE/DOYE and
   FRIEY/FRIEN, overwritten HONEY and retraced VERY. The working transcription
   keeps the reviewer's selected readings without hiding the alternatives.
5. **Presentation/date:** rewrote this document and notes with ordinary
   spacing; retained the uncertain handwritten date and postmark day.
   The unverified signature is also explicitly unresolved.

Changes affect transcription honesty and scope, not the substitution key
or the overall reading. The record now distinguishes literal decipherment from editorial repairs
and preserves all unresolved signs and identities.

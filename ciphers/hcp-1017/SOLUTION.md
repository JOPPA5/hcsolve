# HCP 1017 - decipherment after review 1

Both identified encrypted regions are covered. Independent reviewer Claude Opus 5.5 returned REVISE on 2026-10-27, confirmed the key and meaning, and requested transcription corrections. All findings are addressed below; the reviewer explicitly said another round is unnecessary after these corrections.

## Origin and context

HC Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1017 , name cpc_1905-06-14_DE_Hamburg_DE_Altona_, private T. Schroedel collection. General, Description and Attachments were inspected on 2026-10-26 UTC: Not solved, no individual attached solution or transcription. Immutable scans and metadata are in source/, provenance in SOURCES.md. No published individual solution was used. The collection paper by Tobias Schroedel (2021), linked in SOURCES.md, was checked only within that bounded scope; no global novelty claim is made.

The address is Fraeulein Erna Dahm, Altona, Gr. Bergstrasse 27. Both postmarks give 14.6.05, Hamburg and Altona (Elbe), supporting same-day delivery. The handwritten date 14.6.05 was Wednesday; MORGEN DONNERSTAG ABEND agrees with Thursday 15 June 1905. The printed card is Danish: "BREVKORT. Paa denne Side skrives kun Adressen." Ejnar is a Danish spelling of Einar. These support the name reading; a Danish linguistic background is plausible but the writer's identity and nationality are not established.

## Cipher and key

Pigpen monoalphabetic substitution. Rotate the original picture 270 degrees clockwise for the seven-line body, and 180 degrees for the separate margin. Read each region left to right. Dots distinguish grid letters; visible writer slips are preserved. BR, BL, TR and TL name the visible corners; openT/openB/openL/openR denote the missing wall.

| Shape | Letter | Dotted shape | Letter |
|---|---|---|---|
| BR | A | BR· | J |
| openT | B | openT· | K |
| BL | C | BL· | L |
| openL | D | openL· | M |
| square | E | square· | N |
| openR | F | openR· | O |
| TR | G | TR· | P |
| openB | H | openB· | Q (not required by this body) |
| TL | I | TL· | R |
| down angle∨ | S | — | — |
| right angle> | T | — | — |
| left angle< | U | — | — |
| up angle∧ | V | up angle· | Z |
| closed diamond◇ | W | — | — |


The closed diamond W is the writer's observed variant. X/Y and unused dotted cross shapes are not verified on this card. The undotted up-angle V occurs literally in HERVLICHSTE. The body has 185 positions, the margin 29: total 214. Of these, 212 have single-letter readings, one final M is inferred beneath a blot, and one canceled patch remains unassigned. An isolated dot before SEI is outside the letter cell and is recorded as stray ink or punctuation, not an additional cipher letter.

## Literal plaintext

```
LIEBSTE ERNA WIE GET ES DIR HEUTE
HAST HOFFENTLICH KE{crossed mark}INE AUSSCHAELTE
GEBRIEGT WEIL DU SO SPAET HINAUFKAMST
DU KOMMST ALSO MORGEN DONNERSTAG ABEND
UND HOLEST MICH SEI BIS DAN AUO DAS
HERVLICHSTE GEGRUEST TON DEINE[M]
EJNAR

TAUSEND TAUSEND GLUEHENDE BUESSE
```

[M] is an inferred letter, not an observed dot. The crossed patch is canceled ink, with no claimed original letter. The T in GET is heavily inked and possibly corrected, but is still a right-angle T.

Probable intended German, with punctuation and spelling explicitly editorial: "Liebste Erna, wie geht es dir heute? Hast hoffentlich keine Ausschelte gekriegt, weil du so spaet hinaufkamst. Du kommst also morgen Donnerstagabend und holest mich. Sei bis dann auf das Herzlichste gegruesst von deinem Ejnar. Tausend tausend gluehende Kuesse."

Literal-to-intended differences include GET/geht, AUSSCHAELTE/Ausschelte, GEBRIEGT/gekriegt, DAN/dann, AUO/auf, HERVLICHSTE/herzlichste, GEGRUEST/gegruesst, TON/von and BUESSE/Kuesse. ABEND is written in full and is no longer listed as a writer error. Missing dots in GEBRIEGT, HERVLICHSTE and BUESSE are not silently restored. BUESSE literally suggests penances; kisses are the contextual intended sense. No AB is added to HOLEST.

## Translation

Probable intended sense in English: "Dearest Erna, how are you today? I hope you were not scolded because you came upstairs so late. So you are coming tomorrow, Thursday evening, to fetch me. Until then, warmest greetings from your Ejnar. Thousands and thousands of ardent kisses."

This translates the editorial interpretation, including FROM and KISSES, rather than claiming the source literally writes VON or KUESSE.

## Reproduction and validation

```
python3 ciphers/hcp-1017/work/decode.py
```

The command verifies original image hashes and decodes explicit manual transcripts body-shapes.json and margin-shapes.json. This is manual-transcript reproduction, not OCR. It emits the literal reading above, slash word separators, and 214 positions. audit.py checks inventory, unchanged hashes, the held-out margin and date. It now prints its results without rewriting audit.json, avoiding the side effect noted by the reviewer.

Discovery first exposed German from an upside-down draft; the correctly rotated scan then established the geometric key. The 29-position margin was held out from body-key discovery. A 16-case orientation screen recovered TAUSEND TAUSEND GLUEHENDE BUESSE under that frozen key; no key change was needed. The former 200-letter optimizer control remains discovery evidence only: it cannot validate dots or stroke transcription. The independent review's sign-by-sign scan reading is the evidence for those corrections.

## Response to review 1

Reviewer: Claude Opus 5.5, REVISE; review/REVIEW1.md and REVIEWED1. I re-examined the disputed review crops against the scan-derived regions and accept every finding.

1. Added the cramped final openL D in ABEND. Body count changes 184 to 185 and total 213 to 214; corrected the decoder, literal text, error list and audit. ABEN is no longer attributed to the writer.
2. Changed the third glyph of AUF from openR to dotted openR. Literal AUO is preserved; intended AUF is editorial.
3. Removed the unsupported dots in GEKRIEGT and HERZLICHSTE. Literal GEBRIEGT and HERVLICHSTE now follow the same rule as BUESSE. The intended K/Z are not source observations.
4. Replaced the TV token with the ordinary right angle T. Literal TON is no longer a T/V glyph ambiguity.
5. Recorded the isolated dot before SEI, the blotted/inferred final M of DEINEM, and heavy GET T. Added the Danish printing, name spelling and same-day postmark context. [M] explicitly marks the one inferred letter without inventing a visible dot.
6. Retained the manual-transcript limitation. Added comparisons with the reviewer's independent decoder after normalizing only the [M] notation and canceled-patch label. The audit is now read-only by default; regenerated audit.json once during this authorized correction pass. The reviewer noted an earlier deterministic regeneration of that JSON; no evidence of source modification was found.

The key and meaning are unchanged; these correct the record as requested. The review explicitly authorizes closure without a second round after these corrections, consistent with README's REVISE-addressed path. No new review verdict is invented.

## Remaining limits

The crossed patch is not read. M under the terminal blot is inferred. The isolated dot may be punctuation or stray ink. The observed writer slips are retained, while translation supplies probable intended wording. The identity/nationality of Ejnar, building identification and a global publication history are not established. Original scans, original metadata, DONE1, REVIEWED1 and the review are unchanged. No external submission is made.

# HCP 1188 — revised Pigpen decipherment

The same interleaved Pigpen key decodes all **114 signs** in eight lines. Review 1 requested two transcription corrections, now incorporated: **WRITINH** is literal, and the signature reads **JESSE DARROW**. The key is unchanged.

## Literal reading

Word divisions are editorial. Spelling is not silently corrected.

```text
DEAR FRIEND AS I
NOW TAKE TIME AND
PLEASURE OF WRITINH
TOYOU IF NOT TO
STORMY WILL BE UP
WEDNESDAY EVENING
RESPFULLY YOURS
JESSE DARROW ANS
```

## Interpreted English

“Dear friend, as I now take time and pleasure of writing to you: if not too stormy, [I] will be up Wednesday evening. Resp[ect]fully yours, Jesse Darrow. Ans.”

WRITING corrects literal WRITINH. TOO corrects literal TO; [I] is supplied for grammar; resp[ect]fully expands RESPFULLY. ANS may request an answer. These are interpretations, not additional recovered letters.

## Slovak translation of the interpreted message

„Milá priateľka / milý priateľ, teraz si nachádzam čas a potešenie napísať ti. Ak nebude príliš búrlivo, prídem v stredu večer. S úctou tvoj, Jesse Darrow. Odpíš [pravdepodobný význam ANS].“

## Origin and scope

Portal 1188, catalogue name `cpc_1913-04-02_USA_Gr_USA__`, date 1913-04-02, North America, Tobias Schrödel Collection. All three rendered tabs were captured 2026-10-25, status Not solved; no supplied transcription or solution. Source scans are immutable. The picture caption is “The Kind We Raise in Gray, N. Y.”, showing oversized apples on a wagon; no encrypted continuation was observed there. Catalogue date, exact postmark and cursive recipient are not independently established by the decipherment.

## Key

Undotted/dotted pairs occupy each outline, followed by four wedge pairs. The portal supplied only the Pigpen family label, not this recovered alphabet.

| Present borders / wedge | Token | Undotted | Dotted |
|---|---|---|---|
| bottom/right | BR | A | B |
| bottom/left/right | B | C | D |
| bottom/left | BL | E | F |
| top/bottom/right | R | G | H |
| all four borders | C | I | J |
| top/bottom/left | L | K | L |
| top/right | TR | M | N |
| top/left/right | T | O | P |
| top/left | TL | Q | R |
| downward wedge | V | S | T |
| rightward wedge | > | U | V |
| leftward wedge | < | W | X |
| upward wedge | ^ | Y | Z |

## Reproduce

```sh
python3 ciphers/hcp-1188/work/decode.py
```

Run from the repository root. The script verifies preserved source hashes and decodes the manually read glyph list in `work/transcription.txt`. It does not OCR the scan. Independent review compared every sign against the scan; source hashes and program output alone do not validate that manual stage.

## Evidence and limits

One unchanged alphabet covers all 114 signs, with 22 distinct tokens and consistent repeated letters. The second TL in DARROW has a small visible dot near its stem; the neighboring stain partly affects O. WRITINH's final sign has a clear dot, unlike G at the end of EVENING. Both records are now literal. Weak dots remain an image-quality consideration, not justification for restoring a different surname.

Jesse Darrow is a decoded name, not a confirmed historical person. Recipient/place/postmark readings remain tentative. ANS, grammar supplied in translation, and the expansions noted above remain interpretation. No published target plaintext was used; no historical-priority claim is made. No FINAL or register entry is created in this revision pass.

## Response to review 1

Review: `review/REVIEW1.md`, Claude Opus 5.5, 2026-10-26, verdict REVISE. The reviewer found the decipherment correct and explicitly required no further round after the following record corrections. The source and review directories remain unchanged.

1. **Surname (major transcription / minor meaning): addressed.** Reinspected the original and `review/work/z-L8-RR-wide.png`, `zc-L8-RR.png`. The second TL carries a small dot against the inner stem, while the adjacent stain affects O. Changed line 8's second TL from TL0 to TL1 in `work/transcription.txt`. Literal **JESSE DARROW** now replaces DARQOW everywhere in the current claim, interpretation and translation. The small dot remains an image-quality caveat, not an unresolved Q/R alternative. This is a decoded signature, not proof of a historical identity.
2. **WRITINH (minor): addressed.** `review/work/z-L3-ING.png` and the original show a separate dot in the last R-outline; `z-L6-evening.png` contrasts the undotted G. Changed line 3's final R0 to R1. Literal **WRITINH** is retained in the transcript/decoder/report; **WRITING** is explicitly editorial correction of the apparent writer's error.
3. **Interpretive points (minor): retained as labelled interpretation.** TO remains literal; “too” and supplied [I] appear only in interpreted English and translation. RESPFULLY is not silently expanded in the literal text. ANS remains three decoded letters; “answer/odpíš” is a possible gloss.
4. **Manual reproduction / roundtrip (minor): addressed.** Removed the exact-token-roundtrip assertion and its success claim from `work/decode.py`. Source hash verification establishes file integrity; decoding establishes mapping execution. Neither proves scan-to-token accuracy. Evidence for that stage is the original scan plus the reviewer's independent all-sign collation, with the two corrections above. Regenerated `work/plaintext-check.txt`; all 114 positions decode with the unchanged key.

The revisions correct two glyph records within the same decipherment; they do not change the cipher method or key. Report source is `report/report.md`. PDF production and final state marking remain with the root solver.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.

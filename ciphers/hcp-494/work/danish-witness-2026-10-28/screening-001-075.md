# Danish cipher collection: bounded screening of viewer pages 1–75

28 October 2026, solver research helper. Page numbers refer to public viewer 260610 / the saved `keys/001.jpg` convention, not original folio numbers. Acquisition URLs and SHA-256 values are in `download-manifest.json`.

## Scope and result

All **75** assigned pages were screened on contact sheets. **19** selected pages were additionally inspected as individual delivered images or larger rotated crops: 2, 3, 4, 5, 6, 7, 8, 11, 14, 16, 54, 55, 56, 61, 62, 65, 68, 69, 75. Individual whole-page displays are reduced by the viewer; two additional crops for 56/65 preserve native pixels after a 90-degree counterclockwise rotation. This is layout/alphabet/selected-entry triage, **not** complete transcription or a full-resolution reading of every cell on 75 pages.

No matching HCP-494 alphabet, expanded target nomenclator, or new target plaintext was identified within this pass. The negative result applies only to the inspected material and observations; no claim is made that the entire collection has been ruled out by exhaustive transcription.

## Observations

| Viewer pages | Observation and limits |
| --- | --- |
| 1 | Collection title card: Tyske Kancellis udenrigske Afdeling, Almindelig Del, Chiffre. |
| 2–7 | Small correspondence fragments, wrappers and correction lists. Page 2 explicitly dates its Copenhagen note 1759; page 3 has 1758 dates; page 4 has 1759. Numeric syllable/word fragments include many four-digit groups. No same-key target alphabet is visible. Not every personal name or fragment is transcribed. |
| 8–12 | Dense French syllable/word list with graphic letter substitutes and letter codes in the 1300s; 8 and 11 give overlapping material. These alphabet structures differ from the HCP table's 20–169 numbers and doubled capitals. No complete nomenclator transcription attempted. |
| 13 | Wrapper/title page; not used to infer a secure name or date. |
| 14–52 | Extended, alphabetically ordered multilingual/French-heavy word and syllable book. Page 14 explicitly gives A=29/30, B=22/34, C=15/38; this is not the transferred HCP alphabet. Page 16 provides direct contrary anchor readings: **601=armoir**, **634=ascension**, **768=avou**. Thus these entries do not support the target's auxiliary Denmark/Holstein/Sweden glosses. The target glosses remain hypotheses; this is a comparison, not proof of their correctness. All continuation pages were only screened for layout/range continuity, not transcribed. |
| 53 | Cover/wrapper. |
| 54 | Small two-homophone alphabet: a=2/4, b=3/6, c=5/10. It differs from HCP's a=20/30/40/50/60 and b=22/32/42/52/62. |
| 55 | Graphic plus numeric alphabet, e.g. A=16, B=2, C=18; country/word list and syllables. Visible entries include Denmark=210, Holstein=216, Holland=218, **601=re**, **Alliance=292**. This is not the target's comparison alphabet or the gloss-supported expanded list. |
| 56–59 | Dense German/diplomatic syllable-word tables. Rotated page 56 shows **Dennemarck=2000**, with other diplomatic names nearby in descending numerical order. No identical target-table block identified at contact-sheet level. No exhaustive reading of the full ranges. |
| 60 | Wrapper/verso layout. |
| 61 | Russia/Northern War-labelled sheet with a homophonic alphabet and inverse. For example a=5/15/25/35/45/55; h includes 19/20/22. Different from HCP's a=20 etc. No date is established from the label alone. |
| 62–63 | Two small differing cipher sheets; page 62 left has ordinary substituted letters and word values including Alliance=54. Right sheet has a different numeric alphabet (a=25) and graphic names. Not the target table. |
| 64 | Wrapper. |
| 65–67 | Another dense German diplomatic codebook. Rotated page 65 gives **Dennemarck=30**, with A=1, B=2, C=9, D=16, E=4 in its alphabet's numeric row. This is incompatible with transferring the HCP table unchanged. |
| 68 | Right cover explicitly refers to cipher papers of **Christian von Lente**. It is not a Lincker identification; no handwriting identity with HCP 494 is claimed. |
| 69 | French letter/syllable table: A=258/257, B=248/247. Word anchors include Danish court=299 and its king=300, Holstein court=360, Berlin=399. Different table and code values. |
| 70–74 | Tables of word/name aliases, screened on contact sheets. No target-style numeric alphabet is visible; not fully transcribed. |
| 75 | Dense letter/syllable numeric table with letter assignments in the 280s–400s and syllables above that, rather than HCP's low-number/doubled-capital alphabet. No matching target table identified. |

The country-anchor comparisons are explicitly **annotation dependent**: they compare the new tables with working country interpretations already known from HCP's manuscript annotations. They are not newly decoded HCP words.

## Crop recipe

The two files under `ending-agent-crops/` are reproducible with Pillow as:

```python
Image.open(f"keys/{page:03}.jpg").transpose(Image.Transpose.ROTATE_90).crop((0, 0, 3436, 1500))
```

for page 56 and 65. The rotation is a right-angle pixel permutation; no sharpening or contrast changes were applied. These are exploratory reading aids, not altered primary sources. The primary downloaded images were not changed.

# HCP 1533 — pc_hcp_214

Solver candidate, not independently reviewed. The complete visible substitution text is read below using the pre-supplied Anna Tichá family key: **known-key transfer, not a new key discovery**. No undeciphered active cipher unit remains in this transcription. The source spellings ANUNKO and VZDIT are preserved.

## Source and context

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1533 . Root inspected all three rendered portal tabs and viewed both original images on 2026-10-28 UTC before this collaborator started. The portal showed **Not solved**, Czech, Substitution, private collection, date 1903-10-28, unknown sender, recipient Anna Tichá. The source page had two postcard-side images and no target transcription or solution attached. Both originals and the rendered metadata remain immutable in `source/`, with exact image URLs in `SOURCES.md`. The ordinary address calls Anna Tichá a teacher in Žirovnice near Počátky. The ordinary date on the picture side is `28./X.1903` (28 October 1903). No identity beyond the cipher signature PEPOUSE / Pepouše is established.

Root's rendered AI-register check found 158 contribution rows / 124 HC Portal IDs, target absent. This is a bounded check, not proof of historical priority. Maxim Egorov / Cipher-Atelier's already published partial family key and eleven partial family readings are acknowledged in `SOURCES.md`; root preserved their generic key and provenance in `batches/easy-2026-10-28/published-anna-ticha-key.txt` and its provenance JSON. The published index checked by root did not include pc213–215. The pre-existing HCP1520–1527 family key was explicitly supplied before this reading, and was copied from HCP1527's machine-readable key. No published target plaintext or initial target transcription was supplied. Root's source collection, family provenance and any later source-derived solver comparisons are collaborative inputs; this work is not an independent-provider or blind test.

## Cipher and key

Monoalphabetic substitution with digit-like and Latin-like handwritten shapes; one special shape encodes the Czech digraph CH. Labels below are conventional identifiers rather than diplomatic reproductions of the handwriting. In particular, `m` means N and `n` means M. `ř` is a neutral label for the special CH glyph, not plaintext Ř. The tentative shallow-v/F class from HCP1526 was not used.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř (special shape) | CH | | | | |

## Exact procedure and reproduction

Rotate `source/picture.jpg` losslessly 90° clockwise (Pillow `ROTATE_270`) to an upright 674×1024 image. Read the left block from A01 through A11, then follow the handwritten upward-right continuation arrow to B01 and read through B08. Manually transcribe these nineteen rows using the shape labels above. Replace each indexed shape by the key value, preserving source row breaks and the printed line-end hyphens. The first ZA-/JISTE, ZI-/ROVNICE and MYSLEN-/KACH splits are preserved in the literal text; joining them in prose adds no base letter.

One read-only standard-library command, from repository root:

```sh
python3 ciphers/hcp-1533/work/decode.py
```

The command verifies all three original-file SHA-256 hashes and three record hashes, decodes all rows from `work/transcription.json`, checks every ordinal in `work/positions.csv`, and verifies exact tokenwise inverse-key round trips, including separators. It prints all 240 base letters. The manual transcription is an explicit input linked to the immutable image by row-coordinate boxes and controls; the command does not perform OCR or independently validate the visual readings. Round-trip success proves internal record/key consistency.

`work/indexed.png` places the nineteen row boxes on the upright original. `work/A01.png`–`A11.png` and `B01.png`–`B08.png` are row crops. Whole-row boxes overlap where ascenders/descenders meet; CSV indices are character ordinals, not fictitious individual glyph pixel boxes. `work/focused-controls.json` gives the precise source boxes for `C01-native.png`–`C10-native.png`; the matching `C01.png`–`C10.png` are 4× nearest-neighbor enlargements without contrast or stroke editing, combined in `work/focused-controls.png`. `build-record.py` and `make-controls.py` are explicit record/crop generators and are not invoked by the reproduction command.

## Full literal base plaintext

No missing letter, grammatical repair, vowel substitution or accent has been silently inserted. Line breaks, line-end hyphens and punctuation follow the manual source transcription. Spaces and punctuation are not counted as cipher units.

```text
VRELOU SOUSTRAST,
DUSICKO MOJE JEDINA,
V ZARMUTKU, JENZ
NA TEBE DOLEHL.
CITIM UPRIMNE
SE SRDECKEM SVYM.
AVSAK BUD, ANUNKO,
KLIDNA, VZDIT PAN
BRATR JE MLAD A ZA-
JISTE CHOROBU
VITEZNE PREMUZE.
KDY PRIJEDE
SLECNA DO ZI-
ROVNICE? TISIC
VRELYCH UPRIMNYCH
PUS OD PEPOUSE,
KTERY V MYSLEN-
KACH STALE DLI U
TEBE.
```

## Editorial Czech reading

Accents, capitalization, paragraphing and joining the three hyphenated line splits are editorial. The unusual vocative **Anunko** remains exactly ANUNKO at the base-letter level. The form **vždiť** retains literal VZDIT; replacing it with modern *vždyť* would require an I→Y substitution and is not done here. Accent choices are not independently encoded by every base shape.

> Vřelou soustrast, dušičko moje jediná, v zármutku, jenž na tebe dolehl. Cítím upřímně se srdéčkem svým. Avšak buď, Anunko, klidná, vždiť pan bratr je mlád a zajisté chorobu vítězně přemůže.
>
> Kdy přijede slečna do Žirovnice? Tisíc vřelých upřímných pus od Pepouše, který v myšlenkách stále dlí u tebe.

The absence of an explicit verb in the initial formula and its sentence punctuation are retained, rather than repaired into a modern letter. The card supports concern over a brother's illness; it does not establish the brother's identity or medical details, nor the identity of the arriving young lady.

## Slovak translation

> Vrúcny súcit, dušička moja jediná, v zármutku, ktorý na teba doľahol. Úprimne súcitím so svojím srdiečkom. Avšak buď, Anunko, pokojná, veď pán brat je mladý a iste chorobu víťazne premôže.
>
> Kedy príde slečna do Žirovnice? Tisíc vrúcnych úprimných bozkov od Pepouša, ktorý je v myšlienkach stále pri tebe.

## Coverage, controls and uncertainties

- **19 rows, 236 active cipher units, 4 CH units, 240 base letters**; all assigned through the pre-supplied key. Ordinary date, postal address, arrow, spacing and punctuation are excluded. No canceled or additional isolated marginal cipher unit was identified on either side.
- A02 DUSICKO is seven units `t2c4sg3`. C01 shows the I/C sequence; an earlier rough visual draft that resembled “JUSJAKO” was discarded after checking the original pixels. No such draft contributes to the final record.
- A06 SRDECKEM uses `cht5sg5n`; C02 shows the E after K. It is not silently read as SRDECKAM.
- A07 ANUNKO is `6m2mg3`. In C03 its third shape matches 2/U in nearby BUD, and differs from 4/I. The unusual nickname is retained; ANINKO and ANICKO are not substituted.
- A08 VZDIT is `fqt4d`. C04 includes the contrasting 1/Y of SVYM above it; the source's 4/I is preserved. The source does not justify changing it to VZDYT to match a familiar Czech spelling.
- A10 CHOROBU (`ř3h3p2`), both B04 CH endings and B07 CH in KACH supply the four special CH units. C05, C08 and C10 show these original-pixel controls.
- B06 MYSLEN has a heavily inked stroke within the first `n`/M shape (C09); no extra separate cipher unit or recoverable canceled letter is asserted. The visible word supports MYSLEN-, followed by KACH in B07.
- A11's arrow points toward the right block and is a continuation mark, not an extra key symbol (C06). Both original sides were inspected for further marginal cipher writing; none was identified.
- The visual source supports the full base-letter reading; accents, punctuation and word separation remain editorial or manual judgments. Neither sender civil identity nor historical events are resolved.

This is a full-card solver candidate with source spelling anomalies preserved. There is no independent reviewer, blind-key recovery, held-out test or historical-priority claim. This collaborator creates no watcher, marker, PDF or register entry; root must inspect the source controls before any handover.


## Root verification before handover

Root inspected both originals, all nineteen rows in the grouped source panels and the focused controls on 2026-10-28. The third unit in ANUNKO is the curved 2/U, and the fourth unit of VZDIT is 4/I; neither was regularized. The dark stroke in MYSLEN remains within its single active M-shaped unit without an invented canceled letter. The continuation arrow and all four CH units are accounted for. The Slovak translation renders SOUSTRAST as sympathy in the context of the brother's illness; no death is asserted. Root ran the documented read-only command: all source/record hashes, 236 indexed units, four CH expansions and exact tokenwise checks passed. The wave source manifest matched. This is a second solver check, not independent provider review.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-28). The reviewer made its own upright frame of source/picture.jpg, read all nineteen rows sign by sign from its own enlarged strips before comparing, and decoded that reading with an independently written script (review/work/decode_review.py). Its 236-sign transcription is identical to the solver's, and its decoded output is byte-identical to rows 1–19 of `python3 ciphers/hcp-1533/work/decode.py`. It confirmed the two retained source spellings ANUNKO (third sign the curved 2/U, as in BUD) and VZDIT (fourth sign the crossed 4/I, not the 1/Y of SVYM), the E of SRDECKEM, the single over-inked M-shaped sign at the start of MYSLEN-, all four CH glyphs, and that neither side carries further cipher signs. The literal plaintext is unchanged.

1. Visible marks and the editorial accents (minor). Accepted as a documentation point. On re-inspection of the row crops (work/A1-4.png, A5-8.png, A9-11.png, B1-4.png, B5-8.png), the only marks standing above signs that we can identify at the 1024 px scan resolution are the tilde/caron-like top of the special CH glyph, which belongs to that single unit, and the cross-strokes of the D-shape (t) and T-shape (d), which are part of those shapes. We identify no separate accent marks over vowels or consonants. No visible mark was used to choose the editorial accents: those of the normalized Czech (for example *zármutku*, *mlád*, *vřelých*, *Žirovnice*, *Pepouše*) are supplied from standard Czech orthography of the period and from the plain address side ("Žirovnici"), and they are not encoded by the cipher. If any small marks are present that the scan does not resolve, they do not change any base letter. The report says this.
2. ANUNKO and HCP 1535 (minor). Accepted. HCP 1535 (same writer, signature PEPOUSE, recipient Anna Tichá, 13 October 1903) has the nominative ANUNKA in its row B02 ("ANUNKA MI URCITE …"). ANUNKO is the regular vocative of that form, so ANUNKO is the writer's own pet name for Anna (Anna → Anunka), not a slip and not a misreading of ANINKO/ANICKO. The report replaces "unusual nickname retained" with this evidence. The same family card also shows the writer referring to Anna in the third person ("Anunka mi určitě slíbila, že … přijede do Prahy"); the report notes, as a possibility only, that "slečna" in "Kdy přijede slečna do Žirovnice?" may likewise be Anna herself.
3. Stale status text (minor). Accepted. The closing paragraphs of the original solution ("Solver candidate, not independently reviewed", "There is no independent reviewer …", "root must inspect the source controls before any handover", "This collaborator creates no watcher, marker, PDF or register entry") describe the state at DONE1 and are left in place as a record; this section supersedes them. Status now: independent review 1 by Claude Opus 5.5 returned ACCEPT; report/report.pdf and register-entry.txt exist.

Additional notes from the closing pass: 28 October 1903 was a Wednesday. The address side reads "Velectěná Slečna / slečna Anna Tichá / učitelka v Žirovnici / u Počátek"; it carries a 5-heller Austrian stamp cancelled PRAHA and an arrival stamp ŽIROVNICE / SEROWITZ whose day is only partly legible. In "Cítím upřímně se srdéčkem svým", *srdéčko* ("little heart") is most naturally an endearment for Anna ("I sincerely feel with my sweetheart"), which is how the solver's Slovak translation already renders it; a literal "with my own little heart" is the alternative. The register type is recorded as monoalphabetic substitution with a CH digraph sign (known family key).

Remaining uncertainties carried into the report: the editorial accents and punctuation; the civil identity of "Pepouš"; the identity of the brother and of the "slečna"; the key is a transferred family key (HCP 1520–1527), with a published partial family key by Maxim Egorov / Cipher-Atelier acknowledged in SOURCES.md; novelty rests on the bounded checks recorded in source/metadata.md and SOURCES.md (portal status Not solved, AI Decipherment Register, Egorov index without pc213–215), which the reviewer did not repeat.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-28.

# HCP 962 — full solver candidate, awaiting review

## Source and scope

The portal identifies this postcard as `cpc_1903-06-06_DE_Bonn_DE_Aachen_`, dated 6 June 1903, addressed to Maria Peters in Aachen, from the private Tobias Schrödel collection. Root inspected all three rendered portal tabs on 28 October 2026: status **Not solved**, no individual transcription or solution attached. The newer AI register had 158 contributions; this item was absent from that bounded inspection. These checks do not establish worldwide novelty. See `SOURCES.md`.

I manually transcribed the original picture-side scan. The complete handwritten cipher occupies four short rows in the white lower-right inset, then two rows along the bottom. The address side contains ordinary handwriting and postal marks; no additional cipher was observed. The printed bridge caption, publisher's imprint, and modern HC Portal watermarks are not ciphertext. The handwritten message has 117 alphabetic glyphs, one of which is explicitly umlauted, plus ordinary punctuation.

The present claim is a complete **literal** reading of those 117 glyphs. One literal word, `HORGEN`, is anomalous; the likely intended `MORGEN` is an editorial interpretation and is not the decoder output. No DONE, independent review, FINAL, or register entry has been created by this collaborator.

## Cipher and key

This is monoalphabetic Pigpen substitution. Successive letter pairs fill the nine lattice cells; the second member receives an interior dot. J is omitted from the 25-letter alphabet. For the remaining angled signs, an interior dot likewise selects the second letter of the pair. The script names lattice shapes by their actual walls: `t` top, `b` bottom, `l` left, `r` right. A suffix `.` means an interior dot, not punctuation.

| Undotted shape / walls | Letter | Dotted letter | Attested here |
|---|---|---|---|
| ┘ / `br` | A | B | both |
| U / `lbr` | C | D | both |
| └ / `bl` | E | F | both |
| ] / `tbr` | G | H | both |
| square / `tblr` | I | K | both |
| C / `tbl` | L | M | both |
| ┐ / `tr` | N | O | both |
| Π / `tlr` | P | Q | neither: inferred alphabet cells |
| ┌ / `tl` | R | S | both |
| v / `v` | T | U | both |
| > / `>` | V | W | V only; W inferred |
| < / `<` | X | Y | neither: inferred alphabet cells |
| ^ / `^` | Z | — | Z |

In `ZURÜCK`, the fourth glyph is the dotted U angle with **two additional dots above it**, giving Ü. It is recorded separately as `v.:umlaut`; the three dots are not silently flattened to a new letter or to ordinary U. All other observed signs use the same fixed key throughout the card.

## Literal plaintext

Capitalization below is a display convention. Line breaks and the `=` continuation are retained; `!` and the stop after `ZURÜCK` are ordinary punctuation on the scan. Spaces separate the visible word groups.

```text
LIEBER ENGEL!
DIR ZU GEFALLEN
KOMME HORGEN
ZURÜCK. BIS SONN=
TAG NACH DER MESSE VERBLEIBE UNTER HERZLICHEM
GRUSS UND KUSS DEIN DICH LIEBENDER M
```

Reading text with the compound line break joined and the likely writer error explicitly corrected:

> Lieber Engel! Dir zu Gefallen komme [morgen; literal HORGEN] zurück. Bis Sonntag nach der Messe verbleibe unter herzlichem Gruss und Kuss dein dich liebender M.

The initial M is not expanded to a personal name. `GRUSS` and `KUSS` are the actual SS readings, not an encoded ß. Sentence punctuation beyond the visible marks has not been added to the literal transcription.

## Translation

With the probable intended **morgen** (“tomorrow”) marked as an editorial correction:

> Dear angel! To please you, I am coming back [tomorrow; the literal cipher says HORGEN]. Until Sunday after Mass, I remain, with heartfelt greetings and a kiss, your loving M.

Without that correction, the isolated literal word **HORGEN** is left untranslated. It is not established as a place name or a different word.

## Reproduction

From the repository root, run:

```sh
python3 ciphers/hcp-962/work/decode.py
```

This single command verifies SHA-256 hashes of both original scans and metadata, decodes the manual shape transcript with the fixed key, prints every row, checks the 117-symbol inventory, and re-encodes every symbol to its transcribed shape. `work/transcript.json` records every glyph by row and position, with its word number and original-picture row bounding box. The script's rows are the authoritative manual transcription; they are not OCR. Source hashes and round trips prove reproducibility and internal consistency, **not** that the glyphs have been extracted automatically or that the visual transcription is independently correct.

To regenerate the machine-readable inventory, append `--write-transcript`. This option changes only the working transcript.

## Visual checks and remaining interpretation

- At picture coordinates approximately **x820, y523**, the first glyph of the second word in row 3 is a right-sided three-wall bracket **open left**, with an interior dot: `tbr.` = **H**. It differs from both left-sided, open-right dotted brackets **M** immediately before it in `KOMME`. See `work/row3.png`. Root separately inspected that crop and agreed with the literal H. The candidate therefore preserves `HORGEN`; `MORGEN` is not a language-forced shape correction.
- The fourth glyph in `ZURÜCK` has a dotted V-shaped sign and two extra upper dots. See `work/row4.png`. The following ordinary period and `BIS SONN=` are kept separately from Pigpen dots.
- The lower rows repeat key controls such as `DER`, `DEIN`, `DICH`, `KUSS`, and the lattice/dot distinctions already visible above. Every displayed glyph has a fixed reading, including the final dotted C-shaped **M**. No unread symbol has been hidden or completed from syntax.
- The script uses the writer's split `SONN=` / `TAG`; joining this to `SONNTAG` in the reading text is editorial line-break handling.
- The angle key and omitted-J pairing provide a compact regular alphabet, not a separate free assignment for every word. Unobserved P/Q/W/X/Y cells are explicitly distinguished from actual evidence.
- There was **no blind held-out test**: the lower rows were visible during the exploratory solution. The full-card reread with the fixed key is a consistency check, not independent discovery validation. No published individual plaintext was used, and the generic source paper check by root found no matching illustrated card. That check is bounded.

All 117 glyphs are accounted for. What remains uncertain is the writer's intended word behind literal `HORGEN`, the identity behind initial M, and interpretation of the social context. The source-specific H/M distinction remains available for independent review rather than being repaired in the transcription.


## Root verification before handover

Root personally inspected both original scans, top inset, all lower-row crop segments and the separate umlaut/HORGEN details. The dotted bracket at the beginning of HORGEN is visibly open left, distinct from both M controls immediately preceding it; literal H is retained. The pair-filled key is consistent with the full source-based reading. Reran the documented decoder: 117 positions, fixed source hashes and exact re-encipherment passed. Rechecked all nine source-file hashes for the batch without changes. These are solver verification steps, not independent review or a blind held-out experiment. The writer's intended MORGEN and identity behind initial M remain interpretation. No watcher/reviewer launched under user override. DONE1 is the next and last cipher-directory mutation.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-28). The reviewer re-read all 117 glyphs from its own upscaled crops of source/picture.jpg before comparing, decoded them with an independently written script (review/work/review_decode.py), and found its reading identical to the solver's in every position, including the literal H of HORGEN (⊐·, open to the left, against the two ⊏· = M of KOMME) and the umlauted Ü of ZURÜCK. One fixed pair-filled key covers the whole card; P, Q, W, X and Y are unattested. The literal plaintext is unchanged.

1. Non-cipher writing not inventoried (minor). Accepted. The complete inventory of marks that are not cipher is: on the picture side, the printed caption "Neue Rheinbrücke", the imprint "Dr. Trenkler Co., Leipzig. 12958", the HCPortal watermark, a handwritten pencil "Bonn" directly above the inset text (about x760–815, y385–405; the place of writing), and faint, illegible violet pencil traces at the top right of the picture (about x880–1010, y160–300), which are cursive-like and not Pigpen. On the address side: printed "POSTKARTE"; the plain address "Fräulein Maria Peters, Aachen, Adalbertsteinweg 46."; the lower half of a departure circle stamp at the top right ("…03. 6-7 V.", "1 m"; the upper half with the town name was on the postage stamp, which is no longer on the card); and the arrival stamp "AACHEN 1 ANKUNFT 6.6.03" at the left, struck upside down. None of this is cipher. These details are in the report; source/metadata.md is unchanged.
2. Weekday and postmark evidence (minor). Accepted. 6 June 1903 was a Saturday. The departure stamp gives the morning hour 6–7 V. (vormittags), and the card arrived in Aachen the same day, 6.6.03. Written on Saturday, "komme morgen zurück" refers to Sunday 7 June, the same day named in "bis Sonntag nach der Messe". This independently supports the intended reading MORGEN. It remains an editorial correction: the literal decoded word stays HORGEN, and the decoder output is unchanged.
3. Parsing of "Bis Sonntag nach der Messe" (minor). Accepted. The preferred reading now treats it as a farewell of its own, followed by the standard closing formula: "Bis Sonntag nach der Messe! Verbleibe unter herzlichem Gruß und Kuß dein dich liebender M." ("See you on Sunday after Mass! With heartfelt greetings and a kiss I remain your loving M."). The card has no punctuation after MESSE, so the solver's run-on parse ("Until Sunday after Mass I remain …") is kept as an alternative. The report gives both, the farewell parse first.
4. Wording of the dot convention (minor). Accepted. "Interior dot" above is the key convention, not a description of every glyph: this writer places dots loosely. The dot of ┐· (O) in KOMME and HORGEN sits just above the top bar, and the dot of v· (U) in UNTER, GRUSS, UND and KUSS sits above the v rather than inside it (in ZU it is inside). Each of these signs is still clearly dotted and the key is unaffected. The report says so.

Additional notes from the closing pass: the normalized German uses the spelling of 1903 (Gruß, Kuß); the cipher itself writes GRUSS and KUSS with two dotted ┌ signs, and the literal text keeps SS. The departure town is illegible on the scan; the Bonn origin rests on the picture (Rhine bridge at Bonn), the pencil "Bonn" and the portal name.

Remaining uncertainties carried into the report: the identity of "M" and the writer's relationship to Maria Peters; MORGEN is an editorial correction, however well supported; the alternative parse of "bis Sonntag nach der Messe"; novelty rests on the bounded checks recorded in SOURCES.md (portal status, AI register, Schrödel paper), which the reviewer did not repeat.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-28.

# HCP 899 — German Pigpen postcard, Bodenwerder → Hameln, 7 Dec 1902

**Status: complete reading of all geometric ciphertext on the card** (263 glyphs: 75 in the upper personal message, 188 in the lower poem). 26 lower glyphs are partly covered by the HC Portal watermark; how each was settled is listed under *Uncertainties*. Review round 1: REVISE; the one wrong word (L4 LIEBCHEN → LIEBES) is corrected below.

## Source and scope

HC Portal cryptogram 899, `cpc_1902-12-07_DE_Bodenschwerder_DE_Hameln_` (portal spelling; the printed greeting reads "Gruss aus Bodenwerder"). The portal gives the date 7 Dec 1902, the recipient Johanne Stiebe, the Tobias Schrödel postcard collection, tags Postcard / Pigpen, and status **Not solved**. It attaches no transcription or solution (see `source/metadata.md`, `SOURCES.md`). The address side is in plain handwriting: "Fräulein Johanne Stiebe, p. Adr. Frau von Blum(?), Hameln a/W., Osterstraße 40". It is postmarked Bodenwerder and Hameln, 8.12.02. There is no cipher on the address side.

The cipher is on the picture side, in two blocks: a personal message at upper right and an 8-line poem below. The printed greeting, the date "7/12.02", the numeral "1000" and the cursive lines in the left margin are in plain writing. They are outside the cipher and were not transcribed here.

## Cipher type and key

The cipher is a **Pigpen variant with three letters per cell**: the shape of the cell picks a group of three letters, and the number of short interior strokes (1, 2 or 3) picks the letter within that group. The alphabet has 27 letters, J included and ß in the last cell. Umlauts are written as two strokes above the sign. Each word ends with a slash. The shapes are written as slanted parallelograms. Shape names: t = top, b = bottom, l = left, r = right wall.

| Shape | 1 stroke | 2 strokes | 3 strokes |
|---|---|---|---|
| ┘ `br` | A | B | C |
| ⊔ `lbr` | D | E | F |
| └ `bl` | G | H | I |
| ⊐ `tbr` | J | K | L |
| □ `box` | M | N | O |
| ⊏ `tbl` | P | Q | R |
| ┐ `tr` | S | T | U |
| ⊓ `tlr` | V | W | X |
| ┌ `tl` | Y | Z | ß |

These 21 cells are attested on the card: A–E, G–I, K–O, R–W (V once, W once), Z (tl2 in SITZEN) and ß (tl3 in GRÄßLICHE). F, J, P, Q, X and Y do not occur, so their cells are inferred from the regular pattern.

## Plaintext (German, original line breaks)

Upper personal message:

```
Ich habe gräßliche
Sehnsucht nach dir.
Schreibst du
mir auch
recht bald?
1000 Küsse
Dein
Hermann.
```

Lower poem:

```
Liebchen mit dem roten
Mündchen,
mit den Äuglein lieb und klar,
du mein liebes, süßes Mädchen,
deiner denk ich immerdar.
Kalt ist heut der Winterabend,
möchte gerne bei dir sein,
bei dir sitzen, mit dir kosen
im vertrauten Kämmerlein.
```

The cipher does not encode capital letters or punctuation. The capitals and the commas and full stops between words here are editorial, except for the slash/comma/full-stop/question marks that are drawn on the card. The card spells SÜSSES with two cipher S signs (┐1 ┐1), not with ß.

### English translation

> I miss you terribly. Will you write to me quite soon too? 1000 kisses, your Hermann.
>
> Sweetheart with the red little mouth, with the little eyes dear and clear, you my dear, sweet girl, I think of you forever. Cold is the winter evening today; I would like to be with you, to sit with you, to cuddle with you in the cosy little room.

### Slovak translation

> Strašne po tebe túžim. Napíšeš mi aj ty čoskoro? 1000 bozkov, tvoj Hermann.
>
> Milá moja s červenými ústočkami, s očkami milými a jasnými, ty moje milé, sladké dievča, na teba myslím naveky. Studený je dnes zimný večer, rád by som bol pri tebe, sedel pri tebe, túlil sa k tebe v útulnej izbičke.

## Literary source of the poem

The poem is a free adaptation of Heinrich Heine, *Buch der Lieder*, "Die Heimkehr" ("Mädchen mit dem roten Mündchen …", public domain). Heine's text reads *Mädchen … süß und klar / Du mein liebes, kleines Mädchen / … / Lang ist heut der Winterabend, / Und ich möchte bei dir sein, / Bei dir sitzen, mit dir schwatzen, / Im vertrauten Kämmerlein*. The card differs in six places: **Liebchen** for Mädchen, **lieb** for süß, **süßes** for kleines (the card agrees with Heine's *liebes* here), **Kalt** for Lang, **möchte gerne** for und ich möchte, and **kosen** for schwatzen. Round 1 of the review showed that one word in L4 had been copied from L1 (LIEBCHEN) and not read from the scan. After that, every Heine-divergent word and every word whose token string repeats another word's was checked again against its own crop (see *Response to review 1*). Three letters (ROTEN T, E; KOSEN S) are not visible on the scan. They were restored when the poem was already known; see *Uncertainties*. Where the card and Heine differ, the card's signs decide. This is a literary source for the verse. It is not a published decipherment of this card, and none was found.

## Reproduction (one command, from the repo root)

```sh
python3 ciphers/hcp-899/work/decode_v2.py
```

The script checks the SHA-256 of `source/picture.jpg`, `source/address.jpg` and `source/metadata.md`. It then decodes every shape token in `work/transcript_v2.json` with the key and prints the upper rows U1–U8 and the poem rows L1–L9. Glyphs partly covered by the watermark are printed in lower case. The script also prints the glyph counts: 75 + 188 = 263, of which 26 are partly obscured. The transcription is manual, and the script does not read pixels. `work/build_transcript_v2.py` is the one-off file that holds the shape readings and writes the JSON. The earlier partial files (`transcript.json`, `decode.py`) are kept as the record of earlier work.

## Uncertainties

The scan is only 1024 × 680 px, and the circular HC Portal watermark lies over the right half of the poem. Every lower glyph was examined in crops enlarged 5–18×, using colour weighting (the ink is bluer than the grey watermark) where that helped. The 26 glyphs marked in the transcript fall into three groups:

- **Shape or ticks partly hidden, but the visible walls and/or ticks agree with the reading** (most cases): MÜNDCHEN n, d; LIEB i, e (I's left wall and three ticks are visible under "P"); KLAR l, a; MÄDCHEN final n; IMMERDAR first i; WINTERABEND w, i, n, n, d; BEI i; SEIN e, i; DIR (L8) i, r; KÄMMERLEIN m, e, r; SÜSSES 4th s (right wall and top visible, tick partly under "C").
- **Tick count not readable, restored because only one letter makes the word**:
  - ROTEN, 3rd and 4th glyphs: under "GPO", a diagonal right wall (┐) and a ⊔-shaped stroke are visible, but no ticks. ┐ gives S/T/U, and ⊔ gives D/E/F. RO?EN with ┐ gives ROTEN; ROSEN does not fit before *Mündchen*.
  - KOSEN, 3rd glyph: hidden under the watermark "T". KO?EN with S is the only German word.
  - DEINER, 1st glyph: ⊔ with an unclear stroke count (1 or 2). D is the only possibility.
- **Readings that replace the earlier provisional ones**: MÄGDELEIN → **MÄDCHEN** (only 5 signs between Ä and N: ⊔1 ┘3 └2 ⊔2 □2), AUF DER → **BEI DIR** (┘2 ⊔2 └3 / ⊔1 └3 ⊏3), IM TRAUTESTEN → **IM VERTRAUTEN** (first sign ⊓1 = V, then ⊔2 ⊏3 ┐2 ⊏3 ┘1 ┐3 ┐2 ⊔2 □2).

Other open points:
- The identity of the writer: "Hermann" is the signature. The portal lists the sender as Unknown.
- The left-margin cursive and the address-side writing are plain text and were not part of the decipherment. The reading of "Frau von Blum(?)" on the address side is tentative.
- The tick counts in the upper message were re-checked on enlarged crops and agree with the earlier reading.

## Why this is correct

- One fixed 27-cell key turns all 263 signs into fluent German of around 1900, with no leftover or inconsistent sign. The same key also produces the rare ß (GRÄßLICHE) and Z (SITZEN).
- The upper message is an ordinary love note, signed Hermann. The lower text is a recognisable 19th-century love poem (Heine's "Mädchen mit dem roten Mündchen"), with metre and rhyme kept: Mündchen/Mädchen, klar/immerdar, sein/Kämmerlein. The card's own variants (Kalt, kosen, liebes, süßes Mädchen) are also metrical, which argues against forced readings.
- The date (7 Dec, a winter evening), the place (Bodenwerder to Hameln, two towns on the Weser) and the addressee (a young woman, "Fräulein") all fit the content.

## Credit

The key, the complete upper message, and the first lower fragments (LIEBCHEN MIT DEM, ÄUGLEIN, DU MEIN "LIEBCHEN" (wrong, corrected to LIEBES after review 1), DEINER, ICH, MÖCHTE GERNE, IM …, KÄMMERLEIN) were established on 2026-10-28 by the earlier solver (OpenAI GPT, GPT-6 Astra / GPT-6.1 Sol) and recorded in `NOTES.md`, `work/transcript.json` and `work/decode.py`. On 2026-10-30 Claude Opus 5.5 completed the lower poem from the scan: the full lower transcription (188 signs after the review-1 correction), identification of the Heine source, and correction of three provisional words. Claude Opus 5.5 also wrote `work/transcript_v2.json` and `work/decode_v2.py` and this file.

## Response to review 1

The verdict was REVISE. All four findings are accepted, and the reading is unchanged except for one word.

1. **[major] L4 word 3 = LIEBES: fixed.** The finding is correct. My own 8× crop of `source/picture.jpg` (x 500–675, y 455–492, `work/crops/L4_word3_LIEBES.png`) shows exactly six signs between the slashes: ⊐3 └3 ⊔2 ┘2 ⊔2 ┐1 = L I E B E S. The last sign is a ┐ with one tick, and no ┘3 or └2 is present. The earlier token string was copied from L1 word 1. In `work/build_transcript_v2.py` the word is now `tbr3 bl3 lbr2 br2 lbr2 tr1`. `transcript_v2.json` was regenerated, and `python3 ciphers/hcp-899/work/decode_v2.py` was re-run: the source hashes are OK, L4 = `DU MEIN LIEBES SÜSsES MÄDCHEn`, and the glyph counts are 75 + 188 = 263 (26 obscured). The plaintext, the English and Slovak translations, the glyph totals, the variant paragraph, "Why this is correct", the credit line and NOTES.md have all been corrected. The card now reads "du mein liebes, süßes Mädchen", which agrees with Heine's *liebes*; only *süßes* replaces *kleines*.
2. **[minor] Over-strong "all read from the signs" claim: fixed.** The claim has been removed from the literary-source paragraph. I re-checked against their own crops the words whose token strings repeat another word's: LIEBCHEN (L1, 8 signs, `L1_left.png`), MIT ×3 (L1, L3 `L3_left.png`, L8 `L8_left.png`), DEN (L3), BEI and DIR (L7 `L7_right.png`, L8 `L8_left.png`/`L8_right.png`). All agree with the transcript. The remaining Heine-divergent words (LIEB, KALT, MÖCHTE GERNE, KOSEN, SÜSSES) were confirmed independently by the reviewer, and MÖCHTE GERNE again by me (`L7_left.png`).
3. **[minor] Basis of the restorations: stated.** The three letters ROTEN T, E and KOSEN S are **not visible on the scan**: only the wall shapes of the ROTEN signs show, and the KOSEN sign is completely hidden under the watermark. They were restored when the Heine poem was already known, by the only word that fits. The literary-source paragraph now says this, and so will the report.
4. **[minor] Reproducible crops: fixed.** `work/crop_evidence.py` (run with a PIL-enabled python, `-I`) writes enlarged, contrast-boosted crops to `work/crops/`: the corrected L4 word, the full L4 row, the ROTEN and KOSEN restorations, the rows containing the duplicated words, and a lower-block overview. Each crop's source box is in the script, or it is passed as an argument and recorded in NOTES.md.

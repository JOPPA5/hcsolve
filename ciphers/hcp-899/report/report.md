# HCP 899 (cpc_1902-12-07_DE_Bodenschwerder_DE_Hameln_): a German Pigpen love card from Hermann to Johanne Stiebe, 1902

Human solver: Tomáš Pavuk

**Status: deciphered in full (263 cipher signs: a 75-sign love note and a 188-sign poem). Three letters hidden by the portal watermark are restored. Independent review 1 verdict REVISE; one word corrected (LIEBCHEN → LIEBES), the rest of the reading unchanged.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 899 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/899), portal name `cpc_1902-12-07_DE_Bodenschwerder_DE_Hameln_`, from Tobias Schrödel's collection of cryptographic postcards (private collection). When the record was captured on 2026-10-28, the portal listed it as **Not solved**. It was tagged Postcard, T. Schrödel Collection and Pigpen, with category Substitution / Monoalphabetic, date 1902-12-07, language Unknown, sender Unknown and recipient Johanne Stiebe. No transcription or solution was attached.

The picture side is a "Gruss aus Bodenwerder" greeting card with printed flowers. Its date "7/12.02" (7 December 1902) is in plain writing. The cipher sits in two blocks: a short personal message at the upper right and a nine-row block of verse below it. The numeral "1000" in the message and a few cursive lines in the left margin are in plain writing and are not cipher.

The address side is in plain handwriting: Fräulein Johanne Stiebe, p. Adr. Frau von Blum(?), Hameln a/W., Osterstraße 40. The card is postmarked Bodenwerder and Hameln on 8.12.02. Bodenwerder and Hameln are small towns about 20 km apart on the Weser, in what was then the Prussian province of Hanover. The card is a love message from a young man, Hermann, to an unmarried young woman ("Fräulein") who was lodging in Hameln "per address" of another woman.

![Picture side (source/picture.jpg). The upper-right block is the personal message and the lower block is the poem. The circular HC Portal watermark covers the right half of the poem.](../source/picture.jpg)

![Address side (source/address.jpg): Fräulein Johanne Stiebe, Hameln a/W., Osterstraße 40.](../source/address.jpg)

## Method

The transcription is **manual**. Every sign was read from crops of the 1024 × 680 px scan, enlarged 5–18× with a contrast boost. Where the watermark overlaps the ink, a colour-weighted view was used, because the cipher ink is bluer than the grey watermark. No OCR was used.

The signs are clearly a Pigpen-type cipher: angular cells with one to three short strokes ("ticks") inside, and a slash after each word. Only nine cell shapes occur, so each cell must hold three letters, and the tick count picks the letter within the cell. Filling the nine cells in alphabetical order (A–Z with J, plus ß in the last cell) gives the key below. The earlier solver (OpenAI GPT) found this key on 2026-10-28 from the upper message, which then read ICH HABE GRÄßLICHE SEHNSUCHT NACH DIR …. The same key, unchanged, was then applied sign by sign to the lower block by Claude Opus 5.5 on 2026-10-30.

After the first rows of the lower block had been read, the text was recognised as an adaptation of Heinrich Heine's poem "Mädchen mit dem roten Mündchen" (Buch der Lieder, "Die Heimkehr"). From then on Heine's text was available as a cross-check. Where the card's signs differ from Heine, the signs decide, and the card differs from Heine in six places. The review found that one word had been filled in by copying another row instead of being read (see "Review summary"). After the correction, all words that repeat or diverge from another reading were checked again against their own crops.

## Key

The cipher is a Pigpen with three letters per cell. The cell shape gives the group, and the number of ticks (1, 2, 3) gives the letter. Shape names: t = top, b = bottom, l = left, r = right wall. The cells are drawn as slanted parallelograms.

| Shape | 1 tick | 2 ticks | 3 ticks |
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

An umlaut (Ä, Ö, Ü) is written as two small strokes above the sign. 21 of the 27 cells occur on the card, including the rare ß (in GRÄßLICHE) and Z (in SITZEN). F, J, P, Q, X and Y do not occur, so their positions are inferred from the regular pattern. The cipher writes no capitals. The word-dividing slashes, and a few drawn commas, full stops and a question mark, are on the card. Other punctuation and the capitals below are editorial.

## Plaintext and translation

Decoded, row by row. Letters under the watermark that were read from partly visible walls or ticks are in lower case, as the reproduction script prints them.

```text
U1 ICH HABE GRÄßLICHE        L1 LIEBCHEN MIT DEM ROteN
U2 SEHNSUCHT NACH DIR        L2 MÜndCHEN
U3 SCHREIBST DU              L3 MIT DEN ÄUGLEIN LieB UND KlaR
U4 MIR AUCH                  L4 DU MEIN LIEBES SÜSsES MÄDCHEn
U5 RECHT BALD                L5 dEINER DENK ICH iMMERDAR
U6 [1000] KÜSSE              L6 KALT IST HEUT DER winTERABEnd
U7 DEIN                      L7 MÖCHTE GERNE BEi DIR SeiN
U8 HERMANN                   L8 BEI DIR SITZEN MIT Dir KOsEN
                             L9 IM VERTRAUTEN KÄMmerLEIN
```

Normalised German:

Ich habe gräßliche Sehnsucht nach dir. Schreibst du mir auch recht bald? 1000 Küsse, dein Hermann.

Liebchen mit dem roten Mündchen, / mit den Äuglein lieb und klar, / du mein liebes, süßes Mädchen, / deiner denk ich immerdar. / Kalt ist heut der Winterabend, / möchte gerne bei dir sein, / bei dir sitzen, mit dir kosen / im vertrauten Kämmerlein.

English:

I miss you terribly. Will you write to me quite soon too? 1000 kisses, your Hermann.

Sweetheart with the little red mouth, with little eyes dear and clear, you my dear, sweet girl, I think of you forever. Cold is the winter evening today; I would like to be with you, to sit with you, to cuddle with you in the cosy little room.

Slovak:

Strašne po tebe túžim. Napíšeš mi aj ty čoskoro? 1000 bozkov, tvoj Hermann.

Milá moja s červenými ústočkami, s očkami milými a jasnými, ty moje milé, sladké dievča, na teba myslím naveky. Studený je dnes zimný večer, rád by som bol pri tebe, sedel pri tebe, túlil sa k tebe v útulnej izbičke.

**Comparison with Heine.** Heine's stanzas read "Mädchen mit dem roten Mündchen, / mit den Äuglein süß und klar, / du mein liebes, kleines Mädchen, / deiner denk ich immerdar. / Lang ist heut der Winterabend, / und ich möchte bei dir sein, / bei dir sitzen, mit dir schwatzen / im vertrauten Kämmerlein." The card has Liebchen for Mädchen, lieb for süß, süßes for kleines, Kalt for Lang, möchte gerne for und ich möchte, and kosen for schwatzen. Each of these was read from the signs. The variants keep the metre and the rhymes (Mündchen/Mädchen, klar/immerdar, sein/Kämmerlein). Whether they come from a popular printed version or from Hermann himself is not known. Heine is the literary source of the verse. No published decipherment of this card was found.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-899/work/decode_v2.py
```

The script uses only the standard library. It checks the SHA-256 hashes of the two scans and the metadata, then decodes the shape tokens in `work/transcript_v2.json` with the key. It prints the eight message rows and nine poem rows above, and the counts `upper 75, lower 188, total 263`, with 26 lower glyphs partly obscured. It does not read the image. The shape readings are recorded in `work/build_transcript_v2.py`. `work/crop_evidence.py` (needs PIL) regenerates the evidence crops in `work/crops/`.

## Uncertainties

- **Three restored letters.** The 3rd and 4th signs of ROTEN (T, E) lie under the watermark letters "GPO": only their wall shapes (┐ and ⊔) are visible, not their ticks. The 3rd sign of KOSEN (S) is completely hidden under the watermark "T". These three letters are **not visible on the scan**. They were restored, when the Heine poem was already known, by the only word that fits (RO?EN with ┐ → ROTEN, since ROSEN does not fit before Mündchen; KO?EN → KOSEN).
- **Partly hidden signs.** 23 further signs in the right half of the poem are partly under the watermark (in MÜNDCHEN, LIEB, KLAR, SÜSSES, MÄDCHEN, DEINER, IMMERDAR, WINTERABEND, BEI, SEIN, DIR, KÄMMERLEIN). For each, enough wall or tick remains visible to agree with the reading, and the word is certain. The first sign of DEINER (⊔ with an unclear tick count) can only be D.
- **Resolution.** The scan is 1024 × 680 px, and no larger image is available. Single tick counts were read from about 3–5 original pixels.
- **People.** The writer is known only as "Hermann". The second name on the address ("Frau von Blum?") is a tentative reading of plain handwriting. The left-margin cursive was not transcribed.

![The corrected word in poem row L4, enlarged 8× (work/crops/L4_word3_LIEBES.png): six signs ⊐3 └3 ⊔2 ┘2 ⊔2 ┐1 = LIEBES.](../work/crops/L4_word3_LIEBES.png)

## Review summary

Reviewer: Claude Opus 5.5 (a separate agent), round 1, verdict **REVISE**. The reviewer ran the reproduction command and rebuilt the key from the stated rule with its own independent decoder, and got identical output. It checked the transcription against its own crops (5–14×) row by row, judged the German fluent and the context (date, places, addressee) consistent, and confirmed that the Heine source was disclosed. It found:

1. **[major] L4, third word.** The word has six signs and reads LIEBES, not LIEBCHEN. The earlier token string had been copied from the first word of L1. **Fixed:** the solver confirmed the six signs on its own 8× crop, corrected the transcription and regenerated the output. The lower block is now 188 signs and the card total 263. The poem line now reads du mein liebes, süßes Mädchen, which is closer to Heine than previously claimed.
2. **[minor] Over-strong claim** that every Heine variant was read from the signs. **Fixed:** the claim was withdrawn. Every word whose token string repeats another word's (MIT ×3, DEN, BEI, DIR, LIEBCHEN) was re-checked on its own crop. The remaining variant words had been confirmed by the reviewer.
3. **[minor] Basis of the restorations.** **Fixed:** this report and SOLUTION.md now state that ROTEN T, E and KOSEN S are not visible and were restored with the poem known.
4. **[minor] Evidence crops not saved.** **Fixed:** `work/crop_evidence.py` writes the key crops to `work/crops/`.

No other letter changed.

## Credit

The key, the complete upper message and the first lower fragments were established on 2026-10-28 by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol). That work included the wrong fragment "DU MEIN LIEBCHEN", which was corrected in review. On 2026-10-30 Claude Opus 5.5 transcribed the whole lower poem, identified the Heine source, corrected three provisional readings (MÄGDELEIN → MÄDCHEN, AUF DER → BEI DIR, IM TRAUTESTEN → IM VERTRAUTEN), answered the review and wrote this report. The review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 899, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/899 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/2757/conversions/cpc_1902-12-07_DE_Bodenschwerder_DE_Hameln__pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/2758/conversions/cpc_1902-12-07_DE_Bodenschwerder_DE_Hameln__adr-large.jpg (source/address.jpg).
- T. Schrödel, paper on the postcard collection linked from the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (general background; it does not discuss this card).
- Heinrich Heine, Buch der Lieder, "Die Heimkehr", "Mädchen mit dem roten Mündchen" (public domain), the literary source of the poem.
- AI Decipherment Register (https://ai.hcportal.eu/register/): no entry for this card, checked 2026-10-29.

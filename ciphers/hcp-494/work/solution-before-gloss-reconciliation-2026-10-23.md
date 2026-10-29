# HCP 494 — revised partial reading, updated 23 October 2026

**Still unresolved.** Follow-up work adds archival identification and corrects a probable transcription error in the published reading. The further 23 October attempt finds a key match for a related 1677 letter, but no additional plaintext in HCP 494. Daniel Bourdeau's partial reading, published 9 October 2026, supplied the original key match and most readings; it was consulted before our work. No independent reviewer has accepted this claim.

## New evidence beyond the published attempt

1. **Correspondents:** Secretary **Linker/Lincker → Chancellor Vultejus**. The official [Marburg record](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3352629) attributes the file to Linker and records provenance “Kanzler Vultejus, Paket 5”. The newly retrieved verso bears the docket `H[err?] Lincker an Cantzl. Vulteium` (preferred reading; abbreviation and spelling ending uncertain). This supports the names directly, without identifying given names.
2. **Six archival images are online**, including the wrapper and docket omitted from the three-image portal record. This corrects Bourdeau's claim that the rest of Nr. 125 is not digitized. The added scans contain no further encrypted passage; the final scan is a printed administrative text dated 1738, apparently reused as wrapper material.
3. **Prefer 427, not 447, before 641 / “Herzog von Plön”.** The middle digit has the manuscript's curved 2 form. The later code is 447, with two angular 4s. Consequently the published argument that the same 447 means Herzog at both positions fails. This is a visual correction awaiting independent palaeographic review; see `work/427-vs-447.png`.
4. **At 602 retain the unstruck gloss “Kayser”.** Withdraw the borrowed inference “Braunschweig”. The earlier “Haus Braunschweig” annotation is crossed/overwritten. The preceding 447 remains unresolved. “Kayser” is a manuscript gloss reading, not an independently recovered codebook value.

## Cipher and key

German despatch from Hamburg, HStAM 4 f Staaten D, Dänemark 125, images 2–4; portal date 4 May 1672, dual date read by Bourdeau as 4/14 May. Two short homophonic passages coexist with three-digit nomenclator entries.

The letter table transferred from HCP key 255 (HStAM 4 d 1234, images 13–16) fits many characters. Its endorsement names Secretary Lincker and 1666, with later reuse in 1676. HCP 254 is the corresponding inverse table. **The word list differs from the letter's codes**, and neither the complete 16-image file nor the additional circa-1670 key in 4 d 1235 supplied the missing list.

The unchanged literal letter outputs are:

```text
disgustirtundertazin<Holstein: borrowed gloss>
<Sueco: borrowed gloss>hottgebdasa?wolabl∅u
```

## Partial plaintext and translation

First passage, following clear `Totaliter`:

> Totaliter disgustirt und [ERTAZ: unresolved] in Holstein …

Approximately: “Completely displeased and [unresolved] in Holstein …”. The surrounding clear text concerns nobles, burghers and peasants joining in complaints. The division after `und` is provisional; the cipher has no source word separators here.

Second passage, borrowed interpretation with explicit corrections:

> [Sueco:] Gott geb das all wol ablauff

“[Sweden:] May God grant that everything turns out well.” This requires 55→g although both transferred tables give h, `[I]`→ll, the 8-like sign→au, and the final XX-like sign→ff. The original image confirms that the first number is 55, not a securely readable 53. The gloss supports “Gott”, but cannot settle copying error versus a differing key cell.

Revised ending, abbreviated to the relevant clear words and code groups:

> Der selbige <427 Herzog> <641 Plön> war auch zu Hamburg … eine estroite <303 alliance> zwischen <447 unresolved> <602 Kayser: gloss> und <834 Rex Daniae: gloss> unter Handen …

“The same Duke of Plön was also in Hamburg … has a close alliance under negotiation between [447 unresolved], [602 Emperor, per gloss] and the King of Denmark …”. The punctuation between the unresolved code and 602 is editorial. The phrase `unter Handen` supports negotiation, not the claim that the alliance had already been concluded. Do not restore “Duke of Brunswick” from the earlier published inference.

This is a partial transcription of encrypted inserts and their context, **not a full diplomatic transcription or translation of all three pages**. Code 625 retains the published uncertainty about the Ahlefeldt gloss.

## Reproduce and inspect

From the repository root:

```sh
python3 ciphers/hcp-494/work/followup.py
```

This applies the independently entered letter table to Bourdeau's preserved ciphertext, displays the assumed readings separately, and prints the revised nomenclator occurrences. It also verifies preservation of the initial downloaded sources. Output is archived in `work/followup.json`. The image-based 427/447 correction is explicit input, not an automatic OCR result. Evidence crops: `work/archive-0005-crop.png`, `work/alliance-codes.png`, `work/427-vs-447.png`; source provenance is in `SOURCES.md`.

The reproducible bounded diagnostic in `work/search_corrected.py` tests ERTAZ and ERTAD separately. Several of Bourdeau's saved search scripts still initialize 66=d despite the corrected BB=z transcription; his free-cell search also exists, so no claim is made that z was never searched. The corrected diagnostic finds no acceptable reconstruction. Its training sample is later than the document and the negative result is limited to the tested substitutions and word splits.

## Unresolved

`28 83 117 20 BB` still gives **e r t a z**. No supported replacement, new key, or unique plaintext has been recovered. Reading `undertan in` would require BB→n and remains an unsupported construction. The borrowed 59/64 “meaningful” measure is not a validated whole-document accuracy rate, particularly after the revised code readings above. No completed-solution marker, final report or register entry is warranted.

## Additional attempt, 23 October

The unsegmented suffix diagnostic in `work/search_lattice.py` tested 90,692 distinct strings with up to two letter/syllable/null substitutions. None was accepted. This is a bounded, model-ranked diagnostic; corpus fragments and high language scores are not evidence of decipherment.

A separately retrieved [Lincker letter from 1677](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=2283126), Dänemark 145, matches the **different** 4 d 1235 table. It gives literal `besagtdr <General> bauditz` and a second `bauditz`; the manuscript gloss reads `besagter`. The 55=d/e discrepancy remains explicit, with 21 of 22 letter positions otherwise agreeing. Reproduce this auxiliary comparison with `python3 ciphers/hcp-494/work/compare_1677.py`.

This comparison demonstrates another apparent local key/text discrepancy in related correspondence. It does **not** identify the correct five-letter reading in HCP 494 and does not justify transferring the auxiliary alphabet. The preferred auxiliary date is 3 March 1677, checked from two image locations; the main target remains the 1672 letter. Provenance, crops, failed searches, and limitations are recorded in `SOURCES.md` and `NOTES.md`.

## Continued investigation, 23 October

Nine newly acquired DTA texts from **1647–1669** replace the earlier late-period language sample for a further diagnostic. They attest `disgustirt` in period usage. The analysis ranks **465** distinct local table-column shifts and **57,089** strings with an insertion, deletion or transposition, optionally combined with one substitution. No reconstruction has both linguistic and cipher evidence; the best-scoring strings are not accepted plaintext. Reproduce with `python3 ciphers/hcp-494/work/period_diagnostic.py`; results, source hashes and limits are in `work/period-diagnostic.json`.

Eight further original key pages from **4 d 1232 and 1236** were visually compared. Their values do not match the target's known country/alliance codes. A related 1666 Lincker file and Danish archival inventories provide leads but no acquired duplicate of this letter or matching expanded key. The title in the 625 gloss remains uncertain. **The partial plaintext above is unchanged; this continuation establishes no additional deciphered word in HCP 494.**

## Numeral grouping and further key comparison, 23 October

`python3 ciphers/hcp-494/work/audit_groups.py` exhaustively enumerates valid numeral groupings under the adopted alphabet/null table, without changing any digit. For the preferred BB reading, all **256** distinct strings respecting visible numeric boundaries, and all **832** allowing crossings of those boundaries, still contain `az`. The latter set includes the former. The historical 66 alternative is recorded separately. This does not test missing nomenclator entries or a different interpretation of 20, and it supplies no accepted reading.

Two newly examined Darmstadt files contain other keys: [D 4, 239/1](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3978954) has a different numeric alphabet and word list; [D 4, 206/6](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3816324) has a graphic-sign alphabet dated 1658. Across these files, 321 thumbnails were used for selection and **15 full-size images** were inspected. Their sampled values do not support transfer to HCP 494. Reproduce the entered comparison with `python3 ciphers/hcp-494/work/compare_darmstadt.py`.

**No new plaintext is claimed from these checks.** The unresolved gap remains ERTAZ under the transferred key. Sources and exact search limits are recorded in `SOURCES.md` and `NOTES.md`.

## Passage-1 gap read from the margin gloss, 23 October (Claude contribution)

The human asked Claude to push the work forward, so this section was written by Claude, not the solver. The contemporary decipherer's margin gloss beside passage 1 reads `disgustirt / undertanin / Holstein`. Bourdeau had left the fifth letter as `erta?in`, r or z. It is read here as **n**: the glosser's r is a tall v-shape, and a z would descend, which this letter does not. See `work/margin-gloss.jpg` and `work/margin-gloss-erta-n.jpg`.

> Totaliter disgustirt [sind die] **Undertan[en]** in <634 Holstein>, nun so wohl als in <601 Dennemarck> Adell, Bürger und Bauren … in plainten combiniret

"The subjects in Holstein are totally disgruntled; now, as also in Denmark, nobility, burghers and peasants … have combined in complaints."

The ciphertext glyph remains BB, which is z in key 255; n would be PP. As with 55→g (`Gott`), the gloss shows the intended letter, but not whether the encipherer slipped or the 1672 key differs in this cell. `Undertan` is a shortened plural: the period sample has only `unterthanen`/`underthanen`. Reproduce with `python3 ciphers/hcp-494/work/margin_gloss.py`.

This resolves the ERTAZ gap. Both letter-cipher passages now have a complete reading, with gloss-supported corrections at three points: 55→g, BB→n, and the passage-2 syllable signs. **Still open:** code 447, the 625 title, and the expanded 1672 nomenclator. This step has not been independently reviewed.

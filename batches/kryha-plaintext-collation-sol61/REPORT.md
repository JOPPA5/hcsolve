# HCP350/351 post-recovery pixel collation

Two residual HCP351 readings can be improved from the physical image: position240 is strongly J rather than U; position231 moderately favors I rather than L. Other word errors examined have clear or preferred source glyphs that should not be replaced merely to obtain grammatical prose. Firstfive symbols are physically clear SOSOL in both messages and remain semantically unexplained.

This is independent examination of the pixels and codec implementation **after seeing the recovered prose**, not a blind transcription or independent key recovery. All writes are in this batch. No cipher files, source pixels, or markers were changed. The recovered keys/texts were copied into350/351subdirectories as snapshots; `verification.json` hashes them and all three immutable images.

`check.py` independently constructs absolute coordinates around the52-stop wheel from adjacent distances, traverses the23selectedholes, decrypts all385letters and independently re-encrypts them. Both saved plaintexts match385/385 and re-encrypt exactly to their saved ciphertext. That validates full key/codec consistency on the supplied working strings; it does not make every working glyph physically correct or explain firstfive symbols. This is known-key validation, not blind recovery.

All positions below are1-based, groupsfiveletters; alternative plaintext/ciphertext letters are consequences of the unchanged supplied key. Pixel confidence describes the printed letter, not confidence in the editorial prose.

|Cipher|Position|Group,slot|Saved glyph→literal plaintext|Prose requires glyph→plaintext|Pixel finding|
|---|---:|---|---|---|---|
|350|81|17,1 GMIAG|G→A in DRAAE|W→H|High: distinctly G, notW. Keep literalDRAAE; readingDRAHE is editorial correction.|
|350|122|25,2 LGHFN|G→T in POPROT|V→S|High: distinctly G, notV. Keep POPROT; POPROS is editorial correction.|
|350|315|63,5 JEUNO|O→K in PRISTUPIK|I→T|High: roundclosed O, notI. Keep PRISTUPIK; PRISTUPIT is editorial correction.|
|351|11|3,1 RWQKK|R→Z in MNOHZJH|P→Y|Moderate: R preferred under thick watermark; P not established. Keep sourcealternative explicitly, do not forceMNOHYCH.|
|351|12|3,2 RWQKK|W→J in MNOHZJH|M→C|Moderate-high: W preferred; watermark prevents absolute reading, but no strong M evidence.|
|351|86|18,1 RFPFN|R→S in PSEDAVAIUCI|P→R|Moderate-high: R preferred with visiblelowerleg. P produces attractivePREDAVAIUCI but is not best glyph.|
|351|231|47,1 LVBMF|L→I in EXIITUIE|I→S|Moderate: narrowupright favors I; lowerfoot region is watermark-obscured, so L remains alternative. PreferredIVBMF gives EXISTUIE.|
|351|240|48,5 IIHUU|U→D in LACNDISIA|J→E|High: visible Jhook on lastletter, unlike precedingU. PreferredIIHUJ gives LACNEISIA.|

The two351pixel-preferred alternatives are saved separately in351/pixel-preferred-alternative-{ciphertext,plaintext}.txt. They are diagnostic working alternatives, not edits to canonical files. Applying only strongposition240J yields LACNEISIA while EXIITUIE persists; additionally applying moderateposition231I gives EXISTUIE. The source evidence for231 is weaker and must remain disclosed separately.

First20collation, directly enlarged from source:

|Positions|350cipher→plaintext|351cipher→plaintext|Physical interpretation|
|---|---|---|---|
|1–5|SOSOL→USMMF|SOSOL→UITLF|Allfivecipherletters highconfidence. No printedseparator or indicator annotation. Unknownplaintextprefix cannot be resolved by changingglyphs.|
|6–10|HUJRZ→ZMNOH|HUJRZ→ZMNOH|J atslot3 has lowerhook; HUURZ is weaker.|
|11–15|PMQKK→YCHMO|RWQKK→ZJHMO|350finalK supported, notX.351R/W remain preferredwithwatermarkcaveat.|
|16–20|EWRTH→ZNOST|EWRTH→ZNOST|Bothsame clearprintedgroup.|

351thenhas a doubledT in MOZNOSTTI, atpositions20–21; 350has MOZNOSTI. BothTs are literal output under the saved key, with the second at351position21 encoded by E in EJPLG. Removing either duplicateT would be a plaintext editorial deletion; it is not a justified missing-cipherletter correction. Near theend351has ROZHODNUTI DOTROCHDNI, whereas350has ROZHODNUTIE DOTROCHDNI: insertingE into351would likewise be editorial, not a pixel-derived extension of its385positions. The two messages differ by a plaintext insertion/deletion plus substitutions under this recovered model; that does not authorize shifting source positions manually.

A readable version must separately disclose these additional interpretations:

- Internal I appears where ordinary Slovak spells J: NAILACNEISIA→najlacnejšia, PREDAVAIUCI→predávajúci, IE→je, EXISTUIE→existuje, TELEGRAFUI→telegrafuj. This is lexical interpretation, not a provedhistoricalI/Jrule. Many literalI genuinely remainI; no globalI→J substitution works.
- Literal J occurs at apparent word/sentence boundaries (afterPTS, DRAAE/DRAHE, TRIDNI, NUTNE, MADRIDE, ODOBRENI, VYSVETLENIE). Period/space interpretation is plausible but not a physical punctuation glyph. Allsourcebody symbols are letters; no punctuation is printed at these positions.
- PATDESATPAT differs from standard diacritic-strippedpäťdesiatpäť/PATDESIATPAT by an I. AddingI is editorial normalization. PTS may meanpesetas fromMadridcontext, but the supplied text only establishes literalPTS.
- Letter labels for rare ringpositions were chosen lexically by the parent, not alluniquely recovered. In particular firstfiveoutputletters must not be advertised as establishedhistoricalplaintextnames. State exactcurrentlabeling and this limitation.

The broadly coherent car-purchase/loan telegram is supported by hundreds of literal letters; it does not require concealing the residualerrors. In a report retain385-character prepared strings separately from a readable proposed text, mark[unknownfirstfive], and annotate DRAAE→drahé, POPROT→popros, PRISTUPIK→pristúpiť in350; MNOHZJH→mnohých, doubledT, PSEDAVAIUCI→predávajúci, and missingfinalE in351. StrongIIHUJ and moderateIVBMF can be presented as source-supportedcollation alternatives with different confidence. An editorial version is not the literaloutput ofdecrypt.py.

Reproduce independent fullcodec checks: `python3 batches/kryha-plaintext-collation-sol61/check.py`. Residual character mappings are inresidual-key-map.json. Crops use only nearest-neighbor enlargement of immutablepixels, no retouch; crop-boxes.json records originalcoordinates. First20additionalboxes:350(264,435,624,474),351(252,414,602,452),4× enlargement. Originalimages1024×768. Source hashes verified inverification.json. No browser or UI was used.

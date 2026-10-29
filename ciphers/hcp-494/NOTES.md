# Solver notes — 22 October 2026

## State and scope

No pre-existing directory, markers, or skip.txt entry for 494. Portal status Partially solved. Solver owns exploratory work. No watcher started, following the recorded user correction for this environment. No independent reviewer has evaluated these files.

## Acquisition and prior work

Read README fully. Inspected all three portal tabs; downloaded three unchanged visible large image conversions. User requested Daniel Bourdeau's catalogue. The JIC republication still lists catalogue 341 as open, but the author's current site links a partial reading dated 9 October 2026. The prior reading was disclosed before analysis. Downloaded its working files and inspected key 255 in the portal viewer.

## Independent checks

- Ran the published decrypt.py unchanged: first passage gives disgustirtundertazin<Holstein>; second literally gives hottgebdasa?wolabl·u (plus its gloss-derived country code).
- Transcribed the numeric letter columns and doubled capitals independently from the key image in work/audit.py. Its output agrees. The key confirms 28=e, 83=r, 117=t, 20=a, BB=z.
- Compared the first encrypted passage and its marginal gloss visually at portal large-image resolution. Enlarged crops are unretouched resampling, not extra source resolution. Five-token transcription remains plausible; this is informed checking after reading prior work, not blind transcription.
- With the author's disclosed gloss-driven correction 55=g and uncertain syllable readings ll, au, ff, the second passage reads gottgebdasallwolablauff. This is a supported partial reading with assumptions, not literal output of the transferred numeric table alone.
- Boundary test: without segmentation, the problematic suffix is undertazin. Reading undertan in would require changing BB=z to n (or retranscribing BB as PP). Not adopted: the image does not independently establish PP and the local sentence remains grammatically uncertain. This assistant-authored construction is not new decipherment.
- Focused web queries for disgustirt with Unterthanen/etats supplied no direct witness to this letter. No historical identification or reading inferred from those hits.

## Limits and next useful evidence

No recovered 1672 word list; no verified new plaintext. Bourdeau's 92.2% measure is his token-based classification and is not an independent whole-document accuracy estimate. The 38 letter tokens are independently counted; code-number interpretations remain principally manuscript glosses borrowed via his list, not recovered by the 1666 word list.

Full-resolution archival images, the actual 1672 table, or another copy/nearby letter could distinguish copying error, a different cell, or transcription. The downloaded images are only the portal large conversions. Do not repeat broad language-model searches already reported by Bourdeau without new evidence.

## Reproduce

python3 ciphers/hcp-494/work/audit.py

No DONE, FINAL, PDF claiming a solve, or register entry: no completed solution and no accepted independent review.

## Follow-up after “Posun to” — 22 October 2026

### New archival evidence

The preceding resolution/access limitations are superseded by this section. Retrieved the portal originals through image URLs in Bourdeau's public GitHub metadata copy; then found the official Arcinsys file via identifier search (HStAM / 4 f Staaten D / Dänemark 125). Its six publicly available images include three pages omitted from the portal record. This refutes the prior work's specific claim that the rest of this file is not digitized; it does not establish that another copy or the exact 1672 key survives online.

- Image 1 is an archival wrapper. The catalogue and its caption identify Secretary Linker. Provenance: “Kanzler Vultejus, Paket 5”.
- Image 5 is the verso/docket: preferred reading of its address line, `H[err?] Lincker an Cantzl. Vulteium`. This directly supports Lincker → Chancellor Vultejus. The initial abbreviation and exact ending of the surname are less certain than the two names. Do not infer given names from this.
- Images 2–4 are the known three-page letter. Image 6 is an unrelated printed administrative text dated 12 May 1738, consistent with reused wrapper material, not an extra 1672 ciphertext. The physical reuse interpretation is an inference.
- No new letter-cipher passage in the three additional scans.

### Corrections in the nomenclator transcription

On the full-size image, the code before 641 (gloss “Herzog von Plön”) is preferably **427**, not the borrowed 447. Its second digit is curved like 2 elsewhere in the manuscript; both 4s in the later 447 are angular and descend. Evidence: `work/alliance-codes.png` and `work/427-vs-447.png`. The preferred transcription is strong but awaits independent palaeographic review.

This removes the stated basis for translating the later 447 as Herzog. The overwritten/struck “Haus Braunschweig” annotation cannot securely restore 447. Immediately above the next number 602, the **uncancelled** annotation reads `Kayser`. Accordingly withdraw the prior inferred 602=Braunschweig and retain “Emperor, per gloss” as the preferred gloss reading. It is not a newly recovered codebook value. The clause should remain `<447 unresolved> <602 Kayser: gloss> und <834 Rex Daniae: gloss>`; do not silently turn it into “Duke of Brunswick and King of Denmark”. The clear words `unter Handen` indicate an alliance under negotiation; the prior narrative's “concluded” is too strong.

Neither correcting 447→427 at the first occurrence nor preferring Kayser at 602 resolves the five-letter gap. Nor does it justify recalculating a global percentage of meaning as a validated accuracy measure.

### Key checks

Checked all 16 images of HStAM 4 d 1234, using both archive and portal copies. Pages 12–16 are the previously published Scala/table and its word list. The endorsement on page 16 mentions Secretario Lincker and 1666, with later reuse in 1676. The word list still does not supply the target's codes: Alliance=311 rather than 303, and its numbering ends at 407. Pages 1–7 are other systems (including word aliases and symbolic codes), and pages 8–11 contain the different alphabet already identified as HCP 253. No additional compatible 1672 table recovered.

- HCP 254 confirms the five disputed values independently of reading across the 255 table: 28=e, 83=r, 117=t, 20=a, BB=z. This is an inverse table in the same family, not an independent witness to what was encoded in the letter.
- HCP 253 and 266 have different numeric letter assignments. 253 makes doubled capitals null; 266 uses single capitals and numbers 33 onward. Neither decodes the known passages consistently. Their word lists also differ from the observed glosses.
- Official file 4 d 1235, circa 1670, is one table with A=41–44, D=53–56, G=65–68; Alliance=301. It does not explain the letter's known values.
- At full size the problematic second-passage first number is visibly 55; no support for silently retranscribing it as 53. Literal h versus interpreted g remains a key difference or encipherment error, not settled evidence of a different whole alphabet.

### Corrected diagnostic search

The saved Bourdeau `search_gap.py` describes BB but initializes `ertad`; `search_glyph.py` starts from numeric 66; `search_vocab.py` likewise records 66=d. `search_free2.py` does free the final cell, so this is not proof that the published work never considered z.

Wrote `work/search_corrected.py` to explicitly test **both ERTAZ and ERTAD**, with 0–2 substitutions across the 24-letter normalized alphabet, and attested two-word splits. Each has 5,406 distinct strings; 6,516 and 6,755 forms were scored respectively. The existing eight DTA texts provide 2,985,266 normalized characters and 40,274 word types. No one-substitution five-letter ERTAZ candidate is attested; loose edit-distance neighbors (ertz, etat, hertz, etc.) do not supply a justified reading of this sentence. Top-scoring alternatives are fragments such as “er das”, “er war”, “er hat”; none adopted. These later texts are not an exact replication of the author's older-period model. Negative results constrain only this small search space.

The unsegmented suffix and possible alternative boundaries remain open. No theme, name or assumed event was inserted to force the gap.

### Reproduction and remaining work

`python3 ciphers/hcp-494/work/followup.py` prints the revised partial claim, prior literal outputs, explicit code-occurrence corrections, and preservation check for initial source hashes. Saved output: `work/followup.json`. `python3 ciphers/hcp-494/work/search_corrected.py` reproduces the bounded language diagnostic. Additional crops: `work/evidence_crops.py` (Pillow required).

Remaining evidence needed: the actual expanded word list, another cipher letter using the same list, or a justified palaeographic/cipher explanation for ERTAZ. A follow-up can search correspondence specifically attributed to Lincker and Vultejus; do not repeat an undirected 0–2-letter search as if new. No DONE/FINAL, reviewer, or register entry created.

## Further attempt after “Skus to rozlustit” — 23 October 2026

### Whole-suffix diagnostic

`work/search_lattice.py` extends the earlier fixed five-character test to the entire ten-token suffix `119 74 26 28 83 117 20 BB 37 104` = `undertazin`. It does not fix the boundaries `und / ERTAZ / in`. It permits zero, one, or two changed tokens, each with any of the 24 alphabet values, 21 syllable values present in the comparison key, or an empty value. There are **90,692 distinct resulting strings**. This is a conditional error diagnostic, not a search through all possible ciphers.

Ranking uses space-free 3/4/5-grams from the same eight later DTA texts. No historical name, event, or target gap word was inserted. The fixed Holstein context is inherited from the disclosed manuscript-gloss reading. Model maxima such as `undertallein`, `undertschein`, and `undernachin` are not coherent restorations. The corpus's word inventory includes line-break fragments, so even exact segmentation is not a grammatical test. The segmentation routine was corrected to use the same minimum-word-length rule as its feasibility filter; these diagnostics still admit noisy short fragments. No candidate is accepted. The result does not establish that an enciphering error is the only explanation or that a solution is impossible.

Outputs: `work/lattice-results.json` and `work/lattice-console.json`; source corpus hashes are included. The corrected script was run to completion. The negative result is limited to this alphabet/syllable set, two-token bound, and language model.

### A separately acquired Lincker cipher letter

Found and downloaded all five images of **HStAM 4 f Staaten D, Dänemark 145 (1677)**, from the official archive. Its preferred date is Copenhagen, **3 March 1677**, checked against both the closing dating line and the pencil heading. An initial rough reading as May was corrected before adopting the result. This is a related correspondent, not evidence that its key is identical to HCP 494's.

The already acquired **4 d 1235** table fits the auxiliary letter:

```text
p3: 45 57 109 44 65 113 55 107 / 320 / 46 43 117 54 73 113 133
    b  e  s   a  g  t   d  r   / General / b a u d i t z
    gloss: besagter General Bauditz
p4: 47 43 120 56 76 116 135
    b  a  u   d  i  t   z
```

The repeated `bauditz` uses different homophones; the independently transcribed table's 320 is General. Of 22 letter positions, 21 agree literally with the manuscript glosses. The one discrepancy is **55=d in this table, e in the `besagter` gloss**. On the scan the source number is preferably 55, not an unambiguous 58. Retain literal `besagtdr`; do not silently repair the ciphertext. This supports a local copying/enciphering-error hypothesis, but does not exclude a differing 55 cell. No biographical identification or modernization of the decoded name is asserted.

This is a new auxiliary key match made with the manuscript glosses visible, not blind cryptanalysis and not a decipherment of the remaining HCP 494 gap. The HCP 255 alphabet produces incoherent control outputs (`hiuchrht?dgtcrr?`, `igwdoo?`), confirming that the letter families must be kept separate. In particular, do not transfer 117=u or 55=e from the auxiliary reading to HCP 494.

Reproduce with `python3 ciphers/hcp-494/work/compare_1677.py`; output `work/compare-1677.json` contains the complete entered table, both literal outputs, differences, negative control, and hashes. Crops and date evidence are reproducible with `work/compare_crops.py` (Pillow). A further context crop of HCP 494, `work/passage1-context.png`, is the unaltered rectangle (450,1850,2430,2450) of `source/full/0004.jpg`.

### Search limits and current claim

The digitized `Linker` search for 1668–1673 returns two descriptions of the already retrieved Dänemark 125, not a second copy. Other examined key descriptions are much later (1220 after 1715; 1236 circa 1715; 1238 early nineteenth century). These were catalogue triage, not proof of absence. The current evidence therefore still leaves **ERTAZ**, code 447, and the expanded 1672 nomenclator unresolved. No additional plaintext in HCP 494 was established in this attempt.

Preservation check passed for all 47 preceding source files; six auxiliary sources were added (53 total). No source was edited, no marker or register entry was created, and no independent review has occurred.

## Continued investigation after “pokracuj” — 23 October 2026

### Earlier language evidence and additional error mechanisms

The earlier diagnostics used texts from 1724–1748. To address that limitation, acquired nine original DTA TEI files from **1647–1669**, including Butschky's letter-writing manual, Seckendorff's statecraft, Pufendorf, four Wartmann volumes, Olearius, and Grimmelshausen. The publicly downloadable 2020 DTA archive supplied the files; their ZIP CRCs and uncompressed lengths were validated. No verification cookie or challenge bypass was used. The unchanged XML files belong in `source/dta-period/`; working extractions are in `work/period-text/`. The TEI headers attribute the editions to Deutsches Textarchiv/BBAW and specify CC BY-SA 4.0.

`work/period_diagnostic.py` extracts the TEI body, excludes running headers and notes, prefers original forms inside `choice`, joins explicitly hyphenated line breaks, and normalizes long s, diacritics, j/i and v/u. The resulting sample has **7,981,726 normalized characters including spaces**, and **72,596 word types**. The vocabulary still includes historical abbreviations and imperfectly joined fragments; it is not a curated dictionary.

The concordance finds `diſguſtirt` in Grimmelshausen (1669), in the phrase `diſguſtirt befinden wolten`, and related disgust- forms in Wartmann. This independently attests the word's period usage, but is not a second textual witness to this letter and does not determine the following phrase.

Additional bounded diagnostics, again on the unsegmented suffix `undertazin`:

- **465 distinct strings** from a constant displacement of one contiguous span across the 24 physical alphabet columns, without wrapping at the table edges. Vertical movement alone keeps the same plaintext letter in this homophonic table and cannot explain the gap.
- **57,089 distinct strings** from one insertion, deletion, or adjacent transposition, optionally followed by one letter substitution. These extend the previous replacement-only search; they are local error hypotheses, not globally consistent alternative keys.
- Attested vocabulary neighbors of `ertaz`, using up to three optimal-string-alignment edits and at least two corpus occurrences. Neighbors such as `ertz`, `estat`, and `ertrag` supply no supported reading of the sentence.

Space-free 3/4/5-gram rankings retain the top 100 strings in each error family. Examples at the top are `undertarin`, `undertanin`, `undertzen`, and `undertein`; none supplies both coherent context and a justified cipher/glyph mechanism. This does not amount to manually rejecting every generated string. The previously considered `undertan in` remains unsupported: changing BB=z to n has no new visual basis. No plaintext candidate is accepted. Results and concordance: `work/period-diagnostic.json`; compact output: `work/period-console.txt`.

### Additional key images, beyond catalogue triage

Downloaded and visually compared eight previously unexamined pages:

- **4 d 1232, images 3–4 / portal key 251:** a French syllabic/word table. For example, Berlin=788, Danemark=799 and Holstein=828; these contradict HCP 494's gloss-supported 829, 601 and 634. No transfer adopted.
- **4 d 1236, images 2, 10 and 21 / portal keys 256, 260 and 264:** related encoding/decoding word lists. Their Allianz=236/440 and König in Dänemark=209/423 differ from the target's 303 and 834. They are not three independent matches. These samples strengthen the previous catalogue-only rejection.
- **4 d 1236, image 4 / key 257:** additions for Dresden, Hanau, Münzenberg and Warsaw, with four-digit values. No explanation of the target's three-digit entries.
- **4 d 1236, image 12 / key 261:** a named list for a congress at Soissons, with four-digit values. No matching target list.
- **4 d 1236, image 16 / key 263:** an extensive German syllabic/word table with a different numbering scheme; the Allianz entry is not 303. No matching table recovered. The full second page of this key was not acquired or exhaustively searched.

Image URLs, original metadata URLs, and SHA-256 hashes are in `work/extra-key-downloads.json`. This is an eight-page comparison, not an exhaustive examination of every key in 1232/1236. New plain crops `work/key1236-0016-detail.png` and `work/key1236-0016-h.png` preserve inspection details. No source has been retouched.

### Archival leads and unresolved palaeography

The official **Preussen 332** record (1666, with 1667) describes Lincker reporting from Cleve/Berlin and has provenance Landgräfin Hedwig Sophie, Paket 15. Its rendered detail lists original and microfiche but exposes no digital-copy link. This is a catalogue lead, not an acquired comparative letter.

Danish National Archives search results also identify Lincker correspondence and a `Chiffernøgler` series (1539–1693) within Tyske Kancelli. Opening the detailed DAISY list failed both through web retrieval and the browser (`ERR_CONNECTION_RESET`). Consequently no inventory item, digitization status, or cipher image from that series was verified. The earlier private-archive inventory lead to letters in Ehrenschild's papers likewise remains a lead, not a recovered copy of the target. No archive was contacted.

Reexamined the title above the 625 gloss (`work/625-gloss-enlarged.png`, an ordinary enlargement of original image 3). A possible reading as a chancellor title, instead of the borrowed Statthalter, is **not secure**. Do not use it to identify the person more precisely, date the gloss, or change the adopted partial plaintext. No such correction is made.

### Preservation and outcome

All **53** preceding sources retain their hashes. Seventeen immutable files were added: nine XML texts and eight key images, **70 sources total**. The new inventory is `work/source-sha256-2026-10-23-period.json`; earlier manifests remain unchanged. The two new scripts completed; the acquisition script also validates the cached XML files offline on subsequent runs. HCP 494 still has no supported reading of ERTAZ or code 447, and no recovered expanded 1672 nomenclator. No DONE/FINAL marker, final report, register entry, or independent review is claimed.

## Further continuation: numeral boundaries and two archival keys — 23 October 2026

### Exhaustive grouping within a stated key model

`work/audit_groups.py` tests a different mechanism from the prior letter-edit searches: it keeps the digits unchanged and enumerates all valid 1–3-digit groupings of the suffix. The adopted letter table and explicit nulls are used; zero and leading-zero groups are invalid, and unknown nomenclator values are not invented. The preferred BB and earlier 66 readings are separate branches. The disputed glyph slot stays separate from the surrounding numeral runs, even in the relaxed branch. Code 20 remains a, as in the table's alphabet; treating it as null would be a separate change of key interpretation.

| Branch | Distinct plaintext strings | Segmentation paths |
| --- | ---: | ---: |
| BB, respecting visible period boundaries | 256 | 1,024 |
| BB, also allowing crossings of numeric period boundaries | 832 | 3,728 |
| 66, respecting visible period boundaries | 512 | 2,048 |
| 66, also allowing crossings of numeric period boundaries | 1,664 | 7,456 |

The relaxed sets include the strict sets; do not add their counts as independent candidates. **Every BB-branch string still contains `az`.** The digits ending in 20 cannot be repartitioned into a different valid terminal group under this model, and BB remains z. Thus changing numeric boundaries alone does not remove this obstacle. This is a bounded structural result, not proof that every candidate is linguistically impossible. The zero-edit reading remains `undertazin`; no candidate is accepted. Machine-readable output: `work/group-audit.json`.

### Fresh rendered archival searches

`Lincker`, years 1668–1673, digital copies only, returned two unrelated property-deed records naming Burckard/Burkhard Lincker, not a diplomatic comparison letter. `Chiffren`, years 1660–1680, digital copies only, returned the known Dänemark 125 and two Darmstadt files. These exact search bounds are recorded to avoid confusing a negative query result with archival absence.

1. **HStAD D 4, 239/1**, archival description 3978954, miscellaneous notes of Landgraf Ludwig VI, Band 2. The catalogue explicitly lists sheets with cipher solutions; its broad date span includes 1640, 1653–58, 1664–74 and other material. Acquired all **258 thumbnails** for layout triage and **11 selected full-size delivery images**: 003, 008–014, 031, 063, 096. This is not a full transcription or full-resolution examination of 258 pages.
   - Image 008 contains a homophonic numeric table, but its values differ from HCP 255: 20=c, 28=w, 83=g, 117=d, against a/e/r/t in the target comparison key.
   - Images 009–010 include an auxiliary numeric ciphertext with interlinear readings. Images 010–011 show the associated nomenclator: France=167, Holland=187, Emperor=194; the Danish king has a graphic sign. These do not match HCP 494's gloss-supported 576/774/602/834. No new target key was recovered.
   - Images 012–014 continue miscellaneous material, not a newly identified expanded 1672 codebook. The other selected pages show names, notes/diagrams, book accounts and a correspondence register. No HCP 494 duplicate was identified.
2. **HStAD D 4, 206/6**, archival description 3816324, negotiations over Georg III's Swedish military service, catalogue dates 1658 and 1660. Acquired **63 thumbnails** and **four selected full-size images**: 017, 048, 061, 062. The wrapper at 061 explicitly dates the alphabet to **1658**. Image 062 contains a letter/graphic-sign substitution with an `Otiosa` list; it is not the target's homophonic numeric table or expanded nomenclator. Images 017 and 048 are accompanying correspondence, not an additional matching key.

The manual incompatibility samples are recorded by `work/compare_darmstadt.py` and `work/darmstadt-comparison.json`, with source hashes. They establish differences between these particular tables, not the impossibility of an undocumented later relationship. No complete decipherment of the auxiliary ciphertext is claimed. The key crop `work/darmstadt239-key-crop.png` is the unchanged rectangle (1760,300,3330,2540) of image 008.

### Outcome and preservation

The current HCP 494 plaintext is unchanged. The new evidence narrows a numeral-grouping hypothesis and rules out transferring the two newly examined tables as identical keys. ERTAZ, code 447 and the matching expanded 1672 list remain unresolved. No markers, report or register entry were created. All 70 earlier sources were checked unchanged; 338 additions comprise two METS files, 321 thumbnails and 15 full-size delivery images. The inventory now contains **408 source files**, recorded in `work/source-sha256-2026-10-23-darmstadt.json`.

## Margin gloss re-read: `undertanin` — 23 October 2026 (Claude Opus 5.5, at the human's request)

Written by Claude, not the solver. The human asked Claude to push this cipher forward. That makes Claude a contributor here, so Claude is no longer an independent reviewer of this step.

- The margin beside passage 1 on `source/full/0004.jpg` (about x 110–640, y 1950–2180) has three gloss lines: `disgustirt` / `undertanin` / `Holstein`. Bourdeau read the second line as `erta?in`, with the fifth letter r or z. Neither the solver nor Bourdeau recorded the reading **n**.
- **Palaeography:** this glosser writes r as a tall v-shape with a left hook, as in `disgustirt` and in the r of `ertanin`. The disputed letter is a low two-stroke form like the glosser's n. A z would descend below the line, and nothing descends here. Crops: `work/margin-gloss.jpg` and `work/margin-gloss-erta-n.jpg`.
- **Context:** `Undertan in <634 Holstein>, nun so wohl als in <601 Dennemarck> Adell, Bürger und Bauren …`. The repeated `in` gives a parallel. "The subjects in Holstein, as well as in Denmark, nobility, burghers and peasants, are combined in complaints" fits the clear text.
- **Cipher side:** the glyph is still BB (= z in key 255; n is PP in the same row, see `source/full/key255.jpg`). The gloss is evidence for the intended letter, of the same kind as the `Gott` gloss that supports 55→g. It does not determine the mechanism: an encipherer slip BB for PP, or a different cell in the 1672 key. The 1677 letter's 55 d/e discrepancy shows such single-cell slips occur in this correspondence.
- **Language:** the 1647–1669 DTA sample has plural `unterthanen` 26× and `underthanen` 5×, and no plural `unterthan`. So `Undertan` is a shortened plural, rendered `Undertan[en]`. No verb is enciphered (`sind` is understood).
- This supersedes the earlier "BB→n has no visual basis" judgement. The basis is the glosser's reading, not the cipher glyph. The lattice and period searches had already ranked `undertanin` near the top, and now an independent witness supports it.
- Reproduce: `python3 ciphers/hcp-494/work/margin_gloss.py` (output `work/margin-gloss.json`; crops need macOS `sips`).
- Still open: code 447; the 625 title; the passage-2 syllable readings (`[I]`→ll, 8→au, final XX→ff), whose interlinear glosses above 20 [I] and 50 32 110 8 XX were not settled at this resolution; the expanded 1672 nomenclator.

## Follow-up to Claude's margin reading — 23 October 2026

This continuation treats Claude's proposed margin **n** as the preferred working reading and preserves attribution. The source BB remains z under the comparison key. Earlier entries rejecting `undertan in` without visual support are superseded by the margin evidence; they remain above as the chronology of the investigation.

### Direct comparison of the passage-2 signs

Reexamined original image 4 and the alphabet/syllable portion of key 255. The placeholder `[I]` has a loop above a vertical stem and a lower bar, matching **ll**. The neighboring **mm** sign has its loop below the stem and provides a useful control. This strengthens Bourdeau's existing `all` reading without adding a new plaintext word.

The 8-like sign is compatible with **au** and its annotation supports that interpretation. The final XX-like form remains more difficult: it resembles the comparison key's ff sign in general structure, but also the source's XX=u homophone in passage 1. Thus final **ff** remains a gloss/context-supported identification rather than a unique visual match. The initial number remains preferably **55**, giving h under the transferred table despite the Gott gloss.

`work/current_evidence_crops.py` produces correctly aligned key/target crops and `work/syllable-evidence-sheet.png`, including ll/mm and ff/XX comparisons. Coordinates are in `work/current-evidence-crops.json`. Some earlier `next-*` crops were exploratory and are not used as the labelled evidence sheet. No source image was changed or generatively enhanced.

### Phrase-level interpretation of 447 602

The surviving **Kayser** gloss may explain the entire adjacent pair **447 602**. Its approximate alignment above 602 alone cannot establish the internal allocation of the phrase. The preferred current rendering is consequently `zwischen <447 602: Kayser, phrase gloss; allocation unresolved> und <834 Rex Daniae> unter Handen`. The former editorial comma between 447 and 602 is withdrawn: an additional person is not established by the unknown code. No assignment 447=dem, Haus, Herzog or null is adopted, and the source 447 is not securely cancelled.

This makes the gloss-based working meaning an alliance under negotiation between the Emperor and the King of Denmark. It is an interpretation of the corrected annotation, not recovery of either codebook entry. The earlier Haus Braunschweig gloss remains crossed/overwritten. The separate first occurrence is still preferably 427 before 641/Plön; it cannot establish 447=Herzog here.

The official GStA catalogue entry I. HA GR, Rep. 11 Staatsverträge, Nr. 291 describes the Danish ratification on 1 October 1672 of a defensive alliance concluded at Braunschweig on 12/22 September 1672, involving Denmark, the Emperor, Brandenburg, the Braunschweig princes and Hesse-Kassel. This supplies context, already raised in Bourdeau's publication, but neither identifies the May letter's code values nor proves that its negotiations led to that treaty. The catalogue HTML is preserved; the treaty manuscript was not acquired.

Code 625 was also reexamined. A possible chancellor title remains insecure, so no revised title, given name, or gloss date is adopted. A HAB scholarly-edition search excerpt gives Friedrich von Ahlefeldt's Statthalter tenure as 1663–1676 and grand chancellorship from 1676; only the excerpt was accessible. It is not used to identify or date the target's annotation. Wider historical-name searches supplied no accepted cipher value.

### Qualifications to the preceding contribution

- The annotating hand is **undated**, as Bourdeau explicitly states in his publication. Calling it a contemporary decipherer or assuming access to the authentic 1672 key is not justified. It is evidence on the manuscript, not a newly discovered independent copy of the letter.
- The corpus's lack of a short plural `unterthan` does not establish an abbreviation. `[sind die]` and `[en]` are editorial supplies in the contextual reconstruction; the grammar remains an open qualification.
- The auxiliary 1677 letter contains another apparent key/gloss discrepancy. It does not demonstrate that either discrepancy was a copying slip rather than a different key cell or annotation error.
- The margin reading supports a **probable reconstruction**, not a proven resolution of the cipher/key mismatch. Claude is a contributor and cannot independently review that contribution.

### Reproducible current reading and preservation

`work/reproduce_current.py` reads the immutable ciphertext, applies the independently entered comparison table, and lists all five interpretive exceptions by exact source position. It keeps BB=z globally, records the local n proposal and the prior attribution, and retains the old nomenclator interpretation as history while adding the current grouped assessment. Saved output: `work/current-reading.json`. Both asserted working strings reproduce, and the preservation check finds no changes to the previous 408 sources.

`SOLUTION.md` now presents one reconciled current assessment instead of contradictory chronological conclusions. Its preceding complete contents, including Claude's original wording, are preserved in `work/solution-before-gloss-reconciliation-2026-10-23.md`. Two unchanged HTML sources were added, bringing the inventory to **410 files**, with URLs/hashes in `work/gloss-followup-downloads.json` and the complete manifest `work/source-sha256-2026-10-23-gloss.json`. No completed-solution marker, report or register entry is warranted; no independent review has occurred.

## Claude feedback: disclose amm versus all — 23 October 2026

The user supplied Claude's follow-up assessment in this chat. Claude accepted the qualifications concerning the undated annotator and editorial expansions, and reported running the reproduction command successfully. Its substantive additional finding was an omission in our evidence table: the annotation above **20 [I] reads amm, not all**. Bourdeau had already recorded `amm` in immutable `source/bourdeau/NOTES.md`, line 26. This is newly acknowledged conflicting evidence, not a new plaintext word or a formal independent-review verdict.

Reinspection of `source/full/0004.jpg`, `work/current-p2-ll.png` and the comparison sheet confirms the visible `amm` annotation. The cipher sign still preferentially matches key 255's **ll** (loop above, lower bar), whereas its neighboring **mm** has the loop below. Thus our preferred `all` rests on the glyph/key comparison and linguistic context and explicitly **disagrees with the manuscript annotation**.

Claude suggests the annotator probably confused the similar neighboring signs while using a key of this family. That is plausible, but the discrepancy alone does not establish possession of the key, a definite annotator error, or identity of the 1672 and 1666 syllable tables. A differing table or our own glyph-reading error remains possible. Likewise, the discrepancy weakens an argument that treats the margin n as authoritative; it does not demonstrate that n is wrong. Preserve `undertan in` as a qualified working reconstruction, with the BB=z mismatch and editorial grammar still open.

Checking the cited source also exposed overly definite wording in our final-sign rationale: Bourdeau records the partial gloss `a b l aut`, not an unambiguous `ablauff`. Removed the claim that the annotator explicitly wrote ablauff. The preferred final ff remains based on context and the comparison key with a visually plausible XX=u alternative. No new interpretation of the partial final annotation is asserted.

Updated `SOLUTION.md` and the exact-position evidence in `work/reproduce_current.py`; the generated `work/current-reading.json` now contains an explicit annotation-conflict record and its implication for passage 1. The preferred working strings are unchanged. Preservation checking now covers the complete existing 410-file inventory; no source was added or modified. This is a solver response to contributor feedback, not a review handover, and no marker is created.

## Original signs and key first — 23 October 2026

The user explicitly requested further work from the original cipher signs and key, using the black annotations only as aids. Rechecked both complete comparison tables, the original three letter images, and the disputed original glyphs. This is not blind analysis: the earlier plaintext and annotation readings were already known. The new decoding command does not apply them as key overrides or expand opaque word codes.

### New competing transcription: the 55-like pair may be II

The beginning of passage 2 was previously treated as certainly numeric 55, leading to h under the table and a gloss-driven restoration to g. There is another existing symbol in **both** tables: the doubled I/J-shaped homophone, normalized as **II**, gives **g**. It has two hooked, crossed stems. The target's two elongated hooked strokes are compatible with that character class; they need not be two digits.

Compared the target against the same writer's numeric 5 in **75, 85 and 625**, all on original image 4. Those examples have compact angled heads, unlike the long target strokes. However, the crossbars present in the key's II are not securely visible in the target, and handwriting variation remains possible. Therefore **II is a plausible competing transcription**, not a proved replacement for 55. The former categorical assertion that the shape is definitively 55 is withdrawn. No claim of a new plaintext word is made: Bourdeau already read Gott.

`work/glyph_first_crops.py` reproduces ordinary crops and the labelled `work/glyph-first-initial-comparison.png`, including the forward G/H columns, inverse II=g entry and numeric controls. The final coordinate record is `work/glyph-first-crops.json`; unlabelled `glyph-*` files were exploratory. No ink separation, retouching or generative enhancement was used. The additional full-page check did not supply a secure same-hand repeated cipher II, so that corroboration is still missing.

### Exact consequences under the unchanged key

`work/glyph_first.py` enumerates **eight** branches for the initial pair II/55, the looped sign au/numeric 8, and the final pair ff/XX. The loop-above-stem sign is read ll by its key geometry; the opposite mm orientation is a contrary control. No black annotation is used to alter a key value. One branch gives:

```text
II 76 [tt] 63 38 22 FF 20 75 20 [ll] YY 96 NN 50 32 110 [au] [ff]
g  o  tt   g  e  b  d  a  s  a  ll   w  o  l  a  b  l   au   ff
```

Thus the familiar passage-2 candidate can be generated with **zero changed key cells**, conditional on II, au and ff being the correct glyph identifications. Numeric 55 still gives hott; final XX gives ablauu; numeric 8 yields ablff or ablu. These alternative outputs are recorded rather than silently rejected by grammar. The script does not rank them with a language model, and fluency of the working branch does not prove its glyph identifications.

Treating the first passage's XX as ff would give `disgffstirt`; treating the final passage-2 pair as XX=u gives `ablauu`. This shows why globally substituting XX=ff is not an acceptable fix. It does not establish that the two handwritten forms must be different symbols. The final ff identification remains unresolved visually.

### First passage: no original-sign basis for n recovered

The literal result remains `disgustirtundertazin<634>`. Direct comparison of the looped pair with BB=z and PP=n in the key still favors BB. The prior numeric 66 alternative would produce `disgustirtundertadin<634>`. Substituting PP would produce the proposed undertanin but is recorded only as a **counterfactual**, because PP has not been securely read in the source. No new n identification is claimed; the margin-based interpretation remains secondary. The prior exhaustive numeral-grouping and bounded language searches are not rerun or represented as new evidence.

### Scope and verification

Saved output: `work/glyph-first.json`. The original-sign command leaves 634 and 768 opaque; the country meanings still depend on annotations and are not recovered from the incompatible comparison nomenclator. Earlier gloss-assisted output remains available in `work/current-reading.json`, with the initial-pair rationale updated to disclose both II and 55 possibilities. The displayed working words are unchanged, but a new possible mechanism removes one previously assumed key mismatch.

Both commands preserve all 410 source hashes. No source download, independent review, completed-solution marker or register entry is added. Remaining decisive evidence would be a secure same-hand II/55 comparison or another witness/key; the present shape hypothesis is not sufficient to mark the entire letter solved.

## Continuation: original-sign controls and remaining 1236 attachments — 23 October 2026

**Outcome: no additional accepted plaintext or newly resolved glyph.** Rechecked the 1672 original, the II/55 comparison, both comparison alphabets, BB/PP, and the final ff/XX-like pair. The auxiliary 1677 `113.55.107` crop has compact numeric 5 heads. It is a useful qualified control, but it is five years later and the same writing hand has not been established. It does not decide II versus 55. No new secure connecting stroke was established for final ff; both ff and XX remain. BB=z remains the preferred transcription/key reading; there is no new original-sign support for PP=n. No brown stroke hidden by black ink was reconstructed.

The previously sampled 4 d 1236 keys had unexamined continuation pages. Retrieved the public metadata records for keys 256–265 through GitHub and acquired **11** additional original images: **3, 5, 7, 8, 9, 11, 13, 15, 17, 22, 23**. The saved audit `work/key1236-followup.json`, reproduced by `python3 ciphers/hcp-494/work/audit_key1236_followup.py`, records the observations and their limits:

- Pages 3, 8, 9, 11 and 22 continue/copy the already encountered word list, rather than providing independent keys. Direct examples include 601=le Pretendant, 576=Bremen, 602=Mr. Martine and 625=Vestung. These differ from the target's annotation-assisted country/name readings. The target's black glosses are secondary evidence, not assumed ground truth.
- Pages 7 and 23 are copies of a different numeric alphabet, with a=10–15 and g=47–52; they do not clarify the target's doubled capitals or syllable glyphs. Page 5 repeats four-digit additions, and page 13 contains four-digit word/name material and correction instructions.
- Page 15 supplies a different place list, including Hollande=256 and Holstein=266. Page 17 continues the dense syllable/word scheme from page 16 through M–Z. Neither establishes the target's expanded list. No exhaustive transcription of the dense lists is claimed.

All image attachments represented by catalogue keys 256–265 have now been acquired and visually screened across the two passes. This is **not** a complete examination of every archival page of 1236, all Marburg keys, or all combinations of reused alphabet and nomenclator. No values from these different tables were silently transferred into HCP 494. The failed 266.json request was a missing public file, not evidence of an access restriction or a missing archival key.

All **410** preceding source files retain their hashes; 10 metadata records and 11 JPEGs bring the total to **431**. Both current decoding scripts now verify this complete inventory. Their letter readings and the eight conditional branches remain unchanged. No marker, completed report, register entry or independent review was produced.

## Continuation: same-page numeral controls and archival cross-references — 25 October 2026

**No additional accepted plaintext or resolved cipher sign.** The rendered portal's General, Description and Attachments tabs still show Partially solved, the description “Message containing encrypted parts.” and the three original image pages, with no new solution attachment. Rechecked complete comparison-key pages 14–16; no newly identified instruction explains BB→n. Prior letter-table and word-list incompatibilities remain.

### Original glyphs before annotations

`work/numeral_six_controls.py` produces `work/numeral-six-controls.png` and its exact coordinate/hash record. It compares the disputed BB-like pair with the same page's 6 in 67, 26, 63, 96 and 625. The last digit of 96 is partly overlapped by the black gloss, a disclosed limitation. The target's small lower loops and elongated upper strokes remain compatible with BB, but variation in numeric 6 prevents a categorical shape-only exclusion of the older 66 alternative. No new support for PP=n was recovered. Thus literal `undertazin` remains; `undertanin` remains an annotation-assisted restoration. No hidden strokes were reconstructed, and no source pixels were changed. An earlier exploratory sheet mislocated the 26 crop; it was discarded and the final sheet was visually checked against the source.

### New catalogue route, with cross-references followed

Browsed selected pages of the Danish politics classification (183 entries, not every record examined), rather than relying only on the earlier digital-copy-filtered name searches. The spelling **Lynker** led to a bounded simple search, years 1660–1680, all archives, without the digital-only filter: three hits, comprising Dänemark 105, a cross-reference to Dänemark 102/105, and an unrelated pastor.

Inspected eight relevant detail pages. Dänemark 105 (1668) mentions secretary Lynker in Berlin; Dänemark 141 (1677) concerns Linker in Hamburg and has Chancellor Vultejus provenance. The apparent nearby Hamburg 2 lead (1671–1672) was followed to its main record, which describes **Otto v. Guericke's** correspondence, so it is not established as a same-writer control. Dänemark 102's main record and political cross-reference share original representation 6846811. All inspected details listed original/microfiche representations without an observed digital-copy link; this does not establish absence of scans elsewhere.

The main political record **Preussen 345**, archival description **4046380**, explicitly names **Georg Lincker**, Hessian secretary reporting to Hedwig Sophie from Berlin and Königsberg in 1668, including his mission to Denmark. This improves the contextual search lead. It does not establish the given name of the 1672 sender, identity of writing hands, a cipher-key change, or a newly decoded name. A further web search returned the already known later Danish diplomatic-archive lead and later Lincker records, not a new acquired 1672 witness. No name or historical narrative was inserted into the cipher output.

Exact search bounds, identifiers, and limits: `work/archive-followup-2026-10-25.json`. These are manual browser observations, not manuscript acquisitions. The existing 431 sources and decoding branches remain unchanged; no completed-solution marker or independent review is warranted.

Verification: both decoding commands completed successfully on 25 October, matched their saved JSON outputs exactly, and checked all 431 source hashes without changes. The final numeral crop sheet was regenerated with the partially obscured control explicitly labelled.

## Different route: numbering constraints and original-text B/P controls — 25 October 2026

The user requested another route from original signs and key. This pass first tested **nomenclator-number structure without accepting the black glosses**, then compared the cipher pair with **original clear-text letters in the same letter body**, rather than only with the other hand's key or the numeral 6.

### Bounded numerical result independent of the gloss meanings

Reinspected the complete key-255 word-list pages: the numerical envelope is 180–407. Read the 26 large-number occurrences from the immutable transcription, using only their page and number fields. With occurrence 21 read as the previously preferred 427 there are 17 distinct numbers; retaining Bourdeau's 447 instead leaves 16. Both variants were tested.

`work/audit_nomenclator_numbering.py` asks whether all these numbers can be reciphered into the old list with one fixed transformation. For each transcription it exhausts the six permutations of three digit positions, all 400 invertible multipliers modulo 1000, and all 1000 offsets, with digit permutation **before and after** the arithmetic. This is 4,800,000 parameter choices per transcription; the orders overlap, so these are not asserted to be distinct functions. Leading zeros are allowed internally. Every integer in 180–407 is accepted, including unassigned gaps, making the target range more generous than the actual list.

| Transcription | Operation order in decoding | Models fitting all codes | Maximum distinct numbers in range | Minimum outside |
| --- | --- | ---: | ---: | ---: |
| 427, 17 distinct codes | digits, then affine | 0 | 12 | 5 |
| 427, 17 distinct codes | affine, then digits | 0 | 13 | 4 |
| 447, 16 distinct codes | digits, then affine | 0 | 12 | 4 |
| 447, 16 distinct codes | affine, then digits | 0 | 13 | 3 |

Thus one misread or exceptional distinct code cannot explain the failure **within these model families and assumptions**. Numerical range coverage is not decipherment accuracy, and the best partial mappings are explicitly rejected. This does not rule out a new/expanded nomenclator, separate transformations for different blocks, arbitrary substitutions, or running-key systems.

The counting implementation is checked against direct enumeration for all 1000 translations of a boundary/wraparound sample. Two synthetic controls, one for each operation order, recover the deliberately generated mappings and produce full-range models. They validate implementation, not the historical model; the synthetic inputs are labelled as constructions. The best reported coverage is also recomputed directly from its mapped values. No statistical or linguistic success is inferred.

A separate **conditional, annotation-dependent** comparison checks the original-key entries France 228, Holstein 253, Holland 232, Denmark 212 and Alliance 311 against the provisional target meanings at 576, 634, 774, 601 and 303. It rejects a common offset, a single rational affine mapping, a modulo-1000 affine mapping, and an order-preserving insertion-only expansion. The country/title distinction for Denmark is explicit; the 447/602 phrase is not used as an anchor. These are not newly recovered code values and are not inputs to the primary range test. Full output: `work/nomenclator-numbering-audit.json`.

Also reinspected the nearby 1234 pages 1–4 and key-253 pages 8–11 while checking whether a differing letter alphabet might conceal a usable word-list component. The viewed key-253 word list runs 300–409, including 303=Chur Cölln and 330=Alliance; page 11 is its endorsement, not a continuation through the target's 800s. The earlier pages shown contain a wrapper, a French-key endorsement/addition, and a graphic-name table. No hybrid matching word list was recovered; this is not a new exhaustive search of every possible combination of archival lists.

### New visual basis for considering PP, with contrary controls retained

**P in the original word Proposition**, on image 0004, has a conspicuous small lower loop and tall upper stroke, like the disputed pair previously transcribed BB. This is in the original brown text, not a black decipherment annotation. It supplies a visual basis for considering **PP=n** under the unchanged key. The previous categorical statement that PP has no original-text support was too strong and is withdrawn.

The comparison deliberately also includes **B in Brunsvicense** on the same page and **b in breviat** on image 0003; these have similar lower loops. **Portrait** has a different P form, and **abfertigung** provides another b. The word contexts identify the comparison letters. Mixed clear-text scripts and cipher-capital conventions prevent treating a match to one plain-text letter as proof. No secure repeated cipher PP or independent handwriting review is claimed. Prior knowledge of Claude's Undertan reading also prevents calling this blind discovery.

The target, initial-letter details, whole-word contexts and contrary controls are in `work/plaintext-bp-comparison.png`, reproduced by `work/plaintext_bp_controls.py`. Its JSON records original coordinates and source hashes. Some panels duplicate each native pixel at 2x for inspection; there is no ink removal, contrast manipulation or reconstructed stroke. The ephemeral exploratory sheet remains outside the repository and is not the labelled evidence.

The exact consequences of the three glyph readings are:

```text
BB -> disgustirtundertazin<634>
PP -> disgustirtundertanin<634>
66 -> disgustirtundertadin<634>
```

All use unchanged comparison-key cells. **PP has moved from a purely counterfactual control to a visually motivated, unproved alternative.** BB remains live. The familiar `undertan in` wording is still credited to Claude; the new contribution is a possible original-glyph mechanism, not a new plaintext word. If PP is correct, no local BB→n restoration is needed. If BB is retained, n remains the secondary annotation-assisted restoration. The grammar, editorial `[sind die]`/`[en]`, and 634's gloss-derived country meaning are still not established by this comparison.

Updated both decoders and `SOLUTION.md` to make that distinction explicit. Preserved the preceding solution and JSON outputs in `work/*before-bp-comparison-2026-10-25.*`. The passage-2 hypotheses and word-code readings have not been strengthened by this B/P result. The current returned Bourdeau webpage still reads the pair as BB and does not present this Proposition comparison; its original key match and most readings remain credited. No source was acquired or modified, and no completed-solution marker or independent review was produced.

Verification after this revision: all three commands (`glyph_first.py`, `reproduce_current.py`, `audit_nomenclator_numbering.py`) completed successfully and each verified all 431 original-source hashes. The eight passage-2 branches, the broader working plaintext strings and all word-code interpretations match the preserved preceding outputs exactly. The new PP branch gives `disgustirtundertanin<634>` with zero changed key cells. No state marker exists.

## Expanded same-letter B/P verification — 25 October 2026

The user requested testing PP against further original signs in the letter. **PP is now provisionally preferred over BB, but remains unverified.** No new nomenclator value or plaintext word is claimed; the contribution is stronger original-sign evidence for the previously proposed Undertan reading.

Visually inspected all three original letter pages and added three capital-B controls: the detached **B in Lit. B** on image 0004, and **Berlin** and **Berlino** on image 0002. Together with Brunsvicense, these show an additional lower right bow/return after the upper bow. No comparable extra bow is visible in either disputed sign, whose termination is closer to P in Proposition. This is more informative than the small lower stem loop shared by P, B and connected b/B. Lit. B supplies an especially useful detached capital: its extra bow is not a connection to a following letter. Both complete target upper loops are retained in the expanded crop.

A separate check compares original clear-text **F in Foedus** with cipher **FF**, and **L in Lit.** with cipher **LL**. Their resemblance supports transferring the writer's clear-text capital forms to the cipher, although it cannot establish a universal writing convention. The second FF has a disclosed black-gloss overlap. These checks concern glyph shapes, not an independently recovered plaintext for the cipher letters.

Contrary and unlike forms remain visible. Connected b/B in breviat is still similar to the disputed pair; Portrait has a different P. German-script beylage (two occurrences), Burger, Bauren and abfertigung are separated from Latin capitals. Lower-case p in passato, promissis and plainten is also separated. Thus this is not a pooled classifier or a claim that every B must have a visible right lower bow. A simplified B remains possible. No second unambiguous cipher PP/BB was found: the preserved two insert transcriptions contain nine doubled-capital tokens with one BB, plus a separate II/55 hypothesis. This count is from the transcription, not automatic recognition of the whole letter.

`work/expanded_bp_controls.py` records 31 rectangles across the original images and comparison key and produces five sheets: `expanded-bp-capitals.png`, `expanded-bp-limits-and-key.png`, `expanded-bp-word-contexts.png`, `expanded-bp-script-variants.png`, and `expanded-bp-cipher-controls.png`. All were visually checked after rendering. Images use native pixels or nearest-neighbor duplication; no ink removal, rotation, sharpening or invented stroke. The feature judgments in `expanded-bp-controls.json` are manually entered observations, not automated conclusions. Some exploratory crops were miscentred; only the corrected, context-checked rectangles are published.

The resulting working branch is still `disgustirtundertanin<634>` with unchanged PP=n; BB=z and 66=d remain explicitly reproducible alternatives. The marker-free source transcription retains BB. The margin n is corroborating evidence only, and is not needed to compute the PP branch. Code 634, segmentation and the proposed plural expansion remain unresolved by this visual comparison. All passage-2 ambiguities and nomenclator interpretations retain their previous status.

Saved the preceding solution and two outputs as `work/*before-expanded-bp-2026-10-25.*`, then updated the current claim and both decoders. No independent review, source acquisition, completed-solution marker, final report or register entry is produced.

Verification: the expanded comparison generator and both decoding commands completed successfully. All 431 source hashes match. The three passage-1 branch strings, all eight passage-2 branches, gloss-assisted plaintext strings, nomenclator occurrences and alliance fragment match the preceding state; only the evidence assessment and preferred passage-1 branch changed. The expanded comparison's three conditional outputs agree exactly with the decoder, and every branch still changes zero key cells. No state marker exists.

## Original-sign verification of II/55 and terminal XX/ff — 25 October 2026

The user requested the same original-sign method for the two remaining passage-2 pairs. **Outcome: II=g is now provisionally preferred over 55=h, while terminal XX=u is provisionally preferred by shape over ff. Neither identification is verified.** This strengthens the initial g hypothesis but leaves a literal `ablauu` ending; the previously fluent `ablauff` remains a separate intended-text hypothesis. No new plaintext word or nomenclator meaning is accepted.

Added original numeral-5 controls in **500, 50, a second 625, 775 and 576**, alongside the previous 75, 85 and page-4 625. All eight have visible bends/bowls rather than the target's long hooked forms. In particular, 500/50 supply initial-position 5, so the comparison is no longer only against numerals ending a group. The two key directions distinguish II=g and 55=h. Original German-script **Ihr/Ihro** gives I/J variants, but no clean same-form capital or second unequivocal cipher II was found. The target key-style upper loops/crossbars remain unestablished; the nearby black gott annotation is not used to invent them. The 1677 numeric-55 control remains qualified by uncertain hand identity and is not new evidence from this pass.

For the ending, the added **inverse-key XX=u** crop has looped upper arms like the final pair, so that small-loop feature does not distinguish ff. Both the target and passage-1 XX have separate crossed forms. Key255 ff instead has two staves connected by diagonals; comparable links are not visible in the target. Original **st/tt** preserve their connecting curves, weakening a blanket claim that the writer routinely omitted connectors. This is not conclusive for ff because there is no independent encrypted ff by this writer. Ordinary plaintext ff is a different writing object and is not used as a special-symbol control. Key254 supplies XX=u but no independent ff entry on the inspected sheet.

Three interpretations are kept separate: (1) both X-like pairs are XX, giving disgustirt and the unresolved ending abl au u; (2) a simplified ff collides graphically with XX, permitting disgustirt and ablauff, but that writing rule is unproved; (3) a global XX=ff reassignment produces disgffstirt and is not applied. A copying error or a changed 1672 scheme is also possible, not established. The global contrary control cannot refute every local homograph model. Bourdeau's published ablauff remains credited; the black partial annotation is not treated as a new ff proof.

`work/p2_original_controls.py` produces **five sheets from 24 rectangles** and `work/p2-original-controls.json`. All final sheets were visually checked against the originals; exploratory miscentred/clipped crops were corrected before inclusion. Original pixels are shown at native size or doubled with nearest-neighbor duplication, without contrast manipulation, rotation, ink removal or reconstructed strokes. These are manual feature judgments made with prior plaintext exposure, not a blind test or classifier. The source set is unchanged.

Preserved the preceding solution and outputs as `work/*before-p2-controls-2026-10-25.*`. Both decoders now expose the difference between the shape-preferred `<768>gottgebdasallwolablauu` branch and the retained language-driven `<768>gottgebdasallwolablauff` candidate. All eight original branch strings remain available. PP's assessment and the word-code readings are not changed. No marker, report, register entry or independent review is produced.

Verification: the crop generator and both decoders completed successfully, checking all 431 source hashes. The three passage-1 alternatives and preferred PP branch, all eight passage-2 alternatives, prior fluent candidate, gloss-assisted plaintext strings, nomenclator occurrences and alliance fragment exactly match the preceding outputs. The newly selected shape branch agrees with both current decoders and the comparison record, and changes zero key cells. The preserved source transcription still has 55 and terminal XX; no marker exists.
## Continuation, 28 October 2026: a new key corpus and a narrower ff argument

Older dated entries remain unchanged. No new verified plaintext word or numeric
code was recovered.

- Live rendered portal 494 remains Partially solved, with three images and no
  solution attachment. The opened Bourdeau article still gives BB and 55; JIC is
  an attributed republication, not another witness.
- Acquired and triaged all 309 images in the newly found Danish TKUA Chiffer
  corpus. The solver team split 1–75, 76–150, 151–309; 49 selected images
  received individual inspection. The bundle includes older/later keys despite
  its approximate 1670–1709 catalogue title. Several concrete alphabet and
  nomenclator conflicts were documented, but no whole-corpus transcription or
  proof of absence is claimed. Research and screening notes retain exact scope.
- The detailed Ehrenschild inventory lists 14 Georg Lincker letters, but none from
  1672. Brandenburg reports 1670–72 are catalogued but absent from its linked
  scan-volume index. Neither Georg nor Johan Henrik Lincker is established as
  the target secretary. No fresh original letter was recovered.
- The official 1236 viewer supplies eight scans 0117–0124, seven new locally and
  one photograph of an already-held sheet. The tested 121–122 table differs:
  a=19–24, 601=Gnad, 768=lar, Holstein=666. No target key found.
- Terminal ff: the key graphic may be two overlapping crossed components. Greater
  spacing could remove contact without deleting independent connectors; original
  st/tt retaining their connections does not directly test that mechanism.
  This qualifies our earlier too-strong connector argument. It does not prove ff:
  XX=u remains directly compatible with passage 1 and inverse key 254. No third
  terminal glyph or supported alternative segmentation emerged.

Updated SOLUTION and decoder evidence notes to disclose that qualification.
The same PP/BB/66 and eight passage 2 branches are retained, with no changed key
cells. The previous solution and decoder outputs are saved as
`work/*before-spacing-2026-10-28.*`. Black annotations remain secondary.

Artifacts: `work/danish-witness-2026-10-28.md`, its range-specific screening
records, `work/danish-screen-root-2026-10-28.md`,
`work/key266-search-2026-10-28.md`, and
`work/ending-alternative-2026-10-28.md`. All new downloaded research material
has a separate hash/URL manifest. No watcher or state marker was created.


Verification: both current decoders passed all 431 prior source hashes. All three passage-1 alternatives, eight passage-2 branches, gloss-assisted plaintext strings, nomenclator occurrences and alliance fragment remain unchanged. The 309 Danish key scans, 22 inventory scans and eight official 1236 downloads matched their acquisition hashes. Exact verification counts are saved in `work/verification-2026-10-28.json`.


## Continuation, 28–29 October 2026: identity, public key delivery and enclosures

**No further cipher word or nomenclator value is accepted.** Original signs and unchanged key255 remain primary; both terminal branches and the PP/BB and II/55 alternatives are preserved. The preceding current solution is saved as `work/solution-before-archival-routes-2026-10-29.md`.

1. Ribbeck1899 was recovered and its opening print pages visually checked. It names Georg Lincker and connects Hessian and Danish service with Berlin until April1672 and subsequent Hamburg/Denmark work. This now strongly supports the contextual identity Georg Lincker; the target signature was not newly expanded. Johannes Vultejus's institutional office chronology identifies the likely recipient. Ribbeck's statement about interlinear decipherments in1666–69 correspondence does not date the1672 black annotations. `work/lincker-identity-witness-2026-10-28.md` preserves exact sources and bounds.
2. The 1235 public METS has one image, identical to the existing source. It is a real table, not merely a cover. Its alphabet and code range remain different. The key255 cover provisionally reads '1676 mit dem Herzog zu Cell[?]'. That led to NLAHA CelleBr76Nr127(1674), which expressly contains a cipher key with Bernstorff's Kassel/Mannheim reports. No scan link was exposed. Other Celle searches and their finite coverage are in `work/key1235-full-2026-10-28.md`.
3. Root rendered all21 rows of HStAM4d's Chiffern group. The adjacent1230–1233 records are catalogued around1730. The separate files1218/1220/1238 supplied624 layout thumbnails; selected parts of60 full scans were inspected, with concrete incompatible alphabets and word values. This does not exclude the untranscribed full pages. See `work/marburg-key-group-root-2026-10-28.json` and `work/marburg-extra-keys-2026-10-28.md`.
4. Public DECODE metadata covers46 records/124 thumbnails of1236 and4 records/16 thumbnails of1234. All140 thumbnails were screened. The ordinary full-image click in R4719 displayed insufficient permissions, so full-image access was not pursued or circumvented. A question about existing user access remains pending. The parent separately opened public HCP266's four images through its normal gallery; three continuation pages were previously missing locally. They do not contain601/634/768 and their numeric list ends454. No HC Portal data API was queried. Exact crosswalk and download evidence: `work/decode-key-search-2026-10-28.md` and `work/hcp266-continuations-2026-10-28/README.md`.
5. The live HCP list filtered by1236 has40 records. Root followed the22 additional observed record links267–288 and captured their displayed large-image URLs. A helper inspected all22 images in full; no matching255 alphabet was found. Repeated table families are explicitly grouped, and no physical-key count is inferred from image count. See `work/hcp1236-expanded-2026-10-29/README.md`. HCP285's single-sheet correction/addendum is not evidence for a correction in HCP494; its date, users and underlying correspondence remain unestablished.
6. The1677 letter comparison does not authenticate the same hand. It supplies no direct cipher controls for PP/BB, II or ff/XX. Its previously known55=d versus annotatione discrepancy stays explicit. `work/same-hand-1677-2026-10-28.md` records full selected inserts and original-word comparisons.
7. A punctuation microcheck found two brown dots after the terminal crossed pair and one after internalP1XX. Other code groups have extra punctuation, and the key gives no ff dot modifier. The final horizontal pair still lacks an exact control; neither an ff-marker rule nor the precise punctuation function is proved. `work/terminal-punctuation-2026-10-28.md` records both20-token inserts and26 word-code occurrences.
8. The original clear text supplies two separate enclosures: A for the Rendsburg Landtag proposition and B for a request by an Anhalt secretary, surname provisionally Raumer. Root's first Kammer guess was superseded by the helper's independent Raumer reading; the subsequent given-name identification is contextual. The apparent second name after Cantzler was withdrawn in favor of uncertain ordinary words 'schon wißen'. The located LASA Raumer-family file has111 scan pages, not556 independent pages. Its catalogue strings have apparent date/name inconsistencies. No enclosure B or cipher witness has yet been identified. Original reading and precise archival lead: `work/enclosure-context-2026-10-28.md`.
9. The nearby Latin text was read independently from brown ink: secure span 'olim non erat ita … hostis'. Helper prefers invidiosus, root initially read insidiosus; punctuation/segmentation remain uncertain. No word-code value follows from this alone. `work/latin-context-2026-10-29.md` preserves the uncertainty and original crop.

All new research downloads stay under work with manifests; the431-file original source inventory is unchanged. No watcher, handover/completion marker, register entry or finished-solution report is created. None of the helper checks is an independent solution review.

## Independent glyph panel, language and context checks — 29 October 2026 (Claude Fable 5.1, at the human's request)

Written by Claude, which the human asked to push the work forward; Claude is therefore a contributor here, not the independent reviewer. Thirteen subagents ran in one workflow; all files are under `work/claude-2026-10-29/`. Nothing in `source/`, `SOLUTION.md` above this point, or the state markers was touched.

### 1. Glyph panel: nine independent judgements, unanimous

Each of the three disputed signs was judged by three subagents with different lenses (refute the solver's preference; refute the alternative; systematic feature comparison), each working from the original scans and both key tables with its own `sips` crops (`panel-*/`). Full output: `panel-summary.md` / `panel-summary.json`. The agents were told both candidate readings, so this is independent but not blind.

| sign | verdict (9/9) | confidence | basis |
|---|---|---|---|
| passage 1, pos. 16 | **PP = n** | 0.80–0.85 | one bow closing on the stem at mid-height, bare lower stem; all 5 capital B's by this hand (Lit. B, Brunsvicense, Berlin, Berlino, Bey) have a second lower bow, all 3 capital P's (Proposition, Praedicat, Pourtrait) do not; key 254/255 draw PP/BB with the same distinction; 66 excluded (writer's 6 has an open rising arc, bowl at the bottom, no foot loop) |
| passage 2, first sign | **II (JJ) = g** | 0.75–0.85 | two strokes ≈57–66 px tall descending below the dot line vs every numeral 5 on the page ≈35–42 px on the baseline with cap bar and bowl; hooked, crossbar-less construction as in the key's JJ and the writer's Ihr/Ihro |
| passage 2, last sign | **XX = u as drawn** | 0.75–0.80 | identical to the passage-1 XX in every writer-specific trait (separate starts, lower-left entry curls, upper-right flags, offset parallel hairlines); the key's ff is a joined monogram with one long slash through both staves, an N-connector and serifs, none of which is present |

Errors the panel found in the solver's evidence, all checked by Claude on the crops:

- The control labelled **"b/B in breviat"** (`expanded-bp-controls.json`, box 1590,1690,1750,1810 on image 0003; cited in `SOLUTION.md` as contrary evidence "connected b/B in breviat still resembles the target") is the capital **P of "Prædicat"** — the solver's own `page3-diplomatic-2026-10-29.md` line 13 reads "kein praedicat". It is a third P control supporting PP, and with it the only visual example of "a B lacking the extra bow" disappears. Crop: `panel-bp-refute-preferred/praedicat-context-3x.png`.
- "Portrait supplies another, differing P form": Pourtrait is a single-bow P with a foot loop, differing only in bow size; not contrary.
- The 28 October "spacing" rescue of ff (`ending-alternative-2026-10-28.md`) misdescribes the key's ff graphic: at 8× it has one continuous slash through both staves plus a separate N-type connector; pulling two crossed components apart would leave collinear fragments, not the two offset parallel hairlines of the terminal pair. The key's own XX glyphs are joined in both tables while the writer separates his, so spacing cannot discriminate XX from ff in either direction.
- Minor: key 254's header reads *"Scala über den Clavem mit Secretarium Linckern"*, tying the comparison key to the sender by name; the group read 50 in passage 2 may be 30 (both = a).

### 2. Period language (`language-passage1.{py,json}`, `language-passage2.{py,json}`; local DTA corpus 1647–1669, DTA online, DWDS/Grimm)

Passage 1:
- Bare *Unterthan* as nominative plural is **unattested** 1600–1700 (corpus: 567 plural -en forms, 28 bare forms all singular or predicative; Grimm knows it only as dat./acc. plural). A **collective singular** *der (arme) Unterthan* = "the subjects" is attested (Sachs, Gryphius, Hohberg 1682, Abraham a S. Clara 1686) but always with an article. So `Undertan[en]` is a restoration without exact parallel; `[der] Undertan` collective is the better-attested alternative, with the article dropped as dispatch shorthand.
- *disgustirt* of persons/estates is well attested (Theatrum Europaeum 1635 "die Catholischen Stände disgustirt", Grimmelshausen 1669, Abraham 1692).
- Exhaustive segmentation of u-n-d-e-r-t-a-?-i-n with ? ∈ 24 letters + 21 syllable signs: **`undertan | in` is the only reading whose every piece is a real period word in sense**; it needs ? = n. BB = z yields nothing; the glosser's own split `und | ertanin` never yields a word.
- The margin gloss is written `und ertanin` with a gap, i.e. the annotator did not himself segment "undertan in".
- Syntax: *disgustirt* most naturally refers back to the Landstände of the preceding sentence; `Undertan[en] in Holstein … Adell, Bürger und Bauren` is then the subject of `in plainten combiniret`. *Adel, Bürger und Bauern* is a generic population triad, not the formal Holstein estates formula.

Passage 2:
- *ablauffe* (3 sg. subj., "turn out") and *wol ablauffen* are solidly attested 1628–1702 (Birken 1652, Wartmann 1650–53, Glauber 1658, Lütkemann, Bucholtz 1659, Hohberg 1682). The exact wish formula *Gott geb daß … wol ablauff(e)* was not found; the apocopated finite *ablauff* occurs in DTA only as the noun (18/18). Apocope itself is normal (DTA "Gott geb" 209 hits) and **the cipher's own `geb` (63 38 22) is apocopated**, so *ablauff* matches the writer's habit.
- **`ablauu` and every segmentation of a-b-l-au-u return zero hits** anywhere; the two dots and clear text after the pair show the word is complete. The shape-literal branch yields no German.
- Pronominal *all* for *alles* is rare (~1:100) but attested in exactly this region and year (Scriver, Magdeburg 1672 "GOtt Lob all wol") and normal in Low German.

Net: the shape says XX, the language says ff, and neither can override the other. The honest statement is: the writer drew the sign for u where the sense requires the ff syllable — an enciphering slip or a graphic collision in the 1672 scheme, not a verifiable ff.

### 3. Historical context (`history-1672-alliances.md`, `history-context-2026-10-29.md`, OCR excerpts in `history-sources/`)

- **Rendsburg Landtag, 24–29 April 1672** (Ratjen, Kiel manuscript catalogue 1858; Rathjen, Findbuch LASH Abt. 65.1 Nr. 311; Pufendorf XI §41; Wienbarg 1862): the dispute was **12 versus 10 Reichstaler per Pflug** for the defence troops, the sovereigns' deputies threatened to impose 12 by patent, the estates ended with a supplication and the 12 were later "theils militariter exequiret". This matches the clear text (proposition, 12 vs 10, "protestando voneinander geschieden", "ad rigorem Executionis") exactly and supplies the unit the solver could not read.
- The Brandenburg envoy of the reception dispute (630 = "Blumenthal" per gloss) is **Christoph Caspar von Blumenthal** (1638–1689), in Denmark autumn 1671 and at Glückstadt/Rendsburg in April 1672 with a documented precedence quarrel; his dismissal letter is dated 26 April 1672 (UA XVII; Pufendorf XI §40–41; GStA Rep. 63 Nr. 327).
- **Frederik von Ahlefeldt** was Statthalter of the duchies from 1663 (storkansler only 1676) and went ahead to Holstein in late March 1672 for the king's visit — consistent with the 625 gloss "Statthalter Ahlefeldt".
- **Duke of Plön = Hans Adolf** (1634–1704), imperial Feldmarschallleutnant, reigning since 5 Oct 1671; he carried the Emperor's alliance draft to Copenhagen in Jan–Feb 1672 (Danish counter-draft 13 Feb 1672), travelled via Berlin to Vienna and back, and reached Rendsburg on 27 April 1672 (Danmark-Norges Traktater VI pp. 525–527; Jørgensen, Griffenfeld II pp. 20–30). Hamburg lies on that route; the letter is the only attestation of Hamburg.
- The *Foedus Dano-Brunsvicense* of the clear text is the **31 March 1672** Danish–Brunswick alliance, already concluded. The alliance still "unter handlung" on 4 May 1672 and expected "ehistes tages" is the **bilateral Denmark–Emperor defensive alliance** (in fact stalled, signed only 16 Jan 1674). So the uncancelled gloss **Kayser fits the history and the struck "Haus Braunschweig" does not**; with exactly two parties named ("zwischen 447 602 und 834"), 447 602 is most plausibly one two-part designation of the Emperor. 601 and 834 can coexist as separate entries (country vs sovereign), as in HCP 266.
- The Franco-Swedish treaty of 3/14 April 1672 excluded Denmark at Sweden's demand, matching the letter's complaint and 768 = Sweden as *insidiosus hostis*.

All of this is context agreement, not key recovery; no code value is established by it.

### 4. A further prior reading, not yet in SOURCES.md

The history agent found, and Claude verified and saved, **Cipher-Atelier / Maxim Egorov, "Lincker's cipher letter to Vultejus (May 1672)"**, https://github.com/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672 (published 6 Oct 2026, migrated from cayde-6/historical-cipher-research, commit 24a7ae8f). Its `diplomatic_inventory.txt` carries a correction dated **2 October 2026**: "Main block group 17 is PP, not bb/BB. It matches the same writer's P in the clear word Proposition. Key PP = n. Revised literal output: disgustirtundertanin[634]." Sequence B is given as `[678?]{g}ottgebdasallw{d/o}lablau{u/ff}`. It offers no nomenclator values or translation. **This means the PP = n reading by the Proposition comparison was published three weeks before the solver's 25 October B/P comparison and before Claude's 23 October margin reading**; it must be credited. Copies with hashes: `work/claude-2026-10-29/cipher-atelier/` (README sha256 8a88267177…, CHANGELOG abe1d38740…). The solver should add it to `SOURCES.md` and to the attribution paragraph of `SOLUTION.md`.

### 5. What Claude concludes and recommends

- PP = n and II = g are now supported by nine independent judgements, by the language test (only `undertan | in` is German) and by the context (Rendsburg Landtag). They should be stated as the preferred transcription, not as "provisional, not verified".
- The terminal sign should be stated as XX by shape with `ablauff` as the intended text, disclosed as the one remaining letter-level discrepancy between sign and sense.
- Correct the "breviat" control to "Praedicat" and withdraw the spacing argument.
- Record Cipher-Atelier in `SOURCES.md`; credit it for PP = n.
- The letter-cipher passages are then fully read; what remains unsolved is the expanded 1672 word list (16–17 codes known only from glosses). On that basis the solver can decide whether to submit a `DONE1` as a partial solution for formal review — a decision for the solver, not for Claude.

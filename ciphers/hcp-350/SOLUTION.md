# HC350 — reviewed content decipherment and working key

**A 23-stop adjustable Kryha model recovers the substance of this telegram:** a car costing 55,000 pesetas, a request for a loan, an alternative purchase in France, and a decision within three days. A complete working key in a mechanically consistent adjustable Kryha interpretation is supplied and decodes/re-encrypts all 385 characters of the declared manual transcription. The first five characters and exact historical preparation remain unresolved. The connected message content and working key are recovered. Claude accepted350 and upheld351 subject to the source corrections addressed below. The exact historical preparation remains incomplete; this is not a claim of error-free archival plaintext or uniquely identified original machine settings.

## Origin and scope

The portal record is MZV message No.3001/1944, Cieker to MZV Bratislava, Slovak National Archive, MZV box42; 28 February 1944. Its status is Not solved and its Unsolvable tag is recorded without treating it as a proof. Original images in `source/` are immutable. No published solution or plaintext for350/351 was found or used. Solved391/392/394 were read as disclosed context for other telegrams, not as the plaintext of this pair.

The human supplied Claude's outside batch review, which identified the decisive350[i]→351[i+1] periodic relationship. We credit that lead. Recovery of the cycle, physically ordered masks, input ring and readable content followed through our scripts and generic Slovak language scoring; the reviewer-provided output cycle and a target plaintext were not search seeds. GPT-6.1 Sol subagents did the cycle, physical and language searches and independent audits; the main OpenAI GPT solver integrated the result and explicitly selected the rare-label interpretation below. Earlier GPT-6 Astra work did not produce this content recovery.

## Reproduce the exact prepared output

From the repository root, one command:

```sh
python3 ciphers/hcp-350/work/kryha-decipherment/decrypt.py
```

Requires Python3 standard library. Because the source is a scan with no supplied transcription, this command uses the **manual source transcription** `work/kryha-decipherment/ciphertext.txt`; it does not claim OCR. Before decoding it verifies every original source-image SHA-256 against `key.json`. All385 source positions are represented, including the first group. Pixel-supported edits relative to the earlier working reading are listed in `pixel-manifest.json` and the original source remains unchanged. Working transcription hashes are recorded in `transcription-hashes.json`.

The default `reviewed` variant includes the post-review351 readings11 R→P,12 W→M and231 L→I, in addition to the earlier240 U→J correction. The source crops and reasoning are in `batches/kryha-review1-main/`; all are prose-assisted reinspection, not blind. Positions11/12/231 agree with Claude's independent pre-recovery blind transcription. Position86 retains visually preferred R despite the blind P alternative; raw PSEDAVAIUCI is not silently corrected. Position73 retains O. The numerical key is unchanged. `--variant collated` preserves the exact DONE1 default via `ciphertext-before-review1.txt`; `strong`, `moderate` and `collated-moderate` preserve their earlier snapshots, including disputed stamp readings. For350 all variants are identical. `--json` reports exact re-encryption. No language cleanup, I/J replacement, omission or indicator removal is performed.

## Physical key and algorithm

- Input ring, letters at coordinates0…25: `JERGZMPADHLQTVNYFSBUICXKOW`.
- Output ring, letters at coordinates0…25: `AKXRMDTGJWNHVIPULYESZQBFOC`.
- Active52-hole selector stops, zero-based and in walking order: `47, 49, 51, 0, 2, 4, 5, 8, 11, 13, 17, 20, 21, 24, 26, 29, 31, 34, 37, 40, 42, 44, 45`.
- Initial stop47; initial displacement0. Consecutive selected stops are joined by summing the literal adjacent-wheel distances in `key.json`; one ordinary press advances to the next selected stop after each character. All23 arcs together traverse52 holes and179 units.

Let P[k] be the input letter at coordinate k and O(c) the output coordinate of ciphertext c. At position i decode `P[(O(c_i)−D_i) mod26]`, with D starting0 and advancing by the next physically walked arc. `key.json` stores P as letter indices and O as **letter→coordinate** (so O's array is the inverse of the output ring printed above). The reverse encoder is checked for every position. This is a mechanically consistent adjustable Kryha key, with 23 active stops, not the earlier17-step original Kryha model.

The two copies share the rings and initial physical stop but differ in selector stops:350 follows47 with49,51,0,2;351 follows47 with48,49,51,2. The selected hole0 is replaced by48. Full masks are in both key files. The output ring and displacement differences were recovered by finite-field/CRT error-tolerant common-cycle analysis. Ordered two-mask DP narrows the physically admissible family; subsequent fixed-ring exhaustive path scoring and all one-swap input neighbors recover meaningful text. The final search exhausts1,084,757 paths per fixed-P pass, not all possible joint rings at once.

The printed input ring includes the explicit lexical relabeling oldG→X, oldQ→G, oldX→J, unusedoldJ→Q relative to the blind six-gram candidate. This gives EXISTUIE, TELEGRAFUI and sentence-boundary J. **These rare labels are semantically selected, not uniquely established by the frozen language model.** The unused coordinate cannot be recovered from observed text. Historical use of J as this sentence marker, or a rule merging word-internal I/J, has not been established. The primary German commercial J/extra-press procedure is not imported; it would be a different model.

## Literal prepared plaintext — all385 positions

```text
USMMFZMNOHYCHMOZNOSTIKUPITAUTONAILACNEISIAIEZAPATDESATPATTISICPTSJAUTASUVELMIDRAAEJPREDAVAIUCIAUTACAKAODPOVEDTRIDNIJPOPROTPANAPREDSEDUOPOZICKUVUVEDENOMOBNOSEPRETOZETUNEMOZEMVZIATNASEBATAKUDLZOBUAAUTOZOSLUZOBNYCHDOVODOVIENUTNEJEXISTUIELACNEISIAKUPAVOFRANCIIZAFRANKYLACNOKUPENEVMADRIDEJNATUTOMOZNOSTVSAKMOZNOPRISTUPIKPOVASOMODOBRENIJMIKUSNECHDAVYSVETLENIEJTELEGRAFUIROZHODNUTIEDOTROCHDNI
```

This is exactly the command's output. The first five raw decoded letters are `USMMF`, arising from the identical initial ciphertext group `SOSOL`. It is probably an unenciphered indicator, an inference rather than a documented procedure: both cipher groups are identical although the two body keys give different displacements and different raw letters there. Its meaning is unknown. We do not invent a natural-language reading. 350 text from position6 begins ZMNOHYCHMOZNOSTI; the reviewed351 reading begins ZMNOHYCHMOZNOSTTI. The shared editorial reading begins “Z mnohých možností…” and the final ten letters read “DO TROCH DNI”; therefore the earlier20-letter prefix/10-letter suffix framing conjecture is withdrawn.

## Readable Slovak reconstruction — editorial, not literal output

> [First five source characters unexplained.] Z mnohých možností kúpiť auto najlacnejšia je za päťdesiatpäť tisíc pts. Autá sú veľmi drahé. Predávajúci auta čaká odpoveď tri dni. Popros pána predsedu o pôžičku v uvedenom obnose, pretože tu nemôžem vziať na seba takú dlžobu a auto zo služobných dôvodov je nutné. Existuje lacnejšia kúpa vo Francii za franky lacno kúpené v Madride. Na túto možnosť však možno pristúpiť po Vašom odobrení. Mikuš nech dá vysvetlenie. Telegrafuj rozhodnutie do troch dní.

Spaces, accents, sentence boundaries, word-internal J and local repairs are editorial. This reconstruction combines the two related copies and Slovak grammar; it is **not** an independently surviving archival plaintext. `editorial-differences.json` records its differences from the raw string after the explicitly declared removal of the first group and putative sentence markers. In particular raw PATDESATPAT is interpreted as päťdesiatpäť, adding a letter; DRAAE/DRAHE, POPROT/POPROS and PRISTUPIK/PRISTUPIT demonstrate why this paragraph must not be presented as exact decryptor output. The same reconstructed wording is proposed for both copies; that does not erase their literal differences.

## English translation of the reconstruction

> [First five source characters unexplained.] Among the many possibilities for buying a car, the cheapest is for fifty-five thousand pesetas. Cars are very expensive. The seller of the car is waiting three days for an answer. Ask the chairman for a loan in the stated amount, because I cannot take on such a debt here, and a car is necessary for official duties. A cheaper purchase is possible in France using francs bought cheaply in Madrid. This possibility can, however, be pursued after your approval. Let Mikuš provide an explanation. Telegraph the decision within three days.

“Chairman” translates predseda without asserting the identity of the officeholder. The reading of PTS as pesetas follows the Madrid/currency context. France, Madrid and Mikuš occur in the recovered text. No external historical event or vehicle identity is asserted.

## Evidence and unresolved points

1. Independent adjacent-hole decoding and separately inverse-indexed encoding reproduce385/385 characters for **both** keys on the archived strong variants; the independently audited fixed-key240J/optional231I variants retain the same full mechanical coverage. `python3 batches/kryha-content-audit-sol61/audit.py` also verifies the signed full-message extension, source hashes, physical rotation and explicit relabeling without importing our decoder. This proves mechanical consistency, not the correctness of every source glyph or label.
2. Fresh TEST-corpus controls, generated with independent random rings and23-stop masks, are recovered385/385 in both messages by the six-gram language/physical stage **conditional on supplied output-ring O and displacement-difference ΔK**. The input ring and physical masks/start are unknown to that stage; this is not an end-to-end ciphertext-only full-ring recovery control. Cipher-only cycle recovery also survives25 independently injected symbol errors. Input-ring, mask and plaintext truth are not supplied to ranking; the stated conditional output structure is supplied. Seven-gram recovery is not uniformly successful and is not used as a blanket negative conclusion.
3. The paired text, physical period23 and long coherent message with a matching ending give strong evidence for the content. Under the archived strong transcription the aligned interior had six literal discrepancies; the DONE1 default correction351240J reduced this to five. The reviewed default also adopts231I and has four:350 positions81,85,122,315 against351 positions82,86,123,316. The old stamp-moderate branch separately had four before240J correction; do not confuse these variant names. The former351240U reading was wrong and is explicitly superseded;231L/I remains ambiguous. Printed350122G/315O and35186R have particularly clear/preferred support despite the prose errors. These may be transmission/preparation errors, genuine differences or model imperfections; their cause is not established.
4. The initial SOSOL group, complete historical preparation rule, unique rare input labels and some glyphs remain uncertain. Original-ring uniqueness up to physically irrelevant gauges is not claimed. The 351 date caveat remains. No register entry is created for the unresolved historical preparation/first-group portion; the accepted content recovery is distinguished from a complete historical-procedure claim.

## Reproducibility and earlier attempts

`batches/kryha-shift23-sol61/REPORT.md` records the credited lead, cycle recovery and source edits. `batches/kryha-two-mask-main/REPORT.md` documents the physical DP. `batches/kryha-two-mask-refine-sol61/REPORT.md` records full-length controls/search and language ambiguities. `batches/kryha-source-residuals-main/REPORT.md` preserves the clear printed discrepancies. `batches/kryha-content-audit-sol61/REPORT.md` is the independent whole-message key check. `batches/kryha-procedure-sol61/REPORT.md` records the failed search for a documented SOSOL/IJ rule. `batches/kryha-plaintext-collation-sol61/REPORT.md` documents the newer240J and231I readings and explicitly corrects the earlier all-eight-glyph agreement. `batches/kryha-prefix-sol61/summary.json` records finite alternate-prefix mechanics: ordinary/extra/held presses and independent prefix resets leave ambiguity rather than a supported natural-language reading. The portal public Cipher Keys global filters SOSOL and Kryha showed no rows on2026-10-11; this is a bounded visible metadata search, not proof that no archival key exists. These are solver-team audits. Claude's independent provider review is complete and addressed below.

The former unresolved SOLUTION is retained verbatim at `work/kryha-decipherment/SOLUTION-before-content-recovery.md` as historical search provenance. Its “no plaintext/key” assertions are superseded by this content recovery. Offset0 mathematical rejections never applied to the actual shifted pair. The original pooled-profile K[0]/K[j] bug is disclosed in NOTES and batch reports; corrected direct separate-mask scoring and independent mechanics avoid it. Earlier unsupported heuristic negatives remain non-exclusions. No watcher or reviewer was launched: the human's explicit outside-review/polling protocol overrides README's watcher paragraphs.


## Response to review 1

Claude Opus5.5 verdict **ACCEPT**. Its independent decoder reproduces all385 letters and re-encrypts them exactly. The review also compares a pre-recovery blind transcription: it agrees with all four350 corrections and independently supports the recovered content. The reviewer supplied the original paired-period lead and explicitly disclosed that limit on independence; the numerical key/content recovery was the solver team's work.

1. **Physical interpretation:** retained “mechanically consistent adjustable Kryha key”; the report distinguishes recovered rings/displacement increments from unverified original machine identification and hardware settings.
2. **SOSOL:** now described as probably an unenciphered indicator, explicitly an inference. Its meaning remains unknown and the decoder still covers all385 positions.
3. **One-stop difference:** the report notes as conjecture that replacing hole0 by48 could explain a repeat being unreadable under the other key. This is not a proven historical error.
4. **Garbles:** the report compares raw350 DRAAE/POPROT/PRISTUPIK with351 DRAHE/POPROS/PRISTUPIT, preserving all clear source letters. Also discloses350 PREDAVAIUCI versus351 PSEDAVAIUCI (sourceR/P alternative).
5. **Outcome:** now states content and working key recovered, while keeping original procedure, first group and rare-label ambiguity open. No register entry for the remaining partial historical claim. Earlier raw snapshots remain reproducible.

Additional validation after DONE1, not rerun by Claude: `batches/kryha-endtoend-sol61/REPORT.md` preserves two fresh clean385-letter paired controls with the full cipher-only chain, supplied only period23, +1 pairing, geometry and generic TRAIN scores. Exact texts and both masks occur among the two predeclared6/7-gram winners in each control. No single objective passes both; automatic single-winner selection remains unvalidated. This supplements rather than replaces the review's actual blind-source check.

# HC350: reviewed car-purchase telegram

Content and working key recovered. The first group and exact historical preparation remain open. Independent review: ACCEPT.

## Origin and recovered message

MZV message No. 3001/1944, Cieker to the Ministry of Foreign Affairs, Bratislava; Slovak National Archive, MZV box 42. Portal status at acquisition: Not solved, tagged Unsolvable. Portal date: 28 February 1944.

These are two copies of one underlying Slovak telegram about a car for 55,000 pesetas, a requested loan from the chairman, a cheaper possible purchase in France using francs bought in Madrid, Mikuš, and a decision within three days. No published plaintext of either target was used.

## How the working key was recovered

Claude’s outside batch review supplied the decisive shifted pairing, 350[i] ↔ 351[i+1], with period 23. The solver team recovered the common output cycle using finite-field/CRT error-tolerant equations, fitted two ordered stop masks to published wheel geometry, and ranked input rings and admissible paths by generic Slovak n-grams. Neither a target plaintext nor Claude’s proposed output cycle was a search seed. A final fixed-input pass enumerated 1,084,757 paths; this was not exhaustive over all joint rings.

Relative to 350, copy 351 has an extra T at position 21 in MOZNOSTTI and lacks E in final ROZHODNUTIE. This accounts for the +1 body alignment and realignment for final DOTROCHDNI. The two model masks differ by one selected stop: hole 0 in 350 becomes 48 in 351. A wrongly set stop could explain an unreadable repeat, but that historical explanation is conjecture.

## Working key and mechanically consistent interpretation

Input ring, coordinate → letter: JERGZMPADHLQTVNYFSBUICXKOW. Output ring, coordinate → letter: AKXRMDTGJWNHVIPULYESZQBFOC. JSON stores output O in the inverse direction, letter → coordinate. The working displacement sequence has period 23 with total advance 179 modulo 26.

Selected stops, zero-based and in walking order: 47, 49, 51, 0, 2, 4, 5, 8, 11, 13, 17, 20, 21, 24, 26, 29, 31, 34, 37, 40, 42, 44, 45. Initial stop 47; initial displacement 0. Ordinary clockwise pressing between selected stops gives increments: 7, 7, 5, 7, 7, 3, 10, 11, 6, 14, 10, 3, 10, 7, 11, 7, 10, 10, 10, 7, 8, 3, 6.

At each character c, decode P[(O(c)−D) mod 26], then add the next increment to D. Both ring arrays are permutations. All 23 arcs traverse the 52-hole wheel once. This is a mechanically consistent adjustable Kryha interpretation; it does not identify the original hardware or prove that these were its historical settings. The recovered rings and displacement increments are the decoding evidence.

## Reproduce all 385 positions

```text
python3 ciphers/hcp-350/work/kryha-decipherment/decrypt.py
```

Run from the repository root using Python 3 standard library. The command checks original-image and manual-transcription SHA-256 values, decodes every position, and independently inverse-encodes the result. It uses a manual source reading, not OCR. It omits no prefix and performs no language cleanup. Key, source provenance, alternate readings and raw snapshots accompany this report in the cipher directory.

## Literal prepared plaintext: all 385 characters

```text
USMMFZMNOHYCHMOZNOSTIKUPITAUTONAILACNEISIAIEZAPATDESATPATTISICPTSJAUTASUVELMIDRAAEJPREDAVAIUCIAUTACAKAODPOVEDTRIDNIJPOPROTPANAPREDSEDUOPOZICKUVUVEDENOMOBNOSEPRETOZETUNEMOZEMVZIATNASEBATAKUDLZOBUAAUTOZOSLUZOBNYCHDOVODOVIENUTNEJEXISTUIELACNEISIAKUPAVOFRANCIIZAFRANKYLACNOKUPENEVMADRIDEJNATUTOMOZNOSTVSAKMOZNOPRISTUPIKPOVASOMODOBRENIJMIKUSNECHDAVYSVETLENIEJTELEGRAFUIROZHODNUTIEDOTROCHDNI
```

## Readable Slovak reconstruction — editorial

[SOSOL: probably an unenciphered indicator, meaning unknown.] Z mnohých možností kúpiť auto najlacnejšia je za päťdesiatpäť tisíc pts. Autá sú veľmi drahé. Predávajúci auta čaká odpoveď tri dni. Popros pána predsedu o pôžičku v uvedenom obnose, pretože tu nemôžem vziať na seba takú dlžobu a auto zo služobných dôvodov je nutné. Existuje lacnejšia kúpa vo Francii za franky lacno kúpené v Madride. Na túto možnosť však možno pristúpiť po Vašom odobrení. Mikuš nech dá vysvetlenie. Telegrafuj rozhodnutie do troch dní.

## English translation of the editorial reconstruction

[SOSOL: probably an unenciphered indicator, meaning unknown.] Among the many possibilities for buying a car, the cheapest is for fifty-five thousand pesetas. Cars are very expensive. The seller of the car is waiting three days for an answer. Ask the chairman for a loan in the stated amount, because I cannot take on such a debt here, and a car is necessary for official duties. A cheaper purchase is possible in France using francs bought cheaply in Madrid. This possibility can, however, be pursued after your approval. Let Mikuš provide an explanation. Telegraph the decision within three days.

## Differences retained, not silently repaired

| 350 position / 351 position | 350 literal | 351 literal |
| --- | --- | --- |
| 81 / 82 | DRAAE | DRAHE |
| 85 / 86 | PREDAVAIUCI | PSEDAVAIUCI |
| 122 / 123 | POPROT | POPROS |
| 315 / 316 | PRISTUPIK | PRISTUPIT |

Positions identify the differing letters in the shown words, not each word’s start. These four interior differences remain in the reviewed default. Copy 351 also has the extra T and missing final E. Their source/transmission/preparation cause is not established.

## Uncertainties and source readings

The same source prefix SOSOL yields USMMF under the 350 body key and UITLF under 351. Because the body displacements differ there, it is probably an indicator sent unenciphered, an inference rather than a documented rule. The count 385 includes it; the decryptor retains it. Its meaning remains unknown.

Rare input labels were explicitly selected by meaning: old G→X, old Q→G, old X→J, unused old J→Q relative to the blind six-gram candidate. The unused label is not determined by this text. Sentence J and word-internal I/J normalization are historical-procedure hypotheses. Spacing, accents and local repairs are editorial; PATDESATPAT is read as päťdesiatpäť by adding I. No archival clear-text draft was found.

After review, 351 positions 11/12 were changed RW→PM and 231 L→I. Prose-assisted source reinspection and the earlier independent blind reading agree; stamp overlap leaves alternatives. Position 86 remains R because its diagonal leg is visible, with P disclosed as the blind-reader and correct-word alternative. Position 73 remains O; blind U was marked uncertain. The earlier strong 240 U→J correction is retained. Default --variant reviewed uses these readings; --variant collated reproduces the DONE1 default. The other archived variants preserve their original glyph alternatives.

## Independent review and responses

Claude Opus 5.5 wrote an independent decoder from the prose and numeric key, covering and re-encrypting 385/385 letters of both copies. Its pre-recovery blind source reader agreed with all four corrected 350 glyphs and produced the same message for 351. Claude supplied the initial pairing lead and disclosed that limit on independence; the recovered rings, stops and plaintext were the solver team’s work.

350 verdict ACCEPT: findings addressed by retaining a qualified physical interpretation, identifying SOSOL only as a probable indicator, marking the one-stop error explanation as conjecture, showing both copies’ garbles side by side, and stating content/working-key recovery clearly. Original hardware, exact preparation and rare labels remain open.

351 verdict REVISE: source positions 11/12 and 231 corrected, 86 R/P and 73 O/U explained, inserted T/dropped E alignment stated, March arrival/November portal-date conflict recorded, and model attribution clarified. The numerical key is unchanged. The reviewer expressly required no second round for these revisions. Full item-by-item responses are in each SOLUTION.md.

Additional solver-team checks after DONE1, not rerun by Claude: two fresh clean paired 385-letter controls recovered exact texts and both masks among the predeclared 6/7-gram objective winners using ciphertext-only stages. One control succeeds under 7-grams, the other under 6-grams; a universally selected automatic winner remains unvalidated. The earlier controls supplied output-ring information and are distinguished from these tests.

## Sources, attribution and outcome

Original rendered portal record: https://crypto.hcportal.eu/dashboard/cryptograms/350. Original images and metadata are immutable in source/; SOURCES.md records all acquisition and research. Solved 391/392/394 and later linked Madrid 373 were disclosed context, not a source of this pair’s plaintext.

Geometry source: Callimahos, Military Cryptanalytics Part III (1977), §52, pp.184–185, https://www.governmentattic.org/41docs/NSAmilitaryCryptalyticsPt3_1977.pdf. Slovak cipher context: Antal/Grošek/Zajac, Vojenská história 24(3), 2020, pp.95–108. German SSA NR2417 does not establish SOSOL or Slovak preparation rules.

Earlier GPT-6 Astra attempts were unresolved. GPT-6.1 Sol subagents recovered the cycle, working key and language, and performed audits; main OpenAI GPT integrated the recovery and selected rare-label semantics. Claude Opus 5.5 supplied the pairing lead and independent review. Content recovered; working key recovered; exact historical procedure open. No register entry is produced for the remaining partial historical claim.

## Original telegram: archival scan 1 of 2

Complete original image as downloaded from the HC Portal. The archive watermark and annotations are retained. This is the source used for the manual transcription, not a reconstructed image.

HC350, source/cryptogram-1.jpg. Provenance: https://crypto.hcportal.eu/dashboard/cryptograms/350; acquisition details in SOURCES.md.

![HC350 original archival scan 1](../source/cryptogram-1.jpg)

## Original telegram: archival scan 2 of 2

Complete original image as downloaded from the HC Portal. The archive watermark and annotations are retained. This is the source used for the manual transcription, not a reconstructed image.

HC350, source/cryptogram-2.jpg. Provenance: https://crypto.hcportal.eu/dashboard/cryptograms/350; acquisition details in SOURCES.md.

![HC350 original archival scan 2](../source/cryptogram-2.jpg)

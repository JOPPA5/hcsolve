# HC351 car-purchase telegram - unreviewed draft

HC351: car-purchase telegram

WORKING DRAFT - not yet reviewed by Claude. Proposed content decipherment, incomplete historical preparation. No register entry. 11 October 2026.

Origin and claim

MZV message No.3002/1944, Cieker to MZV Bratislava, Slovak National Archive, MZV box 42. Portal status Not solved; its Unsolvable label is not treated as a mathematical result. Portal date 3 November 1944 is disputed by arrival stamp 2.III.44-23; exact dispatch date is not established.

We recover a coherent car-purchase/loan message and a full physical 23-stop adjustable Kryha key. Every 385 character position of the declared manual source transcription decodes and re-encrypts exactly. The first 5 source letters SOSOL remain unexplained. Exact historical I/J preparation and rare input-letter labels are not established. This report keeps literal output separate from an editorial reconstruction.

Method and validation

The human-supplied Claude batch review identified the decisive 350[i] to 351[i+1] relationship of period 23. The solver team then independently recovered the common output cycle by finite-field/CRT error-tolerant analysis, solved ordered two-mask wheel constraints, and ranked input-ring/physical-mask candidates by generic Slovak n-grams. The reviewer cycle and a target plaintext were not seeded into recovery.

The final fixed-input-ring pass exhausts 1,084,757 physically admissible paths; input neighbors are then tested. Fresh 385-letter TEST controls recover both full texts conditional on supplied output ring O and displacement-difference ΔK. These are language/physical-stage controls, not end-to-end ciphertext-only complete-key recovery. Independent adjacent-hole decoding and a separate encoder audit reproduce every source position for both target keys. Exact re-encryption establishes consistency, not every glyph or historical rule.

Physical key

Input letters at coordinates 0-25: JERGZMPADHLQTVNYFSBUICXKOW. Output letters at coordinates 0-25: AKXRMDTGJWNHVIPULYESZQBFOC. Initial stop 47, displacement 0. One ordinary press per character, clockwise adjacent-hole walk.

Selected stops (zero-based, 23 of 52): 47, 48, 49, 51, 2, 4, 5, 8, 11, 13, 17, 20, 21, 24, 26, 29, 31, 34, 37, 40, 42, 44, 45. All 23 arcs traverse the 52 holes once and sum 179 units.

Adjacent physical distances, indices 0-51: 4, 3, 4, 3, 3, 3, 4, 3, 4, 4, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 3, 4, 3, 3, 4, 3, 3, 4, 4, 4, 3, 3, 4, 3, 3, 3, 4, 3, 4, 3, 3, 4, 5, 3, 3, 3, 3, 4, 3, 3, 4, 5.

For cipher letter c at displacement D, output P[(O(c)-D)mod 26]; then advance D by the next selected-stop arc. Key JSON stores P as coordinate-to-letter indices and O as letter-to-coordinate indices, the inverse of the printed output ring. The two messages differ by selected hole 0 in 350 replaced with 48 in 351.

The printed input ring explicitly applies semantic relabeling old G→X, old Q→G, old X→J, unused old J→Q to the blind 6-gram key. EXISTUIE and TELEGRAFUI support this interpretation; the frozen model does not uniquely settle the rare labels. It is not proof of historical sentence J or I/J merging. We do not import German commercial J/extra-press rules.

Reproduce

python3 ciphers/hcp-351/work/kryha-decipherment/decrypt.py

Run from repository root with Python 3 standard library. Original source-image SHA256 values and manual transcription hashes are checked before decoding. No supplied source transcription exists: this is source-bound manual reading, not OCR. Default collated contains strong 351240 U→J correction; --variant strong preserves the older snapshot. --variant collated-moderate adds uncertain 351231 L→I. Older --variant moderate preserves disputed stamp alternatives and is not the preferred glyph reading. For 350 variants are identical. No language cleanup is performed.

Literal prepared plaintext: all 385 characters

UITLFZMNOHZJHMOZNOSTTIKUPITAUTONAILACNEISIAIEZAPATDESATPATTISICPTSJAUTASUVELMIDRAHEJPSED
AVAIUCIAUTACAKAODPOVEDTRIDNIJPOPROSPANAPREDSEDUOPOZICKUVUVEDENOMOBNOSEPRETOZETUNEMOZEMVZ
IATNASEBATAKUDLZOBUAAUTOZOSLUZOBNYCHDOVODOVIENUTNEJEXIITUIELACNEISIAKUPAVOFRANCIIZAFRANK
YLACNOKUPENEVMADRIDEJNATUTOMOZNOSTVSAKMOZNOPRISTUPITPOVASOMODOBRENIJMIKUSNECHDAVYSVETLEN
IEJTELEGRAFUIROZHODNUTIDOTROCHDNI

Readable Slovak reconstruction: editorial

[First five source characters unexplained.] Z mnohých možností kúpiť auto najlacnejšia je za päťdesiatpäť tisíc pts. Autá sú veľmi drahé. Predávajúci auta čaká odpoveď tri dni. Popros pána predsedu o pôžičku v uvedenom obnose, pretože tu nemôžem vziať na seba takú dlžobu a auto zo služobných dôvodov je nutné. Existuje lacnejšia kúpa vo Francii za franky lacno kúpené v Madride. Na túto možnosť však možno pristúpiť po Vašom odobrení. Mikuš nech dá vysvetlenie. Telegrafuj rozhodnutie do troch dní.

English translation of the reconstruction

[First five source characters unexplained.] Among the many possibilities for buying a car, the cheapest is for fifty-five thousand pesetas. Cars are very expensive. The seller of the car is waiting three days for an answer. Ask the chairman for a loan in the stated amount, because I cannot take on such a debt here, and a car is necessary for official duties. A cheaper purchase is possible in France using francs bought cheaply in Madrid. This possibility can, however, be pursued after your approval. Let Mikuš provide an explanation. Telegraph the decision within three days.

Remaining uncertainty

Unknown prefix raw UITLF. Both source prefixes are clear SOSOL; alternative pressing/reset hypotheses do not select a unique plaintext. Sentence boundary J and internal I/J interpretation are lexical hypotheses. PATDESATPAT is edited to päťdesiatpäť by adding I; spaces, accents and local error repairs are not exact machine output.350 DRAAE/POPROT/PRISTUPIK remain literal errors; 351 has damaged MNOHZJH, doubled T, PSEDAVAIUCI, missing final E and an ambiguous 231 glyph. The source-supported 240 J correction fixes LACNEISIA without refitting the key. No printed letter is changed only to force prose.

The default aligned interior still has five discrepancies between copies; the separate 231 I alternative leaves four. Differences may reflect source, transmission, preparation or genuine textual changes; their causes are not proved. The old 20-letter prefix/10-letter suffix framing conjecture is withdrawn: most of the opening and DOTROCHDNI ending are plaintext. Input-alphabet uniqueness is not claimed.

Sources and review

Portal https://crypto.hcportal.eu/dashboard/cryptograms/351; all rendered tabs and immutable images are attributed in the cipher SOURCES.md. No published 350/351 plaintext was used. Solved 391/392/394 were separately read as attributed context for other telegrams. The car text is recovered here, not imported from those records.

Machine geometry: Callimahos, Military Cryptanalytics Part III(1977),§52, pp 184-185, public primarycopy https://www.governmentattic.org/41docs/NSAmilitaryCryptalyticsPt3_1977.pdf. Slovak contextual evidence: Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During WW2, HistoCrypt 2020, pp 25-26. SSA NR2417 German procedures do not establish this traffic’s SOSOL or I/J preparation.

Solver: main OpenAI GPT with GPT-6.1 Sol subagents; earlier GPT-6 Astra attempts retained as provenance. Independent provider reviewer Claude is pending after DONE1; this draft does not claim its acceptance. Final report must include the actual verdict and each response before FINAL. No register entry for this partial claim.

# Solver log — OpenAI GPT-6 Astra
## 2026-10-11
Read README in full for resumed assignment. Parent solver captured all three tabs and full original scan; source immutable. Portal Not solved; skip.txt empty of numbers. No markers existed.

Manual transcription in work/transcription.txt: 100 letters plus numeric prefix 3100. A cropped working copy is work/crop.jpg. Uncertain faint letters include row1 vceps (damaged interior glyphs), tcvst (middle glyph), row2 olkdo, adasz, imdns, row3 cbpwy, aitte, yvxao and imsii. The final line has six groups; line1 seven and line2 seven. No portal transcription supplied. The numeral prefix was excluded from letter analysis; its role is unknown.

IC 0.057373737373737375 is consistent with a transposition preserving natural-language frequencies, not sufficient to identify a system. Metadata title "Nariadenie previesť úpravu podľa 80216 a odobrať pas" gives possible subject matter, not a known plaintext.

Downloaded public UD Slovak SNK train corpus and formed 42,544 types of four-letter ngrams after removing diacritics, whitespace and punctuation. train.py reads only # text fields and counts within sentences; scores are log raw counts, unseen fourgrams score -4.0. Common total-normalization terms would be constant across equal-length candidates.

attack.cpp implements irregular single-columnar decryption: first n%w plaintext columns have one extra letter; key is ciphertext readout order of plaintext column indices. Seed 393, widths 2–30, 30 random restarts per width, 20,000 mutations each, swap and segment reversal moves with annealed acceptance. Ran both original ciphertext order and reversed ciphertext. This is heuristic, not exhaustive outside tiny widths. See results.txt and results-reverse.txt. No output is coherent Slovak. Higher widths produce more language-looking fragments through optimization; these are not a solution.

Known limitations: short text, ambiguous glyphs, corpus modern rather than diplomatic 1944 Slovak, only single-columnar family searched. Multiple transposition and indicators are not attacked. Parent communicated a historical source suggesting triple-columnar R/XQ systems, but I have not independently read or verified that source and make no identification on that basis.

Watcher started through bash non-login. No DONE/FINAL because no plaintext or key is recovered.

## Exact finite route-transposition enumeration — OpenAI GPT (main solver)
`python3 ciphers/hcp-393/work/routes.py` enumerates row/column, alternating row/column, diagonals and clockwise spiral routes, their reflections/reversals, widths2–30, and all pairs of fill/read routes. Partial final rows retain only actual occupied cells. Permutation duplicates are removed per body. An independently generated100-letter snake-fill/spiral-read control recovers its entire plaintext as the highest-scoring candidate among29406 cases. The target full100 plus each possible5-letter indicator omission gives637006 distinct cases; none yields a coherent whole-message reading. This exhausts this finite geometric route set, not arbitrary keyed columnar permutations or multiple transpositions. Source/transcription unchanged; no solution imported or marker warranted. Full results/control and planted strings are preserved in work/routes-*.json.

## 2026-10-11: exact width-ten double-square structure, controlled rank test

Read README in full, checked marker state, inspected original scan, and kept source/transcription unchanged. Under the user's override no watcher or reviewer was started. Full body is exactly 100 letters, making two complete width-ten columnar transpositions equivalent to independently permuted rows/columns.

New exhaustive algorithm in `work/square10/`: all 10! column orders scored with cross-row precomputed 3/4/5-gram tuples; retain 64, then enumerate all 10! row orders for each, reranking best 2,000 with frozen full-text lexical/POS score. Separate longer 6–9-gram TRAIN-only boundary model and wider 50,000 frontier also tested. This differs structurally from the width-20 SA search; no repeated identical annealing was used.

Two authored 100-letter diplomatic controls, different planted key pairs: exact full plaintext and both keys recovered at rank 0 in both base and phrase models. Two genuine held-out UD TEST controls: exact column keys, failed row keys. The complete real Slovak sentence is absent from TRAIN; no control text was injected into frozen training. Independent inverse permutation verifies exact reencryption of every saved top-100 candidate.

Concrete ambiguity: with true columns, 22,462 row orders score higher than truth, with four ties within 0.001. Wider full-text lexical reranking puts the true sentence at rank 1,440 rather than first. True combined score -1525.53 is lower than the incoherent best alternative -1480.26. Thus rank bias persists after exact search. Longer TRAIN-only phrase boundaries likewise fail this control.

Actual full-100 width-ten base/phrase/wider bounded scouts give no coherent message. These are weak negatives and do not exclude the family. Uncertain letters and unknown numeric prefix `3100` remain open. Detailed parameters, keys, reproduction and limitations: `work/square10/README.md`, `controls.json`, `validation.json`, exhaustive rank and score logs. No solution marker or register entry.

The final structural extension covers an odd number of equal-width-ten passes: transpose the literal 10 × 10 input, then recover independent row/column permutations. A separately generated control encrypted by three ordinary columnar keys recovers exact plaintext and reduced keys at rank 0, with independent exact reencryption through all three original keys. The actual transposed full-100 wider scout remains incoherent. This is a bounded odd-pass/triple structural test, not a complete exclusion because columns are pruned and genuine held-out row ranking fails. `work/square10/validation.json` includes this positive control and both orientations of the actual target.


## Controlled Myszkowski scout — main solver, 2026-10-11

A new repeated-rank transposition model was checked against the primary ACA example and two genuinely held-out Slovak controls:100-position width8 and85-position width7 with two erasures, both exact at rank0. All ordered rank assignments at widths2–8 and independent dictionary patterns at widths9–22 were searched (2,242,481 evaluations per case). Completed current cases for this cipher: 2. Whole best candidates are incoherent; independent re-encryption verifies each implemented key/model but does not prove language. Full keys and top100 texts are saved in batches/myszkowski/target-summary.json and result files. No cipher identification or family exclusion is claimed; wider patterns are incomplete, finite controls are not universal guarantees.363 uses separately labeled literal erasures and conditional4→A/8→B/?→X or A readings, never source changes. Additional explicitly labeled group-removal and C/O cases are still running; consult the batch summary for current scope.

## Completed Myszkowski extended scout
Main solver completed206 total cases across10 ciphers, with all retained20,600 whole candidates independently re-encrypting exactly (`batches/myszkowski/verify-targets.py`). No coherent winning whole plaintext emerged. All single-group omissions for396/345/393/367/374 and396 C/O, both orders, were explicit conditional branches;363 literal erasures and A/B-X/A guesses remain separate. Exhaustive widths2–8 plus frozen dictionary patterns9–22, two fresh exact controls, limits and case counts are in `batches/myszkowski/REPORT.md`. Negative heuristic/wider-dictionary results do not exclude a historical family. No source changes or marker.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

## Generic autokey exploratory scout
Main independently verified primaryCrypToolplaintextautokey example, then tested6algebras(plaintext/ciphertextfeedback ×Vigenere/Beaufort/variant), primers1–12, wholebodyforward/reverse(396C/Oexplicit). Twelvefresh55/115controls: all55exact,115plaintextfeedbackexact,115cipherfeedback110/115with5prefixerrors; tailagreementisstructural, no primerrecovery. Targetwinningwholetexts remainincoherent; all1,008retained key/text pairs across14scouts independentlyreencryptexact. Fixedmodels/controls/repro/sourceboundaries: `batches/autokey/REPORT.md`. No historicalautokeyidentification, no familyexclusion, no guessedtitleplaintext or sourcechange/marker.

## Periodic polyalphabetic scout — GPT6.1Sol
48genuine heldout controls acrossSK/DE/CS,55/85/100/115letters,3/9/15/12periods andVigenere/Beaufort/variantBeaufort/Porta allrecoverentireplaintext at rank0 atplantedperiod. PrimaryPortaKEY/GEHEIMNISvector and12,800incrementalscorechecks pass.714actualmodelruns cover238literal/reverse/conditionalgroupomission cases across369/345/396C-O/393/367/374, periods1–16, phase-preserving erasures367. All182,784targetcandidate rows independentlyreencryptexact; leading wholetexts incoherent. Lower-budget conditional omissions andfinite controls give no universal recovery/exclusion. Completefullkeys/texts, languageprovenance, modelcontrols/repro: `batches/periodic-sol61/README.md`. Sourceunchanged/no marker.

### Column-fragment beam, completed rectangular scouts (2026-10-11)

Main solver independently developed a beam that orders whole ciphertext column fragments and scores newly closed n-grams across all rows. Five of seven genuinely heldout short controls and a fresh400-character control recover their complete plaintext at rank0;95/115-short-row and two-erasure controls fail. The batch covers1262 rectangular literal/reverse/explicit conditional cases across ten ciphers, retaining97696 full candidate keys with exact independent re-encryption; no coherent whole plaintext identified. See batches/columnar-stratified/README.md, beam-targets.py and beam-summary.json. This one-stage scout does not exclude tripleR, other widths or other cipher families. No published target answer used.

### One-long-column fragment beam (2026-10-11)

Main solver tested a distinct n mod width=1 transposition beam: enumerate the one long ciphertext chunk, place it in plaintextcolumn0, then order all equal-heightshortcolumns. Fresh heldout85/100/115 and400-letter controls recover full text at globalrank0;55/65 and two-erasure controls fail. Across94 whole/reverse/explicit omitted-group scouts,91200 full candidate keys independently re-encrypt exactly. No coherent targetwholetext. Method, all controls/keys and widths in batches/columnar-stratified/README.md and one-long-targets.py. Short or damagedtargetfailures provide no exclusion.

### Alternating readout directions, keyedcolumnar (2026-10-11)

GPT6.1Sol tested a distinct conditional keyedcolumnar geometry: readout-rankedcolumns alternate down/up, both initialdirections, ratherthan arbitrarycolumnreversals. Frozenbeamnormalizesciphertextchunks bydirection; rectangularandn modwidth1 cases. Twelvefreshundamagedcontrols9wholeexact; both400characterfive-erasurecontrols exactmaskedplaintext.160 literalwhole forward/reverse targetcases across363/393/345/396/369, widths2–26applicableonly, finishedwithoutcoherentwholeplaintext. Fullkeysincludepermutation,directions,widthandstreamorder, independentlyencodeandinvert. Noindicatoromissions/glyphcorrections. No historicalattribution orfamilyexclusion. Fullbatch batches/columnar-serpentine-sol61/README.md andNOTES.md.

### Repeated-keyword Myszkowski dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN keyword rank patterns with repeated ranks, reading tied columns by rows. Four fresh genuine55/65/115/400controls recover full plaintext as language rank0; dictionarycoverage, not unrestrictedkeyrecovery. Whole literal forward/reverse body scouts give incoherent texts. Numeric administrative header excluded wherepresent; other marks are phase-preserving erasures, no group omission. All retained complete key/text candidates independently encode/invert/rescore; full batch480rows. Conditionaldictionary failure excludes no otherkey/preparation/transposition. PrimaryPDFworked-example discrepancies are disclosed. Full evidence/reproduction: batches/myszkowski-main/REPORT.md and verification.json. No recoveredsolution or marker.

### AMSCO single/double-cell transposition dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN repeated-keyword candidates, each resolved to unique numeric order, under four declared cell parities (continuous/alternating-row starts, beginning1/2). All four fresh genuine55/65/115/400controls recover whole plaintext at language rank0. Actual whole literal forward/reverse scouts remain incoherent. Administrative numeric header excluded wherepresent, no group omission, marks retainpositions as erasures. Independent fullbatch480position bijections/encodings/inverses and frozen scores agree. This is finite dictionarycoverage, not unrestrictednumeric-key recovery or historicalfamily exclusion. Full evidence: batches/amsco-main/REPORT.md and verification.json. No solvedtext/marker.

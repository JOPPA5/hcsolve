#363 analysis — GPT-6 Astra

2026-10-11. Parent captured source and all portal tabs. No source modification, browser or watcher. Explicit useroverride:external reviewer managed by parent. No markers.

## Source structure and damage
Manual tentative raw transcription in work/transcription-raw.txt:80groups of5symbols=400, matching printed13400suffix. Handwritten upper-right395could reflect400minus5indicator; this is inference, not established. Group3SGTYRis visibly struck through; unclear whether cancellation applies to cipherbody. Group25JUZWVcontains the onlyW, a possible indicator alternative. Neither was declared the actual indicator.

Preserved literal4inP4AV4and4ATXS,8inV8LME; obscuredlastglyph ofUIDA?is explicitly unresolved. Several other faint I/L/V/U readings remain tentative. work/prepare.py creates labeled HYPOTHESIS variants4→A,8→B,?→X orA; these are not silently corrected originals. They haveIC0.0577068and0.0582957. Lower notice appears to state a correction involving Bobula and the Bratislava routing, not a supplied decryption. 'Correction en meilleure suivra' line and the archival Unsolvable tag do not prove what body symbols were damaged or that decryption is impossible.

## Attacks and calibration
Single irregular columnar transposition widths2–22,10restarts/10000proposals per width, tested400symbolX/Avariants and395symbolvariants dropping group3or25. No coherent plaintext. Uses393Slovak fourgram scores.

Positive controls:395letter explicitly synthetic Slovak text encrypted with known permutations at16,19,22, plus a triple16/19/22cascade, seed363, recorded work/controls.json. Independently implemented inverse recovers all known-key controls (work/validate_controls.py and control-validation.txt). Search recovered single16exactly but did NOT recover single19,single22or triple exactly. This establishes a search limitation, not invalid cipher inversion.

Modified search adds contiguous block relocation beside swap/reverse,20restarts/20000proposals, widths16–22. Retested19/22controls and group3/25target omissions. It improved language fragments/scores but STILL FAILED exact19/22control recovery; target remains incoherent. No exclusions of19/22singlecolumnar or triple justified by this search. No ciphertext alterations made to produce candidate phrases.

## Reproduction and limits
`sh ciphers/hcp-363/work/reproduce.sh` reconstructs hypotheses and reruns search/controls; this does NOT decrypt the image. Saved logs include original and improved results, controlsummary and independent inversion validation. Files omit-3.txt and omit-25.txt are stored derived inputs from the raw transcript with the stated substitutions.

Remaining blockers:uncertain raw characters/cancellations; indicator identity; cipherfamily and dailykeys. Transposition is plausible from frequency but unproved. The400letter length is above the historical recommended250letterR limit, adding caution. All encrypted content remains unresolved. No published solution consulted, no plaintext/key, no registerentry/DONE/FINAL.

## Segmentation-aware follow-up — GPT-6.1 Sol,2026-10-11

Read source and original scan; markers absent. No watcher/reviewer started under explicit parent/useroverride; original source immutable. Newfiles only in363. Existing search/control logs preserved.

The failing ordinary-columnar attack couples physical order and ciphertext segmentation. Long/short swaps move many subsequent chunk boundaries. New work/segmented/ search enumerates length patterns independently and mutates order only within same-length physical classes.395 modulo19=15 gives3,876 possible patterns;395 modulo22=21 gives only22. Precomputed bigram row-adjacency and wrap scores screen all patterns, followed by frozen Slovak3/4/5gram refinement of strongest40. Model from batches/scoring-sol61 read-only; bigrams from primary read-only393 UD training, not controls.

First separated search still failed controls. Adding within-class contiguous-block moves and hotter annealing (appropriate for395letters) recovers both full395-letter controls EXACTLY, including planted width19/22 keys. Independent Python inverse and re-encryption pass; see control-v3-validation.json. search-v4 avoids immutable chunk copying without changing RNG/score/search semantics; complete results equalv3 on both controls. No plaintext/key crib supplied to optimizer. Earlier failures remain valid records, superseded for these two cases only, not erased.

Applying unchanged search to400 X/A and395 omittinggroup3/group25 X/A, widths16–22. Explicit raw replacements4→A,8→B,?→X/A and cancellation hypotheses preserved; source image does not resolve them. Target results/checkpoints live only in work/segmented/. No cipher-family identification or target plaintext claim follows merely from successful controls. Algorithm limits and reproduction in that directory README.

### Separate square double-transposition structure

400=20×20 permits a distinct algebraic case: two ordinary full width20 transpositions reduce to row/column permutations of the square matrix. This does not assume R, and does not apply to395 omissions. work/square-double/ creates two random planted keypairs on400 synthetic letters (earlier395text continued5letters, never trained). Frozen within-row multigrams recover the EXACT first key for both. Exact Hamiltonian row ordering under boundary grams fails second-key/fulltext; adding frozen lexical/POS joins still fails. Whole-objective diagnostic actually favors wrong ordering (-6053.05) over truth (-6086.09), exposing a semantic/scoring limitation. Neither partially readable control nor re-encryption alone is a decipherment. Files preserve both failures and exact first-key successes.

A bounded scout of two literal400 X/A readings uses this successfully calibrated first stage to look for readable row fragments; full-controls failure prevents any negative double-family exclusion. Saved keys/fragments/candidates are hypotheses only. No identical restart expansion of the completed single-columnar batch. Source remains unchanged; no DONE.

### Completed target batch

All42 planned single-columnar cases are finished: six explicit400/395X/A/omission readings × widths16,17,18,19,20,21,22. target-summary.json retains every whole candidate and hypothesized key; audit-targets.py independently checks permutation, full coverage and exact re-encryption to each derived input. All pass that mechanical check, but ALL are semantically incoherent. Highest model ranks do not justify positive plaintext or cipher identification. completion.json records bounded coverage; no additional identical restart expansion is made.

The two400-letter square-double scouts are also finished, with hypothesized first/second keys and20row fragments preserved. Neither has intelligible full row fragments/message. The underlying full-controls failure at row ordering means these negative scouts do NOT exclude double transposition. They are retained as unaccepted hypotheses, not solutions.

Markers re-scanned after completed runs: none. Source image and metadata not edited; new source SHA256 snapshot in work/segmented/source-hashes.json. Status remains unresolved, no DONE/FINAL/register entry. Substantive progress is exact395-letter width19/22 recovery and identification of a distinct double-square row-order scoring limitation. Other transposition families and source ambiguities remain open.


## Controlled Myszkowski scout — main solver, 2026-10-11

A new repeated-rank transposition model was checked against the primary ACA example and two genuinely held-out Slovak controls:100-position width8 and85-position width7 with two erasures, both exact at rank0. All ordered rank assignments at widths2–8 and independent dictionary patterns at widths9–22 were searched (2,242,481 evaluations per case). Completed current cases for this cipher: 6. Whole best candidates are incoherent; independent re-encryption verifies each implemented key/model but does not prove language. Full keys and top100 texts are saved in batches/myszkowski/target-summary.json and result files. No cipher identification or family exclusion is claimed; wider patterns are incomplete, finite controls are not universal guarantees.363 uses separately labeled literal erasures and conditional4→A/8→B/?→X or A readings, never source changes. Additional explicitly labeled group-removal and C/O cases are still running; consult the batch summary for current scope.

## Completed Myszkowski extended scout
Main solver completed206 total cases across10 ciphers, with all retained20,600 whole candidates independently re-encrypting exactly (`batches/myszkowski/verify-targets.py`). No coherent winning whole plaintext emerged. All single-group omissions for396/345/393/367/374 and396 C/O, both orders, were explicit conditional branches;363 literal erasures and A/B-X/A guesses remain separate. Exhaustive widths2–8 plus frozen dictionary patterns9–22, two fresh exact controls, limits and case counts are in `batches/myszkowski/REPORT.md`. Negative heuristic/wider-dictionary results do not exclude a historical family. No source changes or marker.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

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

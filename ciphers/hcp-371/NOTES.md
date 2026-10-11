# Notes — hcp-371

## 2026-10-11 — GPT-6.1 Sol resumed captured source

Read README in full. Parent supplied three-tab metadata and scan. No existing work files/attempts or markers were present. User override: no watchers; parent manages review/finalization. Source remains unchanged.

Viewed the actual 1024×768 scan before transcription. The printed grouping is not regular five-letter grouping. Literal transcription preserves all visible groups; 203 alphabetic body characters. The header `4207` does not justify silently adding four characters. Earlier suggestion of 202 letters/five missing letters was not confirmed.

Statistics: IoC 0.0585280203, vowels AEIOUY 0.4236453. Distribution compatible with Slovak plaintext letter counts and hence transposition, but not diagnostic.

Implemented seeded columnar-transposition simulated annealing (`attack.cpp`, derived from the shared 393 script; own seed 371). Widths 2–24, 12 restarts ×20,000 mutations, swap and segment-reversal key mutations. Quadgram model copied from 393's Slovak SNK training. Best forward result 29.1466 at width24 is incoherent; do not interpret isolated words as a solution.

Positive control: independently written Slovak diplomatic prose, normalized to 203 letters and encrypted with width11, column order [7,2,9,0,5,10,1,8,4,6,3]. The identical attack recovered the complete exact plaintext and key, score556.927. This validates this ordinary columnar implementation at one tested width and length, not every width or other transposition families.

Also tested reversal of the complete ciphertext with the same width range and budget (results-reverse.txt). Preserve this as a bounded negative result, not a rejection of transposition generally. No ciphertext holes, permutation key, plaintext or translation established.

Next useful work: investigate the exact period-specific Slovak diplomatic cipher system or double transposition with controls, and clarify header/group conventions from comparable unencrypted telegrams. Do not assume OCR count discrepancy is ciphertext damage. No DONE marker: unresolved.


## Controlled Myszkowski scout — main solver, 2026-10-11

A new repeated-rank transposition model was checked against the primary ACA example and two genuinely held-out Slovak controls:100-position width8 and85-position width7 with two erasures, both exact at rank0. All ordered rank assignments at widths2–8 and independent dictionary patterns at widths9–22 were searched (2,242,481 evaluations per case). Completed current cases for this cipher: 2. Whole best candidates are incoherent; independent re-encryption verifies each implemented key/model but does not prove language. Full keys and top100 texts are saved in batches/myszkowski/target-summary.json and result files. No cipher identification or family exclusion is claimed; wider patterns are incomplete, finite controls are not universal guarantees.363 uses separately labeled literal erasures and conditional4→A/8→B/?→X or A readings, never source changes. Additional explicitly labeled group-removal and C/O cases are still running; consult the batch summary for current scope.

## Completed Myszkowski extended scout
Main solver completed206 total cases across10 ciphers, with all retained20,600 whole candidates independently re-encrypting exactly (`batches/myszkowski/verify-targets.py`). No coherent winning whole plaintext emerged. All single-group omissions for396/345/393/367/374 and396 C/O, both orders, were explicit conditional branches;363 literal erasures and A/B-X/A guesses remain separate. Exhaustive widths2–8 plus frozen dictionary patterns9–22, two fresh exact controls, limits and case counts are in `batches/myszkowski/REPORT.md`. Negative heuristic/wider-dictionary results do not exclude a historical family. No source changes or marker.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

## Generic autokey exploratory scout
Main independently verified primaryCrypToolplaintextautokey example, then tested6algebras(plaintext/ciphertextfeedback ×Vigenere/Beaufort/variant), primers1–12, wholebodyforward/reverse(396C/Oexplicit). Twelvefresh55/115controls: all55exact,115plaintextfeedbackexact,115cipherfeedback110/115with5prefixerrors; tailagreementisstructural, no primerrecovery. Targetwinningwholetexts remainincoherent; all1,008retained key/text pairs across14scouts independentlyreencryptexact. Fixedmodels/controls/repro/sourceboundaries: `batches/autokey/REPORT.md`. No historicalautokeyidentification, no familyexclusion, no guessedtitleplaintext or sourcechange/marker.

### Column-fragment beam, completed rectangular scouts (2026-10-11)

Main solver independently developed a beam that orders whole ciphertext column fragments and scores newly closed n-grams across all rows. Five of seven genuinely heldout short controls and a fresh400-character control recover their complete plaintext at rank0;95/115-short-row and two-erasure controls fail. The batch covers1262 rectangular literal/reverse/explicit conditional cases across ten ciphers, retaining97696 full candidate keys with exact independent re-encryption; no coherent whole plaintext identified. See batches/columnar-stratified/README.md, beam-targets.py and beam-summary.json. This one-stage scout does not exclude tripleR, other widths or other cipher families. No published target answer used.

### Repeated-keyword Myszkowski dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN keyword rank patterns with repeated ranks, reading tied columns by rows. Four fresh genuine55/65/115/400controls recover full plaintext as language rank0; dictionarycoverage, not unrestrictedkeyrecovery. Whole literal forward/reverse body scouts give incoherent texts. Numeric administrative header excluded wherepresent; other marks are phase-preserving erasures, no group omission. All retained complete key/text candidates independently encode/invert/rescore; full batch480rows. Conditionaldictionary failure excludes no otherkey/preparation/transposition. PrimaryPDFworked-example discrepancies are disclosed. Full evidence/reproduction: batches/myszkowski-main/REPORT.md and verification.json. No recoveredsolution or marker.

### AMSCO single/double-cell transposition dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN repeated-keyword candidates, each resolved to unique numeric order, under four declared cell parities (continuous/alternating-row starts, beginning1/2). All four fresh genuine55/65/115/400controls recover whole plaintext at language rank0. Actual whole literal forward/reverse scouts remain incoherent. Administrative numeric header excluded wherepresent, no group omission, marks retainpositions as erasures. Independent fullbatch480position bijections/encodings/inverses and frozen scores agree. This is finite dictionarycoverage, not unrestrictednumeric-key recovery or historicalfamily exclusion. Full evidence: batches/amsco-main/REPORT.md and verification.json. No solvedtext/marker.

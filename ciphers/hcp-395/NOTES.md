# Working notes — GPT-6 Astra

2026-10-11. Parent captured all portal tabs and original image. Portal Not solved. No solution attached. Watcher started.

Manual tentative transcription in work/transcription.txt; watermark and faint print make multiple letters uncertain. Source is unchanged. Numeric indicator 9285, 57 groups (285 letters). Clear cover note states requests to repeat telegrams80213 and80214 and says earlier texts were checked and resent unchanged because likely postal error. This is contextual plaintext, not established plaintext of this ciphertext.

## Reproducible initial attacks
Run `python3 ciphers/hcp-395/work/analyze.py` from repository root. Output saved in work/analysis.txt. Tentative transcription has285 letters and IC0.05737583395107487. Letter distribution is consistent with transposition but does not establish it.

Enumerated46232 single-columnar permutations at widths2–8, each forward/reversed; then9048 elementary routes at widths2–40, with no removal or removal of each possible five-letter indicator. Ranking uses an explicitly limited manually chosen Slovak word list, not a trained language model. Top candidates are not coherent Slovak. This does not exclude larger widths, double/triple transpositions, alternative routes, or transcription changes. Only top25 scores were stored.

## Context hypothesis and limitations
Historical paper cited in SOURCES.md describes R/XQ triple columnar transposition; three daily permutations, rotated per message, and an inserted five-letter indicator. No daily key or indicator mapping is known. It is a plausible hypothesis here, not established. Printed header provisionally read9285; could be R285. The image body is longer than the paper's stated R recommendation (250 letters), so direct classification needs care. Comparator396 is short and from the same date/recipient, but no shared key was recovered.

Transcription remains tentative: prominent uncertainty in line1(groups2–6), line2(groups3–7), line4(groups5–8), line6(groups3–8), line7(groups2–8), where the blue watermark overlaps faint type. No proposed plaintext justified changing ambiguous characters. Exact digit/header reading and all transcription must be checked before serious key search.

## 2026-10-11 — GPT-6.1 Sol segment and daily-indicator analysis

User override: no watcher is started in this continuation. Existing source remains immutable. Reviewed entire scan and saved a non-destructive cropped copy `work/body-inspection.jpg`. Body is one uninterrupted block:7lines of8groups and one finalgroupEDIVN, total57groups/285letters. No second numericheader, blankline, punctuation or visible segmentmarker appears. The ambiguous first character of9285may be9/R; no confident new headerreading claimed. Existing transcription remains tentative, particularly beneathwatermark; it was not silently corrected from attack output.

### Published length limits and controls

The primary2020paper distinguishes R50–250payload and XQ50–200payload, plus a5letter insertedindicator. Treating285cipherletters as twoRsegments implies275totalpayload and boundaries after groups11–46 (55–230cipherletters); XQrequires groups16–41. A250+35rawsplit violates the secondblock50payloadminimum. The normal mathematical triple-columnar transform still works on280/285letters, so a published manual length limit does not itself prove physical segmentation. Exactknownkey controls at lengths50,75,200,250,280,285 and a properly formed285letter two-block control (205+80cipherletters,200+75payload,2indicators) all roundtrip. `segment_constraints.py` reproduces these and all conditional indicator possibilities; JSON preserves outputs/keys. These are implementationcontrols, not blindtriplecryptanalytic recovery.

### New bounded segmented single-columnar attack

`split_columnar.cpp` tests each36Rcompatibleboundaries, bothsegments independently, widths2–7 allpermutations, reversed/normalinput, omission of eachgroupor noomission. Total25,114,176evaluations. This is new coverage of possible segmentation; it does not repeat the existing whole-body tests. TrainedSlovakquadgrams copiedfrom shared393model. An independently generated285letter two-segment single-columnar control (payload200+75, width7,key[3,6,1,4,0,5,2],5letterindicator atgroup5each) recovers BOTH completeexactplaintexts,keysandindicatorpositions. Targetsegments remain incoherent; best normalizedshortblock `ozjaatnlozvitvidaciuchnemapasimusierueokaamammrzlesnfutajulo` is not a decipherment. Scores acrosslengths must not be compared raw. Reproduce:
`c++ -O3 ciphers/hcp-395/work/split_columnar.cpp -o ciphers/hcp-395/work/split_columnar`
`ciphers/hcp-395/work/split_columnar ciphers/hcp-395/work/quadgrams.tsv ciphers/hcp-395/work/split-columnar-control.txt control`
`ciphers/hcp-395/work/split_columnar ciphers/hcp-395/work/quadgrams.tsv ciphers/hcp-395/work/transcription.txt`

### Concrete joint daily-indicator constraints

Assuming395and396use the SAME Rdaily re-encryptiontable andindicatorposition, the paper's fixedletter→digitmapping and atmost3homophonesperdigit can constrain bothindicatoralignments jointly, WITHOUT assumingheadernumbersarealignment. Script `joint_indicator_constraints.py` uses395tentativegroups and396's disclosedC/Oreadings; generated positive/negative mappingcontrols pass. It writes allpairs to`joint-indicator-constraints.json`.

Sharedpositions2,7,9,10,11 are impossible in BOTH396C/Oreadings under these assumptions. Position1permits only(n395,n396)=(1,22)or(12,22):395AVCMU/396VEPES. Thus allthreeRkeywidths wouldneed22 under same-numberalignment; n39622cannot supportprogressive n,n+1,n+2alignment atRmax22. Position4(395VCAEA) requiresn39519 and18possible396alignments. Position6(395NIUAS/396SZTRA) allows only5pairs:(7,19),(8,20),(11,20),(16,7),(20,11). Position5has36pairs,position3has212,position8has337. These are genuine conditional structural deductions, NOT recoveredtable/key/plaintext; transcriptionerrors or differentdailytable/indicatorpositions invalidate them. They can reduce joint395/396triplemodel hypotheses materially.

The covernote concerns retransmitted oldertexts; therefore it is NOT an exactcrib for thebody, and no publishedtargetplaintext was read. No supported decipherment orDONEmarker.


## Controlled Myszkowski scout — main solver, 2026-10-11

A new repeated-rank transposition model was checked against the primary ACA example and two genuinely held-out Slovak controls:100-position width8 and85-position width7 with two erasures, both exact at rank0. All ordered rank assignments at widths2–8 and independent dictionary patterns at widths9–22 were searched (2,242,481 evaluations per case). Completed current cases for this cipher: 2. Whole best candidates are incoherent; independent re-encryption verifies each implemented key/model but does not prove language. Full keys and top100 texts are saved in batches/myszkowski/target-summary.json and result files. No cipher identification or family exclusion is claimed; wider patterns are incomplete, finite controls are not universal guarantees.363 uses separately labeled literal erasures and conditional4→A/8→B/?→X or A readings, never source changes. Additional explicitly labeled group-removal and C/O cases are still running; consult the batch summary for current scope.

## Completed Myszkowski extended scout
Main solver completed206 total cases across10 ciphers, with all retained20,600 whole candidates independently re-encrypting exactly (`batches/myszkowski/verify-targets.py`). No coherent winning whole plaintext emerged. All single-group omissions for396/345/393/367/374 and396 C/O, both orders, were explicit conditional branches;363 literal erasures and A/B-X/A guesses remain separate. Exhaustive widths2–8 plus frozen dictionary patterns9–22, two fresh exact controls, limits and case counts are in `batches/myszkowski/REPORT.md`. Negative heuristic/wider-dictionary results do not exclude a historical family. No source changes or marker.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

### Column-fragment beam, completed rectangular scouts (2026-10-11)

Main solver independently developed a beam that orders whole ciphertext column fragments and scores newly closed n-grams across all rows. Five of seven genuinely heldout short controls and a fresh400-character control recover their complete plaintext at rank0;95/115-short-row and two-erasure controls fail. The batch covers1262 rectangular literal/reverse/explicit conditional cases across ten ciphers, retaining97696 full candidate keys with exact independent re-encryption; no coherent whole plaintext identified. See batches/columnar-stratified/README.md, beam-targets.py and beam-summary.json. This one-stage scout does not exclude tripleR, other widths or other cipher families. No published target answer used.

### Repeated-keyword Myszkowski dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN keyword rank patterns with repeated ranks, reading tied columns by rows. Four fresh genuine55/65/115/400controls recover full plaintext as language rank0; dictionarycoverage, not unrestrictedkeyrecovery. Whole literal forward/reverse body scouts give incoherent texts. Numeric administrative header excluded wherepresent; other marks are phase-preserving erasures, no group omission. All retained complete key/text candidates independently encode/invert/rescore; full batch480rows. Conditionaldictionary failure excludes no otherkey/preparation/transposition. PrimaryPDFworked-example discrepancies are disclosed. Full evidence/reproduction: batches/myszkowski-main/REPORT.md and verification.json. No recoveredsolution or marker.

### AMSCO single/double-cell transposition dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN repeated-keyword candidates, each resolved to unique numeric order, under four declared cell parities (continuous/alternating-row starts, beginning1/2). All four fresh genuine55/65/115/400controls recover whole plaintext at language rank0. Actual whole literal forward/reverse scouts remain incoherent. Administrative numeric header excluded wherepresent, no group omission, marks retainpositions as erasures. Independent fullbatch480position bijections/encodings/inverses and frozen scores agree. This is finite dictionarycoverage, not unrestrictednumeric-key recovery or historicalfamily exclusion. Full evidence: batches/amsco-main/REPORT.md and verification.json. No solvedtext/marker.


### Bounded original-80213 lookup

The main solver used the rendered public Cryptograms table (1875 total records) and Global Filter `80213`, 2026-10-11. It returned zero rows (Showing 1 of 0 Pages). No original 80213 document or plaintext was obtained; absence from this bounded table lookup is not proof of archival absence. Original 80214 is identified separately as Solved387 context for396, with ambiguity reported in `batches/repeat396-387-sol61`.


### Independent historical R fixture audit

The new source-led check `batches/r-primary-example-audit-sol61/REPORT.md` independently reproduces both full intermediate55-letter grids of Figure5 and validates the existing row-write/ascending-label core and physical alignment. Final indicator spelling and before/after group5 placement are not certified; the older tentative index4 assembly is not a primary known-answer vector. `placement-impact.json` finds the index4 synthetic segment control internally consistent, with no actual inspected target search requiring rerun solely for this boundary issue. Broad omission tests include both observed positions.

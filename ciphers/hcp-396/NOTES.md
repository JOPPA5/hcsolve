# Work log — HC Portal 396

## 2026-10-11 — source and transcription

Solver: OpenAI GPT-6 Astra. Parent agent captured the three live portal tabs and the displayed image. The portal status was Not solved; no attached transcription/solution was shown. I inspected the complete scan and a crop, manually transcribing its cipher body to `work/transcription.txt`. Source files were not edited.

Clear context on scan: “Viď záznam a telegram pod č.80229/44”, “Dr. Šulík”, “Ministro Slovacco SIDOR”, “Citta del Vaticano”, “Vaše 102”, “Mračna”, “80230”. Header reads `755`; interpreting it as day 7 plus length 55 is a hypothesis, not established.

Cipher groups:

`vepes nmono drtsi uzoip ujpta sztra cscnu dwjpm ciasi ujiui oormt`

There are 55 letters in 11 groups. Group 7 initial is best read C from the enlargement, with O retained as an uncertainty. The first group-2 letters are close-set typed `nm`. Crops were generated with `sips`; an earlier Pillow crop attempt failed because default Python has no PIL.

## Historical hypothesis

Antal, Zajac and Grošek's 2020 paper (see SOURCES.md) describes MZV cipher R/XQ as three columnar transpositions with daily keys. R keys have lengths 16–22. An inserted five-letter group encodes a rotation/alignment; its position and substitution table are also shared key material. The method admits 50-letter payloads. This is a plausible family for our 55-character text. `dwjpm` (group 8) contains the only W and is a candidate indicator; removing it leaves 50 letters. Neither the identification nor this indicator position is proved.

## Reproducible checks

Run `python3 ciphers/hcp-396/work/analyze.py` from the repository root. It writes `work/analysis.json`:

- Frequencies and IC for C/O readings, with/without candidate group 8.
- Exhaustive ordinary single-columnar decryption, widths 2–8, over those four scenarios: 184,928 keys in total.
- Unkeyed row/column routes, widths 2 to N−1, both forward and reversed input, for both C/O readings and every possible single-group omission (plus no omission): 2,324 routes.
- Ranking uses explicitly listed short Slovak substrings only. This is a weak heuristic; high scores are not decryptions. The highest-ranked candidates are incoherent.

These tests do not cover general triple transposition or prove the ciphertext unsolvable. Statistical profile is compatible with transposition but does not establish it. IC is 0.05253 (full C reading), 0.05714 (C reading without group 8), 0.05455 (full O reading), or 0.05959 (O without group 8).

The context title about repetition must not be promoted into a plaintext crib without verification. For instance, literal `opakujte` or `telegram` cannot occur in a pure transposition of these letters (K/L absent), though different wording is possible.

## Related material

Another solver transcribed same-day message 80229/44 at `ciphers/hcp-395/`, which this scan references. It is 285 letters; no shared recovered key or plaintext was obtained. Its existence is a useful lead, not evidence of a common permutation or recovered message.

## Current blocker and handover status

No coherent plaintext or key recovered. The three daily permutations, possible alignment table and indicator location remain unavailable. Further useful evidence would be the applicable daily R/XQ key sheet, or authenticated related plaintext/ciphertext pairs. No DONE marker, register entry, or final report was created: there is no completed solution to review.

## 2026-10-11 — GPT-6.1 Sol alternative transposition tests

Viewed the complete preserved scan independently. Continued existing work without rerunning completed single-columnar/route tests. Tested AMSCO alternating 1/2-letter cells, both starting phases, continuous versus row-alternating phases, complete ciphertext reversal, every width2–8 column permutation. Scenarios: C/O initial reading of group7, no omission or each of11possible group omissions. Total8,876,544 evaluations, with duplicate parameter-equivalent transformations retained transparently. `amsco_driver.py` produces input and result files. Exact50-letter independently written Slovak positive control encrypted at width7 with order[3,6,1,4,0,5,2], phase1,row-alternating cells recovered exact text/key; score124.522. The best target score23.104 is incoherent (`wjjvecnozasupmipendroztjciusnutsirapasimodiupostiu`) and retains W; no decipherment. Even group8 omission did not yield supported AMSCO plaintext.

Also exhaustively tested ordinary railfence zigzag for rails2..N−1, every cycle offset, normal/reversed rail order and normal/reversed complete input, over the same24scenarios:229,872evaluations. A generated Slovak control with7rails/offset3 roundtrips exactly. Best target score−8.29256 is incoherent; no key/message established. `railfence.py` reproduces and writes `railfence-results.json`.

Both alternatives are hypotheses, not documented R variants. Language scoring uses copied Slovak quadgrams from shared393model. Score comparisons across different lengths cannot identify omitted indicator position. Strongest point is absence of a coherent complete reading, not any absolute scoring cutoff. These negative results do not reject the historical triple-columnar hypothesis.

Reproduce new alternatives from repository root:
`c++ -O3 ciphers/hcp-396/work/amsco.cpp -o ciphers/hcp-396/work/amsco && python3 ciphers/hcp-396/work/amsco_driver.py && python3 ciphers/hcp-396/work/railfence.py`

### Triple-system control and preparation constraints

`triple.cpp` implements three ordinary irregular columnar stages. Generated50-letter control with widths16/18/20 and random seeded keys roundtrips with independent Python known-key inversion. Blind joint annealing100restarts×50,000mutations does NOT recover that control. It instead produces nonsense scoring146.619, above true-control124.522. This explicitly demonstrates short-text score overfitting; no target-negative conclusion is drawn from this unvalidated blind triple attack. `triple-control-key.json`, ciphertext and result preserve the failure.

Read the primary Antal/Zajac/Grošek2020 paper directly (pp22–23) again for preparation rules. Under its documented pure-transposition procedure: numbers are spelled digit by digit; short(<50) input is extended with KONIEC and padding; proper nouns/abbreviations use Q separators. This ciphertext has no K,L,G,Q,X anywhere. Therefore the title's “telegram80214/44” is incompatible with a literal plaintext mention of TELEGRAM or of80214 written with digit names (zero=NULA, four=STYRI, and eight=OSEM). Likewise mandatory KONIEC cannot occur, so a50-letter Rpayload would have to contain at least50letters before padding, or use a different preparation convention/transcription. The header755 is not proven alignment7. These are conditional constraints, not proof against R or instructions to replace absent letters.

The only V occurs in group1, and the only W in group8. Omitting group8 removesW but leaves just oneV; candidate phrase VASE STO DVA would need twoV and is excluded under pure transposition. “PROSIM ZNOVU” has compatible individual counts; it is merely an unverified possible phrase, not a recovered crib. No supported full plaintext obtained.

### Indicator equality constraints (novel bounded structural result)

`python3 ciphers/hcp-396/work/indicator_constraints.py` reproduces possible alignment numbers1–22 for each group under the paper's specified fixed letter-to-digit re-encryption table. Repeated ciphertext letters must imply equal digits; distinct letters may represent equal digits (homophony). The script checks this and maximum3letters per digit, with generated controls for every alignment1–22. Creading: groups2(nmono),7(cscnu),9(ciasi),10(ujiui) cannot be indicators for any1–22 alignment. Groups1(vepes) and11(oormt) permit only11or22. Groups3,4,5,6,8 have no such equality restriction. Under the alternative Oreading, group7(oscnu) is unrestricted. Alignment22 would require all relevant permutations to include22, so it would imply22-letter keys if the stated R16–22limit applies. This is conditional on the exact documented indicator algorithm and transcription, not a recovered key/table. Group8remains one structurally possible indicator, not uniquely established.


## Controlled Myszkowski scout — main solver, 2026-10-11

A new repeated-rank transposition model was checked against the primary ACA example and two genuinely held-out Slovak controls:100-position width8 and85-position width7 with two erasures, both exact at rank0. All ordered rank assignments at widths2–8 and independent dictionary patterns at widths9–22 were searched (2,242,481 evaluations per case). Completed current cases for this cipher: 24. Whole best candidates are incoherent; independent re-encryption verifies each implemented key/model but does not prove language. Full keys and top100 texts are saved in batches/myszkowski/target-summary.json and result files. No cipher identification or family exclusion is claimed; wider patterns are incomplete, finite controls are not universal guarantees.363 uses separately labeled literal erasures and conditional4→A/8→B/?→X or A readings, never source changes. Additional explicitly labeled group-removal and C/O cases are still running; consult the batch summary for current scope.

## Completed Myszkowski extended scout
Main solver completed206 total cases across10 ciphers, with all retained20,600 whole candidates independently re-encrypting exactly (`batches/myszkowski/verify-targets.py`). No coherent winning whole plaintext emerged. All single-group omissions for396/345/393/367/374 and396 C/O, both orders, were explicit conditional branches;363 literal erasures and A/B-X/A guesses remain separate. Exhaustive widths2–8 plus frozen dictionary patterns9–22, two fresh exact controls, limits and case counts are in `batches/myszkowski/REPORT.md`. Negative heuristic/wider-dictionary results do not exclude a historical family. No source changes or marker.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

## Revised controlled short MASC scout — GPT6.1Sol
Twelve genuine whole55/65letter TEST controls acrossSK/DE/CS26/28 were searched without truthseeding. German26both complete; revised generic perwindow TRAINfrequency anchorquotas recover Czech26both complete. Slovak controls fail (rare55true scores below false;65searchfailure); raw28calibration incomplete.60actual wholetext language/alphabet/order/readingscouts for345and396C/O yielded no coherent full candidate;7,680full raw key/text pairs independently reencrypt completely. Scores/fragmentary words are not plaintext. No familyexclusion; complete raw/folded evidence and reproduciblecommands: `batches/short-masc/README.md`. No source/markers.

## Generic autokey exploratory scout
Main independently verified primaryCrypToolplaintextautokey example, then tested6algebras(plaintext/ciphertextfeedback ×Vigenere/Beaufort/variant), primers1–12, wholebodyforward/reverse(396C/Oexplicit). Twelvefresh55/115controls: all55exact,115plaintextfeedbackexact,115cipherfeedback110/115with5prefixerrors; tailagreementisstructural, no primerrecovery. Targetwinningwholetexts remainincoherent; all1,008retained key/text pairs across14scouts independentlyreencryptexact. Fixedmodels/controls/repro/sourceboundaries: `batches/autokey/REPORT.md`. No historicalautokeyidentification, no familyexclusion, no guessedtitleplaintext or sourcechange/marker.

## Periodic polyalphabetic scout — GPT6.1Sol
48genuine heldout controls acrossSK/DE/CS,55/85/100/115letters,3/9/15/12periods andVigenere/Beaufort/variantBeaufort/Porta allrecoverentireplaintext at rank0 atplantedperiod. PrimaryPortaKEY/GEHEIMNISvector and12,800incrementalscorechecks pass.714actualmodelruns cover238literal/reverse/conditionalgroupomission cases across369/345/396C-O/393/367/374, periods1–16, phase-preserving erasures367. All182,784targetcandidate rows independentlyreencryptexact; leading wholetexts incoherent. Lower-budget conditional omissions andfinite controls give no universal recovery/exclusion. Completefullkeys/texts, languageprovenance, modelcontrols/repro: `batches/periodic-sol61/README.md`. Sourceunchanged/no marker.

### Column-fragment beam, completed rectangular scouts (2026-10-11)

Main solver independently developed a beam that orders whole ciphertext column fragments and scores newly closed n-grams across all rows. Five of seven genuinely heldout short controls and a fresh400-character control recover their complete plaintext at rank0;95/115-short-row and two-erasure controls fail. The batch covers1262 rectangular literal/reverse/explicit conditional cases across ten ciphers, retaining97696 full candidate keys with exact independent re-encryption; no coherent whole plaintext identified. See batches/columnar-stratified/README.md, beam-targets.py and beam-summary.json. This one-stage scout does not exclude tripleR, other widths or other cipher families. No published target answer used.

### One-long-column fragment beam (2026-10-11)

Main solver tested a distinct n mod width=1 transposition beam: enumerate the one long ciphertext chunk, place it in plaintextcolumn0, then order all equal-heightshortcolumns. Fresh heldout85/100/115 and400-letter controls recover full text at globalrank0;55/65 and two-erasure controls fail. Across94 whole/reverse/explicit omitted-group scouts,91200 full candidate keys independently re-encrypt exactly. No coherent targetwholetext. Method, all controls/keys and widths in batches/columnar-stratified/README.md and one-long-targets.py. Short or damagedtargetfailures provide no exclusion.

### Explicit repeated-telegram context cribs underMASC (2026-10-11)

Main solver independently tested32 distinct request/digit formulations (33 saved entries) as unproved context hypotheses, bothC/O andorders, literalbodyoronesinglegroupomission. Exactbijectivepatternmatching produces84 compatibleconditions; no phrase assumedfact. Locked completionsearch preserves allcribletters,32randomcompletions×20000proposals. Conditionalknown15lettercribcalibration on reusedheldout65control iswholeexact,55control fails. All172 savedactualkey/textpairs independentlyre-encrypt; no coherentwholeplaintext. Forcedsuppliedphrases are notdeciphermentevidence. See batches/context-masc-396/README.md, phrases.json, matches.json, controls.json and targets.json. NoMASCfamilyexclusion.

### Alternating readout directions, keyedcolumnar (2026-10-11)

GPT6.1Sol tested a distinct conditional keyedcolumnar geometry: readout-rankedcolumns alternate down/up, both initialdirections, ratherthan arbitrarycolumnreversals. Frozenbeamnormalizesciphertextchunks bydirection; rectangularandn modwidth1 cases. Twelvefreshundamagedcontrols9wholeexact; both400characterfive-erasurecontrols exactmaskedplaintext.160 literalwhole forward/reverse targetcases across363/393/345/396/369, widths2–26applicableonly, finishedwithoutcoherentwholeplaintext. Fullkeysincludepermutation,directions,widthandstreamorder, independentlyencodeandinvert. Noindicatoromissions/glyphcorrections. No historicalattribution orfamilyexclusion. Fullbatch batches/columnar-serpentine-sol61/README.md andNOTES.md.

### Repeated-keyword Myszkowski dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN keyword rank patterns with repeated ranks, reading tied columns by rows. Four fresh genuine55/65/115/400controls recover full plaintext as language rank0; dictionarycoverage, not unrestrictedkeyrecovery. Whole literal forward/reverse body scouts give incoherent texts. Numeric administrative header excluded wherepresent; other marks are phase-preserving erasures, no group omission. All retained complete key/text candidates independently encode/invert/rescore; full batch480rows. Conditionaldictionary failure excludes no otherkey/preparation/transposition. PrimaryPDFworked-example discrepancies are disclosed. Full evidence/reproduction: batches/myszkowski-main/REPORT.md and verification.json. No recoveredsolution or marker.

### AMSCO single/double-cell transposition dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN repeated-keyword candidates, each resolved to unique numeric order, under four declared cell parities (continuous/alternating-row starts, beginning1/2). All four fresh genuine55/65/115/400controls recover whole plaintext at language rank0. Actual whole literal forward/reverse scouts remain incoherent. Administrative numeric header excluded wherepresent, no group omission, marks retainpositions as erasures. Independent fullbatch480position bijections/encodings/inverses and frozen scores agree. This is finite dictionarycoverage, not unrestrictednumeric-key recovery or historicalfamily exclusion. Full evidence: batches/amsco-main/REPORT.md and verification.json. No solvedtext/marker.


### Original387 known-plaintext lead

All11groups collated independently against387/396: 53/55 preferred positions match; group9 CIAAI/CIASI and11 OORNT/OORMT differ. Published draft “Podajte šifrou stručnú zprávu o situácii a možnej činnosti.” normalizes50. Exact inventories fail because F is absent from ciphertext. Closest387 omit8DWJPM yields only F1missing/P1surplus; no glyph forced. Main agrees MOŽNEJ upon viewing full original. Conditional key tests can consider P positions3/20/23→F while retaining uncertainty and full source. Report: `batches/repeat396-387-sol61/REPORT.md`.

### R primary example

`batches/r-primary-example-audit-sol61/REPORT.md` validates actual55-letter intermediate grids, physical key rotations and existing encoders/inverses. Final indicator glyph and ip=5 assembly boundary remain ambiguous; no inspected target search inherited a fixed index4/5. Synthetic group5 insertion is not historical procedural proof.


### Conditional50-letter key pilot

`batches/r396-knownpair-sol61/REPORT.md` retains independent chunk-cover and position-tracing21/19/20 formulations. Known-key full50 encoders/inverses pass, but two fresh blind controls per formulation remain UNKNOWN after30seconds; no target runs follow failed calibration, no negative target inference. Hypothetical P→F variants at3/20/23 remain explicit and source glyphs unchanged. Key recovery and uniqueness remain unavailable.

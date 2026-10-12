# Analysis log — GPT-6 Astra

2026-10-11. README reread; explicit current user override conveyed by parent: no watcher, external reviewer polls DONE. No watcher started. Portal source captured centrally by parent: Not solved; no attached solution/transcription. Originals remain untouched.

## Transcription
Manual85-letter tentative reading in work/transcription.txt (17five-letter groups), matching printed length85. Header outside cipher body: Legación Eslovaquia / Vaše3032; Šulík;80174. Slight uncertainties in watermark-overlapped characters: CRTCS, BVBPT, SPQHO and QOQPM should be independently checked. Source remains authoritative.

## Statistics and attacks
- IC0.037815126050420166 (work/stats.txt), close to a uniform alphabet. This weakens an ordinary transposition of normal Slovak but85letters is too short to identify a cipher reliably.
- Single columnar transposition widths2–30:30 deterministic simulated-annealing restarts per width,20000proposals each, seed393 inherited from the shared implementation. Result for every width in work/columnar-results.txt. No coherent complete plaintext.
- Monoalphabetic substitution:100 deterministic restarts with50000proposals each, seed374, forward ciphertext and reversed ciphertext tested separately. Reverse is relevant because historical cipher C encrypted reversed plaintext. Slovak fourgram scoring; results in work/substitution-results.txt and work/substitution-reverse-results.txt. Best scores43.4586 and34.7374 are uncalibrated heuristic scores, not solution probabilities. Both candidates contain short language fragments embedded in nonsense; no valid key recovered.
- Reproduction: `sh ciphers/hcp-374/work/reproduce.sh` from repo root. This reproduces attacks, not plaintext. Shared quadgrams copied read-only from393; original corpus attribution in SOURCES.md. Training source not a solution source.

## Historical interpretation and next evidence
Antal et al.(2020), pp25–26, report Kryha machines sent to Madrid in1944. Kryha is polyalphabetic; the flat frequencies are compatible but do not prove this system. Missing machine/settings or daily key prevent a supported decipherment. Metadata title says a request to repeat15last groups of telegram80172; this is a contextual crib suggestion only, not known complete plaintext. No published solution encountered. No DONE, FINAL, or register entry.

## Sliding Kryha crib — OpenAI GPT (main solver), 2026-10-11
`python3 ciphers/hcp-374/work/kryha_crib.py` tests96 guessed repetition-request phrases, every possible body offset,17 original Kryha step phases and both signs (161840 cases). It propagates exact modular constraints between the two arbitrary26-letter ring positions, rejecting inconsistent cycles and forced duplicate positions within either ring. A planted85-letter random-ring control with a43-letter embedded crib passes, and a deliberately inconsistent pair is rejected. All longer templates containing `poslednych` fail the necessary constraints;2402 short-template cases survive. Survivors are only partially constrained hypotheses, not keys or readings; global component displacement/permutation completion is not yet checked. This is an exact test of these literal guesses under the original17-step machine, not a general exclusion of Kryha or proof of the plaintext wording. The archival description supplies meaning, not exact wording. Source unchanged.


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

### Repeated-keyword Myszkowski dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN keyword rank patterns with repeated ranks, reading tied columns by rows. Four fresh genuine55/65/115/400controls recover full plaintext as language rank0; dictionarycoverage, not unrestrictedkeyrecovery. Whole literal forward/reverse body scouts give incoherent texts. Numeric administrative header excluded wherepresent; other marks are phase-preserving erasures, no group omission. All retained complete key/text candidates independently encode/invert/rescore; full batch480rows. Conditionaldictionary failure excludes no otherkey/preparation/transposition. PrimaryPDFworked-example discrepancies are disclosed. Full evidence/reproduction: batches/myszkowski-main/REPORT.md and verification.json. No recoveredsolution or marker.

### AMSCO single/double-cell transposition dictionary scout (2026-10-11)

Main solver tested12,866frozenTRAIN repeated-keyword candidates, each resolved to unique numeric order, under four declared cell parities (continuous/alternating-row starts, beginning1/2). All four fresh genuine55/65/115/400controls recover whole plaintext at language rank0. Actual whole literal forward/reverse scouts remain incoherent. Administrative numeric header excluded wherepresent, no group omission, marks retainpositions as erasures. Independent fullbatch480position bijections/encodings/inverses and frozen scores agree. This is finite dictionarycoverage, not unrestrictednumeric-key recovery or historicalfamily exclusion. Full evidence: batches/amsco-main/REPORT.md and verification.json. No solvedtext/marker.

## Source-collated conditional350/351-ringtransfer

Allcontrolled85letterbeam/direction/Jscoringresults in batches/kryha-transfer374-sol61/. SourcepreferredQ/VandambiguousC/Gbranchesexplicit. No key/text; noKryhaexclusion. Old17-step cribnegativewithdrawn dueunsettledglyphs/unprovedhistoricmodel; sourceunchanged.


### Original80172 / Solved373 context

Full130groups650 from public373 begin KIDAH; this does not establish five-letter indicator semantics. Published numerical preparation is not known exactly: digitwise640 plus4sentenceJ+5initial+1filler is only length-compatible. Sources/uncertainties/counts attributed at `batches/kryha373-collation-sol61/REPORT.md`. Main necessary-recursion test of350rings on known93-letter pre-number prefix has no exactmatch across48declared glyph/preparation cases, both directions/signs and counts2–52. Freshphysical23-stop control passes all70constraints; fixedring-only result. Evidence: `batches/kryha373-knownprefix-main/REPORT.md`. Other rings/procedures/preparation remain open.


### Completed373 procedural cross-checks

`batches/kryha-transfer373-sol61/REPORT.md` confirms eight fresh650-letter physical controls recover their exact texts and settings; seven calibrated configurations on both full source snapshots remain incoherent. Published373 plaintext was not supplied to transfer ranking. Unknown-ring equations tested independently in `batches/kryha-knownpair373-sol61/REPORT.md` reject only the stated pre-number prefix, finite preparation/glyph/alignment hypotheses and constant per-cycle unit advance, including one selective-J press rule. Even the source-led chronological USTRENI branch (omitting handwritten D27) supplies no witness. Controls disclose shortened72 ambiguity18/20, rather than claiming complete held-out prediction. These are conditional known-context incompatibilities, not a Kryha-family exclusion or a new373 solution.


## Q-marked proper-name context branch

Live rendered portal General remains Not solved. New main-solver context attack uses already published373 first prefix, preserving Roessner/Madrid source words with conditional Q delimiters suggested by primaryR instructions; Madrid-machine adoption unproved. Eight preparation branches, four glyph branches, omit0/5, periods2..52:3264 exactUNSAT aftertwo independent mixed-ring controls pass. No new key to transfer to374. This is a finite conditional preparation/machine rejection, not a general Kryha exclusion. REPORT, controls and allresults: batches/kryha374-qcontext-main/. No source or ciphertext changes, no marker.


## Alternative cycle advance, main solver
Published373 context tested under arbitrary mixed rings, the source-preserving pre-number prefixes, and constant even cycle residue2. Two positive fresh fixed-cycle controls pass independent full enc/inverse;4896 actual cases exactUNSAT. Unitsmod26 map residue2 to every gcd2cycle residue, so this is a bounded broader-cycle result, not a physicalwheel claim. Unknown-cycle calibration and fixed0/13 calibrations timedout; noactualtargetunderthosefailedmodels. Full retainedevidence: batches/kryha374-freecycle-main/REPORT.md. Other prep/framing/error/stepping families remain open; no374key.


## Prefix offset search and all52 physical specialization
Main widened only ordinary prefixalignment: allnewcharacter offsets1..25 exceptalreadytested5,12source-preservingpreparations,4glyphbranches,periods2..52. Freshmatched97controlblindlyfindsoffset13;independentenc/inversepasses.58752actualcases:58746UNSAT,6UNKNOWN;the6remainUNKNOWN30s. NoSATcontextkey. See batches/kryha374-prefix-offset-main/REPORT.md.

A separate exactphysicalall52 specialization uses only350's52adjacentwheel distances, neveritsrings orselectedmask. Fresh92random-ring controlblindlyrecoversstart22withfullenc/inverseverification;thefourperiod52 UNKNOWNcontextbranches×52starts are208UNSAT. Thisonlyexcludesfixed179allholes/everyletteronepress/stated92prefix/glyph/offsets. ArbitraryK50/52,differentwheelorpreparationremainopen. Report: batches/kryha373-all52-physical-sol61/REPORT.md. No374plaintextkeyornew373solutionclaimed.


## Exact completion of ordinary-prefix timeouts
The six unrestricted-ring period50/52 SMTtimeouts were resolved by audited effective-GF parameter enumeration, completing unseenalphabetletters afterward. All6UNSAT (four676assignments,two1352),about0.55s. PreservedpreviousUNKNOWN andphysicalspecializations are not overwritten. Combinednewordinaryoffsetscan58752cases nowall exactUNSAT in itsstatedprep/glyph/offset1..25-except5/fixed179-cycle/arbitraryrings family. Finitehelper audit and8positivecontrols: batches/kryha373-unemitted-spaces-sol61/FINITE-AUDIT.md; results/reproduction: batches/kryha374-prefix-offset-main/REPORT.md. No374key.


## Unemitted word-boundary advances and exact completion
Public373knownprefix examinedunderunprovedoperator-spacehypothesis:1or2unemittedextraadvances atlexicalboundariesoronlyliteralwhitespace;sourcewords,Damended/unamended,naturalJ/I,glyph53L/I90E/A,andomit0/5remainexplicit. Eightfreshphysical-mask92/93controls recoveronlyplantedperiod20/23/30withfullindependentenc/inverse;withheld20scores20/18/20/20/20/19/20/20arepreserved,notclaimedallunique.128variants×51periods:6520UNSAT+8UNKNOWN2s,0SAT. Originalbatchpreserved: batches/kryha373-unemitted-spaces-sol61/REPORT.md.

The8remaininggenericm52caseswereexactlycompletedwithvectorizedGFactive-coordinateenumeration:6×456976+2×913952=4569760assignments,allUNSAT inabout2.98s. Newalgorithmmatches20independent676paircasesandeightpositivecontrols,withouttruekeys. Combinedinvisible-spacefamilynow6528exactUNSAT;scope/partialpredictionlimitsunchanged. Report: batches/kryha373-invisible-finite-sol61/REPORT.md.

Independentphysicalall52jump-walkspecializationalsorejectsall8×52=416profilesafterafreshmatched92controlpassesfullenc/inverse. Geometryonlyfrom350,noringreuse. batches/kryha373-invisible-all52-sol61/REPORT.md. No374key,new373decipherment,sourcechangeorhandover.


## Remaining constant-cycle residue classes
Afterauditedactive-coordinateenumeration,theearlierD0/D13controltimeoutsbecomepositivefullknown-prefixfits; independentrecurrenceenc/inversepassesall4cyclecontrols. New D0/D13cases12preps×2omits×4glyphs×51periods×2classes=9792exactUNSAT,0UNKNOWN. TogetherwithD2andearlierunit179checks,thiscoversallfourmod26cycleclassesonlyatomit0/5andthespecifiedpreps/sourcereadings. Itdoesnotidentify373machineor374key. Earlierfailedcalibrationspreserved; batches/kryha374-freecycle-main/REPORT.md,finish_degenerate.py,finite-controls.json,degenerate-summary.json.
## Comma-only prefix preparation with unknown rings (2026-10-12)

Earlier comma-only J/X tests on public Solved 373 used fixed 350 rings, while unknown-ring tests used concatenation or markers at every word boundary. This genuine preparation gap is now checked in `batches/kryha373-comma-marker-sol61/REPORT.md`. The source prefix before 6.000 has one literal comma after CELULOZIEK. Eight preparations preserve its words, combine the documented USTREDNI/USTRENI readings and natural J/I, and emit only that comma as J or X. Natural J→I is applied before inserting delimiter J.

All 42,432 cases (eight preparations, offsets 0–25, four source-glyph combinations, periods 2–52) are exact UNSAT, with no UNKNOWN. Arbitrary independent alphabet rings and cyclic displacement variables are searched under ordinary presses and full-cycle displacement 179. Two fresh 94/93-letter physical controls uniquely recover their offset/period and pass independent full-prefix encoding/inversion. Complete case identifiers and source hashes were checked.

This is attributed published-context work toward 374, not a new solution of 373. It does not prove that either Madrid telegram used this Kryha mechanism, reject another preparation or recover a transferable key. The actual 374 plaintext remains unknown.
## Source and alternative-machine diagnosis (2026-10-12)

Independent inspection of the public 373 scans confirms ROESSNER MADRID is inline message text, with no source basis to remove it. The exact reflector-machine no-self-encryption filter rejects 1,216 of 1,248 explicit prefix/preparation/offset/glyph cases; 32 survive. The faithful 93-letter corrected prefix survives only at offset 20, which the source does not mark as framing. This is a necessary Enigma property only, not a machine identification or key fit.

The primary historical paper explicitly records Madrid's Kryha introduction during 1944 without an exact issue date. It also cites a January 1941 change to Roman numeral preparation and instructions for reformulating stored message content. Those findings weaken the assumption that the public typed draft is literal machine input; they do not authorize invented words or a guessed representation of 6000. Neither explains the failed pre-number prefix fits. Full primary references, scan observations, transparent filter inputs and limits: `batches/kryha373-framing-diagnostic-sol61/REPORT.md`.
## Recovered Madrid key and 374 body (2026-10-12)

The breakthrough comes from a different, source-faithful crib: the final 186-letter sentence of the public373draft, which contains no numerals. Sliding this sentence through the650-letter working transcription avoids the speculative digit-word preparation and the inaccurate initial ROESSNER crib. Across four declared J/I and Q-name preparations, all offsets and periods2–52, the necessary mixed-ring model gives one witness in94,656 cases: J→I, no Q, offset462, period23. Nine declared source-uncertain positions are treated as equation erasures with original press indices retained; three fall inside the winning span. All183 retained equations fit. Three fresh physical controls recover their entire186/188-letter texts. Full surrounding decode immediately becomes coherent and spells ROESNER with one S, explaining why earlier exact prefixes from the typed ROESSNER draft failed. That is decoded evidence, not a silent edit to the archival draft.

Independent physical DP and an independent coordinate-translation audit identify exactly one cyclic23-stop mask within the52-hole/179-distance geometry, preserving recovered rings and displacement cycle. Hole numbers in those reports are ZERO BASED. Root's body key starts at zero-based34 with displacement1 modulo26. It uses this new Madrid key; the failed350-ring transfer hypothesis is superseded only as a proposed route, not rewritten into a success.

Transfer to374 finds a unique phase3/shift8 among all598 phase/displacement pairs: the old reading matches71/76 known published suffix positions, with next candidate21/76. A fresh independent source reading, frozen before decoded374 consultation, prefers G/Q/V at absolute9/25/60 and reads35M versus earlier35N. Neither source image nor old transcription is overwritten. The new `work/transcription-collated.txt` is explicitly a working copy. Its literal80-letter body is `aupozornuiespanlelskeprotibodvvkyuzpevnekupenenazakladepovodnychciencelulozyxxxx`; alternate35N gives PROTIBODAVKY. Source21S and32L are retained, with corresponding L/B discrepancies against public373's SPANIELSKE/PROTIDODAVKY. Their cause is not established. We do not turn expected words into fake scan corrections.

`work/decrypt.py` verifies source-image and manual-reading hashes, physically walks the selected mask and returns every body letter. `work/verify.py` independently uses absolute wheel coordinates; both complete80-letter readings invert and re-encode exactly. Prefix KIDAH remains unchanged and is explicitly not deciphered. All26 output labels and19 tail input labels are recovered; M24 is from held-out published context, X19 is a padding hypothesis, and unused F/G/J/Q/W labels are canonical completion. Those unused labels do not affect this decoded body. Internal solver audit in `batches/kryha374-final-solver-audit-sol61/` independently checks the actual source body with a continuous edge-walk method.

SOLUTION.md now supersedes its old all-unresolved claim. The commercial wording is attributed to public373; the new work is machine-key recovery and the374transfer with literal source discrepancies preserved. Partial historical limits are explicit, so no register entry is written. Review submission concerns the recovered80-letter body and working physical key, not a proved historical indicator or fully recovered rare alphabet. External Claude owns review; no watcher or reviewer was started.
## Review1 accepted; final default and held-out validation (2026-10-12)

Claude Opus5.5 accepted the body/working-key claim with six minor findings and no second round. The physical/ring key is unchanged. The reviewed default now uses source35N, supported by the older pre-key Claude reading and the published word; new GPT35M remains an alternative. The complete DONE1 data/scripts/SOLUTION are preserved in work/round1-default-M. Source JPEG and markers are unchanged. Source21S/32L are not corrected: the same key reads SPANIELSKE/PROTIDODAVKY correctly in373, so their L/B forms here are garbles of this copy, with cause unknown.

New independent phase comparison on the reviewed reading: all598 pairs, best3/8 gives74/76, next21/76, median3. The same key reads the645-letter373body including459 letters outside the fit, with cardinal numbers, sentenceX and finalXX. This held-out result supports X19 and XXXX, while retaining literal source/canonical rare-label errors. Command work/heldout373.py and saved JSON reproduce it. Reviewer's ORWKM prefix example is a computed projection, not the actual source: both373 and374 ciphertexts beginKIDAH. The possible indicator is still an open lead with one repeated value under this key. Detailed item-by-item responses are in SOLUTION.md. No register entry is authorized for this already published-content key-recovery result.
## Human-updated review1: shared indicator and fresh encipherment (2026-10-12)

The reviewer amended finding5 after the human pointed out its initial ORWKM/source-prefix mistake. The updated finding is incorporated:373 and374 both actually startKIDAH and use the same initial selected-stop ordinal0 and displacement1 (physical zero-based hole34). The source373sentence begins at letter573 after567 body emissions; source374enciphers it anew at emission0. Measured76-character slices have0 ciphertext agreements and74 plaintext agreements. This explains the absence of repeated body cipher groups without assuming a different key. The shared indicator's association with the starting state is established for this pair; its internal coding remains open. work/indicator-comparison.json preserves slices/counts. The physical/ring key and reviewed N default are unchanged; this is documentation/interpretation, not a substantial new solution requiring another round.
## Closure after updated ACCEPT review (2026-10-12)

All six minor findings are addressed, including the human-updated shared KIDAH indicator/fresh encipherment explanation. Default35N and alternateM reproduce all80 body letters exactly; source21S/32L remain garbled literally. The physical key is byte-equivalent in all mechanical arrays/parameters to DONE1. The original source JPEG hash is unchanged. The final standalone Slovak report has three visually inspected pages, full key, original scan, attributed content, held-out evidence, review response and remaining indicator/rare-label limits; report/QA.json records validation. No register entry is written without separate human authorization for this public-content key-recovery contribution. FINAL is created only after these files are complete.

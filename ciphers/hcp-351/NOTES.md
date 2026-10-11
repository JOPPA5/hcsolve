# HC351 solver log — historical Astra attempts; content recovery with GPT-6.1 Sol
## 2026-10-11
Read README, checked skip.txt (no entries); directory initially absent. Parent supplied all three live portal tab readings and browser-downloaded full scan. Stored immutable copy and metadata. User overrides README watcher instructions: no watchers launched, external reviewer polls markers. No marker created, no decipherment claim.

Manually transcribed 77 five-letter groups, 385 letters. The clear routing line reads approximately "SOLAKOVI 385"; opening numeric or plain routing fields, "CIERER/CIEKER 3002" signature and all other cleartext excluded from cipher. Ambiguous glyphs: HUURZ, RWQKK, ULOLL, STRFV, HANEN, PXNDQ, XUCNC, RFPFF, ABZQJ, HRLZO, ELJOY, ZYYYQ, LVBNF, BBXOB, UBXQV, NNWCS, IILZM, JXFHL, EYRMI, TGMDH, HWUTS. First-pass transcription should not be treated as ground truth. Scan includes Madrid routing and a 2.III/2.XI-like postal stamp; portal gives 1944-11-03. No correction to the portal date is asserted.

Letter IC = 0.039082792207792205, close to uniform 26-letter expectation 0.0384615385. Unlike earlier transposition cases, no strong native Slovak frequency profile is apparent. This suggests examining polyalphabetic encryption, but does not establish a family or prove impossibility. Preserved all exact readings for future correction.

analyze.py tried unkeyed rectangle transposes of divisor widths 5,7,11,35 in both full reversal directions; none coherent. diagnostics.py reports mean coset IC for periods1–40 and lag matches, and all repeated trigrams. None of the period averages shows a strong Slovak-like spike; this is descriptive, not a formal significance test.

vigenere.cpp uses copied Slovak quadgram scores derived locally from UD Slovak SNK in the393 attempt. It tests standard additive A–Z Vigenere (A=0; P=C-K mod26), periods1–30, ten restarts and10,000 mutations per period, seed351; retained highest-scoring candidate per period. All outputs in vigenere-results.txt are incoherent as full messages, despite optimized isolated word fragments. This is heuristic and not an exclusion of Vigenere. No autokey, other alphabets, Beaufort, transposition-composition or machine cipher search was performed.

The portal's Unsolvable tag and title "Nerozlúštiteľný telegram" are source claims, not proof. No key or plaintext recovered; possible damaged transmission, key mismatch, other family remain hypotheses only.

## 2026-10-11 — calibrated full385 two-ring Kryha attempt

Apply unchanged projected-IC → all-candidate MASC language ranking → top-seed joint refinement procedure validated on an independent385letter held-out Slovak control in350 (exact385/385). Copied code/models and control verification into351 work; training excluded the control. Literal351 transcription unchanged. Known17step schedule, unknown two mixed26rings, all17phases and both optimization signs; signs are equivalent under reflection of both rings. Shared message framing does not establish a shared cryptographic regime. No watchers/reviewer started.

### Conditional uniform two-press model control

Read-only350 method sources copied into351 work and changed ONLY displacement update to consecutive pairs: d[i+1]=d[i]+sign*(s[(phase+2i)%17]+s[(phase+2i+1)%17]) mod26. This is not2*s[i]. Independent random ring seed3512385, phase9/sign+, sameheldout385 plaintext; unchanged models and generic budgets, seed ranked solely by language. IC3000×10k retains300 candidates; MASC8×30k each, topseed joint8×100k: MASC418.441, final659.126, EXACT385/385, independent encryption exact. Files double-control-verified.json, ring_double_control.py and *_double.cpp. The absent control letters allow keyambiguity; uniqueness notclaimed.

Parent read primary SSA memo NR2417 (https://cryptocellar.org/kryha/nr2417.pdf, page1): encrypted J wordspacer and extra lever depression after plaintext J; later52stop selector20–30 active. Thus uniform doublepress is ONLY a conditional scout, not this documented content-dependent mechanism, not established Slovak procedure. Original17step schedule is earlymodel. Baseline351 completes first, then bounded350 uniformscout saved only here with read-only350 input. No identical restart inflation.

Full351 baseline completed34 phase/sign cases,10200 IC candidates, MASC8×30k each and top language seed joint8×100k. Best joint score-413.007 atphase6/sign1; bestMASC-461.099. All are incoherent; exact re-encryption of385 baseline letters is key-fit consistency only. Heuristic failure doesnotexclude early17step Kryha. Candidatekeys/outputs and budgets retained in ring-ic-target-report.json and per-case directories. No DONE.

### Selective plaintext-J model: genuine control, no target claim

Conditional early17step simulator advances one selectorstop after each plaintextletter, two after literalJ. Gauge fixes inputJslot0; for given outputpositionsO, ciphertext alone then determines projectedslots and entire skip path. Thus unknown other25inputletters are an ordinary constrainedMASC. German TESTwordtokens were joined byJ; original naturalJ retained, accents removed/ß→ss. Independentrandomrings seed3519385, phase11/sign+. Every literalJ obeys extraadvance; this is a constructedcontrol convention, not asserted Slovak adoption. Germanfrozen models from batches/scoring-sol61/german, outside TEST.

KnownO, fixedJ, eight×30k genericinputMASC: quad score removesallJ and recovers370/385. Its incorrectw/k/f/p substitutions score2717.41, above true2705.26, so additional identicalrestarts cannotfix scorer. Frozen5gram model withheaderfloor−21.00641251703732 instead givesEXACT385/385 including70J withsamebudget. Independent reencryption exact; absentletterkeyambiguity remains. RemovingallJ is a named scoring convention only; allJ retained infullplaintext/encryption. Compile/run selective_j_known_output_five.cpp with workdir, selective-j-control-cipher.txt,11,1,selective-j-control-output.txt; python3 ciphers/hcp-351/work/verify_selective_j_control.py verifies corpus preparation, plantedrings and fullkeyencryption.

UnknownO pilot selective_j_ic.cpp recomputeswhole385symbolpath at everyOswap, unlike invalidfixedhistogramdeltas. Jslot0 fixesgauge, so O[A] is NOTnormalized. Budget100×10k independentrestarts; retain100candidates; fixedO5gramMASC8×30k each. Trueconcentration12487 outranks1000randomO null(range5841–6499). Optimizedrings reachonly7343–8897. HighestLANGUAGEcandidate matches24/385; diagnosticbestmatches29. No truthbasedselection used. Therefore unknownOattack FAILScontrol; no selectiveJtargetsearch/negativeinference. Increasingidenticalrestarts deferred; structuralcandidateimprovement needed. Alloutputs/calibration in selective-j-control-ic100-*.json/txt.

### Structurally distinct selective-J control search failures

Partial-O sequential beam width10000 uses TRAIN-only fixedJ/sortedother25 unigram likelihood; repeatedcipher symbols reuse assignedOposition. Complete candidateOstreams get frozen5gramconstrainedMASC. Top language candidate20/385, diagnosticbest31. Alternate renewalhazards for J-separated segmentlengths plus conditionalnonJ unigrams, samewidth, top19/385, best30. Neither recoverscontrol; no target inference.

More substantial pathbeam instead branches only J/nonJ, deferring allotherOassignments. Jforces O[c]=currentoffset; nonJ removes thatoffset fromdomain[c]. Repeatedsymbols share26positiondomains. SingletonallDifferent propagation and full bipartitematching reject inconsistent partialrings; remainingdomains completed bymatching after385symbols. TRAIN-only segmentlengthhazards rank paths. Width1000, top300 completions language-reranked withsame5gramMASC, top14/385 diagnosticbest30. This also FAILSknowncontrol. Arbitrarymatching of underdetermineddomains need not include plantedO; beam pruning is heuristic. No targetselectiveJsearch, no key/plaintext claim. Threebeam codefiles, allrawstreams/reranks retained. A reproduciblecommand is sh ciphers/hcp-351/work/reproduce-selective-j-control.sh; it intentionally reruns thesecontrols, not target.

## Uniform doublepress350 conditional scout completed

All34 phase/sign cases on literal385letter350, read-onlyinput, alloutputs stored351/work. Same validated budgets:3000×10k IC,300 retainedO eachcase, MASC8×30k each, top language seed joint8×100k. Total10200 candidates. Independent doublepress control recovered385/385; best target joint-413.29 phase4 sign-1, bestMASC-464.889. Outputs incoherent, no supported plaintext/key; exact completebaseline reencryptions are only key-fit checks. This uniformtwo-press model is conditional and differs from the primary memo selectiveJ mechanism. Heuristicfailure not exclusion; historicalSlovakadoption unproved. Report work/ring-double-target350-report.json. No351 doublepress scout requested after parent cap350only; no sourceedits/watchers/DONE.


## Verified later Kryha stepping geometry — main solver synthesis, 2026-10-11

A primary NSA Military Cryptanalytics Part III scan (Callimahos,1977, printedp185) supplies a complete52-hole table of effective letter displacements. GPT-6.1 Sol independently transcribed and checked the scan against27 SSA fragment/cumulative checks; see batches/kryha-wheel-sol61/{wheel52.json,verify_geometry.py,verification.json,SOURCES.md}. Every selector cycle over any chosen active-stop subset sums179 letter positions, residue23 modulo26. Reflected arbitrary rings give the equivalent opposite direction; literal hardware orientation is separate. This establishes a constrained step family instead of52 independent unknown increments, but does not establish which machine or stop mask was used by Slovak diplomats. One conflicting SSA preliminary sum is disclosed rather than silently repaired.

Independent385-letter controls with20/26/30 chosen stops validate forward/inverse mechanics. A blind unknown-mask/output-ring pilot fails the control, so no actual message has been decrypted or excluded under this model. Fixed-mask/known-output checks are limited positive diagnostics. Primary source provenance, full controls and all failed candidate keys remain in the wheel batch. No marker or register entry follows from hardware reconstruction alone.

## Fixed TRAIN-profile objective and framing refinement
A changed output-ring optimizer, sorted frozen TRAIN frequencies plus multinomial count-factor, followed by unchanged generic MASC/joint language refinement recovered a fresh independent385-letter control exactly. Outputring26/26 up rotation; input24/26, G/W absent and unidentified. A fresh365-letter control failed (42/365 after4grams,25/365 after5). Optimized false rings can still beat truth profile likelihood; this is a useful exploratory search, no exclusion power. Reproducible report: `batches/ring-profile-sol61/REPORT.md`; actual all17-phase target sweep now running. Prior crop365/355 generic5gram postrefinement completedall34 noise candidates in `batches/kryha-framing-sol61/REPORT.md`, with independent inverse/reencryption. One prior near-correct365 control became exact by5gram postrefinement,355 stayed337/355. No historical plaintext.

## Primary Kryha indirect symmetry reconstruction — GPT6.1Sol
From SSA NR2417 commonpreparedprefix attack, exact modular pairconstraints solved overGF2/GF13 recover all12affineequivalent outputrings in0.006s on a fresh9message385lettercontrol with true52holegeometry,26activestops, selectiveJextra press and40lettercommonprefix. This is partialringrecovery requiring supported depths, not plaintextrecovery. Actual350/351 first20/last10/combined framing rejects a single constantshift isomorph; equalpositions alone impose no useful outputring information. Partialmappingcollisions/equallettersplusmismatch force contradictions. Their dates1944-02-28/1944-11-03 differ; no same-day peers in our16messages. This does not exclude changingstepping, typos or unencryptedframing. Primarysource distinction, equations, fullcontrols, actualconditionalchecks: `batches/kryha-method-sol61/NOTES.md`.

### Conditional progressive mixed-ring attack (2026-10-11)

GPT6.1Sol independently tested C_i=O^-1(I(P_i)+i mod26), unknown mixed input/output rings, all whole forward/reverse350/351/369 bodies. A fresh prepared heldout385-letter control is exact including both rings; the115-letter control fails9/115. No whole target text is coherent after fourgram/fivegram joint refinement and blind complete325 input-swap neighborhoods. Full report: batches/progressive-ring-sol61/REPORT.md. All7632 saved full key/text candidates independently invert and reencrypt. This generic progressive displacement is not a verified programmable Kryha wheel or historical attribution; short369 is particularly weak due calibration failure. No solution or family exclusion.

### Real52-hole cycle identity: failed output-ring objectives (2026-10-11)

The independently verified179-total wheel entails displacement23mod26 after one full selected-stop cycle, regardless of mask/phase. Three fresh385-character heldout controls with20/27/30 stops verify the identity exactly. Blind output-ring pair and consistent-triple collision optimization nevertheless selects false rings whose scores exceed truth in every control. Triple clusters worsen overfit. No actualtarget attempted with these failed objectives; no exclusion. Full diagnostic keys, encoder checks and report in batches/kryha-cycle-sol61/REPORT.md.

### Histogram-profile mixed-ring scouts complete (2026-10-11)

All68 ring-profile target branches finished: seventeen phase families each for350whole385,351whole385,conditional350crop365 andcrop355. No coherent completeplaintext after fourgram and genericfivegram refinement. Fresh385 control exact; independent365 control still25wrong underfivegrams. Independent verification of136final full keys, scores and inverse/re-encryption passed;20400 intermediateMASCkeys codec-checked, sourcehashes unchanged. See batches/ring-profile-sol61/TARGETS.md and target-summary.json. Cropping remains an unproved framing condition; failure excludes no cipher family.

### Structural real52-hole mask recovery (2026-10-11)

GPT6.1Sol developed a structurally different real-hole language beam. Three fresh385-letter known-ring controls (20/26/30selectedstops) recoverexactmask,startingstopandwholetext atglobalrank0. Bothringswere SUPPLIED for this conditionalcalibration; this is notunknownkeyrecovery. Blindmask/ringalternation atknownm26,8randomringstarts×4passes,beam64,30000jointproposals/pass fails atmax25/385;bestscore-1112.01 versusknowntruth388.77. All7312 savedcompletephysicalmask/ring/textrows independentlyrescored,invertedandreencrypted. No actualtargetrun underfailedunknown-ringcalibration. Fullreport batches/kryha-mask-sol61/REPORT.md.

### Fresh physical source/framing audit (2026-10-11)

GPT6.1Sol sourceaudit, independently viewedby main, supportsalternate350character15K(PMQKK),351character8J(HUJRZ) andcharacter378K(TGKDH). Variants retainedseparatelyin batches/source-variants-350-351/ withimageshashes; originalsource/metadata/worktranscriptionunchanged. Pairprefix18/20 andsuffix10/10nowmatches, versusbaseline16/20 and9/10; middle2/355. Physicallyboth77groups×5=385andprinted385count, no delimitermarking20prefix/10suffixasheader. Source351arrivalstampfavors2.III44−23, service1/2200, hencepossibleMarch1send/March2arrivalnear350Feb28insteadportalNov3; noportaltypoconclusionorassertedsharedkey. Fullpixel evidence: batches/framing-source-audit-sol61/REPORT.md/comparison.json.

### Restricted standard-ring Kryha scout and ring calibration (2026-10-11)

GPT-6.1 Sol tested two distinct calibration conditions. With the real mask and initial stop supplied, three fresh 385-letter controls recover the entire output ring; fivegram plaintext recovery is 385/380/385, and the blind complete input-swap neighborhoods retain truth at ranks 0/2/0. This isolates the difficulty of discovering the mask jointly with both rings; supplied settings are explicitly not blind full-machine recovery.

A restricted A–Z input/output-ring family, with all 26 relative offsets, passes two fresh controls with unknown stop count, mask and phase: counts 20–30, all 52 starting stops, beam 64. Eight whole-body target branches then test original/source-preferred readings in each stream direction for 350/351. No complete candidate is coherent. All 11,440 saved standard-ring mask/text rows independently reproduce the physical wheel and full language scores. This does not identify historical rings or exclude unknown mixed rings, selective extra presses or other settings. Reports: batches/kryha-mask-sol61/ring-calibration/REPORT.md and its standard-rings/ subdirectory.

### Paired whole-message search under the old17-step wheel (2026-10-11)

GPT-6.1 Sol jointly searched shared unknown input/output rings for both385-letter messages under all17 phases of the documented old17-step sequence, resetting each body independently. Both literal and source-preferred whole pairs were tested:34 cases, with no coherent complete plaintext. Two of three fresh770-letter controls recover exactly; the third differs only by Q/X labels and both frozen objectives favor the false label assignment. Independent verification covers11,100 retained candidates and74 operative winners, including complete encoding/inverse and message-separated scoring. This is a restricted old-wheel/shared-key hypothesis and does not exclude another wheel, start or key. Full evidence: batches/kryha-pair-sol61/README.md and summary.json. No solution or marker.

### Blind real52-hole wheel, shared-ring physical histogram bridge (2026-10-11)

A substantive main-solver initializer projects pooled column histograms through actual physical selected holes and uses sorted TRAIN multinomial frequency likelihood, without knowing the input ring. GPT-6.1 Sol implemented cycle-output initialization,256physical profiles, all pairedMASC seeds and language-selected joint mask/ring refinement. Fresh two385-letter random-ring/random-mask control at known count26 recovers all770letters and exact ordered physical mask/start. Root independently checks both complete texts using absolute wheel coordinates, separately from the agent's arc walker: batches/kryha-pair-main-audit/verification.json. Every optimizer starts blind and does not read planted keys/text.

Four actual complete whole350/351 paired scouts (original/preferred, forward/reverse) remain incoherent. Preferred glyph variants are separately pixel-supported; no framing group omitted or crib forced. This tests known count26, shared rings/mask/reset, ordinary one-stop presses. A new independent355+355 control for a proposed framing crop fails55/710, so cropped actual body search is withheld under that pipeline. The initial385success alone is no proof of the historical count/model or broad robustness. Full evolving controls/keys/audits and failures: batches/kryha-mask-pair-sol61/REPORT.md. No historical key/plaintext or marker.

### Real-wheel count20 coupled anchor/ring refinement (2026-10-11)

GPT-6.1 Sol generalized physicalhistogram bridge to counts20–30, keeping alphabet26. Mechanical known-key checks pass all11counts, notblindkeyrecovery. Fresh20-stop pair control initially recovers730/770, all40errors in firstordinalcolumn. Changing the firsthole requires a compensating global inputring rotation; ordinary swaps cannotcross this scoringbarrier. Generic660maskneighbors×325inputswaps+26cyclicrotations from unchanged blindlanguagewinner recovers exact770, physicalmask/start and bothrings upgauge. Root separate absolute-coordinate check agrees: batches/kryha-pair-main-audit/verification-m20.json. Fresh30-stop control still fails41/770 (bestdiagnostic57), so no30target. Whole preferred350/351 forwardcount20 bridge+refinement remains incoherent score−2629.07. Eachcase3600complete pairedkeys independently verified. No historicalcount/model exclusion. Fullreport: batches/kryha-count-pair-sol61/REPORT.md. No marker.

### Human batch review: offset+1, period23 priority (2026-10-11)

The human supplied an independent Claude batch review, outside marker protocol. Its major lead is350[i]→351[i+1] period23 consistency. Root separately counts all equal-letter pairs inside residueclasses:97/114equal at+1 vs4/114at0, with23/46 clear outliers overperiods2–59. Agent independently reproduces fixed-reference83/97. This is substantial shifted-text evidence overlooked by offset0pair scouts. All prior exactoffset0 UNSATclaims remain conditional only and cannot reject this relation. SOLUTION.md now prominently states that limit; source immutable. Main models/randomcontrols do not replace source-based shiftedpair recovery. New evidence in batches/review-leads-main and batches/kryha-shift23-sol61. No marker.


## Outside-review lead: recovered cycle and physical two-mask feasibility

The outside Claude batch review redirected work to the +1 alignment and period 23. Blind finite-field recovery independently found the common output cycle, including a fresh corrupted physical 23-stop control; provenance and pixel-assisted transcription variants are in `batches/kryha-shift23-sol61/REPORT.md`. Pixel corrections are explicitly prediction-assisted, not blind evidence. Updated overlap is 350[20:374] versus 351[21:375]; four clear interior discrepancies remain. No plaintext has been recovered.

Main solver's exact two-mask dynamic program (`batches/kryha-two-mask-main/REPORT.md`) independently passed four fresh 23-stop controls, then found physical witnesses for only two of the twelve unit-equivalent coordinate rows. Both admit fifteen initial-hole pairs on the acquired 52-hole, circumference-179 wheel. This is a structural fit under stated wheel and relation assumptions, not unique masks or plaintext. The earlier CP target-sized control timed out and carries no negative result. Feasible-path counting and language recovery are now being tested with matched controls.


### Correction to paired histogram profiling
The main and subagent audit found that prepooling both message histograms under A's path requires subtracting per-residue K[j] from B, rather than constant K[0]. The earlier profile shortlist used the latter and is superseded as a heuristic. This does not invalidate independently checked physical witnesses or candidate reencryption, which project B under its own path. Corrected profiles are in batches/kryha-two-mask-reset-sol61; full exhaustive two-path language scoring is in batches/kryha-two-mask-refine-sol61. No historical plaintext is yet verified.

## Full385 content recovery, provisional handover

Current SOLUTION supersedes the previous unresolved write-up, preserved in work/kryha-decipherment/SOLUTION-before-content-recovery.md. Both full keys pass independent adjacent-hole decode/inverse encode385/385. Content is the car-purchase/loan telegram; first5 remains unexplained. Main lexical relabel oldG→X,oldQ→G,oldX→J,unusedoldJ→Q is explicitly semantically chosen, not unique model-selected evidence. Word-internal I/J and sentence J are editorial hypotheses. All physical positions are decoded; old20/10 framing withdrawn. Raw, editorial, translation, source hashes, pixel manifest and comparison are retained separately. No register entry for this partial claim; outside Claude review is required. No watcher/reviewer launched.

### Post-recovery source correction before handover

Independent Sol6.1 offline pixel check and main reread agree351240J (not priorU). Defaultcollated transcription corrects it; priorstrong archived separately, source unchanged.351231I is a weaker foot-obscured alternate, neverdefault.35186R preferred; oldstampmoderateP is notpreferred evenifprosebetter. Correspondingrawtext+variantcounts in SOLUTION updated; explicittranscriptionhashguard added. Fresh language-stage controls condition onO/ΔK, not an end-to-end full-ring ciphertext-only claim. Prefix alternatepress/reset scouts remainambiguous; publicportal Cipher Keys metadatafilterSOSOL/Kryha showednorows.


## Review1 addressed

Claude Opus5.5 verdict **REVISE**, expressly upholding the decipherment and requiring no second round unless the key changes. All numerical key fields are unchanged; only three source readings and documentation changed. The350 general findings are addressed in both reports.

1. **11/12:** source reinspection prefers PMQKK: printed P lacks a securely separate R leg and the outer strokes support M, while the blue stamp crosses both. Adopt11P/12M, agreeing with the independent pre-recovery blind reading. The raw opening becomes ZMNOHYCHMOZNOSTTI. R/W remain obscured alternatives in the DONE1 snapshot; this reinspection is not blind.
2. **86:** retain R because a diagonal leg is visible. Explicitly disclose P as the blind-reader and grammatical alternative: R gives PSEDAVAIUCI, P gives PREDAVAIUCI. The latter remains in the older moderate variant, not silently imposed.
3. **231:** adopt I as the reviewed default, with the straight stem and independent blind agreement; a lower-foot watermark leaves L as an alternative. Raw EXIITUIE becomes EXISTUIE under the unchanged key.
4. **73:** retain O: closed oval, raw SUVELMI. Blind U was uncertain and gives SLVELMI.
5. **Offset:** relative to350,351 has an extra T at position21 (MOZNOSTTI) and lacks E in final ROZHODNUTIE, giving ROZHODNUTI. This explains the +1 body alignment and return to alignment for final DOTROCHDNI. These are literal differences, not proof of where an error arose.
6. **Date:** source postmark reads −2 III44−23 and handwritten816/1229. Thus arrival appears2March1944, conflicting with portal1944-11-03; dispatch day is not thereby proved. SOURCES and report now state the conflict explicitly.
7. **Attribution:** earlier GPT-6 Astra produced unresolved attempts; GPT-6.1 Sol subagents recovered the cycle/working key/language and performed audits. Main OpenAI GPT integrated the result and selected rare-label semantics. Claude Opus5.5 supplied the paired-period lead and independent review. Historical NOTES header is clarified rather than relabeling earlier work.

Post-review source corrections and raw snapshots are explicit; no numerical key field changed. Final report retains the full literal output and uncertainties. No watcher/reviewer started.

Final verification: all5 decoder variants retain385 positions; collated reproduces DONE1 output exactly; only351 glyphs11/12/231 changed. Numerical key fields and original source SHA-256 values unchanged. Claude independent decoder rerun read-only reproduces both reviewed outputs and reencryption385/385; output retained in batches/kryha-review1-main/independent-post-review-output.txt. All6 rendered PDF pages visually inspected, no clipping or overflow. Editable source and builder accompany each final PDF.

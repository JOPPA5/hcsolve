# HC350 solver log — historical Astra attempts; content recovery with GPT-6.1 Sol

2026-10-11. Two originals supplied from parent browser capture copied unchanged. All tabs had been read by parent. Status Not solved; tag Unsolvable and description indecipherable. These are archival classifications, not a mathematical proof. No watcher used, per explicit user override; external reviewer is managed by parent.

## Transcription and structure
Manual transcription in work/transcription.txt, with eight physical cipher lines (six on image1, two on image2),77groups385letters. This matches printed body length385. Excluded routing/signature HOLAKOVI, CIEKER3001 and ordinary telegram addresses. No attached transcription. Paper heading also contains85/84 in word-count area; not treated as missing-letter evidence. Several uncertain type characters remain: first-page groupEWRTH, DWXTI, IMIRM and last group on page2HWUTS, along with I/L/J ambiguities. Source images control all readings.

## Reproducible attempts
`sh ciphers/hcp-350/work/reproduce.sh` reproduces attacks from work/cipher.txt and stored quadgrams, plus source corpus in393 for unigram model. No full plaintext command exists.

1. Frequency/period analysis: length385, IC0.039028679653679656, close to uniform26letter value1/26. Period-averagedIC1–30 has no compelling low-period peak. This favors considering polyalphabetic systems over ordinary transposition but does not establish any system.
2. Hypothesis-only visible-name keys HOLAKOVI, CIEKER, MADRID, BRATISLAVA in ordinary Vigenere, Beaufort and variant Beaufort:12candidates, none readable. Visible words are not claimed to be keys.
3. Ordinary Vigenere key estimates for periods1–30, maximizing per-column Slovak unigram likelihood from the preserved UD Slovak corpus: no coherent full plaintext. Not exhaustive key search.
4. Monoalphabetic substitution, both forward and reversed:100restarts x50000proposals for each direction, deterministic seed374 inherited from350's copied374 script. Fourgram scoring from393. Best scores-803.253 and-799.81 are incoherent, not decryptions. Scores are uncalibrated heuristic sums.

Kryha is a historically plausible Madrid cipher in1944 based on Antal et al.; machine settings and identification remain unknown. Could also include transmission/key error, but neither is established. No source solution found; no recovered key, plaintext or solved claim. No markers or register entry.

## Cross-message mechanism analysis:350 against351
Read351 only; no source or working file in351 changed. Reproduction: `python3 ciphers/hcp-350/work/compare_kryha.py`; output work/compare-kryha-results.txt. The script reads current351 transcription, so future corrections may alter exact figures.

### Headers and date evidence
351 image postal stamp appears `2.III.44` and transmission line ends `...85/84 1 2200`; the body reference is3002, immediately after350's3001.350 transmits day28 at1445 and portal dateFeb28. This supports a possible March1/2 follow-up rather than portal351'sNov3, but remains a source-reading inference. Portal metadata retained unchanged.351 routing word appears SOLAKOVI whereas350 appears HOLAKOVI; possible transmission/read differences. Both are8letters, not a six-letter key indicator. All cipher groups have5letters and there is no visible six-letter prefix or explicit300letter paragraph boundary. Pasted strips alone are ordinary line wraps, not evidence of a machine reset.

### Quantitative relation
Both have385letters. First20positions share16letters; final10share9. Identical first groupSOSOL, fourthEWRTH and finalHWUTS; second and penultimate groups differ by1letter. Interior positions20..374 (zero-based,355letters) share only2, against13.608 expected for independent letters with observed marginals. A5000shuffle diagnostic gave no equal-or-lower result (plus-one tail estimate1/5001); this is exploratory with visually selected boundaries and tentative transcriptions, not a calibrated historical conclusion. The contrast suggests related framing and/or constrained relationship, rather than two wholly unrelated uniform strings. It does not prove equal plaintext or retransmission.

### Genuine Kryha discriminator
For the original fixed17step Kryha, if both messages encrypt the same aligned plaintext with shared ring alphabets and only selector phase/initial setting changed, each position modulo17 must give one fixed bijection between their ciphertext letters. In the355letter interior there are129pairs sharing the same first ciphertext letter and phase; only4also share the second. Random shuffle expectation is5.017. Thus this restricted common-key/same-plaintext explanation is contradicted far beyond a few glyph errors. Checking periods1–40 similarly finds no near-consistent mapping. This does not exclude different alphabets, different plaintext, inserted/deleted characters, or the later adjustable model.

Separately tested the original published17step displacement sequence7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9. Cumulative positions modulo26 identify repeated machine alphabets without knowing either mixed ring. Pooling within those positions over each of17selector phases yields maximumIC0.04948 for350 and0.04427 for351, both at phase2relative to the chosen interior start. Against1000shuffles taking the maximum over17phases, tails are0.0909 and0.6723: no compelling evidence for this fixed schedule. These statistics alone do not mathematically exclude it; ring settings never recovered.

The primary historical description also distinguishes a later adjustable52stop mechanism with different possible step sequences. Our17step tests do not address its unknown screw settings. A defensible next step is to locate the actual Madrid machine/control-wheel instructions or an independently known-plaintext companion; testing all unknown modernized settings would be a different attack. No supported plaintext gained.

### Explicit transmission-shift check requested by parent
`python3 ciphers/hcp-350/work/align_pair.py` outputs work/alignment-results.txt. Exact Levenshtein distance is320for full385letter streams and315for355letter interiors. One optimal full alignment uses272substitutions,24insertions and24deletions (89matches); the interior uses267substitutions,24insertions,24deletions (64matches). This is not a small missing/extra-letter repair.

Interior offset+1is the strongest among−20..20, but only28/354matches(7.91%); offset0has2/355. Initial exploratory−100..100also had+1as strongest by count. Exact shared five-letter groups are onlySOSOL,EWRTH,HWUTS at the framing positions. Difflib longest exact interior blocks are only3–4letters; no long shifted passage is concealed by the same-position comparison. Source glyph corrections may alter isolated matches, but the present transcriptions do not support a simple shifted-copy telegram. The modest+1correlation is insufficient to identify a mechanism. No new cipher or plaintext claim.


## Continued paired-message test for adjustable schedules

`python3 ciphers/hcp-350/work/adjustable_phase_test.py` extends the necessary phase-bijection test to every stop count1–52. Same aligned plaintext, same ring alphabets and same repeating step schedule imply a fixed ciphertext-to-ciphertext bijection in each residue, even with different wheel phases. No actual step values are assumed.

52 independent phase-bijection controls all passed exactly. Literal355-letter target interiors fail at every period1–52. At52:38 repeated-input and38 repeated-output pairs, only2jointmatches;36violations each direction. Least-conflicting51 still has30input/36outputviolations. Full outputs in adjustable-phase-results.json.

This contradicts only the stated restricted shared-key/same-plaintext explanation on currenttranscriptions. It does not exclude adjustableKryha with differentplaintext/rings/schedules or errors, and produces no plaintext. Earlier source wording originalbytes means acquiredbytes preserved; scans are displayedlargeconversions, not original-resolution uploads.

## 2026-10-11 — GPT-6.1 Sol exact direct re-encryption test

Parent proposed a NEW conditional hypothesis: the literal 355-letter middle of351 is encryption of the corresponding middle of350, treating350 ciphertext as arbitrary known input. This differs from previous same-natural-plaintext/shared-ring tests. No historical re-encryption premise or recovered natural-language plaintext is asserted.

### Exact model and matched controls

`python3 ciphers/hcp-350/work/reencrypt_kryha.py` uses Z3 (session installation `/private/tmp/hcsolve-z3`) and writes control/results JSON plus progress output if redirected. It reads350 and351 transcriptions but writes ONLY350/work. Extracts zero-based[20:375], leaving355symbols in each. Uses original published17step cycle[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]. For every phase0–16 and displacement direction±1, unknown input/output ring positions are two permutations of0..25. Each input/outputpair requires `O[output]-I[input]` congruent to cumulative displacement modulo26. `I[a]=0` fixes equivalent global rotation; arbitrary initial rotation is absorbed by the outputring. Displacement starts0 at the middle's firstcharacter; scanning all phases handles its relative wheel position. No printedheader is assumed to give machinephase.

A355symbol synthetic positive control uses350middle asinput, independent mixed input/output rings, phase6 and direction−1. Solver recovers both exact planted rings up to the fixedglobalrotation and reproduces all355outputsymbols. A separate control substitutes outputletters atpositions31/167/302; exact Boolean error budget `PbLe(errors,3)` recovers the same planted rings and exactly those3positions. Control JSON preserves input/output, both planted rings, normalized recovered rings and reproduction. These are synthetic known-input encryption controls, not historical plaintext/key claims.

### Target outcome and scope

All68 literal-target tests (17phases×2directions×budgets0/3) return UNSAT, none UNKNOWN. Total solver-check time approximately0.74seconds in this run. As an independent necessary-condition diagnostic, repeated identical input/output letterpairs requiring different displacements would need at least79–84badpositions for every phase/direction. This lower bound is far above3; it cannot be repaired by a few glyph corrections. The actual rejection uses full exact permutation/error-budget constraints, not just heuristic scoring.

Therefore the current aligned transcriptions contradict DIRECT re-encryption350middle→351middle by the ORIGINAL FIXED17step Kryha with two arbitrary mixedrings and atmost3erroneous alignedpositions. This does not reject later adjustable52stop Kryha, an unknown different steppingcycle, a machine reset within the middle, extra substitution/transposition, arbitrary inserted/deleted symbols, or many transcription errors. It produces no natural-language plaintext and establishes no actual cipher family. It is not a solvedtelegram; noDONEmarker/report/registerentry. Source remains unchanged, no watcher started.

## 2026-10-11 — GPT-6.1 Sol arbitrary periodic re-encryption, periods1–52

Extended the NEW direct350middle→351middle hypothesis to UNKNOWN repeating displacement increments, periodT from1through52. Every increment is unrestricted0..25. This is a SUPERSET of constant unknown periodic selector schedules, not a claim that these increments match historical52stop pin/gear settings. Actual mechanical restrictions have not been established. Both ring alphabets remain arbitrary26permutations. Phase is absorbed into the unknown cyclic step array; direction is absorbed into signed/mod26 increments. An arbitrary starting relative ring offset is absorbed into the output ring.

### Exact periodic model

If increments repeat withperiodT, cumulative displacement atpositioni is `R[i mod T]+floor(i/T)*S mod26`, withR0=0 andS=sum ofonecycle. Conversely everyR/Sassignment yields a repeating increment array (successiveRdifferences and finalS−R[T−1]). Thus the known-input/output constraints are homogeneous linear equations modulo26:
`O[y_i]−I[x_i]−R[i mod T]−floor(i/T)*S = 0 mod26`.
`I[A]=0` normalizes simultaneousrotation. This uses all355literalalignedpositions[20:375]. Source files and351work remain unchanged.

The first directintegerZ3version in`reencrypt_periodic.py` timed out on itsfirstunknownperiodcontrol (UNKNOWN;60second timeout); it therefore ranNOtargetsearch and suppliesNONEof the rejection evidence. This limitation is preserved in`reencrypt-periodic-controls.json` and progress.

### Independent algebra and exact controls

`periodic_algebra.py` solves the homogeneous system independently by RREF overGF2/GF13 and CRT, enumerating remainingnullspaceparameters and requiring both reconstructedrings to be26permutations. Generated355symbol controls use350middle asarbitraryknowninput, independentseededmixedrings and arbitrary independentlygeneratedstep arrays atT17/26/52. Each control hasnullity1inbothprimecomponents afterrotationnormalization and recovers a validring/schedule representation reproducingALL355outputs. Unitmultiplication modulo26 creates equivalent representations; recovery is not claimedunique. Files`periodic-algebra-controls.json` discloseplanted/recoveredparameters.

LiteralTARGET:ALL52periods haveNULLITY ZERO inBOTHprimecomponents. Only thecollapsedzero-vector solution remains, incompatiblewithringpermutations. Exact no-error rejection completed inabout1.74seconds total. No heuristic scoring or unknowntimeout is interpretedasUNSAT.

### Exact three-error certificate

`periodic_three_errors.py` allows up to3arbitrarybadalignedpositions. It constructs theGF13linear code of equation residuals, using an invertibleindependentrowbasis and a systematicparitycheckmatrix. Inverseverification assertions check bothidentity and originalbasis×inverse. Normalizationrows areNOTeligibleerrors. It exhaustively tests everypossible support ofweight≤3 through systematiccases: onlynonbasisunitcolumns; onebasiscolumnplus≤2unitcolumns; twobasiscolumnsplus≤1unitcolumn withall12nonzero fieldratios; andthreebasiscolumns with exact2×2minor coefficient recovery andfullcolumn verification. This is an exact finiteerror-budget UNSATcertificate for a RELAXATION of thefullringmodel, rather than MaxSAT or heuristic typo guessing. Any valid ringpermutation has a nonzeroGF13coordinatevector; if thatvector violated≤3equations, its residual wouldbe a nonzerocodewordofweight≤3. No suchcodewordexists atANYT1–52. Hence thefullarbitraryperiodicringmodel is also impossible with≤3badpositions.

Matched3typo controls atT17/26/52 identifyexactactualpositions31/167/302, thenindependentCRT/ring recovery afterexcludingonlythosesupportpositions reproduces theENTIRE underlying355symbolcontroloutputs. Controlresults include bothsparsecertificates and recoveredunderlyingrepresentations. Alltargetperiods output`NO_CODEWORD_WEIGHT_LE3`;0inconclusive. Targeterrorcertificates takeabout7.6seconds total.

Reproduce:
`python3 ciphers/hcp-350/work/periodic_algebra.py`
`python3 ciphers/hcp-350/work/periodic_three_errors.py`
RequiresZ3onlybecause sharedinput/helpermodule imports it; the evidence-producingalgebra is finite-field Python and doesnot dependonZ3search. SessionZ3installationpath is disclosed inscripts.

### Exact scope

This refutes DIRECT ALIGNED re-encryption of350's355lettermiddle into351's by arbitrarymixedrings and UNINTERRUPTED PERIODIC ADDITIVEsteps ofperiod≤52, evenwith≤3erroneouspositions. It doesNOTrefute insertion/deletion, unknownalignment, machine resets, period>52, nonperiodic/other steppingmechanisms, additionaltransformations, manyerrors, or encryptionofdifferentnatural-languageplaintexts. No physicalKryha identity, dailykey, or historicalplaintextis recovered. NoDONEmarker/watchers/registerentry.

## 2026-10-11 — GPT-6.1 Sol ciphertext-only original17step two-ring attack

This tests the actual ciphertext-only task, separately from the paired known-input/output rejection. Assumed originalfixed17step schedule, arbitrary mixedinput/output alphabets. For givenphase/sign, decrypt `inputSlots[(outputPosition[c]−cumulativeShift) mod26]`. Alternating simulatedannealing swaps the26inputslots or26outputpositions, with occasional ringrotations. `ring_attack.cpp` uses trainedSlovakquadgrams. Neither historicaltype nor phases are established.

### Independent held-out385letter control

`ring_control.py` splits the shared public UD SNK corpus by complete sentences:6786training,1697heldout. Prepared sentences removeaccents, spell decimaldigits independently, delimit PROPNtokens withQ, and appendXsentence markers. This is an explicitly disclosed control-preparation convention, not a proved mandatoryKryha convention. The385lettercontrol is taken ONLYfrom heldoutpreparedsentences and independentlyencrypted withrandommixed26rings, phase6/sign−1. Nocontrolplaintext is a targetcrib. Models include unigram/quadgram/5gram files withtrainingheldout separation.

Controlcontains noF/W, so theirinputringpositions are intrinsicallyambiguous. Criterion is a completevalid26ringrepresentation producingEXACT385plaintext, not uniqueness of everyplanted unusedcoordinate.

Even withcorrectcontrolphase/sign supplied, baseline two-ringblind100restarts×100,000proposals recovers only62/385positions, score−224.794 versus truequad659.125. A justifiedprogressiveunigram→quad/5gram objective,150restarts×100,000proposals, recovers70/385, notexact. Thus TWOUNKNOWNRINGattack isNOTvalidated; no general two-ring targetsearch or negativeconclusion is inferred from thosefailures.

### Limited known-output and A–Z-output family

`ring_attack_known_output.cpp` fixes theoutputring, recovering theinputring by20restarts×50,000proposals. Withthe independentlyplanted outputring GIVEN, it recoversall385controlplaintextsymbols exactly. This validates a STRICTLYLIMITEDone-unknown-ringattack and inverse/scoring, not theblindgeneralcase.

`ring_az_sweep.py` re-encodes thecontrol into the explicitlyfixedA–Zoutputring family. Forprefix-removals0/5/20, matchedcontrols oflength385/380/365 ALL recoverEXACTplaintext with phases shifted appropriately and unknowninputring (initial relativeoffsetabsorbed ininputslots). OnlyafterALL3controls passed was theboundedtargetA–Zfamily tested. The17phases×2signs×3prefixchoices doNOTcover arbitraryunknownoutputringpermutations. Statisticaloptimization is not exhaustive; failuredoesNOTmathematicallyexclude eventhislimitedfamily.

Reproducegeneralcontrols:
`python3 ciphers/hcp-350/work/ring_control.py`
`c++ -O3 ciphers/hcp-350/work/ring_attack.cpp -o ciphers/hcp-350/work/ring_attack`
`ciphers/hcp-350/work/ring_attack ciphers/hcp-350/work ciphers/hcp-350/work/ring-control-cipher.txt 6 -1 100`
Forprogressiveversion compile/run`ring_attack_progressive.cpp` with150restarts and finalargument`five`. ForlimitedAZsweep compile`ring_attack_known_output.cpp` andrun`ring_az_sweep.py`. Allplanted/recoveredkeys andcandidateplaintexts retainedinwork; no sourceediting/watchers/reviewhandover.

AZtarget sweep completed102cases. Bestnormalized candidate isprefix20/phase15/sign+1, rawscore−710.978, incoherent (`badvneqqcemalrlqixgpdrvqjfnhtibysq...`). Other topcandidates are likewise incoherent. Fullkeys/outputssavedin`ring-az-target-results.json`; summary`ring-attack-report.json` separatesallcontroloutcomes. No supportedplaintext/key recovered, noDONEmarker. These are controlledbounded attempts ononeoutputringfamily; thegeneral two-unknown-ring problem remainsopen.

## 2026-10-11 — GPT-6.1 Sol structural projected-IC control BREAKTHROUGH

A materially different ciphertext-only attack bypasses the blindtwo-ringSA basin. At fixedphase/sign, count cipherletters against cumulativeoffset modulo26. For outputpositionsO, project eachsymbol into `(O[c]−offset) mod26`; unknowninputring onlypermutesthese26symbols, preserving theirfrequencyconcentration. OptimizeO alone by sumprojectedcounts² (equivalenttoIC forfixedlength), with cheap26bucketdeltaupdates forposition swaps. KeepdistinctOsolutions normalizedbyO[A]=0 (globalrotation gauge). Then solve eachprojectedsymbolstream asordinaryMASC, rankONLYbytrainedheld-out-control-independentSlovakquad score, and seedjointtwo-ringrefinement from thetoplanguagecandidate. Truecontrol plaintext/ringcloseness is DIAGNOSTICONLY, NEVERoperative selection.

### Calibration and exactcontrol recovery

`ring_ic.cpp`:3000restarts×10,000proposals, retainup to300normalizedoutputpermutations. The385letterheldoutcontrol trueconcentration9267 (IC0.06007846) outranksALL10,000independentrandomoutputpermutations (range5831–6949,mean6196.59). However ALL251retainedoptimizedoutputrings scoreHIGHER9299–9801; ICobjectiveoverfits sampling, so itsmaximizer alone is NOTthekey. Closestretainedcontrolring matches20/26positions upglobalrotation (diagnosticonly).

`ring_ic_masc.cpp`: eachretainedO gets8restarts×30,000MASCproposals. OperativeLANGUAGE ranking selectedICcandidateindex149, whosepartialcontroloutput matches269/385. `ring_ic_refine.cpp`:8restarts×100,000jointproposals fromthat seed. FIRSTlanguage-rankedseed recoversEXACT385/385controlplaintext and both26ringpermutations upglobalrotation. Bothplantedinput/outputringvalues happen to matchall26positions afterrotation. F/Wareunusedinputletters, so theirpositions remaininherentlyambiguous; uniquefullkeyidentification is notclaimed. IndependentPythonencryption reproducesALL385controlciphertextsymbols. Verificationfile`ring-ic-control-verified.json` disclosesindex149,seedrank0,andallchecks.

This is theFIRSTvalidatedblindtwo-ringciphertext-only method inthiswork, for thegivenoriginal17steps andcorrect suppliedcontrolphase/sign. Validation doesnotestablish350'shistoricalmechanism orguaranteeeveryothercontrol/phase. `sh ciphers/hcp-350/work/reproduce-ring-ic-control.sh` reproducescorpusheldoutsplit,trainedmodels,ICcandidates,10k-nullcalibration,MASC-rerank,jointrefinement. No publishedtargetsolution/targetcrib wasused.

### Targetfull385firstpass and performance-preserving batching

`ring_ic_target.py` appliesthesamegenericICbudget,ALLretainedcandidateMASCbudget,LANGUAGE-onlyrank,andjointrefinement fromTOPseed across17phases×bothdirections,fullbaseline385cipherletters. Allcandidatesindependentlyre-encryptthecompletebaseline; thattautologicalkey-fitcheck alone doesNOTprove meaningfulplaintext. Further39language-rankedseeds areretained ifjustified by initialoutcomes; theobserved successfulcontrol usedonlytopseed0.

Initialphase0−/phase0+ finishMASC−483.08/−483.381 andjoint−443.727/−417.174, incoherent. No sourcecorrection orkeyclaim. Parentvisualreread flaggedgroup3PMQKXpossiblyPMQKK; baseline ispreserved, no mid-runtranscriptionchange. Anyfuturevariant must beseparate andindependently checked.

Legacy per-candidateMASCprocesses loadedmodelsrepeatedly. `ring_ic_masc_batch.cpp` precomputesprojectedindices, computesidenticalquadindicesdirectly,loadsmodelonce,andRESETStheoriginalRNGseedforEVERYcandidate. First3completecontroloutputsareBYTEIDENTICAL, includingplaintext,score,andkeys (`ring-ic-batch-verification.json`). Budgets/objective/selectionunchanged. Targetrunwasgracefullyinterrupted forbatchresumption; completedphase0± and existingcompletedMASCfiles arenotrepeated. Originalrunner retainedas`ring_ic_target_legacy.py`. Workingsource/cipherbaseline isunchanged.

### Completed full385 sweep

All34 requested phase/direction runs completed: phases0–16, signs−1/+1. Each retained300 normalized IC candidates (10,200 total), each received8×30,000 MASC proposals, and its highest LANGUAGE-ranked seed received8×100,000 joint proposals. No true-key selection was used. Best MASC score−455.784 (phase4,+1); best joint score−417.174 (phase0,+1). All34 joint outputs are incoherent; no supported historical plaintext or key was found. Independent re-encryption checks cover all385 literal baseline letters for every final candidate, but such key-fit checks cannot establish linguistic correctness. The exact matched control scored659.126 and recovered385/385.

The sweep is a bounded heuristic failure, not a mathematical exclusion of original17step Kryha. Opposite signs with arbitrary mixed rings are equivalent under reflecting both ring-position systems; the34 runs provide17 phase families and different optimizer trajectories. Only one top language seed per case was refined, as in the successful control; further ranked seeds remain saved. Group3 transcription ambiguity was not altered. Results: work/ring-ic-target-summary.json, work/ring-ic-target-report.json, and per-case directories. Reproduction runner: python3 ciphers/hcp-350/work/ring_ic_target.py (resumes saved completed runs). No DONE marker is justified.


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

Claude Opus5.5 verdict **ACCEPT**. Its independent decoder reproduces all385 letters and re-encrypts them exactly. The review also compares a pre-recovery blind transcription: it agrees with all four350 corrections and independently supports the recovered content. The reviewer supplied the original paired-period lead and explicitly disclosed that limit on independence; the numerical key/content recovery was the solver team's work.

1. **Physical interpretation:** retained “mechanically consistent adjustable Kryha key”; the report distinguishes recovered rings/displacement increments from unverified original machine identification and hardware settings.
2. **SOSOL:** now described as probably an unenciphered indicator, explicitly an inference. Its meaning remains unknown and the decoder still covers all385 positions.
3. **One-stop difference:** the report notes as conjecture that replacing hole0 by48 could explain a repeat being unreadable under the other key. This is not a proven historical error.
4. **Garbles:** the report compares raw350 DRAAE/POPROT/PRISTUPIK with351 DRAHE/POPROS/PRISTUPIT, preserving all clear source letters. Also discloses350 PREDAVAIUCI versus351 PSEDAVAIUCI (sourceR/P alternative).
5. **Outcome:** now states content and working key recovered, while keeping original procedure, first group and rare-label ambiguity open. No register entry for the remaining partial historical claim. Earlier raw snapshots remain reproducible.

Post-review source corrections and raw snapshots are explicit; no numerical key field changed. Final report retains the full literal output and uncertainties. No watcher/reviewer started.

Final verification: all5 decoder variants retain385 positions; collated reproduces DONE1 output exactly; only351 glyphs11/12/231 changed. Numerical key fields and original source SHA-256 values unchanged. Claude independent decoder rerun read-only reproduces both reviewed outputs and reencryption385/385; output retained in batches/kryha-review1-main/independent-post-review-output.txt. All6 rendered PDF pages visually inspected, no clipping or overflow. Editable source and builder accompany each final PDF.

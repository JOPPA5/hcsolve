# HCP-364 attempt log

## Source and transcription

The rendered portal says Not solved and tags the record Unsolvable. The image is a displayed large conversion, not an original-resolution upload. The portal identifies message 67/1944, but the scan contains a proposed outgoing reply and the outgoing ciphertext headed 1170, associated with Holák's message 80149. The note about a missing number concerns the incoming message; it does not establish that this outgoing ciphertext cannot be deciphered.

The main solver and a second reader independently read the same 14 groups (70 letters). This is our transcription, not a portal transcription. Possible glyph alternatives remain in group 7 (I/L), group 8 (M/N), group 10 (initial C/E, watermark overlap), and group 12 (U/V). No letters were changed to fit a proposed plaintext.

## Conditional known-plaintext attack

The unencrypted proposed reply visible on the scan reads: “Nelúštiteľné. Neudal si číslo pred textom. Viď bod tri pokynov. Uveď číslo.” This is source context, not recovered plaintext. Its accent-free letters total 60. A preparation with four sentence-end X characters and one unknown final filler totals 65, compatible in length with removal of one five-letter indicator from the 70-letter body.

The literal inventory lacks one N, E and V relative to the 60-letter quote. Removing group 3 ITPKA leaves corresponding excess C, M and U, plus X characters and R. This motivates a bounded error-tolerant test but does not justify correcting the transcription.

`work/known_quote_test.py` exhaustively assigns expected plaintext columns to ciphertext chunks for widths 2–22, both whole-stream directions and each of 14 possible indicator removals. It tolerates at most three substitution errors and uses a state cap. All 588 target cases finished below the cap; none matched.

A separately planted 65-letter width-21 control with three injected errors recovered the exact original key in 22 states. This verifies this narrow conditional test. It excludes only the tested single-columnar preparation within the error bound; it does not exclude triple transposition, another preparation, another plaintext, or more transcription errors. No recovered key or plaintext exists.

Reproduce from repo root: `python3 ciphers/hcp-364/work/known_quote_test.py`.

No DONE marker or register entry: the attempt remains open and unresolved.


## Continued work: optional punctuation and exact cascade constraints

`python3 ciphers/hcp-364/work/preparation_variants.py` tests all sixteen subsets of four optional sentence-end X characters, with unknown suffix padding to65 letters. All9,408 indicator/direction/width2–22 cases completed without matches at the three-substitution bound; every preparation passed an independent width19 control. These remain conditional crib tests.

Installed standard PyPI z3-solver5.1.0.0 in /private/tmp/hcsolve-z3. work/constraint_transposition.py exactly models cascaded irregular columnar permutations. Independent65-letter double controls recovered original keys for widths5/6,13/13,16/17 (15.772s for16/17). Triple13/13/13 array-model control timed out20s; no target exclusion follows.

Raw target omit3 under fixedfour-X preparation and <=3errors timed out55s at widths16/17. A hypothetical glyph variant TSMND→TSNND,CLOEN→ELOEN,ERCUU→ERCUV, zero further errors, was UNSAT in9.243s. Source/literal transcription unchanged; variants are assumptions. Double13/13 rawtarget timed out20s. JSON outputs preserve results. Manual1939 example keys21/19/20 tested all admissible same/progressive alignments, omissions/directions: closest quote distance52/64; not established1944 keys.

Sol6.1 helper's alternative Boolean exact-cover model in batches/constraint-sol61 recovers quote+r double16/17 in0.244s and triple13/13/13 in3.68s, exact planted keys and re-encryption. Inventory constraints reveal the three-error budget saturates N/E/V deficits, restricting replacement letters and unknown filler. This reduced rawdouble16/17 to UNSAT0.643s; it supersedes the earlier timeout for that particular model. Further49width-pair controls and target tests are ongoing. None is a decipherment.


## Complete double sweep and alignment controls

The independent Sol6.1 Boolean exact-cover run completed all49 ordered double width pairs16–22. All49 controls re-encrypt exactly (46original keypairs,3equivalent keypairs). All49 rawtarget cases at<=3errors and49explicit glyph-variant cases at0errors are UNSAT. All16 alignmentsn1–16 of equal-width triple16/16/16 also passed matching controls; all32target cases are UNSAT. A same-family unknown-filler/three-error triplecontrol recovered original keys, fillerR and exactly damagedpositions0/2/3 in4.86s. All are narrow conditional exclusions, never recovered text.

An eagerSAT backend recovered an unequal aligned16/17/18 n11 control exactly in59.38s; both corresponding targetcases timedout60s, so neither is rejected. A separate main CP-SAT interval/NoOverlap encoding (`work/cp_transposition.py`, OR-Tools9.15.6755 staged in /private/tmp/hcsolve-ortools) timed out on its different independently planted unequal n11control at20s and55s. It has not been used to exclude targets. Logs preserve these failures. Official API source: https://developers.google.com/optimization/cp/cp_solver .

Public HC Portal cipher-key catalog was checked through renderedUI, All319records andFullFilters; no displayed metadata matchedSlovak/MZV/Bratislava/1938–1945/Kryha/SVERK. This does not establish absence of archivalkeys. Evidence in batches/portal-key-catalog-check.json. No published targetsolution was read.


## Exact multistage quote checks (main synthesis,2026-10-11)

IndependentBoolean exact-cover double-transposition controls passed all49ordered width16–22pairs; both targetreadings were UNSAT in all98conditional cases. Equal-width16triple with all16possible sharedrotations recovered control plaintext/keys and gave32UNSATtargets. Unrestricted13³blind control recovered keys; bothconditionaltargets UNSAT. Unrestricted11³glyphreading UNSAT, raw≤3UNKNOWN. Otherblindcontrols12/14/15 and17–22 timedout; this is a solverlimit, not ciphertext exclusion.

A distinct unequal16/17/18 sharedn11 control recovered exactkeys in59.38s. Both conditionaltargetreadings remained UNKNOWN after600s each. Exploratory equal17–22sharedn11 targetcases all12 UNKNOWN60s. Sixknown-key encoding checks SAT only validate encoding, notblindkeyrecovery and nottargetsolutions. These targettests all assume the visibleproposedreply as plaintext, omitindicatorgroup3, fixedsentenceXpreparation, and particularliteral/glyph/errorbranches. Noactualkey orplaintextwitness. Model-conditioned UNSAT is not a claim of historicalunsolvability.

Fullscripts/logs/reproduction and explicitassumptions: `batches/constraint-sol61/SUMMARY.md`, `double-sweep-tight.jsonl`, `regular13-targets.jsonl`, `sustained-unequal.jsonl`, `exploratory-equal-targets.jsonl`. Furtherlowwidthgeneric cases mayappendthere. NoDONE orregister.

## Primary published R-key reuse hypothesis
Main solver tested physical label arrays21/19/20 from independently verified HistoCrypt2020 workedexample, all221 valid constant/progressive dailyalignments and6stageorders. Across11ciphers322explicit cases (including separate numeric-header removal for393/371/399), no winning whole plaintext is coherent. Two fresh heldout115/100controls exactrank0; all retained whole key/plaintext pairs independently reencryptionexact. Reuse of that historical key on our target date is unsupported, so failure excludes no unknown-key R cipher. Full arrays, hypotheses, literal erasures/header handling, sourceprovenance and reproduction: `batches/r-published-keys/REPORT.md`. No source change/marker.

### Primary21/19/20 widths: exact conditional sweep complete (2026-10-11)

GPT6.1Sol completed74distinct conditionalquote cases: constantdailyalignment1–19 andprogressive1–18, rawinventorywithin3errors andexplicitglyphinventoryzeroerrors, presumedomitgroup3 and64-letter coverquote+oneunknownfiller. ExactlytwoUNSAT: constantn1bothreadings, additionally verified by solver-free invariant: all3columnsstartatphysical0 and must preservefirstN, whereas sourcebeginsI; underthatcondition minimuminventoryerrors4raw/2glyph exceedbudgets3/0. Other72casesUNKNOWNat60seconds; noSAT/plaintext/keywitness. All37fixed-keyencodercheckspass, bothfresh65blindcontrolsUNKNOWN. No exclusion foranyUNKNOWN, nor proof ofquote/alignment/filler/indicator. Fullreport: batches/r364-primary-sol61/README.md, summary.json and first-alignment-independent-audit.json.

### Direct known-plaintext three-key Hungarian search (2026-10-11)

GPT6.1Sol tested a new stochastic alternative to exactSMT, at widths21/19/20: Hungarian physical-column assignment separated byheight, long/short chunkpatternflips, jointannealing andordinarykeys swaps. Three fresh65-letter random-key controls,200×5000proposals each, fail at48/65,48/65,49/65. All saved complete3keypredictions independently reproduce/invert,300exhaustive smallHungarianchecks pass; known-keyconsistency is notblindrecovery. No targetrun underfailedcalibration. Full evidence batches/r364-key-search-sol61/REPORT.md.

### Exhaustive210 long/shortpattern coordinate improvement (2026-10-11)

The stage21 Hungarian update now enumerates all210lengthpatterns underfixedotherstages, a genuinealgorithmic improvement overlocalpatternflips. Originalcontrolseed201andfreshseed204/fillerC,60×1000outerproposals, bothfail45/65. Fullthree-keypredictions independentlyreencrypt/invert. With otherstages suppliedcorrect, localupdate65/65 confirmsconsistencyonly. No targetrun; controlsprovide noexclusion. Evidence batches/r364-key-search-sol61/full-pattern/REPORT.md/results.json.

### Independent CP-SAT interval model audit and failed improvements (2026-10-11)

The main solver implemented complete physical-column intervals with NoOverlap/Element, inventory constraints and explicit daily alignment. GPT-6.1 Sol independently exhaustively checked 216 small cases against 348,192 permissible key triples: all 106 SAT and 110 UNSAT results agree, including 86 structural same-inventory negative cases. This validates the tested encoding, not historical key recovery. Blind 65-letter triple widths21/19/20 control remains UNKNOWN60s, although supplied-key consistency passes. Redundant unique-letter coordinate propagation also leaves both blind controls UNKNOWN60s. CP-SAT LNS from prior blind Hungarian candidates leaves 17/17/16 mismatches, with no improvement. No actual target was run under these failed performance controls. Full disclosure/reproduction: batches/r364-cpsat-main/REPORT.md and batches/r364-cpsat-audit-sol61/REPORT.md. No key, plaintext or new marker.

### Separate full letter-trajectory solver (2026-10-11)

Main solver replaced intermediate character variables with complete occurrence trajectories through three physical-column permutations. Final occurrence domains contain all positions of the same letter, with AllDifferent at each stage; repeated letters are not prematurely matched. A fresh7-letter small control passes with independent full encoding and position checks. Two fresh65-letter21/19/20 controls remain UNKNOWN60s each. No planted key or hint enters the blind search. This currently models fully known, undamaged plaintext/ciphertext only; no actual364 run. Evidence: batches/r364-coordinate-main/REPORT.md and controls.json. No plaintext/key exclusion or marker.


### Corrected double sweep

See `batches/r364-corrected-double-sol61/REPORT.md`: 49 ordered width pairs 16–22, both EXCUV/EXCVU alternatives, free fifth-X position, omit group 3: all UNSAT. Three fresh blind controls pass exact full encoding/inversion. This is the first valid exclusion for this precise corrected-input double family; older ERC tests do not exclude the corrected text. No historical R exclusion follows.

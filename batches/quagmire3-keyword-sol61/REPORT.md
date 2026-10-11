# Keyword-generated shared alphabet QIII — positive controls, no target solution

Two fresh genuine150position erasure controls recover all148readable plaintext letters, the exact planted keyword-generated alphabet and all absolute periodic shifts. The independently reconstructed26letter substitution maps agree with truth in every phase. ActualHCP334tests atT3/T9andallfiveFWXXerasure placements return no coherent complete readable text. This is a distinct restricted keyword family, not recovery or exclusion of arbitrary-alphabet QIII.

Model: C_i=A^-1((A(P_i)+R[i modT]) mod26). A is the SAME unknown alphabet on both sides, represented by deduplicated keyword letters followed by unused standard a–z. R consists of unknown absolute shifts, includingR0. No R0=0canonicalization was applied. Allshift classes can take0..25during search. Controls deliberately have independently sampled nonzero shifts, not zero-shift identity exposure.

Dictionary is solely normalized tokenforms andlemmas from the first6786TRAINsentences of the recorded UD Slovak corpus, keywordslength3..24withatleast3distinct letters. Exact full alphabet strings are deduplicated:18,098candidatealphabets. No target text or published solution contributes words. Corpus, dictionary, frozen TRAINunigram/4gram/5gram and source hashes are in manifest.json. Controlkeywords are independently randomized from the TRAINcandidatepool withatleast7distinct letters; neither keyword nor shifts initialize the search. Their inclusion in the declared broad dictionary is the family calibration condition, not a truth-picked candidate seed.

Fresh TESTplaintexts are150letters from held-out sentence offsets1180and1350, absent from TRAIN. Preparation follows the frozen language models: accents removed, digits spelled, PROPNQmarkers and sentenceX. Erasureindices70and94are retained, not removed; laterperiod phases never shift. Language windows containing an erasure are omitted. Original complete controls and keys are kept for after-search diagnostics only.

Fixed pipeline:
1. For every18,098alphabet, per-phase unigram likelihood evaluates all26absolute shifts using TRAINprobabilities. Then up to6coordinate passes evaluate all26shifts perclass using frozen4grams. Keep128best whole-window language candidates.
2. Refine each ofthose128shiftvectors with4starts×5000annealingmoves, including random absolute shifts and generic coordinate updates. Alphabet stays in its keyword family. Retain64best4gram candidates.
3. Refine all64withfrozen5grams,4starts×10000moves. Highest5gram score is selected. No truth- or crib-based selection; jointshift optimization remains heuristic despite complete dictionary screening.

| Independent control | TESToffset | TRAINkeyword | Readable text | Full alphabet / shifts | Seconds |
|---|---:|---|---:|---|---:|
|T3|1180|stanoveniu|148/148|exact / exact|4.726|
|T9|1350|nepovazoval|148/148|exact / exact|9.396|

Full26letter perphase map equivalence is checked, rather than accepting reencryption alone as control success. Two erased plaintext letters are still questionmarks in search outputs and are not claimed recovered. These matched controls demonstrate attack power in the selected keyword family atT3/T9, not all possible keywords/periods or historical adoption.

## Actual334branches

Working literal30group150position hypothesis is read without modification. The obscured firstslot of?DZQRremains atindex70. Each ofthefive possible insertions of?among/around the four orderedFWXXletters is tested atindices90..94; all150positions and periods are preserved. The literalWstaysW. No extra missinggroup, glyphVreplacement or arbitrary letter correction is introduced. Fivevariants×T3/T9=10branches, unchanged dictionary/models/optimization budgets. Twoindependent worker processes affect concurrency only.

| Period | Branches | Best5gram gap index / score | Selected TRAINkeyword | Coherent full readable text |
|---|---:|---|---|---|
|T3|5|0 / −575.431|nahlit|No|
|T9|5|0 (also2/3/4) / −492.46|dovolim|No|

Gap index0means?FWXX; the physically preferred missingterminalslot isgap4(FWXX?). This table ranks generic language scores only and does not select a source reading. Allwhole outputs contain widespread nonsense with incidental ordinary fragments. No historical plaintext or key is claimed. Source group length150/twoerasures, period choices and keyword protocol remain explicit hypotheses. Dictionary pruning, heuristic jointshift optimization, and imperfectlanguage models prevent an exclusion, even with two successful controls.

Each320complete savedcandidatekeys percontrol/target (128screen+128four+64five) is independently inverted, reencryped against allobserved150position strings, and rescored inPython. Across12runs that is3840savedrows. Exact key-fit on actualtarget is only model consistency; it does not validate its language. Both sourceimage hash and workingtranscription hash are unchanged. Completekeywordalphabets, shifts, allstageplaintexts, scores, selected winners and erasurepositions are retained in control/target directories and results.json/target-results.jsonl. target-summary.json preserves top3perperiod, all10branches and sourcehash checks.

Reproduce: `python3 batches/quagmire3-keyword-sol61/prepare.py` (frozen TRAINdictionary and independent controlfixtures); compile search.cpp with clang++ -O3 -std=c++17; then `python3 batches/quagmire3-keyword-sol61/run_controls.py` and `python3 batches/quagmire3-keyword-sol61/targets.py`. Runners resume saved candidatefiles. Allwrites remain inside this batch. No source/cipher/marker/reviewer/watcher operation or targetsolution lookup occurred; no process remains running.

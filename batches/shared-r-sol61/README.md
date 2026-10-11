# Conditional shared daily R keys, HCP 395/396

No target solution. No target search has been run with this uncalibrated solver. All source ciphers are read-only. No marker or watcher was created.

The primary worked example was independently checked against `batches/historical-context/r-example-verification.json`: standard irregular row write, ascending physical column label read, widths 21/19/20. Alignment rotates the PHYSICAL label array to start with label n. It is not a rotation of the sorted column reading order.

A daily base array has an exact cyclic gauge: any cyclic rotation gives identical aligned arrays for every n. Keys are canonicalized to label 1 first. This removes redundant search without assuming any target key order.

Two independent daily key sets encrypt held-out 200/50-letter excerpts at alignments 3/13 and 6/16. The UD test sentences used are absent as normalized full sentences from the training partition, have no digits and no PROPN tokens. See controls.json for exact sources and truncation. The frozen score uses original training-only 3/4/5 gram tables, weights .15/.4/.8. The sum over both whole messages gives each letter its natural contribution. No test text is added to the models.

## Reproduction

From repository root:

```sh
python3 batches/shared-r-sol61/controls.py
clang++ -O3 -std=c++17 batches/shared-r-sol61/joint.cpp -o batches/shared-r-sol61/joint
clang++ -O3 -std=c++17 batches/shared-r-sol61/compound.cpp -o batches/shared-r-sol61/compound
python3 batches/shared-r-sol61/validate.py
```

For each pair p=0,1 and diagnostic stage s=0,1,2,3:

```sh
batches/shared-r-sol61/joint batches/scoring-sol61 batches/shared-r-sol61/heldout-pair-0.input.txt batches/shared-r-sol61/heldout-pair-0.keys.txt 3 4 50000
```

Stages 0–2 deliberately supply the other two true keys; these are conditional implementation/search diagnostics, not blind recovery. Stage 3 randomizes all three keys and is the genuine discovery control. Four starts, 50,000 proposals each, fixed seed. Keys supplied for stage 3 are used only to establish widths and calculate retrospective score/matches; all three are shuffled independently before search. Truth never guides acceptance, proposal generation, ranking, or termination.

The structurally different refinement uses exhaustive arbitrary contiguous block rotations and all swaps in each physical cycle. It retains the top 12 proposed changes per stage and tests paired changes across two stages, including changes individually worse than the current candidate. This tests a wider, coupled neighborhood, not extra identical annealing restarts:

```sh
batches/shared-r-sol61/compound batches/scoring-sol61 batches/shared-r-sol61/heldout-pair-0.input.txt batches/shared-r-sol61/heldout-pair-0.keys.txt batches/shared-r-sol61/pair0-stage3.log
```

## Results and limits

Independent inverse: two held-out pairs and 72 random messages under 12 fresh daily label sets, lengths 50/55/199/200/245/250, exact. Encoder and inverse use different algorithms. Generic primary example also matches every stage in primary-verification.json.

Known-two-key diagnostics recover both full messages and the remaining key in four of six stage/pair cases: pair 0 stages 1/2 and pair 1 stages 0/2. Pair 0 stage 0 and pair 1 stage 1 fail. Thus even a single unknown stage can have a hard basin at these short lengths and irregular column sizes.

Blind three-key search fails both pairs. Highest-scoring candidates match 12/250 and 17/250 positions. Wider compound refinement remains false: 12/250 and 19/250. In conditional failed-case refinement, all stages were allowed to change, so known supplied keys could also be displaced; results remain false (13/250 and 24/250). Long near-English/Slovak-looking runs in these outputs do not establish keys or full plaintext.

Truth scores -3997 and -3879.53 are substantially above discovered false candidates (~-4888 and -4859). Observed failure is a search/landscape problem, not a demonstrated preference of this scorer for the false full solution. A high score or accidental word fragment is not a positive result.

No recovery/exclusion claim for HCP 395 or 396 follows. Shared date/channel does not prove shared keys or indicator table. Widths 21/19/20 are one historically attested example, not proved target widths. Whole 395 has 285 characters including a putative indicator; its 280-character payload exceeds the stated R recommended 250-letter maximum, with no visible source split established. 396's 50-letter minimum and absence of expected short-padding letters remain unresolved.

## Conditional indicator deductions

The original joint constraints assume a shared daily letter-to-digit indicator table and common indicator position, neither established. For these exact widths, constant n must be <=19; progressive n,n+1,n+2 requires n<=18. At candidate indicator position 6, constant alignment leaves (n395,n396)=(7,19) or (16,7); progressive leaves only (16,7). Candidate position 4 is impossible under progressive alignment. Other positions retain many possibilities. See target-conditional-scenarios.json for explicit lists; original transcriptions and constraints are unchanged.

Progressive alignment was filtered structurally only, not attacked. The tested controls use the primary example's constant n convention.

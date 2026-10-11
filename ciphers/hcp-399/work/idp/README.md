# Primary IDP and consistent-column-path control study, GPT-6.1 Sol

**Unresolved, no target attack with these methods.** Exact known-key decryption and successful first-stage reconstruction given the true second key are separate from discovering that key. The latter failed every full control here; no negative cipher-family exclusion follows.

## Primary algorithm and implementation

References: Lasry's primary [methodology thesis](https://www.uni-kassel.de/upress/online/OpenAccess/978-3-7376-0458-1.OpenAccess.pdf), book pp180–184, and official [CrypTool2 IDPAnalyser.cs](https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/IDPAttack/IDPAnalyser.cs). Downloaded code retains its Apache2 attribution. The official source adds protection against premature cycles to greedy neighbor selection. This differs from the earlier sum of independent row/column maxima.

The adapted IDP computes normalized pairwise digram scores across feasible first-stage column offsets, then greedily selects one left/right neighbor per column without prematurely closing a cycle. The final cycle edge is revisited if it was previously rejected. `reference.py` independently implements feasible offsets and repeated greedy scans; 42 random cases at lengths240/245 and first widths16–22 agree within0.00006. For negative score tables maxima start at minus infinity; the reused bigrams are frozen log-counts from primary UD TRAIN.

`idp-physical.cpp` stores ordinary encryption readout keys but applies segment moves to their inverses, the ranked keys on physical column positions. It samples4,000 random outer keys, retains64, applies left-to-right improving swaps, retains16, then does at most30 steepest improvement rounds over3,876 unique physical segment-slide/block-swap/swap transformations for width17. `idp.cpp` preserves the earlier readout-position variant and logs; it is not silently substituted for the physical version. These are bounded searches, not exhaustive outer-key searches.

## Independent full controls

`controls.py` plants20/17 double transpositions at both240 and245letters on two different texts:

- An explicitly authored diplomatic control, preserved from the earlier study, never inserted into training.
- A real primary UD Slovak SNK TEST excerpt. TEST's longest individual normalized sentence is212letters, so this is explicitly a fragment crossing sentences, not a purported whole240/245letter sentence. It excludes complete TEST sentences present in TRAIN and keeps the raw excerpt. Models predate TEST download and remain unchanged. Parameter development uses these controls; they are independent of model training, not an untouched final algorithm holdout.

Each uses a distinct seeded random key pair. `controls.json` contains all plaintexts, keys and raw provenance, with corpus hashes. `w16-controls.py` separately tests regular240 at16/17: first columns have15rows rather than12, a justified stronger-signal check, still unsuccessful in outer discovery.

Every independent known-key round trip passes. With the **true supplied second key**, `single.cpp` (copied read-only implementation from363) recovers all four full plaintexts AND first keys exactly. Its incomplete245case separates length patterns from ordering, with15,504 possible patterns. This is a diagnostic of inverse/scorer/first-stage ability; it is not a ciphertext-only double-transposition success.

## Actual key discovery results on controls

The physical IDP discovery candidates never recover the true second key. Their inferred intermediate strings reencrypt exactly, as expected of any valid key. `pipeline.py` reconstructs first keys for four outer candidates in each regular240case and one outer candidate in each245case, then `refine.cpp` alternates steepest whole-key physical segment transformations using frozen full-text3/4/5grams. Best plaintext position matches:

| Control | Best matches after full reconstruction/refinement |
|---|---:|
| authored240 |22/240|
| real TEST240 |14/240|
| authored245 |18/245|
| real TEST245 |13/245|

No result is coherent or a partial plaintext claim. For TEST245 the best false IDP7.25327 exceeds the true outer key's7.10411. This is a concrete IDP objective counterexample in this short/incomplete setting. The true authored240 score7.36303 exceeds the searched best7.11222, indicating an unresolved search gap in that case instead. These two distinct failure causes must not be conflated.

## New invariant consistent-path objective

`trigram-beam.cpp` reconstructs a **consistent complete first-column path** from sums of across-row trigram cooccurrence. A bounded beam grows paths at either end while tracking visited columns and future boundary context, rather than independently cherry-picking favorable neighbor pairs. Pure trigram beam recovers the true supplied-outer first path on authored240 but fails on the real TEST240; its bounded authored outer discovery also fails.

`multigram-beam.cpp` adds frozen3/4/5grams (.15/.4/.8) to the consistent path. Its original64-state approximation merged paths sharing only two columns at either end; logs are preserved as the developmental version. `multigram-beam-v2.cpp` correctly retains four boundary columns at each end for the5gram increments, uses16states and at most two seeds × three improvement rounds. It starts from80 random second keys plus previously searched false IDP candidates, **never true keys**. Both supplied-true-outer240first paths recover exactly. Full outer discovery still fails: authored240 candidates15/240and13/240; real TEST240 candidates12/240and13/240. The complete-rectangle objective explicitly asserts that the first width divides length; it has no calibrated incomplete245extension yet. These control failures prohibit a target sweep.

## Verification, limits and reproduction

`validation.json` and `validate.py` independently decrypt and reencrypt every saved intermediate and complete candidate, verify all four true-outer first-key exact recoveries, and expose key-discovery failure. They also fingerprint source, primary references and frozen model files. Scores are diagnostics, never probabilities or solution thresholds. Target source/transcription, glyph uncertainties, `5245`, indicator position and historical system remain untouched. The known unchanged retransmission of reportedly solved391 is disclosed in the main SOLUTION; no391plaintext was consulted.

From repository root:

```sh
ciphers/hcp-399/work/idp/reproduce.sh
python3 ciphers/hcp-399/work/idp/validate.py
```

The reproduction command preserves original logs, writing fresh controls/search outputs to `reproduced/`; deterministic planting input files and compiled binaries can be regenerated. Validation checks the saved original outputs. It reuses only read-only frozen393corpora,363bigrams and `batches/scoring-sol61` models. It does not attack the actual target or start watchers/reviewers.

The generic columnar inverse, physical key transformations and full-text refinement can support a future **conditional shared-key multi-message objective**, summing each message's score with its own segmentation. Such an extension would need independent joint controls with the actual unequal lengths and a third stage if testing R. This is reuse potential, not evidence that any messages share keys.

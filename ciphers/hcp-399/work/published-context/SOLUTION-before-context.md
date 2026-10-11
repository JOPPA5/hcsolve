# Unsolved attempt: HC Portal399
Solver: OpenAI GPT-6 Astra. Date:2026-10-11.

No plaintext or key has been recovered. No DONE, FINAL or register entry is warranted.

## Source and attribution
The preserved original scan is MZV80233/1944, portal date10August1944, status Not solved. No attached transcription or solution exists. Its clear note says it repeats80219 unchanged after the recipient could not decipher it. The parent solver separately observed portal391 is **Solved**, named80219/1944 and dated5August1944. No391 plaintext or attachment was accessed. Thus399 appears to duplicate an already-solved entry; any future recovery must disclose that relationship and must not be presented unqualified as previously unknown plaintext.

## Transcription and header
Manual first-pass transcription contains245 letters after5245. Reinspection produced work/transcription-v2.txt with dmrer→dmren and kjeaj→kjaaj; ambiguous readings remain, documented in NOTES.md. Source unchanged. Trailing245 agrees with the ciphertext letter count. The former suggestion that prefix5 denotes the original day is withdrawn as unsupported: same-date neighbouring records have different prefixes, and no verified prefix rule is known. Archival plaintext and the second typing in solved391 are now being consulted as explicitly attributed context; any matching plaintext is a published duplicate, not an independent new decipherment.

## Tested hypotheses
IC0.051589 in the first-pass text supports considering transposition, without identifying a type. A historical R/XQ hypothesis is documented in work/historical-context.md. Necessary indicator constraints leave41 possible five-letter groups in both transcription variants, rather than uniquely determining an indicator. Also retained the no-deletion case.

After initial simple attempts, single-columnar widths16–22 were searched over all42 whole/deletion choices:294 cases per transcription. No coherent message appeared. Language scoring used Slovak corpus fourgrams; this is heuristic, not exhaustive.

## Attack validation and limits
Synthetic texts were explicitly invented controls, not target cribs. Known-key C++ decryption recovered all six240/245-letter single/double/triple controls exactly. Key search recovered240/240 for a single-stage240-letter control. A245-letter single-stage control needed an extended budget to recover245/245; the shorter budget recovered207/245.

Crucially, the search recovered only13/240 and15/240 positions for double and triple controls even when stage widths were supplied. Therefore this optimizer **is not a validated attack on multiple transposition**, and its failures cannot reject R/XQ. Source glyph uncertainty, unknown indicator table/location, unknown daily permutations and their widths remain unresolved. There is no verified partial plaintext or translation.

## Reproduction
From repository root:

```sh
sh ciphers/hcp-399/work/reproduce-deeper.sh
```

Requires Python3 and C++17. Reproduces synthetic controls, known-key checks, indicator enumeration and target screening using preserved manual transcriptions and quadgram table. It reproduces attempts, not a plaintext; no automatic scan-to-plaintext command exists. Details and output files are in work/ and NOTES.md. No watcher is running on our authority; user instructed external reviewer polling and no watcher launches.

## Continued method development — GPT-6.1 Sol

A new regular-first-stage double-transposition adjacency objective was tested on an independently generated240letter20/17control. Its initial and extended searches recovered only11/240and13/240positions respectively. The target was not attacked with this unvalidated method; no new negative conclusion about399is drawn. Exact scripts, planted keys, outputs and source-preparation observations are recorded in NOTES.md. The plaintext and key remain unavailable.

## Primary-algorithm control development — GPT-6.1 Sol

The new primary-source IDP implementation matches an independent reference on42 random cases. A stronger first-stage solver recovers all four independently planted240/245texts exactly when the correct second key is supplied. However, discovery of that second key remains unsuccessful, including after full-text two-key refinement. A genuine held-out245control even gives a higher IDP to a false second key than to truth. These are separate facts: known-key diagnostics do not validate key discovery.

A new consistent first-column path objective uses frozen3/4/5gram cooccurrence and a bounded beam; its independent bounded control tests also fail to discover the outer key. The improved16-state beam retains the correct four-column boundary context and recovers both regular240first keys only when the true outer key is supplied. The incomplete245path extension remains uncalibrated, so no actual target use occurred. No target-negative conclusion follows from its control failures. Primary references, scripts and results are in `work/idp/`, with source uncertainties unchanged. Still no plaintext, key, translation or solution marker is claimed.

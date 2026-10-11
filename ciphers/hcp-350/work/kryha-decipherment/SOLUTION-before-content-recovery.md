# HC350 — unresolved

**No cipher key or plaintext recovered.** The two original telegram images are preserved in source/. Manual tentative transcription contains77five-letter groups,385letters, matching the printed length. Ambiguous letters remain documented in NOTES.md.

The portal labels the document Not solved and Unsolvable, titled “Nerozlúštiteľný telegram” (“Indecipherable telegram”). This is metadata, not an independently demonstrated impossibility result. No original-language deciphered body or translation is claimed. HOLAKOVI is a clear routing word outside the encrypted body, and CIEKER3001 is the signature/reference.

Frequency analysis, low-period Vigenere tests, visible-word key hypotheses and forward/reversed monoalphabetic substitution searches yielded no coherent full plaintext. `sh ciphers/hcp-350/work/reproduce.sh` reproduces those attempts; it does not decrypt the source images. All385letters remain unresolved, and no complete plaintext reproduction command exists.

A polyalphabetic machine is plausible from the distribution and Madrid1944 context, but cipher identity and settings are unverified. No published solution was imported. SOURCES.md discloses both original images, helper corpus and historical reference. No DONE/FINAL marker or register entry is justified.

## Cross-message findings, still unresolved
A comparison with351 found strongly similar first20 and final10cipher letters, but only2equalities in the355letter interior.351's scan appears to bear a March2,1944 postal stamp despite its portal dateNov3; metadata was not altered. These observations suggest a related-message investigation, not a solution.

**New evidence from the human-supplied batch review:** compare350[i] with351[i+1], not351[i]. Within the interior, repeated350letters in the same residue class modulo23 overwhelmingly map to repeated351letters. Main independent all-pairs counting gives97/114 equal pairs at offset+1, versus4/114 at offset0. The separate agent's fixed-reference repeat count gives83/97 at offset+1, matching the reviewer. Both statistics identify23/46 as clear outliers across periods2–59. See `batches/review-leads-main/shift-period-audit.json` and `batches/kryha-shift23-sol61/scan.json`. This supports a shifted related-text investigation; it does not yet supply either plaintext or a physical key. Earlier aligned-offset0 rejection must not be used to reject this shifted relationship.

The implemented Kryha-specific consistency test contradicts only the narrow offset0 hypothesis of identical aligned plaintext, shared ring alphabets and only changed start/selector phase for an original17step machine. It does not address the newly observed offset+1, period23 relationship. A separate cumulative-wheel-positionIC test found no persuasive signal for the published17step schedule. Later adjustable52stop controls and conditional count20/26 whole-pair searches are now recorded in NOTES.md; their earlier reset/alignment assumptions do not cover the new shifted-text evidence. No plaintext or key is established.

## Exact conditional direct re-encryption check — GPT-6.1 Sol

A new exact known-input/output model tests whether351's middle is encryption of350's middle by the original fixed17step Kryha, with arbitrary mixedring permutations. Matched355symbol controls recover both exactrings up to globalrotation; a3typo control also recovers the exacterrorpositions. All17phases in bothdirections reject the literal target, both with0and3allowed erroneous positions (68UNSATcases). Repeatedpair displacement contradictions alone require at least79badpositions. Script/results are `work/reencrypt_kryha.py`, `work/reencrypt-control.json`, and `work/reencrypt-target-results.json`.

This refutes only that precise conditional model on current transcriptions. Adjustable stepping, resets, different transformations, alignment changes and extensiveerrors remain open. No historicalplaintext orkey has been obtained.

## Exact periodic re-encryption rejection at offset0 only

The direct350→351model was extended to arbitraryunknown repeating additive steps, allperiods1–52, and mixedringpermutations. IndependentGF2/GF13RREF+CRT recovers valid complete355symbol controls atperiods17/26/52. Everyliteral targetperiod has onlycollapsedzero-ring solutions and is rejected. An exactGF13paritycheck sparse-codeword enumeration further rejects allperiods with up to3badalignedpositions; matched3error controls identifytheplantedpositions and recover theentire underlyingoutputs. Reproduce with`work/periodic_algebra.py` and`work/periodic_three_errors.py`; exactmodels, controls and limits are inNOTES.md.

This is a conditionalmathematicalrejection of aligned, uninterrupted, additiveperiodic re-encryption, not a decipherment or historicalmachineidentification. Resets, differentalignment, nonperiodicmechanisms andothertransformations remainopen. NoDONEmarkeris warranted.

## Ciphertext-only original17step control development

Aheld-out385letterSlovak control withindependentrandommixedrings wasnot recovered byblindtwo-ringoptimization (62/385baseline,70/385progressive). Therefore thosemethods supplyno targetnegativeconclusion. Givingtheoutputring yields exact385/385control recovery. ASTRICTLYLIMITED fixedA–Zoutputringmodel passesmatched385/380/365controls, thena102case target sweep over17phases,bothdirections,prefix0/5/20findsno coherenttext. This finiteheuristic search doesnotexclude eventhatlimitedfamily mathematically anddoesnotcover arbitraryoutputrings. Scripts, controls, keys andsummaryare inwork/ring-attack-report.json andNOTES.md. No historicalplaintext/key claimed.

## Validated structural two-ring attack, unresolved target

A ciphertext-only projected-frequency concentration search followed by ordinary substitution language ranking and joint ring refinement recovered the independent385letter held-out Slovak control exactly. Seed selection used only IC/language scores; independently re-encrypting the recovered text reproduces all385 control symbols. Full ring uniqueness is not claimed because F/W are absent from the control. Reproduce with `sh ciphers/hcp-350/work/reproduce-ring-ic-control.sh`.

Applying the identical generic procedure to all17 phases and both signs of the literal full385letter350 transcription retained10,200 output-ring candidates, but no coherent plaintext emerged. Only the top language-ranked candidate per phase/sign underwent joint refinement. Best final score−417.174 versus exact control659.126; these are model scores, not probabilities. This bounded heuristic failure does not exclude the original17step model. All candidate outputs and keys, exact re-encryption checks, budgets and limitations are in `work/ring-ic-target-report.json` and NOTES.md. The possible PMQKX/PMQKK scan ambiguity remains unresolved and the baseline is unchanged. No supported historical key/plaintext, no DONE marker.

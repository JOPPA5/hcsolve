# Internal solver audit of the source-bound 374 working key

**PASS for the complete claimed 80-letter encrypted body and its disclosed alternative reading.** This is an internal solver audit, not the external reviewer handover. No cipher documentation, source, key, transcription, or marker was modified.

`audit.py` imports no parent decoder/verifier functions. It advances continuously by one physical adjacent wheel edge, emits only at the selected mask holes, and then applies the separately read alphabet-position tables. The 52 positive adjacent distances sum to 179. The 23 distinct stop indices are zero based, valid in 0..51, and in positive cyclic order. The emitted stop sequence agrees with the supplied phase. Every 23 emissions add exactly 179 physical units. The initial integer representative 27 is congruent to the claimed first displacement 1 modulo 26; its unreduced value is a coordinate convention, not an independently recovered historical register setting. Both P and O are complete 26-position bijections.

The immutable JPEG SHA256 is `04897cf373b3e411dd2cea9d87e255d05d5d9bd0dd07879a3f30aefd29b6fff7`. It agrees with the key and the frozen blind-reader manifest. The exact 85-letter working transcription agrees with every group of the reader's frozen artifact. Source reading and cryptographic interpretation therefore remain separate. I also viewed the full JPEG; this audit does not replace the original blind pass or claim that pixels mathematically certify each letter.

Independent literal output:

```
AUPOZORNUIESPANLELSKEPROTIBODVVKYUZPEVNEKUPENENAZAKLADEPOVODNYCHCIENCELULOZYXXXX
```

All 80 actual transcribed ciphertext body positions independently re-encode exactly, with full position records in `audit-results.json`. The first five source letters KIDAH are retained unchanged and are never deciphered or stepped through by this body convention. An “85-letter round trip” is 80 cryptographically checked body letters plus five copied prefix letters; it supplies no historical interpretation of KIDAH.

Source position 21 is literal S and decodes to L at body position 16; source position 32 is literal L and decodes to B at body position 27. They remain unchanged despite the grammatical expectation SPANIELSKE/PROTIDODAVKY. Preferred source position 35 M decodes to V at body position 30, yielding PROTIBODVVKY. The declared alternative source35 N decodes to A, yielding PROTIBODAVKY. Its complete 80-letter alternative reading also re-encodes exactly. The original blind artifact favours M; N is an explicitly separate later alternative, not silently promoted to the preferred source reading. Parent claimed literal outputs agree exactly with both independently computed outputs.

The final four decoded **coordinates** are exactly 19,19,19,19. Naming that coordinate X and interpreting XXXX as padding remain disclosed hypotheses. F/G/J/Q/W completion values are never encountered in the body; changing their permutation among those remaining slots cannot affect this body's output. M at coordinate24 is also unused by this body. `madrid-context-audit.py` independently verifies its external binding: the frozen 373 tail key gives the unique known ADRID coordinate suffix at source positions14..18, preceded by coordinate24 at source13. The attributed published word MADRID then supplies M24. This is a held-out contextual constraint, not a new 373 plaintext discovery or a full 650-letter literal-preparation claim.

The body uses 25 ciphertext alphabet labels: D occurs only in the retained prefix, so its output-ring binding is inherited from the published-context key, not independently measured by the 374 body. Whole-key bijectivity is confirmed, but this audit does not certify unique historical values for every unused label. The tail witness and its physical-mask report already disclose their erasures and one literal373 mismatch; this audit does not turn them into an exact 373 source fit.

The complete source-bound decode agrees; no mechanical inconsistency was found in the new key/decoder/result fields. At audit start, the pre-existing `SOLUTION.md` and portions of `NOTES.md` still said “no key recovered / all85 unresolved.” On the final document check, root had replaced SOLUTION with the recovered-body/working-key claim and appended a recovered section explicitly superseding the old all-unresolved state in NOTES. SOURCES now attributes public373, the independent reader and solver audit. The current SOLUTION code block equals the independently audited literal 80-letter body exactly and explicitly distinguishes 80 deciphered body letters from the five copied prefix letters, unused labels, M24 context, X19 hypothesis and source35 alternative. This documentation inconsistency is therefore resolved. Root should keep the prefix-copy distinction, canonical completion, M context binding, X hypothesis, literal spelling anomalies, source35 alternative, and public373 attribution in the final claim. Exact inversion alone confirms implementation consistency; it does not independently prove every historical machine setting or plaintext label.

Reproduce from the repository root:

```
python3 batches/kryha374-final-solver-audit-sol61/audit.py
python3 batches/kryha374-final-solver-audit-sol61/madrid-context-audit.py
```

Evidence: `audit-results.json` includes all 80 preferred and all 80 alternate source-position records; `madrid-context-audit.json` preserves the held-out source window and hashes; `provenance.json` records immutable and working inputs. This batch writes only to its own directory.

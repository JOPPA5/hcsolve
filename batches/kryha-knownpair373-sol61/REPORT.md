# Published HCP373 known-prefix modular-ring experiment

No target key was recovered. The content is transcribed from an already published Solved HCP373 attachment and is not a new decipherment. The useful result is a calibrated exact known-pair solver and finite conditional incompatibility results, not a general exclusion of Kryha.

## Model and preparation

For plaintext letter p_i and ciphertext c_i, the unknown shuffled rings P and O are permutations of 0..25. Unknown K has m arbitrary residues, m=2..52. The equation is O(c_i)-P(p_i)=K[i mod m]+179 floor(i/m) modulo 26. This deliberately permits arbitrary K and does not enforce a physical 52-hole mask. A programmable wheel of circumference179 with m selected stops is contained in this family only if it advances once per character, repeats unchanged, and the stipulated plaintext alignment/preparation is right.

P(A)=O(A)=0 fix two harmless ring rotations; K absorbs their difference. All K entries, both rings and the tested period remain unknown. Exact Gaussian elimination separately over GF(2) and GF(13) expresses every dependent slot in free finite variables, then CRT reconstructs 0..25 positions and imposes both ring permutations. No language score or true key seeds the search. Direct integer modular Z3 timed out on the first control; the exact CRT formulation solved it in milliseconds.

The literal published prefix before the first numeric token 6.000 has93 normalized letters. Six finite preparations retain its spelling, remove diacritics, and either omit word boundaries or insert X or J between every word, with natural J retained or mapped to I. Separators are not inserted after the final word NA. These word-boundary hypotheses differ from comma-only punctuation hypotheses tested by root. Each tests ciphertext alignment starting at position1 or after its first5 letters; initial-five omission is conditional, not an established indicator interpretation.

The preferred prefix transcription has position53 L and position90 E. Independent source collation preserves position53 L/I and position90 E/A ambiguities. All four complete branches were tested without changing the source. Later source corrections at233/268/270 are beyond this prefix and cannot affect these equations. Other unenumerated source or plaintext preparation uncertainty remains outside this experiment.

## Fresh controls and held-out prediction

The matched93-letter prefix was independently encrypted under random mixed rings, independent unrestricted K, and periods20,23,30. All three blind controls recovered complete consistent encoders, without true keys or alignment. Each unknown-period sweep2..52 identified only the planted period as SAT. Each fit of the first73 predicted all withheld20 letters exactly. Independent full inverse verification is retained for20/30; all full fits are independently reencryption-checked.

A blocked second complete-key witness at23 changes only unused input letters B,F,G,Q,W,X. Its output ring and all23 K entries are unchanged. Thus complete alphabets are not uniquely identifiable from this prefix even when the operative mapping is constrained; planted raw-key identity is not a success criterion.

The fully determined constant case in an added20 control revealed an interface issue: Z3 Distinct required wrapping plain integer expressions in IntVal. This was fixed; all target cases were rerun after the correction. No mathematical constraint was weakened.

## Finite target results

The original preferred L53/E90 branch produced612 UNSAT cases: six preparations × two alignments ×51 periods. The three other source-supported glyph combinations contributed1836 UNSAT cases. Combined:2448 exact UNSAT, no UNKNOWN, no SAT witness. The original preferred run had611 linear CRT contradictions and one incompatibility with the permutation requirements. These are contradictions only within the stated prefix, finite glyph/preparation/alignment and fixed179-cycle family.

Separate first73 fits used m20,21,23,25 and both L/I at53, with all six preparations and both alignments. All96 were UNSAT. Position90 is excluded from these fits. Therefore no target held-out prediction or target second-key witness exists; neither should be claimed.

## Selective-J extension

The primary SSA NR2417 memo documents a practice of an additional lever depression after literal J in certain historical traffic. This does not establish Slovak adoption. For known prepared plaintext, that extension gives a deterministic press index t_i=i+number of preceding J letters, and the same exact equation uses K[t_i mod m]+179 floor(t_i/m). It requires no cipher-only step inference.

Two fresh independent word-J controls at23 and30 pass full consistent-ring fitting, unknown-period sweeps, and all33 withheld letters after fitting the first73. No true key is supplied. The finite actual extension contains1632 cases with literal J present, over all four glyph branches, six preparation choices where applicable, two alignments and periods2..52. All are UNSAT. Preparations with no J have identical press paths to the earlier2448-case family and are not rerun. This is one precisely defined extra-press model, not every historical stepping rule.

## Limits and reproduction

These results do not exclude another initial plaintext/address, spelling convention, punctuation representation, numeral preparation, nonunit cycle advance, rekeying, stepping rule, source glyph outside the enumerated alternatives, or an erroneous/mismatched published draft. Because both rings are arbitrary permutations and K is unrestricted, any invertible cycle advance g modulo26 is included by decimation: multiplying both rings and every K residue by u=23·g⁻¹ modulo26 converts g to179≡23. The finite results therefore cover all unit advances in this algebraic family, not solely one numerical circumference. Nonunit advances are outside it; physical arc geometry is not preserved by arbitrary decimation. No physical mask was reconstructed. A guessed crib alone, especially on a short follow-up such as374, cannot certify a key without mechanical constraints and held-out/full inverse evidence.

From repository root:

```
python3 batches/kryha-knownpair373-sol61/control.py
python3 batches/kryha-knownpair373-sol61/crt_control.py
python3 batches/kryha-knownpair373-sol61/validate.py
python3 batches/kryha-knownpair373-sol61/run.py
python3 batches/kryha-knownpair373-sol61/glyph_check.py
python3 batches/kryha-knownpair373-sol61/selective.py
```

Raw controls, alternative witnesses, complete finite results and provenance hashes are retained in this batch. `control.py` is the deliberately preserved slow direct formulation; its UNKNOWN does not invalidate the subsequent exact CRT controls. All processes exited. No cipher/source directory, marker or watcher was modified.

## Source-backed chronological preparation alternative: USTRENI

A subsequent independent view of `pt-first.png` shows typed USTRENI with a handwritten D correction above the e/n region. The amended published transcription remains USTREDNI. A separate chronological-stage hypothesis tests the machine input before this correction; it is not a correction of the ciphertext or a fact about when encryption occurred.

Deleting only this D removes normalized prefix position27 in the no-boundary93-letter string, yielding92 letters. With one marker between each word it removes position30, yielding105 letters. No other source word, letter, address, alignment or punctuation is changed. Preferred and alternate ciphertext glyphs at53 L/I and90 E/A remain separate finite branches.

A fresh independent92-letter ordinary control passes full blind ring/schedule recovery and reencryption. Its shortened72-letter fit predicts only18/20 withheld letters: this source variant does not demonstrate unique held-out prediction, and the failure is preserved. A separately saved fresh105-letter word-J selective-press control passes full fit and predicts32/32 after fitting73 letters. The generic selective rule was validated before the target extension; this exactly length-matched additional control was obtained after the finite extension and is documented as such. The reproduction script now runs the matched control before that extension.

The unamended ordinary target contributes816 no-marker and1632 word-marker cases, all UNSAT; the selective-J extension contributes1632 additional nonduplicate cases, all UNSAT. Periods2..52, omit0/5 and all four source glyph combinations are included. There is no target witness, no source modification and no general machine exclusion. The earlier amended results are preserved separately.

Reproduce this exact chronological alternative:

```
python3 batches/kryha-knownpair373-sol61/unamended.py
```

The later optional press-index extension required a minor held-out default-index fix: when a default ordinary schedule is used, its index list must cover the held-out suffix as well as the fitted prefix. Earlier stored results remain valid; this fix only repairs reproduction of ordinary held-out checks after adding the optional selective schedule.

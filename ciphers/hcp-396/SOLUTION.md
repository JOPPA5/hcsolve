# HC Portal 396 — unresolved

**No decipherment is claimed.** Solver: OpenAI GPT-6 Astra.

The preserved source is a Slovak MZV telegram, 80230/1944, dated 7 August 1944, sent by Mračna to Sidor in Vatican City. The portal labels it Not solved. Its supplied title describes a request concerning repetition of telegram 80214/44; this description is not itself the encrypted plaintext.

The image has no attached transcription. My manual transcription in `work/transcription.txt` contains 55 letters:

```
vepes nmono drtsi uzoip ujpta sztra
cscnu dwjpm ciasi ujiui oormt
```

Group 7's initial C is uncertain; O was also tested. The number preceding the body is read 755.

A historically plausible type is R/XQ triple columnar transposition; see the contextual scholarly source in SOURCES.md and the explanation in NOTES.md. This type has **not** been established for this message. Group 8 `dwjpm` may be a five-letter indicator, leaving 50 payload letters, but this is also unproved. No key has been recovered, and there is no supported plaintext or translation.

Reproduce the implemented analysis from the repository root:

```
python3 ciphers/hcp-396/work/analyze.py
```

This produces diagnostic candidates, **not full plaintext**. All 184,928 tested single-columnar keys and 2,324 route controls failed to produce a supported complete reading; these finite tests do not exhaust the possible cipher family. The source remains intact, no published solution was used in that earlier attack, and no successful-solution marker or register entry is appropriate at this stage.

## Continued analysis — GPT-6.1 Sol

Additional controlled alternative-family tests remain unsuccessful: AMSCO (8,876,544 key/parameter/scenario evaluations at widths2–8) and offset railfence (229,872 evaluations). AMSCO recovered an exact50-letter Slovak control and its width7key; railfence recovered its independent generated control. Neither produced a coherent telegram under C/O readings, with the full body or any single five-letter group omitted. Reproduction commands and precise scope are in NOTES.md. This expands analysis; it does not establish any plaintext or eliminate the historically plausible triple R system.

The documented R indicator construction supplies conditional structural constraints: with the C reading, groups2/7/9/10 cannot encode any alignment1–22; groups1/11 could encode only11or22, while groups3/4/5/6/8 remain eligible. With O reading, group7 also remains eligible. These constraints and source-preparation checks are reproduced in `work/indicator_constraints.py` and explained in NOTES.md. They narrow a hypothesis without recovering plaintext.


## Published original 80214 / HCP387

The main solver found public Solved387 by rendered Global Filter 80214. Its original cipher and published handwritten draft are attributed in `batches/solved-context-main/387/SOURCES.md`; this is archival context, not newly recovered plaintext. The physical original bears 80214 / 2.VIII.1944, despite its portal Description typo 80124. The independently preferred full 55-letter original and repeat agree at 53 positions; original CIAAI/OORNT versus repeat CIASI/OORMT differ at positions 44 and 54. Watermark caveats remain. Original group 2 is NMONO, correcting an early provisional MMONO impression.

Preferred published draft: “Podajte šifrou stručnú zprávu o situácii a možnej činnosti.” A crossed phrase tentatively reads “svojej činnosti” and is excluded from this preferred final draft. English: Send a brief report in cipher on the situation and possible activity. This reading is source-led and does not claim a decipherment key.

The 50-letter normalized draft contains F in ŠIFROU; both 55-letter source readings contain no F. None of 432 declared inventory cases matches exactly. Original387 with group 8 DWJPM omitted, no added X, is uniquely closest: one F missing and one P surplus. All printed P glyphs remain unchanged. Replacing one of three remaining P positions (3,20,23) with F is a conditional one-symbol-error experiment, not a corrected transcription. Repeat396 additionally retains its A/S and N/M differences. No complete known pair or key has yet been established. Detailed confidence, scans, inventories and reproduction: `batches/repeat396-387-sol61/REPORT.md`.

## Actual worked-example validation of the R core

An independent visual transcription and fresh encoder reproduce both full intermediate grids in the published HistoCrypt2020 Figure5 example. Existing 21/19/20 encoders and inverses also pass the actual fixture, including physical alignment. The final indicator spelling and whether ip=5 means insertion before or after payload group5 are not unambiguously verified. A targeted code audit found no actual target result requiring rerun solely for that boundary ambiguity. This supports the transposition implementation, not its applicability to396 or a recovered key. Evidence: `batches/r-primary-example-audit-sol61/REPORT.md`.


## Key-search continuation — GPT-6.1 Sol, 2026-10-12

The independent 50-letter calibration in `batches/r396-key-next-sol61/REPORT.md` did not recover a complete key. Exact Hungarian decompositions, global position/rank CP, constrained repairs and legitimate known-crib fragment scoring reached at most43/50 letters. This is not nearly recovered key evidence: the two best controls agree with only13/50 and12/50 planted position mappings. A distinct rank-conditioned repair and globally free unique-letter-endpoint repair also failed. Equal17 closed-form constant/progressive controls pass known-key fixtures but remain UNKNOWN under the declared blind bounds. No actual target key searches followed these failed recovery calibrations; there is no negative target inference.

`python3 batches/r396-key-next-sol61/verify.py` independently checks15 saved candidate key sets and finds zero complete observed-ciphertext witnesses. Prediction round trips are explicitly distinguished from decryption of observed ciphertext; earlier partial-candidate inverse labels were clarified without changing keys. Published387 plaintext remains attributed context, and P→F alternatives remain hypothetical errors rather than source corrections.

Public Solved386 was inspected only as same-day/channel context. Its source audit (`batches/solved-context-main/386/AUDIT.md`) finds280 cipher letters versus574–591 draft letters and no exact inventory across declared contiguous windows, minimal padding or group omissions. Best preferred gap is22 substitutions; loose source-variant bounds still require at least15. Thus no valid386 known pair or shared-key constraint was established or used. Daily-key sharing is unproved. Full methods, bounds, failures, provenance and source-only crops are preserved in the new batch. No source, marker, watcher or review changes were made.
## Exact backend continuation (2026-10-12)

Two CaDiCaL engines recover whole50-letter equal17 controls with unknown keys and a conditioned n. The source387oneP/F context union, common/progressive all32 legal n cases, gives4 UNSAT and28 UNKNOWN, no actual key. Generic21/19/20 remains uncalibrated at its full50 control; no mixed-width source-context target followed. The true source glyphs and published plaintext attribution remain explicit. Reports: `batches/r396-cadical17-sol61/REPORT.md`, `batches/r396-mixed-cadical-sol61/REPORT.md`.

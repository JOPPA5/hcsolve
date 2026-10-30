# Work log — HCP 1021

## 2026-10-26/27: first bounded inspection

Read README fully. The explicit no-watcher override applies: no watcher, reviewer, or review marker launched. Root had read all three rendered portal tabs, including Not solved/Pigpen and absence of an individual attached solution. I independently inspected both original scans saved by root. The picture contains a child bathing; the address side contains ordinary handwriting, stamps and postmarks. Cipher-like angular writing is confined to the top of the picture. Other cursive margins are not fully transcribed and are not silently treated as covered plaintext.

The supplied collection reference is Schrödel2021, already retained in hcp1081. Root inspected the paper and its addendum without identifying this card or a key for it. This is bounded source checking; it is not a claim of global novelty. I did not use a recovered phrase from that paper.

### Visual transcription

`work/transcript.json` records **29 positions, including one heavily canceled position**, with original-image boxes. Twenty-eight noncanceled shapes are recorded, not 28 decoded letters. Five tall strokes may divide six groups. Position 26 is not silently deleted: its interpretation and scope of cancellation are unresolved.

This is a **manual geometry transcription**, not OCR. The weak ink makes a short detached wall hard to distinguish from a dot. Positions 3,5,6,9,10,16,17,18,23,29 retain explicit alternatives. In particular, first assigning every lower-left stroke under a top-right corner as a dot caused implausible repeated initial symbols. That suggested revisiting geometry, not inventing plaintext. Positions 11 and 24 are visibly T-like (vertical stroke with a right-facing arm); they must not silently become three-sided outlines. Their appearance repeats at x338 and x705.

Working crops: top strip from picture y8..68/x60..860, enlarged; coordinate strips x65..260,260..455,455..650,650..850 at y12..53, 4x; gray autocontrast details and corner comparison retain unresolved alternatives. These are viewing aids only, all originals remain unchanged.

### Bounded key check

`work/decode.py` verifies SHA256 hashes of all three original source files, checks record IDs/count, prints geometry/coordinates, and applies an explicitly **unestablished reference key**: A–I/J–R on ordinary/dotted 3×3 cell outlines and S–V/W–Z on ordinary/dotted cross sectors. It also prints all 24 permutations of those four alphabet groups while keeping their internal orientation fixed. It does not run a general arbitrary monoalphabetic search, all orientations, a keyword search, or a full historical-variant survey. No linguistic score or exhaustive failure claim is made.

The two T-like shapes have no entry in this reference family. Thus the reference cannot provide full coverage even before language judgment. Forcing them to ordinary cell forms, or fixing weak wall/dot choices to fit a familiar German sentence, would make the apparent result depend on unsupported transcription choices.

### Result / next discriminating action

No consistent key and no plaintext established. Need identify a historical Pigpen family that actually admits the two T-like forms, or better imaging that resolves whether those forms have missing surrounding walls. Keep the original glyph identity evidence and alternatives when testing such a family. Do not infer a full reading from the postal route, the bath image, or a fluent candidate phrase. No DONE marker created.

## 2026-10-27: custom-alphabet and direction follow-up

### Context and orientation

Inspected additional autocontrast working views: `context-right.png`, `context-bottom.png`, `context-left.png` (left margin rotated 90°), `context-top_mirror.png` and `context-top_rot180.png`. The printed picture text is “Gruss aus”; the address has ordinary postal handwriting. The weak cursive prose remains insufficiently certain to supply an exact crib. No plaintext was imported from it. The mirror/rotation views do not reveal an obvious ordinary-letter sentence or remove the two repeated T-like forms.

`orientation_audit.py` checks the recorded outline geometry under all eight plane symmetries. The right-facing T has a three-way junction; rotations/mirroring retain that junction, whereas the conventional grid-cell/cross-sector outlines in this test have no three-way junction. This is a **conditional observation about the manual geometry**, not proof that the original has no faint missing wall and not exclusion of every historical Pigpen variant. A custom MASC can still assign a letter to that form; the next test explicitly allows that.

### Finite arbitrary MASC dictionary experiment

Command: `python3 ciphers/hcp-1021/work/masc_constraints.py`.

Data: existing repository `batches/scoring-sol61/german/words.tsv`, sourced there from LibreOffice de_DE_frami and UD German GSD. The command records its SHA256. It is a modern normalized dictionary (umlauts fold to A/O/U, ß to SS); it contains inflections, names, abbreviations and foreign words. A matching entry is not grammatical or historical evidence. No internet phrase was supplied as a crib.

The experiment uses **arbitrary bijective substitutions**, including an unrestricted letter for each T-like form. It enumerates each listed manual geometry alternative, permits omission of canceled position 26 **only as a conditional hypothesis**, and assumes the five tall strokes separate six words of lengths 4,4,3,5,4,8. It does not silently change any other geometry. Candidate word keys must agree in both directions: one glyph cannot map to two letters, and two distinct glyph labels cannot map to the same letter.

Training groups were fixed as **1,2,4,6**; physical groups **3 and 5** were withheld from training and ranking. Test cases reverse letters within every group for right-to-left reading; whole-line reversal also reverses group order, which does not change these per-group constraint results. Group identities in the saved JSON remain original physical identities.

Results (`work/masc-constraints.json`):

| Direction | Complete training assignments | Assignments predicting group 3 as a dictionary word |
|---|---:|---:|
| Forward | 98,901 | 26,269 |
| Reverse | 258,842 | 77,047 |

These counts include duplicate training words under different geometry/key assignments; they are not distinct complete plaintexts. Keys are retained only for the top25 summed `log1p(training-word frequency)` scores, with **no held-out score in selection**. Inspection of those predictions did not produce a defensible sentence. Several dictionary “passes” are abbreviations rather than German words. The large number of fits demonstrates why individual apparent words are weak evidence here.

**Important validation limit:** the third glyph of physical group5 (`open_left_dot`) appears nowhere in the training groups. Its prediction therefore necessarily contains `?`. The reported zero “full heldout passes” is mechanically guaranteed under this split and **must not be interpreted as evidence against a solution**. The known letters and group3 predictions remain visible; no missing glyph is filled to manufacture a passing sentence. Passing a dictionary test alone would not validate a reading anyway.

Implementation checks reject conflicting cipher→plain and plain→cipher maps. A separately planted rotation-substitution example predicts withheld `dich` and `sehr` from a training alphabet. This checks the constraint/prediction logic, not the ability to solve historical Pigpen from pixels. The first version of that synthetic check used a training word set lacking D; its expectation was corrected by replacing `habe` with `dabei`, and the completed run passes. No target alphabet or transcript was changed for that correction.

### Search boundaries / outcome

This is a finite, reproducible custom-alphabet test beyond 24 conventional group orders. It does not cover tall strokes as additional cipher letters, arbitrary word resegmentation, cancellation retained as a letter, homophonic/nonbijective alphabets, altered dot inventories, or unknown shapes outside the listed alternatives. No general negative result follows. No key, plaintext or translation established; no DONE created. A better-resolved transcript or independently identified historical key remains the discriminating next evidence.

## 2026-10-30 (Claude Opus 5.5): solved — card turned 180°

Looked at enlarged (5–14x, autocontrast) crops of the top line. Key observation: the line was
written with the card upside down — the signs stand on the frame line and the five comma-like
dividers descend below it. Rotating the strip 180° and reading left to right with the **standard
Pigpen key** gives `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS` = "Radfahren soll leben! All Heil! Gruß"
(cyclists' greeting). The earlier "tee_right" signs (ids 11, 24) are A (⌟ with the horizontal drawn
a little above the foot), confirmed by ALL and FAREN; glyph 28 is a plain ⌟ = A (the dot near it
belongs inside glyph 29 = R). Dots outside cells at 27 and 4 treated as stray. Glyph 26 cancelled,
not read. Earlier dot/wall alternatives resolved by inspection (all consistent with the reading).
Command: `python3 -I ciphers/hcp-1021/work/solve_1021.py`. SOLUTION.md rewritten; DONE1 created.

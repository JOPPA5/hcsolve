# Shifted 350/351 pair: independently recovered common cycle

This batch verifies a new lead supplied by the human's external review. It establishes strong shifted common-cycle structure, not plaintext or a complete historical machine key. Sources and earlier solver directories are unchanged; no marker, watcher or register entry is created.

## Lead and independent scan

The human provided the reviewer text in `/Users/tomaspavuk/.codex/attachments/b49bf446-0fb2-44d6-bca4-a9e557d9baec/Pasted text.txt`, section 1.3. It identifies the shifted relation, period 23, and an independent reader's candidate cycle. This lead is credited rather than claimed as newly discovered. The candidate cycle was NOT seeded into our recovery program; it was compared afterward.

On both original working files and earlier source-preferred variants, scanning every offset −1, 0, +1, +2 and period 2–59 independently reproduces 83/97 repeated-letter matches at offset +1 / period 23, versus 4/97 at offset 0. Period 46 gives 46/53; the next ratio is period 44 at 10/41. The analysis interval is exactly zero-based 350 indices 21…374 paired with 351 indices 22…375, 354 cells. The original/preferred edits lie outside this interval, so these scans agree. Our period-26 denominator is 72 rather than the review's 73; it does not affect the strong contrast.

## Error-tolerant cycle recovery

The finite-field/CRT construction in the existing `batches/kryha-method-sol61/isomorph_solver.py` is generalized to 23 residue-specific powers. Unknowns are 26 letter coordinates plus 23 shift powers. Each observed cell imposes O(y)−O(x)=K[i mod23] modulo 26, with O(a)=0 gauge. Randomized independent rank-48 bases over GF(2) and GF(13) provide one-dimensional candidate nullspaces. Candidates must have 13 coordinates of each parity, two of each mod-13 coordinate, and 26 distinct CRT coordinates. Complete candidates are ranked only by all observed cells; planted or reviewer rings are never used as seeds.

Ten thousand deterministic randomized bases (seed 35035123) recover 12 unit-equivalent coordinate solutions in about eight seconds on the original/preferred data. Each fits 323/354 cells. One gauge-zero representative, listed in coordinate order, is:

`ASVDOYNRBUJKZITCEHMFLWXQPG`

Absolute-residue powers for this representative, residues 0…22:

`18 0 0 25 25 7 6 17 14 24 6 7 6 25 17 25 6 6 6 25 10 7 14`

Only afterward, comparison with the reviewer cycle `DVSAGPQXWLFMHECTIZKJUBRNYO` gives exact equivalence: our coordinates = 25 times reviewer coordinates + 3 modulo 26. This is a reversed/rotated generator of the same cyclic subgroup. The abstract cycle coordinate has 12 unit multipliers and a rotation gauge; the physically ordered machine output alphabet is not yet uniquely known.

## Independent physical noisy control

A fresh genuine prepared Slovak UD TEST segment at offset 37000 supplies two 385-letter messages whose underlying texts differ by one leading character. Shared independent random mixed rings, two different random 23-of-52 physical masks and starts generate the ciphertexts. Each message resets at its own start, with one ordinary press per letter. Direct adjacent-distance walking and a separate absolute-coordinate inverse agree on both complete bodies. Twenty-five independently random symbol corruptions are then added to the second body.

The same blind recovery program, reading only the noisy pair, recovers the correct output-cycle coordinates up to unit/rotation, fitting 329/354 cells after 155 randomized bases. No true rings, shifts, masks or plaintext are supplied. This validates the cycle-recovery mechanism under real-wheel same-plaintext shifted-pair conditions with transcription noise; it does not validate discovery of the actual target masks or plaintext.

## Pixel collation and explicit variants

Source images were inspected first in full, then using ordinary cropped/resampled source pixels. No enhancement or reconstruction is used. Reading is explicitly prediction-assisted rather than blind, because the discrepant relation locations were already known. The checksum is used to locate candidate glyphs, never as sufficient evidence to change a clear glyph.

Twenty strong 351 edits and four strong 350 edits are supported by the enlarged printed forms. Exact locations, before/after readings, confidence, crop filenames and image hashes are in `pixel-manifest.json`. The four 350 edits are JBMLT (position 232 D→B), FQMVH (280 N→H), PLUSN (320 W→N) and CWJCB (321 G→C). Strong variants improve the originally fixed cycle to 347/354 cells and a fresh blind recovery yields the same 12 equivalent cycles.

Two additional 351 readings, position 82 V→N and 86 R→P, are obscured by the blue stamp and remain moderate-confidence alternatives. They are kept in a separately named variant. Conditional inclusion yields 349/354, matching the second-reader claim. This does not silently promote those two readings to fact. Remaining clear disagreements are not corrected merely to force the cycle.

## Framing extent

The recovered relation also matches 350 index 20 with 351 index 21. At the other end, 350 index 374 maps into 351 index 375, the first letter of its repeated suffix, and fails. Thus the common overlap supported by the data is 350 zero-based [20:374] paired with 351 [21:375], 354 cells. Strong variants match 348/354 there; strong-plus-moderate variants match 350/354. The corresponding prefix has only 1/20 matches and the nine later suffix-aligned cells have none.

This supports a possible 20-letter prefix / 10-letter suffix framing, with one initial unpaired 351 body character and one final unpaired 350 body character, but is not proof of a header format or plaintext. Remaining interior discrepancies in the moderate variant are 350 one-based positions 122, 230, 239 and 315, paired with 351 positions 123, 231, 240 and 316. Their literal printed readings are retained. Period powers have 14–16 matching observations per residue in this interval.

## Physical interpretation remains open

Common-cycle powers are displacement differences between two streams. They must not automatically be treated as single selected-stop jumps. A necessary sum-179 test over every unit multiplier and additive constant gives only one direct-arc positive-residue candidate (our multiplier 3, constant 11), with minimum sum 153. It contains two unit distances 1; both would require at least +26 to reach the minimum physical hole spacing 3, exceeding total 179. The parent independently checks all anchors and units by actual ordered-hole DP and also finds no direct-arc fit. It additionally reports no exact same-mask arbitrary-relative-phase fit. Those restricted failures do not exclude Kryha: two different 23-stop masks, procedure differences and remaining transcription uncertainty remain open.

For different schedules, the legitimate condition is K_j = D351(j+1)−D350(j)+constant, so K_(j+1)−K_j = arc351_(j+1)−arc350_j modulo 26. Both complete physical cycles advance 179. Absolute cyclic phase and relative ring/start offset are unknown. The parent is pursuing that coupled physical constraint independently.

## Reproduction and verified scope

Run `sh batches/kryha-shift23-sol61/reproduce.sh` from the repository root. It preserves all whole input variants, scans, deterministic controls, error-tolerant solver outputs, pixel crops and coordinate evidence. `verify.py` independently applies each recovered 26-cycle power to every observed pair, validates all 36 saved cycle/power rows, and confirms unit equivalence. No target plaintext or target full re-encryption is claimed. The previous offset-zero rejections do not apply to this offset-one relation and should not be used as a family exclusion.

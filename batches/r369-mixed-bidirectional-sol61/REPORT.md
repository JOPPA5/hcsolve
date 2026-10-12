# Mixed-width R: prefix-path and bidirectional calibration

This is a genuinely changed exact model for widths21/19/20 at110letters. Previous CP-SAT interval/rank and native forward-only models failed blind recovery; their records remain unchanged. This model encodes prefix path states `(k,longs)`: after k output chunks, how many are long. Exact domains need only303Boolean states, with one state per prefix depth, at most one per physical boundary, and selected-column edges connecting consecutive states. Common or progressive unknown alignment couples physical column0's actual prefix rank across stages. No numeric-header interpretation is supplied.

Cached direct endpoint support is imposed **both forwards and backwards**. First+middle placements require a supported final placement; last+middle placements require a supported first placement. There are4,892selected-start variables,686,394forward clauses and686,490reverse clauses. Cache sharing kept construction to52.74seconds, compared with approximately93seconds for the older forward-only model. No intermediate plaintext character variables or trajectory variables are introduced. Exactly one predictedN→literalU endpoint is allowed, with no preselected location or source correction.

Forty independently enumerated toy cases, widths2/3/4, common and progressive unknown alignment, agree exactly:17SAT/23UNSAT. All legal key triples are independently enumerated, and returned witnesses separately re-encrypt. A fresh matched110-letter/five-X control uses the fixed attributed365plaintext preparation and independent keys seed369612212001. Keys and n appear only in separate truth records and a known-key consistency check. They never initialize blind search. The known-key check is SAT, but that is not key recovery.

The global native blind control returned **UNKNOWN at120.01seconds** after52.74seconds construction. The positive calibration gate therefore prevented every actual target call.

One distinct bounded adaptation retains one compiled native solver across ascending unknown rank assumptions n1..19,8seconds each. This is neither a truth-rank hint nor a collection of fresh solver restarts. Construction took48.11seconds. The same frozen control was used for an algorithm comparison. Control rank1 is exactUNSAT; ranks2..19 are allUNKNOWN. Aggregate status is UNKNOWN, not UNSAT. No key was recovered and no actual369branch ran. Full timing/status rows are in `partition/control.json`.

Source/procedure inspection found no new licensed lexical or glyph correction. Removing WITPK from both copies gives an exact sequence relation: repeat payload = original first two payload groups + UCNIO + all remaining original payload groups. Both printed headers plan115letters, while original365physically lacks one five-letter group. The added group and indicator relocation should not be converted into invented plaintext or a numeric n hint.

One additional objective preparation constraint was checked: the two published sentences have55and50letters after72→SEDEMDVA. For both permitted X placements, independently encrypting the sentences as contiguous blocks fails per-block inventories in **both** sentence orders, far beyond the oneN/U discrepancy. The unique F bridges preferred plaintext position39 to cipher payload position93; unique B bridges plaintext98 to cipher55. Thus a simple sentence-by-sentence contiguous transposition shortcut is incompatible with these exact assumptions. This is not a claim about arbitrary segmentation or interleaving. Full counter differences and grouping proofs are in `source-check.json`.

Mixed-width historical R remains open: model consistency and finite audits do not supply an effective blind key-recovery algorithm at this budget. No target solution, historical key, source error or family exclusion is claimed. No marker/source file changed.

Reproduce:

- `python3 batches/r369-mixed-bidirectional-sol61/toy.py`
- `python3 batches/r369-mixed-bidirectional-sol61/run.py`
- `python3 batches/r369-mixed-bidirectional-sol61/partition/run.py`
- `python3 batches/r369-mixed-bidirectional-sol61/source_check.py`

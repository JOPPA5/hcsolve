# Reconstructed programmable Kryha wheel

The complete effective stepping family is recoverable from the primary NSA manual, printed p185/PDF p190. `wheel52.json` and CSV contain all52 adjacent distances. Index `a[h-1]` means displacement from hole h to the following hole, wrapping52→1. No missing values were guessed. Hole1→2 is4, and the full cycle is179, residue23 modulo26.

A selected set of active holes determines the steps: follow increasing hole numbers cyclically and sum every intervening adjacent distance until the next active hole. Individual steps cannot vary independently. For m active holes their sum is always179 and the mechanical state repeats after26m presses. This follows from coprimality of179 and26 and was checked independently. The memo's observed20–30 active stops is an operational German traffic restriction, not a universal mechanical limit.

`python3 batches/kryha-wheel-sol61/verify_geometry.py` checks27 primary memo fragments/arc sums, compares direct traversal against coordinate differences for1,000 independent random masks, and verifies the complete stop/relative-offset state period. The script also exports the table and cumulative effective coordinates. These coordinates count cipher-letter positions; actual physical angles were not measured. Converting them to angles would additionally assume the stated179-tooth drive geometry and gearing.

The memo says ordinary letters advance one active stop and a plaintext J word spacer advances two active stops. That skips the next **active stop**, not necessarily one physical hole. Uniform doublepress, ordinary stepping, and selective-J rules are distinct models. A ciphertext-position period cannot be assumed when extra presses depend on plaintext.

Increasing hole order is established by the primary tables. Physical handedness and which ring is designated plain/cipher require separate conventions. Reflecting both arbitrary ring-position permutations reverses the algebraic sign; do not treat signs as distinct cryptographic families. Initial before/after-press conventions can be absorbed into starting stop and ring offset when those are unknown.

The modern NR2417 transcript has a discrepancy in its provisional p7 hypothesis: it assigns16 to hole17→19, while the verified table gives6. Hole17→22 would give16, but that possible correction is NOT assumed. Other tested fragments match. The web search extraction also corrupts the middle20 table entries; use the actual scan/CSV.

This documents later programmable Standard geometry. It does not establish which version or operating procedure Slovak diplomatic traffic used in1943–1944, or identify any target cipher. No target plaintext/key is claimed.

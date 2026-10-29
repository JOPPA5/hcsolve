# HCP 494: a spacing alternative for the terminal pair

28 October 2026. Solver research helper; not an independent review. Prior knowledge of Daniel Bourdeau's proposed `ablauff` was retained, so this is not a blind decipherment.

## Result

No new word or nomenclator value is established. The useful additional observation concerns the **mechanism** required for the already known `ff` candidate: key 255's symbol can be parsed as **two crossed components whose arms overlap**, rather than two components plus separate joining strokes. Greater spacing between the components could therefore remove their contact without deleting an independent connector. This is a manual geometric hypothesis, not a demonstrated writing convention.

The target still resembles passage 1's XX and inverse key 254's XX=u directly. Consequently this check does **not** establish ff, recover a new key cell, or resolve the literal `ablauu` branch. It does suggest that describing ff as *only* a language-driven candidate requiring omitted connectors is stronger than the available evidence warrants: a specific original-shape mechanism is also possible. The existing provisional XX preference may be retained, with that qualification.

## Evidence and limits

- In the enlarged key-255 ff cell, each of two near-vertical staves is crossed by a rising diagonal. The diagonal arms contact the neighbouring stave. Treating those contacts as the overlap of two crossed components is geometrically possible; stroke order, pen lifts and the intended construction cannot be recovered from this photograph alone.
- Passage 2 has two separated crossed forms. Passage 1 and inverse key 254 also show that form for XX=u, including looped upper arms. These remain positive contrary evidence against uniquely selecting ff.
- The original st and tt symbols retain connections, as the prior audit correctly records. That observation tests a blanket connector-omission claim; it does not directly test spacing of overlapping crossed components in ff, because the st/tt structures are different.
- Neither key 253 nor the available key-266 image corroborates separated-cross ff. Their ff graphics differ: a triangle-like graphic in 253 and a different looped/stacked graphic in 266. No values from those tables are transferred.
- Reinspection of the complete key inventory and the original passage supplied no well-supported third terminal glyph or new segmentation. The visible `50 32 110` sequence remains consistent with `abl` under the existing table. No punctuation supports dividing 110 into separately enciphered units.
- The upper portion of the following au/8-like sign overlaps black annotation. Its lower loop alone does not decide au versus numeric 8; no upper stroke is reconstructed. The earlier au and null-8 branches are retained.
- Splitting the final pair into two independent single-X cipher letters is unsupported by the inspected key. The paired homophone XX represents one u; the special ff sign is another single token. No new single-X mapping is introduced.

## Reproduction

`ending_alternative_2026_10_28.py` creates ten exact crops, a comparison board and a JSON record from existing source images. It uses integer nearest-neighbour pixel duplication only, without ink removal, thresholding, rotation, sharpening or reconstruction. The full passage context and alphabet/syllable table are included to avoid relying on isolated signs.

Run with a Python environment containing Pillow. The environment used here was:

```text
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-494/work/ending_alternative_2026_10_28.py
```

All **431** existing source hashes passed. The board was visually inspected after rendering. Source files, current solution, current decoders, their plaintext branches and repository state markers were not changed by this helper.

Main image: `ending-alternative-spacing-board-2026-10-28.png`. Exact rectangles and source hashes: `ending-alternative-2026-10-28.json`.

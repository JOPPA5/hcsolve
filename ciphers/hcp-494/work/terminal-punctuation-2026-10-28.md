# Terminal punctuation microcheck — 28 October 2026

**Result: the extra dot does not establish ff instead of XX.** This finite check supplies no new accepted plaintext and changes no key, decoder or source.

The original P1 crossed pair has one trailing dot. The P2 terminal crossed pair has two solid, roughly baseline dots; faint specks above the second are not counted as punctuation. The two occurrences differ in position: P1 is internal to an encrypted stretch, whereas P2 is followed by the clear-text continuation. Consequently sign identity and terminal position are confounded. There is no independent same-writer ff token to disambiguate them.

The forward ff cell has no two-dot feature. The forward XX cell does not supply one either; an isolated faint lower-right speck is not identified as a meaningful glyph element. In the inverse table XX is followed by a dot before the clear u, consistent with table separation. None of these entries states a dot modifier that turns XX into ff.

Both 20-token cipher inserts were screened against the original. P1 visibly uses a trailing dot after each group, including XX and final 634. P2 does the same internally, but **leading 768 has a close dot followed by a farther vertical pair of marks** (approximately `. :`). Thus additional punctuation around an encrypted stretch is visible without any crossed-pair glyph. The P4 625 also has two vertical marks, an upper short dash and lower dot. Its P3 counterpart has one secure dot, with the upper area too uncertain to count as a colon. Original 834 has its close dot and a separate lower comma-like stroke.

All 26 catalogued large-code occurrences were screened; the occurrence table is in the accompanying JSON. Original P3 630 is obscured by the black annotation and is explicitly not confidently counted. No hidden strokes were reconstructed. The numeric controls are **not an exact horizontal two-dot duplicate** of the terminal pair, so they support only the limited finding that extra marks are not unique to ff. They do not prove the exact syntactic function of the terminal dots.

The economical interpretation is a group separator with additional punctuation, but this remains an interpretation. A special ff marker would require an independently established ff occurrence with the same dots, a written key rule, or a consistently contrasting set of original uses. None is available here. Both existing terminal branches must therefore remain open.

The comparison sheet is `terminal-punctuation-2026-10-28/punctuation-board.png`. Exact crop rectangles, integer scales, source hashes, the occurrence table and limitations are in `terminal-punctuation-2026-10-28.json`. All crops preserve original pixels and use only nearest-neighbour integer enlargement. Reproduce with the bundled Python on `work/terminal_punctuation_2026_10_28.py`; the script also verifies all 431 source hashes against the existing preservation manifest.

No new deciphered word is claimed, and this microcheck is not an independent solution review.

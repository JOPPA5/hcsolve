#!/usr/bin/env python3
"""Round-2 record: applies the review-1 corrections (checked against the scan) to
transcription.json and writes transcription-r2.json. Standard library only."""
import json
from pathlib import Path
W = Path(__file__).resolve().parent
rec = json.loads((W / 'transcription.json').read_text())
fixes = {  # row: (old, new, reason)
 'T03': [('n4 f6cd5 84d3', 'n4 qf6cd5 84d3', 'R1-1: Z glyph before f6cd5 was dropped -> ZVASTE')],
 'T04': [('{U1} t4fg2, gd5h3', '{U1} t4fg2, gd5h5', 'R1-2: final glyph is flagged 5 (E) -> KTERE')],
 'B01': [('d3 cm6t d4n', 'd3 c4s5 d4n', 'R1-3: glyphs are c 4 s 5 -> SICE (not SNAD)')],
 'B02': [('{A2}d58', 'rd58', 'R1-8: plain r, no CH tilde -> literal HTEL (editorial CHTEL)')],
 'B03': [('h2qm5r3', 'h2qm5h3', 'R1-7: tall looped h (R) -> literal RUZNERO (editorial RUZNEHO)')],
 'B04': [('d2 6q g', 't2 6q g', 'R1-6: bowl-less crossed t (D) -> literal DU (editorial TU)'),
         ('6c p2t5-84', '6s p2t5-84', 'R1-4: s (C) shape -> AC = ac')],
 'L09': [('q6{A1}n32s5m5r3', 'q6hn32s5m5r3', 'R1-9: tall looped h (R) -> ZARMOUCENEHO')],
}
log = []
for r in rec['rows']:
    for old, new, why in fixes.get(r['id'], []):
        assert r['cipher'].count(old) == 1, (r['id'], old)
        r['cipher'] = r['cipher'].replace(old, new); log.append(f"{r['id']}: {old!r} -> {new!r}  ({why})")
# U1: seven sign positions [blot] 3(overinked) g 3 m [blot] 5; blots restored as t (D) and s (C).
rec['uncertainties'] = {
 'U1': {'kind': 'restoration', 'glyphs': '{t}3g3m{s}5', 'plain_literal': '[D]OKON[C]E',
        'description': 'T04 retraced word: positions 1 and 6 are ink blots whose outlines are compatible with t (D) and s (C); position 2 overinked O; K O N E plain. Restored as DOKONCE, not read.'}}
rec['round'] = 2
rec['corrections_r2'] = log
(W / 'transcription-r2.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n')
print('\n'.join(log))

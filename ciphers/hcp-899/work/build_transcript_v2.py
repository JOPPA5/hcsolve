#!/usr/bin/env python3
"""One-off helper (Claude Opus 5.5, 2026-10-30): writes transcript_v2.json.
The shape tokens below were read glyph by glyph from enlarged crops of
source/picture.jpg; they are written here as shape names, not generated from
plaintext. 'obscured' lists 1-based glyph positions within a word whose walls or
tick count are partly covered by the HC Portal watermark (see SOLUTION.md)."""
import json, hashlib
from pathlib import Path
root = Path(__file__).resolve().parents[1]
old = json.loads((root/'work/transcript.json').read_text())
upper = [(r['label'], r['tokens']) for r in old['rows'] if r['region'] == 'upper']
W = lambda t, obs=(), note='': {'tokens': t, 'obscured': list(obs), 'note': note}
lower = [
 ('L1', [W('tbr3 bl3 lbr2 br2 br3 bl2 lbr2 box2'), W('box1 bl3 tr2'), W('lbr1 lbr2 box1'),
         W('tbl3 box3 tr2 lbr2 box2', (3, 4), 'T and E under watermark letters GPO: walls partly visible, ticks hidden')]),
 ('L2', [W('box1 tr3:umlaut box2 lbr1 br3 bl2 lbr2 box2', (3, 4), 'N and D partly under watermark letters RS/L')]),
 ('L3', [W('box1 bl3 tr2'), W('lbr1 lbr2 box2'), W('br1:umlaut tr3 bl1 tbr3 lbr2 bl3 box2'),
         W('tbr3 bl3 lbr2 br2', (2, 3), 'I under watermark P, E under watermark e'),
         W('tr3 box2 lbr1'), W('tbr2 tbr3 br1 tbl3', (2, 3), 'L and A under watermark letters e/t')]),
 ('L4', [W('lbr1 tr3'), W('box1 lbr2 bl3 box2'), W('tbr3 bl3 lbr2 br2 lbr2 tr1', note='LIEBES: 6 signs, re-read from scan after review 1 (work/crops/L4_word3_LIEBES.png)'),
         W('tr1 tr3:umlaut tr1 tr1 lbr2 tr1', (4,), 'fourth glyph partly under watermark C'),
         W('box1 br1:umlaut lbr1 br3 bl2 lbr2 box2', (7,), 'final N under watermark E')]),
 ('L5', [W('lbr1 lbr2 bl3 box2 lbr2 tbl3', (1,), 'first glyph: tick count unclear (1 or 2)'),
         W('lbr1 lbr2 box2 tbr2'), W('bl3 br3 bl2'), W('bl3 box1 box1 lbr2 tbl3 lbr1 br1 tbl3', (1,), 'I under watermark cross')]),
 ('L6', [W('tbr2 br1 tbr3 tr2'), W('bl3 tr1 tr2'), W('bl2 lbr2 tr3 tr2'), W('lbr1 lbr2 tbl3'),
         W('tlr2 bl3 box2 tr2 lbr2 tbl3 br1 br2 lbr2 box2 lbr1', (1, 2, 3, 10, 11), 'W/I/N under watermark S/3; N/D under watermark P/R')]),
 ('L7', [W('box1 box3:umlaut br3 bl2 tr2 lbr2'), W('bl1 lbr2 tbl3 box2 lbr2'), W('br2 lbr2 bl3', (3,), 'I under watermark diagonal'),
         W('lbr1 bl3 tbl3'), W('tr1 lbr2 bl3 box2', (2, 3), 'E right wall and I under watermark e/O')]),
 ('L8', [W('br2 lbr2 bl3'), W('lbr1 bl3 tbl3'), W('tr1 bl3 tr2 tl2 lbr2 box2'), W('box1 bl3 tr2'),
         W('lbr1 bl3 tbl3', (2, 3), 'I and R under watermark S/H'),
         W('tbr2 box3 tr1 lbr2 box2', (3,), 'S hidden under watermark T: restored')]),
 ('L9', [W('bl3 box1'), W('tlr1 lbr2 tbl3 tr2 tbl3 br1 tr3 tr2 lbr2 box2'),
         W('tbr2 br1:umlaut box1 box1 lbr2 tbl3 tbr3 lbr2 bl3 box2', (4, 5, 6), 'middle glyphs partly under watermark OF')]),
]
d = {
 'status': 'COMPLETE manual transcription (Claude Opus 5.5, 2026-10-30); upper rows carried over from earlier GPT work after re-checking on the scan',
 'key': old['key'], 'source_sha256': old['source_sha256'],
 'upper': [{'label': l, 'tokens': t} for l, t in upper],
 'lower': [{'label': l, 'words': w} for l, w in lower],
}
(root/'work/transcript_v2.json').write_text(json.dumps(d, ensure_ascii=False, indent=1))
print('written')

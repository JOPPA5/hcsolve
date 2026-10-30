#!/usr/bin/env python3
"""Geometry audit independent of language guesses; no decoding claim."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
# Coordinate tuples on a 3x3 lattice encode visible line segments only.
# A dot is a disconnected point and never changes a junction's degree.
base={
 'corner_br':[((-1,1),(1,1)),((1,1),(1,-1))],
 'cup':[((-1,-1),(-1,1)),((-1,1),(1,1)),((1,1),(1,-1))],
 'corner_bl':[((-1,-1),(-1,1)),((-1,1),(1,1))],
 'open_left':[((-1,-1),(1,-1)),((1,-1),(1,1)),((1,1),(-1,1))],
 'square':[((-1,-1),(1,-1)),((1,-1),(1,1)),((1,1),(-1,1)),((-1,1),(-1,-1))],
 'open_right':[((1,-1),(-1,-1)),((-1,-1),(-1,1)),((-1,1),(1,1))],
 'corner_tr':[((-1,-1),(1,-1)),((1,-1),(1,1))],
 'cap':[((-1,1),(-1,-1)),((-1,-1),(1,-1)),((1,-1),(1,1))],
 'corner_tl':[((-1,1),(-1,-1)),((-1,-1),(1,-1))],
 'angle_up':[((-1,1),(0,-1)),((0,-1),(1,1))],
 'angle_right':[((-1,-1),(1,0)),((1,0),(-1,1))],
 'angle_down':[((-1,-1),(0,1)),((0,1),(1,-1))],
 'angle_left':[((1,-1),(-1,0)),((-1,0),(1,1))],
 'tee_right':[((-1,-1),(-1,0)),((-1,0),(-1,1)),((-1,0),(1,0))]
}
def canonical(edges):return tuple(sorted(tuple(sorted(e)) for e in edges))
def transform(edges,rot,mirror):
 def p(pt):
  x,y=pt
  if mirror:x=-x
  for _ in range(rot):x,y=-y,x
  return x,y
 return canonical([(p(a),p(b)) for a,b in edges])
lookup={canonical(v):k for k,v in base.items()};out=[]
for m in [False,True]:
 for r in range(4):
  labels={k:lookup.get(transform(v,r,m),'UNMATCHED') for k,v in base.items()}
  out.append({'mirror':m,'quarter_turns':r,'labels':labels,
   'tee_in_conventional_cell_or_cross_family':any(transform(base['tee_right'],r,m)==canonical(v) for k,v in base.items() if k!='tee_right')})
assert not any(o['tee_in_conventional_cell_or_cross_family'] for o in out)
(P/'orientation-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('All 8 plane symmetries preserve the T-family mismatch under the recorded geometry.')
print('This is conditional on the manual T-form reading, not a proof that faint walls are absent.')
print('Rotations/mirroring and reverse reading preserve glyph-equality constraints of a MASC.')

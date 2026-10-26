"""Bounded geometric orientation screen, provisional visual tokens only."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
# Closed grid shape by its present edges; directional angles by vertex.
words=[['box','up','up','box','right','openB'],['box','openR','box.','box','openT','box','right','TR.','BL'],['openR','box.','box','up','right','TL','left'],['openR','box.','box','up','right','TL','left']]
edges={'BR':set('RB'),'BL':set('LB'),'TR':set('RT'),'TL':set('LT'),'openT':set('LBR'),'openB':set('LTR'),'openL':set('RTB'),'openR':set('LTB'),'box':set('LTRB')}
key=json.loads((p/'body-shapes.json').read_text())['key']
rmap={'T':'R','R':'B','B':'L','L':'T'}
a={'up':'T','right':'R','down':'B','left':'L'}
def xform(t,rot,mirror):
 dot=t.endswith('.');b=t.rstrip('.')
 if b in edges:s=edges[b].copy();typ='grid'
 else:s={a[b]};typ='angle'
 if mirror:s={('L' if x=='R' else 'R' if x=='L' else x) for x in s}
 for n in range(rot):s={rmap[x] for x in s}
 out=next(k for k,v in (edges if typ=='grid' else {k:{v} for k,v in a.items()}).items() if v==s)
 return out+('.' if dot else '')
out=[]
for mir in (False,True):
 for r in range(4):
  for rev in (False,True):
   ws=[w[::-1] for w in words[::-1]] if rev else words
   reading=' / '.join(''.join(key.get(xform(t,r,mir),'?') for t in w) for w in ws)
   out.append({'rotation':90*r,'mirror':mir,'reversed_order':rev,'reading':reading})
for x in out:print(x)
(p/'margin-orientations.json').write_text(json.dumps({'status':'provisional geometry test; not frozen transcription or plaintext','words':words,'outputs':out},indent=2)+'\n')

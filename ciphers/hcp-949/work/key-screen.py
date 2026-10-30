"""Finite generic alphabet-family screen, no plaintext cribs.
Exploratory score only; margin withheld. Detached strokes not letter-assigned.
"""
import json,itertools,math,heapq
from pathlib import Path
P=Path(__file__).resolve().parent
j=json.loads((P/'inventory.json').read_text());seq=[r['shape'] for r in j['records'] if not r['id'].startswith('margin.') and r['shape']!='I']
f=Path('batches/scoring-sol61/german/model4.tsv').open();head=f.readline().split();floor=float(head[1]);grams={}
for line in f:
 t,v=line.split();grams[t.upper()]=float(v)
def score(s):return sum(grams.get(s[i:i+4],floor) for i in range(len(s)-3))
grid={'BR':(-1,-1),'LBR':(0,-1),'BL':(1,-1),'TBR':(-1,0),'box':(0,0),'TBL':(1,0),'TR':(-1,1),'TLR':(0,1),'TL':(1,1)}
wedges={'down':(0,-1),'right':(-1,0),'left':(1,0),'up':(0,1)}
def tf(p,r,reflect):
 x,y=p
 if reflect:x=-x
 for _ in range(r):x,y=-y,x
 return x,y
pos=list(grid.values());wp=list(wedges.values());out=[]
# Two block orders, alphabets with/without J, alphabet shifts/reversal, grid and X dihedrals.
for alphabet in ['ABCDEFGHIJKLMNOPQRSTUVWXYZ','ABCDEFGHIKLMNOPQRSTUVWXYZ']:
 for revAlpha in [False,True]:
  aa=alphabet[::-1] if revAlpha else alphabet
  for shift in range(len(aa)):
   a=aa[shift:]+aa[:shift]
   for family in ['blocks','pairs']:
    for rg,fg,rw,fw in itertools.product(range(4),[False,True],range(4),[False,True]):
     key={}
     for name,p in grid.items():
      k=pos.index(tf(p,rg,fg))
      for dot in [0,1]:
       ix=2*k+dot if family=='pairs' else k+9*dot
       key[name+'.'*dot]=a[ix] if ix<len(a) else '?'
     for name,p in wedges.items():
      k=wp.index(tf(p,rw,fw))
      for dot in [0,1]:
       ix=18+2*k+dot if family=='pairs' else 18+k+4*dot
       key[name+'.'*dot]=a[ix] if ix<len(a) else '?'
     s=''.join(key[x] for x in seq)
     for reverse in [False,True]:
      ss=s[::-1] if reverse else s;sc=score(ss)
      info=dict(score=sc,text=ss,family=family,alphabet=alphabet,alphabet_reversed=revAlpha,shift=shift,grid=[rg,fg],wedge=[rw,fw],reverse=reverse,key=key)
      out.append(info)
out.sort(key=lambda d:d['score'],reverse=True)
(P/'key-screen-results.json').write_text(json.dumps(out[:40],indent=2)+'\n')
print('Cases',len(out),'body glyphs excluding detached strokes',len(seq))
for r in out[:12]:print(round(r['score'],2),r['text'],r['family'],r['alphabet'],r['shift'],r['grid'],r['wedge'],r['reverse'])

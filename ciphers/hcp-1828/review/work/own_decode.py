# Independent reviewer decode. Signs below were typed by the reviewer from review/work/crops,
# in reviewer's own shape labels, in scan order; no use of work/key.json or the solver's tokens
# except the final equality check. Reading order: reverse rows, reverse each row.
import sys,re,os,collections
R="""
PAREN3 IIIL STAR
GLASSES MOON LENS CLOSE
PAREN3 DMD MOON PRONG CAP III CROSSX HH
BOX PAREN3 BOX BOX PAREN3 LENS III II STAR PAREN3 LENS MOON GLASSES
NINE GRID STAR III PAREN3 CUP III GRID STAR II SWASH MOON NINE
GRID PAREN3 CAP HH PAREN3 GRID CROSSX PRONG GRID CROSSX SWASH LENS
LENS MOON PAREN3 PRONG III BOX STAR II PAREN3 CAP III GRID CROSSX
CUP GRID CROSSX CAP III NINE GRID STAR IIIL GRID PAREN3 BOX
NINE III SWASH STAR PAREN3 I STAR IIIL LENS STAR II
LENS MOON CLOSE BOX LEGS GRID STAR CAP III
"""
rows=[l.split() for l in R.strip().splitlines()]
seq=[s for r in rows[::-1] for s in r[::-1]]
print(len(seq),len(set(seq)))
# key recovered by reviewer's own hill climb (below), then fixed by reading:
K=dict(STAR='A',I='B',II='C',IIIL='D',PAREN3='E',CLOSE='F',CUP='G',CAP='H',CROSSX='I',LEGS='K',PRONG='L',GLASSES='M',GRID='N',MOON='O',LENS='R',BOX='S',III='T',SWASH='U',DMD='V',HH='W',NINE='Y')
pt=''.join(K[s] for s in seq); print(pt)
sol=[l.split() for l in open('../../work/transcription.txt') if l.strip() and not l.startswith('#')]
m={}
ok=True
for a,b in zip(rows,sol):
    if len(a)!=len(b): ok=False;print('len',a,b)
    for x,y in zip(a,b):
        m.setdefault(x,set()).add(y)
print('row lengths equal',ok,'map one-to-one',all(len(v)==1 for v in m.values()),len(set(next(iter(v)) for v in m.values())))
print(collections.Counter(pt).most_common())

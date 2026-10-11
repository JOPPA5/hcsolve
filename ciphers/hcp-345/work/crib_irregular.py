from pathlib import Path
from functools import lru_cache
p=Path(__file__).parent;g=p.joinpath('transcription.txt').read_text().split()
phrases=['effektivneleiposielamekurierom','effektivneleivamposielamekurierom','effektivneleivamposlemekurierom']
def solve(c,w,phrase,start):
 q,r=divmod(len(c),w);full=(1<<w)-1
 tests=[[(i//w,phrase[i-start]) for i in range(start,start+len(phrase)) if i%w==col] for col in range(w)]
 @lru_cache(None)
 def dfs(mask,off):
  if mask==full:return ()
  for col in range(w):
   if mask>>col&1:continue
   size=q+(col<r)
   if all(c[off+j]==letter for j,letter in tests[col]):
    tail=dfs(mask|1<<col,off+size)
    if tail is not None:return (col,)+tail
  return None
 key=dfs(0,0)
 if key is None:return None
 cols=['']*w;off=0
 for col in key:sz=q+(col<r);cols[col]=c[off:off+sz];off+=sz
 t=''.join(cols[j][i] for i in range(q+1) for j in range(w) if i<len(cols[j]))
 return key,t
cases={f'omit-{i+1}':''.join(v for j,v in enumerate(g) if j!=i) for i in [-1]+list(range(13))}
pt='effektivneleivamposielamekurieromprosimvaspotvrdteprijempenazix'[:60]
for w in [16,19,22]:cases[f'control-{w}']=''.join(pt[j::w] for j in range(w-1,-1,-1))
for name,c in cases.items():
 for phrase in phrases:
  hits=[]
  for w in range(16,23):
   for st in range(len(c)-len(phrase)+1):
    out=solve(c,w,phrase,st)
    if out is not None:hits.append((w,st,out))
  print(name,phrase,'count',len(hits),'examples',hits[:2],flush=True)

from pathlib import Path
import json,math
B=Path(__file__).resolve().parent;R=B.parents[1];G=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text());A=G['adjacent_distances'];CO=G['unwrapped_effective_coordinates'];SMALL=R/'batches/kryha-mask-sol61';LARGE=R/'ciphers/hcp-350/work'
def schedule(holes):
 m=len(holes);assert 20<=m<=30 and len(set(holes))==m and all(0<=h<52 for h in holes)
 out=[]
 for j,h in enumerate(holes):
  x=h;distance=0
  while True:
   distance+=A[x];x=(x+1)%52
   if x==holes[(j+1)%m]:break
  out.append(distance)
 assert sum(out)==179;return out

def encode(plain,P,O,holes):
 steps=schedule(holes);pi={c:i for i,c in enumerate(P)};oi={p:c for c,p in enumerate(O)};d=0;out=[]
 for i,c in enumerate(plain):out.append(chr(97+oi[(pi[ord(c)-97]+d)%26]));d=(d+steps[i%len(holes)])%26
 return ''.join(out)

def inverse(ct,P,O,holes):
 # Coordinates, independent of adjacency walking used by encoder.
 m=len(holes);start=holes[0];out=[]
 for i,c in enumerate(ct):
  h=holes[i%m];distance=CO[h]-CO[start]+(179 if h<start else 0)+179*(i//m);out.append(chr(97+P[(O[ord(c)-97]-distance)%26]))
 return ''.join(out)

def models():
 return {n:{s:float(v)for s,v in(line.split()for line in (SMALL/f'model{n}.tsv'if n<4 else LARGE/f'ring-{n}grams.tsv').read_text().splitlines())}for n in range(2,6)}
def score(texts,models):return sum(w*sum(models[n].get(t[i:i+n],-n)for i in range(len(t)-n+1))for t in texts for n,w in [(2,.1),(3,.15),(4,.4),(5,.8)])
def check(row,cts,tables):
 P=row['input_slots'];O=row['output_positions'];holes=row['holes'];texts=row['plaintexts'];assert sorted(P)==sorted(O)==list(range(26));assert len(texts)==len(cts)==2;schedule(holes)
 for ct,text in zip(cts,texts):assert len(text)==len(ct)==385 and encode(text,P,O,holes)==ct and inverse(ct,P,O,holes)==text
 err=abs(score(texts,tables)-row['score']);assert err<.13,(err,row['score']);return err

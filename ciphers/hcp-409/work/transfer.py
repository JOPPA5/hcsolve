from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
ct=''.join((out/'transcription.txt').read_text().split())
model={g:float(v) for g,v in (l.split() for l in (root/'ciphers/hcp-350/work/ring-4grams.tsv').read_text().splitlines())}
def score(p):return sum(model.get(p[i:i+4],-8)for i in range(len(p)-3))/max(1,len(p)-3)
results=[]
for n in [350,351,374]:
 f=root/f'ciphers/hcp-{n}/work'/('key.json' if n==374 else 'kryha-decipherment/key.json');k=json.loads(f.read_text())
 if n==374:
  pp=k['input_positions'];P=['']*26
  for i,pos in enumerate(pp):P[pos]=chr(97+i)
  O=k['output_positions'];holes=k['holes_zero_based']
 else:P=[chr(97+i)for i in k['P']];O=k['O'];holes=k['holes']
 edges=k['adjacent_distances'];steps=[]
 for a,b in zip(holes,holes[1:]+holes[:1]):
  s=0
  while a!=b:s+=edges[a];a=(a+1)%52
  steps.append(s)
 for omit in [0,5]:
  for phase in range(len(holes)):
   for d0 in range(26):
    d=d0;p=''
    for i,c in enumerate(ct[omit:]):
     p+=P[(O[ord(c)-97]-d)%26];d+=steps[(phase+i)%len(steps)]
    results.append(dict(key=n,omit=omit,phase=phase,displacement=d0,score=score(p),plaintext=p))
results.sort(key=lambda r:-r['score']);(out/'transfer-results.json').write_text(json.dumps(dict(length=len(ct),cases=len(results),source_sha256=hashlib.sha256((out.parent/'source/cryptogram.jpg').read_bytes()).hexdigest(),best=results[:30]),indent=2)+'\n')
for r in results[:5]:print(r)

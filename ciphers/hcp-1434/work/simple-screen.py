from pathlib import Path
import json,hashlib,itertools,string
p=Path(__file__).resolve().parent.parent
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest,name
x=json.loads((p/'work/transcription.json').read_text())
a=string.ascii_uppercase
def caesar(s,n): return s.translate(str.maketrans(a,a[n:]+a[:n]))
def raildecrypt(s,k):
 path=list(range(k))+list(range(k-2,0,-1))
 order=[path[i%len(path)] for i in range(len(s))]
 rails={};start=0
 for r in range(k):
  n=order.count(r);rails[r]=iter(s[start:start+n]);start+=n
 return ''.join(next(rails[r]) for r in order)
choices=[]
for row in x['rows']:
 choices.append([''.join(v) for v in itertools.product(*[v if isinstance(v,list) else [v] for v in row])])
for n,(r1,r2) in enumerate(itertools.product(*choices),1):
 s=r1+r2
 print(f'VARIANT {n}: {r1} / {r2}; letters={len(s)}')
 for shift in range(26): print(f'Caesar+{shift:02}: {caesar(s,shift)}')
 print('Atbash:',s.translate(str.maketrans(a,a[::-1])))
 print('Reverse-all:',s[::-1]);print('Reverse-rows:',r1[::-1]+r2[::-1])
 print('Odd/even:',s[::2]+' / '+s[1::2])
 print('Interleave-rows:',''.join(''.join(t) for t in itertools.zip_longest(r1,r2,fillvalue='')))
 for k in range(2,7): print(f'Railfence-decrypt-{k}: {raildecrypt(s,k)}')
print('Sourcehashes passed. Bounded candidate listing, not automated languageproof.')

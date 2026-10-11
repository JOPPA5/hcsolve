from model import solve
from pathlib import Path
import random,json,unicodedata
B=Path(__file__).resolve().parent
src=Path('batches/kryha373-collation-sol61/plaintext-typed.txt').read_text();raw=src.split('6.000')[0];norm=lambda t:''.join(c for c in unicodedata.normalize('NFD',t.lower())if'a'<=c<='z');p=norm(raw);rng=random.Random(3733741011);P=rng.sample(range(26),26);O=rng.sample(range(26),26);m=23;K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)};c=''.join(inv[(P[ord(a)-97]+K[i%m]+179*(i//m))%26]for i,a in enumerate(p));(B/'control-truth.json').write_text(json.dumps(dict(p=p,c=c,P=P,O=O,K=K,m=m),indent=2)+'\n')
r=solve(p,c,m,10000);(B/'control-fullfit.json').write_text(json.dumps(r,indent=2)+'\n');print('full',len(p),r['status'],r['seconds'],flush=True)
if r['status']=='sat':
 q=solve(p,c,m,10000,blocked=r);(B/'control-second-witness.json').write_text(json.dumps(q,indent=2)+'\n');print('second',q['status'],flush=True)
r=solve(p[:-20],c[:-20],m,10000,heldout=(p,c));(B/'control-heldout.json').write_text(json.dumps(r,indent=2)+'\n');print('heldout',r['status'],r.get('heldout_matches'),r.get('heldout_total'),flush=True)

from pathlib import Path
from itertools import product
from collections import Counter
import json,unicodedata,random,hashlib,time
from engine import fit
from crt import solve
b=Path(__file__).resolve().parent;src=Path('batches/kryha373-collation-sol61');raw=(src/'plaintext-typed.txt').read_text().split('6.000')[0];ct=(src/'ciphertext650.txt').read_text().strip();assert raw.count(',')==1
norm=lambda s:''.join(c for c in unicodedata.normalize('NFD',s.lower())if'a'<=c<='z')
preps=[]
for short,ji,marker in product([False,True],[False,True],['j','x']):
 text=raw.replace('Ústredni','Ústreni')if short else raw
 if ji:text=text.replace('j','i').replace('J','I')
 p=norm(text.replace(',',marker));assert len(p)==(93 if short else 94);preps.append(dict(short=short,natural_j_to_i=ji,comma_marker=marker,p=p))
def search(p,c,m):
 r=fit(p,c,list(range(len(p))),m)
 if r['status']=='bounded-out':
  bounds=r;r=solve(p,c,m,1000);r['vector_bound']=bounds
 r['m']=m;return r
def verify(r,p,c):
 if r['status']!='sat':return
 P,O,K,m=r['P'],r['O'],r['K'],r['m'];ip={v:chr(97+i)for i,v in enumerate(P)};io={v:chr(97+i)for i,v in enumerate(O)};enc=''.join(io[(P[ord(a)-97]+K[i%m]+179*(i//m))%26]for i,a in enumerate(p));dec=''.join(ip[(O[ord(a)-97]-K[i%m]-179*(i//m))%26]for i,a in enumerate(c));assert enc==c and dec==p;r['independent_full_prefix_encoder_inverse']=True
if __name__=='__main__':
 (b/'input.json').write_text(json.dumps(dict(source_raw_prefix=raw,comma_count=1,preparations=preps,offsets=list(range(26)),periods=list(range(2,53)),glyphs=[['l','i'],['e','a']],cycle_total=179,source_hashes={str(src/n):hashlib.sha256((src/n).read_bytes()).hexdigest()for n in ['plaintext-typed.txt','ciphertext650.txt']}),indent=2,ensure_ascii=False)+'\n')
 geo=json.loads(Path('batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];coords=geo['unwrapped_effective_coordinates'];controls=[]
 for j,prepindex in enumerate([2,6]):
  f=b/f'control{j}.json'
  if f.exists():r=json.loads(f.read_text())
  else:
   p=preps[prepindex]['p'];rng=random.Random(373426612+j);m=[23,20][j];P=rng.sample(range(26),26);O=rng.sample(range(26),26);holes=sorted(rng.sample(range(52),m));phase=rng.randrange(m);holes=holes[phase:]+holes[:phase];invO={v:chr(97+i)for i,v in enumerate(O)};disp=0;c=''
   for i,a in enumerate(p):
    c+=invO[(P[ord(a)-97]+disp)%26];h=holes[i%m];end=holes[(i+1)%m]
    while h!=end:disp+=edges[h];h=(h+1)%52
   alt=''.join(invO[(P[ord(a)-97]+coords[holes[i%m]]-coords[holes[0]]+179*(holes[i%m]<holes[0])+179*(i//m))%26]for i,a in enumerate(p));assert alt==c;offset=[5,6][j];framed=''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(offset))+c+'q'*25
   (b/f'control{j}-input.json').write_text(json.dumps(dict(p=p,framed=framed,offset_family=list(range(26)),period_family=list(range(2,53))),indent=2)+'\n');(b/f'control{j}-truth.json').write_text(json.dumps(dict(P=P,O=O,m=m,holes=holes,offset=offset,c=c,independent_physical_encoder_exact=True),indent=2)+'\n');rows=[]
   for off,period in product(range(26),range(2,53)):
    rr=search(p,framed[off:off+len(p)],period);verify(rr,p,framed[off:off+len(p)]);rows.append(dict(offset=off,result=rr))
   r=dict(cases=rows,planted_full_model_accepted=any(x['offset']==offset and x['result']['m']==m and x['result']['status']=='sat'for x in rows));f.write_text(json.dumps(r,indent=2)+'\n')
  assert r['planted_full_model_accepted'];controls.append(r);print('control',j,'PASS',flush=True)
 # High-value source350-like commaJ/naturalJ->I offsets5/6, periods16..30 first.
 priority=[(j,off,a,z,m)for j,pr in enumerate(preps)if pr['natural_j_to_i']and pr['comma_marker']=='j'for off in [5,6]for a,z in product(['l','i'],['e','a'])for m in range(16,31)]
 allcases=product(range(8),range(26),['l','i'],['e','a'],range(2,53));cases=priority+list(allcases);seen=set();f=b/'results.jsonl'
 if f.exists():seen={tuple(json.loads(s)['case_id'])for s in f.read_text().splitlines()}
 start=time.monotonic()
 for cid in cases:
  if cid in seen:continue
  j,off,a,z,m=cid;pr=preps[j];cc=list(ct);cc[52]=a;cc[89]=z;cc=''.join(cc);p=pr['p'];c=cc[off:off+len(p)];r=search(p,c,m);verify(r,p,c);r.update(case_id=cid)
  if r['status']=='sat':
   ip={v:chr(97+i)for i,v in enumerate(r['P'])};r['full_context_decode_after_offset']=''.join(ip[(r['O'][ord(ch)-97]-r['K'][i%m]-179*(i//m))%26]for i,ch in enumerate(cc[off:]));print('SAT',cid,flush=True)
  with f.open('a')as out:out.write(json.dumps(r)+'\n')
  seen.add(cid)
  if len(seen)%500==0:print('progress',len(seen),'elapsed',round(time.monotonic()-start,1),flush=True)
 rows=[json.loads(s)for s in f.read_text().splitlines()];(b/'summary.json').write_text(json.dumps(dict(cases=len(rows),expected=42432,statuses=dict(Counter(r['status']for r in rows)),unknown_cases=[r['case_id']for r in rows if r['status']=='unknown'],sat_cases=[r['case_id']for r in rows if r['status']=='sat']),indent=2)+'\n')

from pathlib import Path
import sys,json,unicodedata,re,random,time,hashlib,os
import numpy as np
B=Path(__file__).resolve().parent;sys.path.insert(0,str(Path('batches/kryha373-comma-marker-sol61').resolve()))
from engine import fit
from crt import solve
raw=Path('batches/kryha373-collation-sol61/plaintext-typed.txt').read_text();tail=raw[raw.index('Vyšetri'):].strip();tail=re.sub(r'-\s*\n','',tail)
norm=lambda s:''.join(c for c in unicodedata.normalize('NFD',s.lower())if 'a'<=c<='z')
ct=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip();assert len(ct)==650
preps=[dict(j_to_i=ji,q_syndikatu=q,p=norm(tail.replace('Syndikátu','QSyndikátuQ')if q else tail).replace('j','i')if ji else norm(tail.replace('Syndikátu','QSyndikátuQ')if q else tail))for ji in [False,True]for q in [False,True]]
erasures={53,90,126,233,268,270,478,479,504}
def save(n,x):(B/(n+'.json')).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def linear(p,c,ix,m):
 n=52+m;a=np.zeros((len(p)+2,n+1),dtype=np.int64)
 for k,(x,y,t)in enumerate(zip(p,c,ix)):a[k,ord(y)-97+26]+=1;a[k,ord(x)-97]-=1;a[k,52+t%m]-=1;a[k,-1]=179*(t//m)
 a[-2,0]=1;a[-1,26]=1
 for q in [2,13]:
  z=a%q;at=0
  for col in range(n):
   nz=np.flatnonzero(z[at:,col])
   if not len(nz):continue
   k=at+int(nz[0]);z[[at,k]]=z[[k,at]];z[at]=(z[at]*pow(int(z[at,col]),-1,q))%q
   rows=np.flatnonzero(z[:,col]);rows=rows[rows!=at];z[rows]=(z[rows]-z[rows,col,None]*z[at])%q;at+=1
   if at==len(z):break
  if np.any((~np.any(z[:,:n],axis=1))&(z[:,-1]!=0)):return False
 return True

def search(p,c,ix,m):
 if not linear(p,c,ix,m):return dict(status='unsat',reason='independent numpy modular linear inconsistency',m=m)
 r=fit(p,c,ix,m)
 if r['status']=='bounded-out':
  bound=r;r=solve(p,c,m,timeout=1000,press_indices=ix);r['vector_bound']=bound
 r['m']=m;return r

def enc(p,P,O,K,ix):
 inv={x:chr(97+i)for i,x in enumerate(O)};return ''.join(inv[(P[ord(a)-97]+K[t%len(K)]+179*(t//len(K)))%26]for a,t in zip(p,ix))
def verify(r,p,c,ix):
 if r['status']=='sat':
  assert enc(p,r['P'],r['O'],r['K'],ix)==c
  ip={x:chr(97+i)for i,x in enumerate(r['P'])};assert ''.join(ip[(r['O'][ord(a)-97]-r['K'][t%r['m']]-179*(t//r['m']))%26]for a,t in zip(c,ix))==p
  r['independent_unerased_encoder_inverse']=True

save('inputs',dict(published_tail=tail,preparations=preps,ciphertext=ct,erased_absolute_onebased=sorted(erasures),periods=list(range(2,53)),offset_bounds=[0,650-len(preps[0]['p'])],source_hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in [Path('batches/kryha373-collation-sol61/plaintext-typed.txt'),Path('batches/kryha373-collation-sol61/ciphertext650.txt')]}))
(B/'owned-pid.txt').write_text(str(os.getpid()))
geo=json.loads(Path('batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];coords=geo['unwrapped_effective_coordinates'];controls=[]
for j,m in enumerate([23,20,30]):
 rng=random.Random(373612901+j);p=preps[j%4]['p'];P=rng.sample(range(26),26);O=rng.sample(range(26),26);holes=sorted(rng.sample(range(52),m));phase=rng.randrange(m);holes=holes[phase:]+holes[:phase];disp=0;c='';inv={x:chr(97+i)for i,x in enumerate(O)}
 for i,a in enumerate(p):
  c+=inv[(P[ord(a)-97]+disp)%26];h=holes[i%m];end=holes[(i+1)%m]
  while h!=end:disp+=edges[h];h=(h+1)%52
 K=[(coords[h]-coords[holes[0]]+179*(h<holes[0]))%26 for h in holes];assert enc(p,P,O,K,range(len(p)))==c
 off=[437,441,439][j];framed=''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(off))+c;ix=[i for i in range(len(p))if off+i+1 not in erasures];pp=''.join(p[i]for i in ix);cc=''.join(c[i]for i in ix);r=search(pp,cc,ix,m);verify(r,pp,cc,ix)
 if r['status']=='sat':r['full_control_cipher_exact']=enc(p,r['P'],r['O'],r['K'],range(len(p)))==c
 save(f'control{j}-truth',dict(P=P,O=O,K=K,holes=holes,m=m,offset=off,p=p,c=c,framed=framed));save(f'control{j}',r);controls.append(r);print('control',j,r['status'],r.get('full_control_cipher_exact'),len(p),flush=True)
assert all(r['status']=='sat'for r in controls),'Calibration gate failed'
# Priority last40 legal offsets and periods20..30; then complete declared family.
cases=[]
for j,pr in enumerate(preps):
 lim=650-len(pr['p']);cases.extend((j,off,m)for off in range(max(0,lim-39),lim+1)for m in range(20,31))
for j,pr in enumerate(preps):cases.extend((j,off,m)for off in range(651-len(pr['p']))for m in range(2,53))
seen=set();counts={};start=time.monotonic();f=B/'results.jsonl'
if f.exists():
 for s in f.read_text().splitlines():r=json.loads(s);seen.add(tuple(r['case']));counts[r['status']]=counts.get(r['status'],0)+1
for cid in cases:
 if cid in seen:continue
 j,off,m=cid;p=preps[j]['p'];ix=[i for i in range(len(p))if off+i+1 not in erasures];pp=''.join(p[i]for i in ix);cc=''.join(ct[off+i]for i in ix);r=search(pp,cc,ix,m);verify(r,pp,cc,ix);r.update(case=cid,erased_count=len(p)-len(ix))
 if r['status']=='sat':
  ip={x:chr(97+i)for i,x in enumerate(r['P'])};r['context_decode']=''.join(ip[(r['O'][ord(a)-97]-r['K'][t%m]-179*(t//m))%26]for t,a in enumerate(ct[off:]));save('SAT-'+str(cid),r);print('SAT',cid,flush=True)
 with f.open('a')as out:out.write(json.dumps(r)+'\n')
 seen.add(cid);counts[r['status']]=counts.get(r['status'],0)+1
 if len(seen)%2000==0:print('progress',len(seen),counts,round(time.monotonic()-start,1),flush=True);save('summary',dict(cases=len(seen),statuses=counts,complete=False))
save('summary',dict(cases=len(seen),statuses=counts,complete=True,seconds=time.monotonic()-start));print('COMPLETE',len(seen),counts,flush=True)

"""Bounded context framing experiment; no claim that skipped symbols are indicators."""
from pathlib import Path
import sys,json,random,time
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha-knownpair373-sol61'))
from crt import solve
ps=json.loads((root/'batches/kryha374-freecycle-main/preparations.json').read_text())
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower()
# Independently encrypt a matched prefix and prepend13 unrelated ciphertext symbols.
# The search receives only the prep and complete ciphertext, not the offset/key.
rng=random.Random(37437362140);p=ps[0]['p'];m=23;P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)}
c=''.join(inv[(P[ord(a)-97]+K[i%m]+179*(i//m))%26]for i,a in enumerate(p));framed=''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(13))+c
controls=[]
for offset in range(26):
 if len(framed)-offset<len(p):continue
 r=solve(p,framed[offset:offset+len(p)],m,2000);controls.append(dict(offset=offset,result=r))
(out/'control.json').write_text(json.dumps(dict(p=p,framed_ciphertext=framed,planted_offset=13,P=P,O=O,K=K,m=m,cases=controls),indent=2)+'\n')
assert any(x['offset']==13 and x['result']['status']=='sat'for x in controls),'offset calibration fails; no actualtarget'
print('matched framed control passed',flush=True)
results=[];t=time.monotonic()
# Only NEW offsets:0 and5 were already tested. Everycharacter offset1..25 is explicit.
for prep in ps:
 for omit in [i for i in range(1,26)if i!=5]:
  for a in ['l','i']:
   for b in ['e','a']:
    cc=list(ct);cc[52]=a;cc[89]=b;cc=''.join(cc)
    for m in range(2,53):
     c=cc[omit:omit+len(prep['p'])];r=solve(prep['p'],c,m,1500);case=dict(p=prep['p'],offset=omit,glyph53=a,glyph90=b,m=m,result=r)
     if r['status']=='sat':
      P,O,K=r['P'],r['O'],r['K'];inverse={v:chr(97+i)for i,v in enumerate(P)}
      r['full_context_decode_after_offset']=''.join(inverse[(O[ord(z)-97]-K[i%m]-179*(i//m))%26]for i,z in enumerate(cc[omit:]));print('SAT',case,flush=True)
     results.append(case)
  (out/'results.json').write_text(json.dumps(results,indent=2)+'\n');print('progress',len(results),'seconds',round(time.monotonic()-t,1),flush=True)
(out/'summary.json').write_text(json.dumps(dict(cases=len(results),counts={s:sum(x['result']['status']==s for x in results)for s in ['sat','unsat','unknown']},seconds=time.monotonic()-t),indent=2)+'\n')

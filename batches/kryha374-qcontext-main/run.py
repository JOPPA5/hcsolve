"""HCP374 context attack using the disclosed published HCP373 prefix.

Q around Roessner/Madrid is a conditional transfer of a primary R preparation
rule, not evidence that the Madrid machine adopted it. No solved cipher dir.
"""
from pathlib import Path
import sys,re,json,random,unicodedata,hashlib,time
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha-knownpair373-sol61'))
from crt import solve
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower())if'a'<=c<='z')
source=(root/'batches/kryha373-collation-sol61/plaintext-typed.txt').read_text()
prefix=source.split('6.000')[0];words=[norm(x)for x in re.findall(r'[^\W\d_]+',prefix,re.UNICODE)]
assert words[:2]==['roessner','madrid']
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower()
assert len(ct)==650
preps=[]
for shared in [False,True]:
 for amended in [True,False]:
  for ji in [False,True]:
   ws=words.copy()
   assert ws[3]=='ustredni'
   if not amended:ws[3]='ustreni'
   ws[:2]=['q'+w+'q'for w in ws[:2]]
   p=''.join(ws)
   if shared:p=p.replace('qq','q')
   if ji:p=p.replace('j','i')
   preps.append(dict(p=p,shared_Q_boundary=shared,handwritten_D_retained=amended,natural_J_to_I=ji))
assert len(set(a['p']for a in preps))==8
(out/'preparations.json').write_text(json.dumps(dict(raw_published_prefix=prefix,variants=preps,source_primary_rule='HistoCrypt2020 printed23, proper nouns divided by Q; its adoption by373 is NOT established'),indent=2,ensure_ascii=False)+'\n')
# Two fresh independent controls exercise natural-J variants and a
# source-word prefix length matched to this variant. No truth supplied to fit.
controls=[]
for index,(prep,m)in enumerate(zip(preps[:2],[23,30])):
 rng=random.Random(374373261+index);p=prep['p'];P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inverse={v:chr(97+i)for i,v in enumerate(O)}
 c=''.join(inverse[(P[ord(a)-97]+K[i%m]+179*(i//m))%26]for i,a in enumerate(p))
 result=solve(p,c,m,5000);assert result['status']=='sat'
 controls.append(dict(plaintext=p,ciphertext=c,planted_P=P,planted_O=O,planted_K=K,result=result))
(out/'controls.json').write_text(json.dumps(controls,indent=2)+'\n')
print('Fresh matched Q-prefix controls SAT; beginning finite source cases',flush=True)
results=[];started=time.monotonic()
for prep in preps:
 for omit in [0,5]:
  for first in ['l','i']:
   for second in ['e','a']:
    cipher=list(ct);assert cipher[52]=='l'and cipher[89]=='e';cipher[52]=first;cipher[89]=second;cipher=''.join(cipher)
    for m in range(2,53):
     c=cipher[omit:omit+len(prep['p'])];r=solve(prep['p'],c,m,2000)
     case=dict(prep=prep,omit=omit,glyph53=first,glyph90=second,m=m,result=r)
     if r['status']=='sat':
      r['withheld20']=solve(prep['p'][:-20],c[:-20],m,2000,heldout=(prep['p'],c))
      P,O,K=r['P'],r['O'],r['K'];inverse={v:chr(97+i)for i,v in enumerate(P)}
      r['full_context_decode']=''.join(inverse[(O[ord(a)-97]-K[i%m]-179*(i//m))%26]for i,a in enumerate(cipher[omit:]))
      print('SAT',case,flush=True)
     results.append(case)
    (out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(len(results),prep['shared_Q_boundary'],prep['handwritten_D_retained'],prep['natural_J_to_I'],omit,first,second,'elapsed',round(time.monotonic()-started,1),flush=True)
(out/'summary.json').write_text(json.dumps(dict(cases=len(results),counts={x:sum(r['result']['status']==x for r in results)for x in ['sat','unsat','unknown']},elapsed_seconds=time.monotonic()-started,original_cipher_sha256=hashlib.sha256(ct.encode()).hexdigest(),targets_written=False),indent=2)+'\n')

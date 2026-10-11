from pathlib import Path
import random,json
p=Path(__file__).parent;groups=(p/'transcription.txt').read_text().split()
def compatible(a,b):
 d={};e={}
 for x,y in zip(a,b):
  if x in d and d[x]!=y:return False
  if y in e and e[y]!=x:return False
  d[x]=y;e[y]=x
 return True
def hits(s,crib):return [{'offset':i,'cipher':s[i:i+len(crib)]} for i in range(len(s)-len(crib)+1) if compatible(s[i:i+len(crib)],crib)]
phrases=['effektivnelei','efektivnelei','kurierom','vamposleme','vamposielame'];report={}
for omit in [-1]+list(range(13)):
 s=''.join(g for i,g in enumerate(groups) if i!=omit)
 for rev in [False,True]:
  ct=s[::-1] if rev else s;report[f'omit-{omit+1}-reverse-{rev}']={crib:hits(ct,crib) for crib in phrases}
rng=random.Random(61034517);alphabet='abcdefghijklmnopqrstuvwxyz';mapping=dict(zip(alphabet,rng.sample(alphabet,26)));plain=('effektivneleivamposielamekurieromkontrolnytextbolvytvorenynezavisleodzadania')[:65];ct=''.join(mapping[x] for x in plain)[::-1]
assert any(h['offset']==0 for h in hits(ct[::-1],'effektivnelei'))
report['independent_control']={'plaintext':plain,'ciphertext_reverse':ct,'key':mapping,'expected_crib_offset':0,'recovered_crib_offset':hits(ct[::-1],'effektivnelei')}
(p/'substitution-crib-pattern-results.json').write_text(json.dumps(report,indent=2)+'\n')
for name,data in report.items():
 if name!='independent_control':
  print(name,'; '.join(f'{crib}:{len(v)}' for crib,v in data.items()))
print('Synthetic reverse-MASC control finds true offset0; not a target solution')

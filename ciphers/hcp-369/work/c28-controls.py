import json,random,subprocess,unicodedata
from pathlib import Path
p=Path(__file__).parent
alpha='abcdefghijklmnopqrstuvwxyz{|'
def norm(s):
 s=s.lower().replace('č','{').replace('š','|')
 return ''.join(c for c in unicodedata.normalize('NFD',s) if c in alpha)
texts=[norm('Minister zahraničných vecí žiada okamžite oznámiť stanovisko vašej vlády k navrhovanej dohode a poslať podrobnú správu kuriérom do Bratislavy.'),norm('Vyslanectvo v Bukurešti potvrdzuje prijatie vašej správy a oznamuje že rokovanie s ministrom zahraničných vecí sa uskutoční zajtra dopoludnia.')]
rows=[]
for i,text in enumerate(texts):
 text=text[:115];key=list(alpha);random.Random(2844+i).shuffle(key);c=''.join(key[alpha.index(x)] for x in text)
 f=p/f'c28-control-{i}.txt';f.write_text(c+'\n')
 r=subprocess.run([str(p/'mono-c28'),'batches/scoring-sol61/frequency',str(f),'40'],capture_output=True,text=True)
 (p/f'c28-control-{i}-result.txt').write_text(r.stdout+'\n'+r.stderr)
 fields=r.stdout.strip().split();bestkey=fields[1];fold=lambda s:s.replace('{','c').replace('|','s')
 found=fields[2];neighbors=[]
 for a in range(28):
  for b in range(a,28):
   k=list(bestkey);k[a],k[b]=k[b],k[a];d=''.join(k[alpha.index(x)] for x in c)
   if fold(d)==fold(text):neighbors.append([a,b,d])
 rows.append(dict(index=i,plaintext_encoded=text,ciphertext=c,planted_key=''.join(key),found=found,exact_folded=found==fold(text),true_folded_in_blind_neighbors=bool(neighbors),matching_neighbors=neighbors))
 (p/'c28-controls.json').write_text(json.dumps(rows,indent=2))
 print(i,rows[-1]['exact_folded'],rows[-1]['true_folded_in_blind_neighbors'],flush=True)

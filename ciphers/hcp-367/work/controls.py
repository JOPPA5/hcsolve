from pathlib import Path
import unicodedata,random,subprocess,json
p=Path(__file__).parent;root=p.parents[2]
lines=[l[9:] for l in (root/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines() if l.startswith('# text = ')]
s=''.join(c for c in unicodedata.normalize('NFD',''.join(lines).lower()) if 'a'<=c<='z');rng=random.Random(367981)
results=[]
for i,w in enumerate([11,19]):
 plain=s[i*80:i*80+80];key=list(range(w));rng.shuffle(key);ct=''.join(plain[j::w] for j in key)
 (p/f'control-{w}-plain.txt').write_text(plain+'\n');(p/f'control-{w}-cipher.txt').write_text(ct+'\n')
 output=subprocess.check_output([str(p/'attack'),str(p),'normal',f'control-{w}-cipher.txt'],text=True);(p/f'control-{w}-results.txt').write_text(output)
 target=[l.split(' ',3) for l in output.splitlines() if l.startswith(str(w)+' ')][0]
 results.append({'width':w,'plaintext':plain,'encryption_column_order':key,'recovered':target[3]==plain,'correct_positions':sum(a==b for a,b in zip(target[3],plain)),'found_score':float(target[1]),'candidate':target[3]})
 print(json.dumps(results[-1]),flush=True)
(p/'control-summary.json').write_text(json.dumps(results,indent=2)+'\n')

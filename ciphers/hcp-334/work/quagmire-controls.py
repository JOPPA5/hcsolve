import json,random,subprocess
from pathlib import Path
p=Path(__file__).parent;pt=(p/'control-vig-plain.txt').read_text().strip();assert len(pt)==150
rows=[]
for family in [1,2]:
 for T in [3,5]:
  rng=random.Random(33444+100*family+T);K=list(range(26));rng.shuffle(K);R=[rng.randrange(26) for _ in range(T)];invK=[K.index(x) for x in range(26)]
  ct=''.join(chr(97+((invK[ord(c)-97]+R[i%T])%26 if family==1 else invK[(ord(c)-97+R[i%T])%26])) for i,c in enumerate(pt));ct=ct[:70]+'?'+ct[71:94]+'?'+ct[95:];f=p/f'quag-control-{family}-{T}.txt';f.write_text(ct+'\n')
  r=subprocess.check_output([str(p/'quagmire'),str(p/'quadgrams.tsv'),str(f),str(family),str(T),'50'],text=True);(p/f'quag-control-{family}-{T}-result.txt').write_text(r)
  found=r.splitlines()[0].split()[1];truth=pt[:70]+'?'+pt[71:94]+'?'+pt[95:]
  row=dict(family=family,T=T,alphabet_key=K,phase_offsets=R,exact=found==truth,matched_known=sum(a==b for a,b in zip(found,truth) if b!='?'),plaintext=truth,found=found);rows.append(row);(p/'quagmire-controls.json').write_text(json.dumps(rows,indent=2));print(family,T,row['exact'],row['matched_known'],flush=True)

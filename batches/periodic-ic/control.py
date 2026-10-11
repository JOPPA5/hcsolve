from pathlib import Path
import random,json,subprocess
p=Path(__file__).parent;rng=random.Random(5201943);pt=Path('ciphers/hcp-350/work/ring-control-plain.txt').read_text().strip();assert len(pt)==385
I=list(range(26));O=list(range(26));rng.shuffle(I);rng.shuffle(O);IP=[I.index(c) for c in range(26)];S=5;T=20;steps=[rng.randrange(3,15) for _ in range(T-1)];steps.append((S-sum(steps))%26);assert sum(steps)%26==S
invO=[O.index(c) for c in range(26)];d=0;ct=''
for i,c in enumerate(pt):ct+=chr(97+invO[(IP[ord(c)-97]+d)%26]);d=(d+steps[i%T])%26
(p/'control-cipher.txt').write_text(ct+'\n');(p/'control-key.json').write_text(json.dumps(dict(plaintext=pt,input_slots=I,output_positions=O,steps=steps,T=T,S=S),indent=2))
r=subprocess.run([str(p/'periodic_ic'),str(p/'control-cipher.txt'),str(T),str(S),'500'],capture_output=True,text=True);(p/'control-candidates.txt').write_text(r.stdout)
def score(k):
 counts=[[0]*26 for _ in range(T)]
 for i,c in enumerate(ct):counts[i%T][(k[ord(c)-97]-(i//T)*S)%26]+=1
 return sum(x*x for row in counts for x in row)
rows=[]
for line in r.stdout.splitlines():
 sc,key=line.split();k=[int(x) for x in key.split(',') if x];assert int(sc)==score(k)
 matches=max(sum((x+off)%26==y for x,y in zip(k,O)) for off in range(26));rows.append(dict(score=int(sc),key=k,matches=matches))
report=dict(T=T,S=S,known_period_and_total_are_control_assumptions=True,true_score=score(O),best_match=max(x['matches'] for x in rows),candidates=rows)
(p/'control-report.json').write_text(json.dumps(report,indent=2));print({k:v for k,v in report.items() if k!='candidates'})

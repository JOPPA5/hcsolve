from pathlib import Path
import subprocess,random,json
p=Path(__file__).parent;rng=random.Random(610345);report={};controls={}
def enc(s,k):return ''.join(s[c::len(k)] for c in k)
for N in [60,65]:
 s='kontrolnyprikladpouzivamenaovereniesifrytextbolvytvorenynezavisleodhistorickehozadania'[:N];ks=[rng.sample(range(w),w) for w in [5,6]];ct=s
 for k in ks:ct=enc(ct,k)
 path=p/f'double-control-{N}.txt';path.write_text(ct+'\n');controls[str(N)]={'plaintext':s,'keys':ks,'ciphertext':ct}
 out=subprocess.check_output([str(p/'double_exact'),str(p/'quadgrams.tsv'),str(path)],text=True);(p/f'double-control-{N}-result.txt').write_text(out);d=dict(l.split(' ',1) for l in out.splitlines());report[str(N)]={'exact':d['plaintext']==s,'matches':sum(a==b for a,b in zip(s,d['plaintext'])),'score':float(d['score']),'evaluations':int(d['evaluations'])}
(p/'double-controls.json').write_text(json.dumps(controls,indent=2)+'\n');(p/'double-control-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if all(d['exact'] for d in report.values()):
 results={}
 for i in range(14):
  src=p/f'omit-{i}.txt';out=subprocess.check_output([str(p/'double_exact'),str(p/'quadgrams.tsv'),str(src)],text=True);(p/f'double-target-omit-{i}.txt').write_text(out);results[str(i)]=dict(l.split(' ',1) for l in out.splitlines())
 (p/'double-target-report.json').write_text(json.dumps(results,indent=2)+'\n');print('Target sweep complete')
else:print('Control gate failed; target sweep skipped')

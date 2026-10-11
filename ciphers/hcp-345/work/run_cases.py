from pathlib import Path
import subprocess,random,json
p=Path(__file__).parent;rng=random.Random(345)
groups=p.joinpath('transcription.txt').read_text().split()
cases={f'omit-{omit+1}':''.join(g for i,g in enumerate(groups) if i!=omit) for omit in [-1]+list(range(13))}
pt='effektivneleivamposielamekurieromprosimvaspotvrdteprijempenazix'
# Explicit synthetic control, not asserted as target plaintext.
def enc(s,key):return ''.join(s[j::len(key)] for j in key)
controls={}
for w in [16,19,22]:
 key=list(range(w));rng.shuffle(key);name=f'control-single-{w}';cases[name]=enc(pt,key);controls[name]={'plaintext':pt,'keys':[key]}
keys=[];s=pt
for w in [16,19,22]:
 key=list(range(w));rng.shuffle(key);keys.append(key);s=enc(s,key)
cases['control-triple']=s;controls['control-triple']={'plaintext':pt,'keys':keys}
p.joinpath('controls.json').write_text(json.dumps(controls,indent=2))
for name,s in cases.items():
 inp=p/(name+'.txt');inp.write_text(s)
 out=subprocess.check_output([str(p/'columnar'),str(p),str(inp)],text=True)
 p.joinpath(name+'-results.txt').write_text(out)
 best=max(out.splitlines(),key=lambda line:float(line.split()[1]));exact=any(line.split()[-1]==pt for line in out.splitlines()) if name in controls else None
 print(name,'exact_control_recovered',exact,'best',best,flush=True)

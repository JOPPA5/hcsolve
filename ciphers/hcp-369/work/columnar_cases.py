from pathlib import Path
import subprocess,random,json
p=Path(__file__).parent;g=p.joinpath('transcription.txt').read_text().split();cases={f'omit-{i+1}':''.join(v for j,v in enumerate(g) if j!=i) for i in [-1,4,18]}
pt='vastelegramnamprisielneskorpretoprosimeopakovatspravuvplnomrozsahuaposlatpotvrdeniezevsetkyudajesupravnexkoniecspravy'[:110]
rng=random.Random(369);controls={}
for w in [16,19,22]:
 key=list(range(w));rng.shuffle(key);name=f'control-{w}';cases[name]=''.join(pt[j::w] for j in key);controls[name]={'plaintext':pt,'key':key}
p.joinpath('controls.json').write_text(json.dumps(controls,indent=2))
for name,s in cases.items():
 f=p/(name+'.txt');f.write_text(s);out=subprocess.check_output([str(p/'columnar'),str(p),str(f)],text=True);p.joinpath(name+'-results.txt').write_text(out);best=max(out.splitlines(),key=lambda z:float(z.split()[1]));print(name,'exact_control',any(z.split()[-1]==pt for z in out.splitlines()) if name in controls else None,best,flush=True)

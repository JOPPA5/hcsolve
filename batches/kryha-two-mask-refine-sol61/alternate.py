from pathlib import Path
import subprocess,json,sys
B=Path(__file__).resolve().parent;inp=Path(sys.argv[1]);p=Path(sys.argv[2]);label=sys.argv[3];n=int(sys.argv[4]);last=-1e100;log=[]
for it in range(1,11):
 pre=f'{label}-r{it}';subprocess.run(['python3',str(B/'run_path.py'),str(inp),str(p),pre,str(n)],check=True);paths=B/f'{pre}-paths.txt';subprocess.run(['python3',str(B/'project_paths.py'),str(inp),str(paths),str(p),pre],check=True)
 out=B/f'{pre}-reranked.txt'
 with out.open('w')as f:subprocess.run([str(B/'rerank'),str(B),str(B/f'{pre}-projected.txt'),str(B/f'{pre}-fixedP.txt')],stdout=f,check=True)
 lines=out.read_text().splitlines();pos=next(i for i,l in enumerate(lines)if l.startswith(f'N {n} '));score=float(lines[pos+1].split()[0]);pn=B/f'{pre}-P.txt';pn.write_text(lines[pos+2]+'\n');subprocess.run(['python3',str(B/'check_paths.py'),str(inp),str(paths),str(out),pre],check=True);log.append(dict(round=it,score=score,changed=pn.read_text().strip()!=p.read_text().strip()));(B/f'{label}-alternation.json').write_text(json.dumps(log,indent=2));print('ROUND',it,score,flush=True)
 if score<=last+1e-8:break
 last=score;p=pn

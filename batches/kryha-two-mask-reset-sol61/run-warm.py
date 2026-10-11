from pathlib import Path
import json,subprocess,sys,time
b=Path(__file__).resolve().parent;name=sys.argv[1];inp=json.load(open(b/(name+'-input.json')))
if name=='control':
 ls=(b/'control-masc.txt').read_text().splitlines();ix=max(range(len(ls)//4),key=lambda k:float(ls[4*k].split()[1]));P=list(map(int,ls[4*ix+1].split()))
else:P=json.load(open('batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json'))[0]['P']
geom=json.load(open('batches/kryha-wheel-sol61/wheel52.json'));vals=geom['adjacent_distances']+inp['delta']+[0]*26+[0]*(23*26);(b/f'{name}-warm-P.txt').write_text(' '.join(map(str,P))+'\n');(b/f'{name}-warm-config.txt').write_text(' '.join(map(str,[inp['K'][0]]+inp['O']+P))+'\n'+inp['ciphertexts'][0][:-1]+'\n'+inp['ciphertexts'][1][1:]+'\n');t=time.monotonic();run=subprocess.run([str(b/'path-refine'),'7','batches/kryha-two-mask-refine-sol61/model7.tsv',str(b/f'{name}-warm-config.txt')],input=' '.join(map(str,vals)),text=True,capture_output=True,check=True);base=name+'-warm';(b/f'{base}-profile.txt').write_text(run.stdout);print(base,run.stdout.splitlines()[0],time.monotonic()-t,flush=True)
subprocess.run(['python3',str(b/'project.py'),str(b/(name+'-input.json')),f'{base}-profile.txt',f'{base}-projected.txt','10'],check=True)
with (b/f'{base}-masc.txt').open('w') as f:subprocess.run([str(b/'masc-warm'),str(b/'dummy-pair.txt'),str(b/'zero-schedule.txt'),'batches/kryha-mask-sol61','ciphers/hcp-350/work',str(b/f'{base}-projected.txt'),str(b/f'{name}-warm-P.txt')],stdout=f,check=True)
with (b/f'{base}-reranked.txt').open('w') as f:subprocess.run([str(b/'rerank'),'batches/kryha-two-mask-refine-sol61',str(b/f'{base}-projected.txt'),str(b/f'{base}-masc.txt')],stdout=f,check=True)
subprocess.run(['python3',str(b/'neighbors.py'),str(b/(name+'-input.json')),f'{base}-masc.txt',f'{base}-projected.txt',f'{base}-neighbors.json'],check=True)

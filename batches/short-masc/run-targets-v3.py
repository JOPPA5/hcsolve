from pathlib import Path
import subprocess,concurrent.futures
w=Path(__file__).resolve().parent;root=w.parents[1]
models={'sk':root/'batches/scoring-sol61','cs':root/'batches/czech-scoring'}
def run(job):
 inp,lang,N=job;label=inp.stem+f'-{lang}-{N}-v3';prefix=w/label
 with (w/(label+'.generation.log')).open('w') as f:subprocess.run(['python3',str(w/'anchors.py'),str(inp),lang,str(N),str(prefix)],stdout=f,check=True)
 with (w/(label+'.result.txt')).open('w') as out,(w/(label+'.progress.log')).open('w') as err:subprocess.run([str(w/'mono'),str(models[lang]),str(inp),str(prefix.with_suffix('.seeds.txt')),str(N)],stdout=out,stderr=err,check=True)
 print(label,'finished',flush=True)
jobs=[(inp,lang,N) for inp in sorted(w.glob('target-*.txt')) if inp.stem.endswith(('forward','reverse')) for lang in models for N in (26,28)]
assert len(jobs)==24
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,jobs))

from pathlib import Path
import subprocess,json,concurrent.futures
w=Path(__file__).resolve().parent;root=w.parents[1]
models={'sk':root/'batches/scoring-sol61','de':root/'batches/scoring-sol61/german','cs':root/'batches/czech-scoring'}
controls=json.loads((w/'controls.json').read_text())
def run(c):
 label=c['label'];prefix=w/label
 with (w/(label+'.generation.log')).open('w') as f:subprocess.run(['python3',str(w/'anchors-v1.py'),str(w/(label+'.txt')),c['lang'],str(c['N']),str(prefix)],stdout=f,check=True)
 with (w/(label+'.result.txt')).open('w') as out,(w/(label+'.progress.log')).open('w') as err:subprocess.run([str(w/'mono'),str(models[c['lang']]),str(w/(label+'.txt')),str(prefix.with_suffix('.seeds.txt')),str(c['N'])],stdout=out,stderr=err,check=True)
 print(label,'finished',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,controls))

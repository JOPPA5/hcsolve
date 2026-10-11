from pathlib import Path
import subprocess,concurrent.futures
w=Path(__file__).resolve().parent;root=w.parents[1]
models={'sk':root/'batches/scoring-sol61','de':root/'batches/scoring-sol61/german','cs':w/'cs-lex'}
def run(result):
 label=result.name.removesuffix('.result.txt');inp,lang,N=label.removesuffix('-v3').rsplit('-',2)
 with (w/(label+'.lex-result.txt')).open('w') as out,(w/(label+'.lex-progress.log')).open('w') as err:subprocess.run([str(w/'lex-refine'),str(models[lang]),str(w/(inp+'.txt')),str(result),N],stdout=out,stderr=err,check=True)
 print(label,'lex done',flush=True)
files=sorted(w.glob('target-*-v3.result.txt'));assert len(files)==24
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,files))

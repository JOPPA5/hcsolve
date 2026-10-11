from pathlib import Path
import subprocess,concurrent.futures
w=Path(__file__).resolve().parent;root=w.parents[1]
models={'sk':root/'batches/scoring-sol61','de':root/'batches/scoring-sol61/german','cs':w/'cs-lex'}
def run(result):
 label=result.name.removesuffix('.result.txt');inp,lang,N=label.rsplit('-',2)
 with (w/(label+'.lex-result.txt')).open('w') as out,(w/(label+'.lex-progress.log')).open('w') as err:subprocess.run([str(w/'lex-refine'),str(models[lang]),str(w/(inp+'.txt')),str(result),N],stdout=out,stderr=err,check=True)
 print(label,'lex done',flush=True)
files=[f for f in sorted(w.glob('target-*.result.txt')) if '-v3.' not in f.name];assert len(files)==36
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,files))

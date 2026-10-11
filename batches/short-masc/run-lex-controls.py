from pathlib import Path
import subprocess,json,concurrent.futures
w=Path(__file__).resolve().parent;root=w.parents[1]
models={'sk':root/'batches/scoring-sol61','de':root/'batches/scoring-sol61/german','cs':w/'cs-lex'}
controls=json.loads((w/'controls.json').read_text())
def run(c):
 label=c['label'];m=models[c['lang']]
 with (w/(label+'.lex-result.txt')).open('w') as out,(w/(label+'.lex-progress.log')).open('w') as err:subprocess.run([str(w/'lex-refine'),str(m),str(w/(label+'.txt')),str(w/(label+'.result.txt')),str(c['N'])],stdout=out,stderr=err,check=True)
 truthfile=w/(label+'.truth-score-input.txt');truthfile.write_text(c['plaintext_folded']+'\n')
 with (w/(label+'.truth-score.txt')).open('w') as f:subprocess.run([str(w/'lex-refine'),str(m),str(truthfile),'score'],stdout=f,check=True)
 print(label,'lex done',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,controls))

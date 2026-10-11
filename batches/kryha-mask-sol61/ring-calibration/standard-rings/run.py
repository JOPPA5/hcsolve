from pathlib import Path
import subprocess,concurrent.futures,time,sys
b=Path(__file__).resolve().parent;r=b.parents[3];kind=sys.argv[1] if len(sys.argv)>1 else 'controls';labels=['control-m21','control-m29'] if kind=='controls' else [x['label'] for x in __import__('json').load(open(b/'targets.json')) if ('preferred' in x['label'])==(kind=='preferred')]
def run(label):
 start=time.monotonic()
 with (b/(label+'.tsv')).open('w') as out,(b/(label+'.log')).open('w') as err:subprocess.run([str(b/'scout'),str(b/(label+'.txt')),'64',str(r/'batches/kryha-mask-sol61/coordinates.txt'),str(r/'batches/kryha-mask-sol61'),str(r/'ciphers/hcp-350/work')],stdout=out,stderr=err,check=True)
 print(label,time.monotonic()-start,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(run,labels))

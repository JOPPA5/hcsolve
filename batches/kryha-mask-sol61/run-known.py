from pathlib import Path
import subprocess,concurrent.futures
b=Path(__file__).resolve().parent;r=b.parents[1]
def run(m):
 folder=b/f'control-m{m}'
 with (folder/'known-beam.tsv').open('w') as out,(folder/'known-beam.log').open('w') as err:subprocess.run([str(b/'maskbeam'),str(folder/'cipher.txt'),str(m),'256',str(folder/'known-rings.txt'),str(b/'coordinates.txt'),str(b),str(r/'ciphers/hcp-350/work')],stdout=out,stderr=err,check=True)
 print(m,'done',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(run,(20,26,30)))

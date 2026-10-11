from codec import *
import subprocess,concurrent.futures
cases=json.loads((B/'controls.json').read_text())
def work(case):
 folder=Path(case['folder'])
 with (folder/'run.log').open('w')as out:subprocess.run(['python3',str(B/'run_case.py'),str(folder),str(case['count'])],stdout=out,stderr=subprocess.STDOUT,check=True)
 print('complete',case['count'],flush=True)
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2)as pool:list(pool.map(work,cases))

from pathlib import Path
import json,hashlib,subprocess,concurrent.futures
b=Path(__file__).resolve().parent;r=b.parents[1];cases=[]
for reading in ('original','preferred'):
 sources=[r/f'ciphers/hcp-{n}/work/transcription.txt' if reading=='original' else r/f'batches/source-variants-350-351/{n}-source-preferred.txt' for n in (350,351)]
 cts=[''.join(p.read_text().lower().split()) for p in sources];assert all(len(c)==385 and all('a'<=x<='z' for x in c) for c in cts)
 for direction in ('forward','reverse'):
  folder=b/f'actual-{reading}-{direction}';folder.mkdir(exist_ok=True);texts=cts if direction=='forward' else [c[::-1] for c in cts];(folder/'ciphertexts.txt').write_text('\n'.join(texts)+'\n');cases.append(dict(folder=str(folder),reading=reading,direction=direction,ciphertexts=texts,sources=[str(p.relative_to(r)) for p in sources],source_sha256=[hashlib.sha256(p.read_bytes()).hexdigest() for p in sources],assumptions='shared unknown mixed input/output rings, shared unknown 26-of-52 mask/start, same physical start reset per whole message, positive ordinary one-stop press; no symbols omitted'))
(b/'targets.json').write_text(json.dumps(cases,indent=2)+'\n')
def run(case):
 folder=Path(case['folder']);print('start',folder.name,flush=True)
 with (folder/'run.log').open('w') as out:subprocess.run(['python3',str(b/'target-case.py'),str(folder)],stdout=out,stderr=subprocess.STDOUT,check=True)
 print('finished',folder.name,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(run,cases))

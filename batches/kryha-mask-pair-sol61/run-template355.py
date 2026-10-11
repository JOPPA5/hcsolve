from pathlib import Path
import json
base=Path(__file__).resolve().parent
# Helpers only; older blind search is not executed.
exec((base/'run.py').read_text().split('def work(number):')[0]);base=b;folder=b/'template355';folder.mkdir(exist_ok=True);(folder/'ciphertexts.txt').write_text((b/'framing355-control/ciphertexts.txt').read_text());ctfile=folder/'ciphertexts.txt';keys=[]
for line in (b/'framing355-control/pair-cycle.tsv').read_text().splitlines():
 ix,sc,key=line.split('\t');keys.append(f'old{ix} {key}\n')
(folder/'blind-ring-seeds.txt').write_text(''.join(keys));command('pair-template',[ctfile,large/'ring-unigrams.tsv',folder/'blind-ring-seeds.txt'],folder/'template-output.tsv');dedup={}
for line in (folder/'template-output.tsv').read_text().splitlines():
 label,sc,key,shift=line.split('\t');O=list(map(int,key.rstrip(',').split(',')));O=[(x-O[0])%26 for x in O];key=','.join(map(str,O));v=float(sc)
 if key not in dedup or dedup[key][0]<v:dedup[key]=(v,label)
rows=sorted([(v[0],key,v[1]) for key,v in dedup.items()],reverse=True)[:32];assert len(rows)==32
(folder/'selected-profile-seeds.json').write_text(json.dumps([dict(score=sc,key=key,label=label) for sc,key,label in rows],indent=2)+'\n');(folder/'physical-ring-seeds.tsv').write_text(''.join(f'{i}\t{round(sc*1000)}\t{key}\n' for i,(sc,key,label) in enumerate(rows)));command('pair-mask-profile',[ctfile,b/'coordinates.txt',large/'ring-unigrams.tsv',folder/'physical-ring-seeds.tsv'],folder/'mask-profiles.tsv')
# Same physical-profile → MASC → generic four seed coupled procedure, no truth access.
def command(binary,args,path):
 if not path.exists():
  with path.with_suffix('.partial').open('w') as out:subprocess.run([str(base/binary)]+list(map(str,args)),stdout=out,check=True)
  path.with_suffix('.partial').rename(path)
 return path.read_text().splitlines()
source=(b/'target-case.py').read_text();source=source[source.index("lines=command('pair-bridge-masc'"):];b=folder
exec(source)

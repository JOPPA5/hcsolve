from pathlib import Path
import json,concurrent.futures
b=Path(__file__).resolve().parent
exec((b/'run.py').read_text().split('# Reads ciphertext/geometry/models only.')[0]);base=b;folder=b/'template355';ctfile=folder/'ciphertexts.txt';seeds=json.load(open(folder/'bridge-results.json'));seeds.sort(key=lambda z:z['score'],reverse=True)
def work(rank):
 current=seeds[rank];out=folder/f'local-seed{rank}';out.mkdir(exist_ok=True);(out/'initial.json').write_text(json.dumps(current,indent=2)+'\n')
 for it in range(2):
  stage=out/f'pass{it}';stage.mkdir(exist_ok=True);ring=stage/'rings.txt';hole=stage/'holes.txt';sf=stage/'old-schedule.txt';ring.write_text(' '.join(map(str,current['input_slots']+current['output_positions']))+'\n');hole.write_text(' '.join(map(str,current['holes']))+'\n');sf.write_text(' '.join(map(str,schedule(current['holes'])))+'\n');lines=command('pair-local-mask',[ctfile,sf,small,large,b/'coordinates.txt',ring,hole],stage/'local.txt');z=parse(lines[:4]);z.update(holes=list(map(int,lines[4].split())),seed_rank=rank,pass_index=it);(stage/'local.json').write_text(json.dumps(z,indent=2)+'\n');sf=stage/'new-schedule.txt';sf.write_text(' '.join(map(str,schedule(z['holes'])))+'\n');ring=stage/'local-rings.txt';ring.write_text(' '.join(map(str,z['input_slots']+z['output_positions']))+'\n');current=parse(command('pair-joint',[ctfile,sf,small,large,ring,30000],stage/'joint.txt'));current.update(holes=z['holes'],seed_rank=rank,pass_index=it);(stage/'result.json').write_text(json.dumps(current,indent=2)+'\n');print('local355',rank,it,current['score'],flush=True)
 return current
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(work,range(4)))
(folder/'local-results.json').write_text(json.dumps(results,indent=2)+'\n')

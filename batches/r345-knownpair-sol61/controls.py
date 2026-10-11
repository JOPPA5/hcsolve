from pathlib import Path
import sys,json,random,unicodedata,concurrent.futures
from position_model import solve,enc
B=Path(__file__).resolve().parent;R=B.parents[1];source=json.loads((R/'batches/repeat345-486-sol61/conditional-pair.json').read_text());pool=list(source['plaintext']);rng=random.Random(345486215);rng.shuffle(pool);matched=''.join(pool);text=''.join(c for c in unicodedata.normalize('NFD',(R/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().lower())if'a'<=c<='z');test=text[48000:48060];cases=[('matched_inventory_shuffled60',matched,345486216),('independent_TEST60',test,345486217)]
def run(case):
 label,p,seed=case;rng=random.Random(seed);keys=[rng.sample(range(w),w)for w in(21,19,20)];c=p
 for key in keys:c=enc(c,key)
 out=solve(p,c,timeout=60000);out.update(label=label,plaintext=p,ciphertext=c,planted_keys=keys,planted_seed=seed,plaintext_keys_not_seeded=True,full_planted_keys_recovered=out.get('keys')==keys);(B/f'{label}.json').write_text(json.dumps(out,indent=2));return label,out['status'],out['seconds']
if __name__=='__main__':
 with concurrent.futures.ProcessPoolExecutor(max_workers=2)as executor:
  for result in executor.map(run,cases):print(result,flush=True)

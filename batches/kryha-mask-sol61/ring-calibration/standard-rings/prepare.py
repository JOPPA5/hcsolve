from pathlib import Path
import json,random,unicodedata
b=Path(__file__).resolve().parent;r=b.parents[3];g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=g['adjacent_distances'];coords=g['unwrapped_effective_coordinates'];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];ns={'digits':digits,'unicodedata':unicodedata};src=(b.parent/'prepare.py').read_text();exec(src[src.index('def prep('):src.index('source=r/')],ns);prep=ns['prep'];train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';test=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';excluded={prep(s) for s in train.read_text().strip().split('\n\n')};text=''.join(prep(s) for s in test.read_text().strip().split('\n\n') if prep(s) not in excluded);controls=[]
for j,(m,off,start) in enumerate([(21,3,20000),(29,19,21500)]):
 plain=text[start:start+385];assert len(plain)==385;rng=random.Random(52385300+j);holes=sorted(rng.sample(range(52),m));phase=rng.randrange(m);jumps=[]
 for i,h in enumerate(holes):
  x=h;d=0
  while True:
   d+=a[x];x=(x+1)%52
   if x==holes[(i+1)%m]:break
  jumps.append(d)
 assert sum(jumps)==179;d=0;ct=''
 for i,c in enumerate(plain):ct+=chr(97+(ord(c)-97+d-off)%26);d=(d+jumps[(phase+i)%m])%26
 decoded=''
 for i,c in enumerate(ct):h=holes[(phase+i)%m];dis=coords[h]-coords[holes[phase]]+179*((phase+i)//m);decoded+=chr(97+(ord(c)-97+off-dis)%26)
 assert decoded==plain;rec={'label':f'control-m{m}','m':m,'offset':off,'active_holes_zero_based':holes,'phase':phase,'ciphertext':ct,'plaintext':plain,'prepared_TEST_offset':start,'seed':52385300+j};controls.append(rec);(b/(rec['label']+'.txt')).write_text(ct+'\n')
(b/'controls.json').write_text(json.dumps(controls,indent=2)+'\n');(b/'benchmark-status.json').write_text(json.dumps({'initial_benchmark_valid_for_whole385':False,'reason':'oldbinary reads one token; transcriptionfilename initially yielded onlySOSOL5letters; no inference or candidate claim','replaced_by_fresh385control_benchmark':True},indent=2)+'\n')

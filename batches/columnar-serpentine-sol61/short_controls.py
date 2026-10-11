from experiment import *
test=REPO/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';train=REPO/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';training={l[9:]for l in train.read_text().splitlines()if l.startswith('# text = ')};sentences=[l[9:]for l in test.read_text().splitlines()if l.startswith('# text = ')and l[9:]not in training];rows=[]
for j,(length,w,kind)in enumerate([(55,11,'beam'),(65,13,'beam'),(55,18,'one-long'),(65,16,'one-long')]):
 selected=[];text=''
 for s in sentences[900+35*j:]:
  selected.append(s);text+=normalize(s)
  if len(text)>=length:break
 pt=text[:length];assert len(pt)==length;key=list(range(w));random.Random(61180000+j).shuffle(key);up=j%2;ct=encrypt(pt,key,up);assert inverse(ct,key,up)==pt;candidates=[]
 for u in [0,1]:candidates+=attack(f'short-control-{length}-{w}',ct,w,kind,u)
 candidates.sort(key=lambda c:c['score'],reverse=True);ranks=[i for i,r in enumerate(candidates)if r['plaintext']==pt];rows.append(dict(length=length,width=w,model=kind,plaintext=pt,ciphertext=ct,planted_readout_columns=key,planted_start_up=up,source_sentences=selected,excluded_from_training=True,rng_seed=61180000+j,exact_best=candidates[0]['plaintext']==pt,true_ranks=ranks,candidates=candidates));(P/'short-controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(length,w,rows[-1]['exact_best'],ranks,flush=True)

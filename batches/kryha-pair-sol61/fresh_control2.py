import run_pair as r
import random,json
sentences=[];words=[]
for line in (r.R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():words.append((f[1],f[3]))
bound=int(.8*len(sentences));heldout=[r.prepare(s)for s in sentences[bound:]];texts=[''.join(heldout[o:])[:385]for o in [200,600]];rng=random.Random(77061102);slots=rng.sample(range(26),26);O=rng.sample(range(26),26);phase=15;sign=-1;cts=[r.encrypt(t,slots,O,phase,sign)for t in texts];folder=r.P/'control2';folder.mkdir(exist_ok=True);plant=dict(input_slots=slots,output_positions=O,phase=phase,sign=sign,plaintext_messages=texts,ciphertext_messages=cts,heldout_sentence_offsets=[200,600],training_boundary=bound,seed=77061102);(folder/'plant.json').write_text(json.dumps(plant,indent=2));assert [r.decrypt(c,[slots[(-i)%26]for i in range(26)],[(-x)%26 for x in O],phase)for c in cts]==texts;v=r.pipeline('control2',cts,phase,texts);r.refine5(v,texts)

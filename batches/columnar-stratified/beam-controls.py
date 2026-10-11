from controls import P, encrypt, normalize
from pathlib import Path
import json,random,subprocess
sentences=[l[9:] for l in Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().splitlines() if l.startswith('# text = ')];training={l[9:] for l in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines() if l.startswith('# text = ')}
rows=[]
for j,(length,width) in enumerate([(55,11),(65,13),(85,17),(95,19),(100,20),(110,22),(115,23)]):
 sentence=next(s for s in sentences[j*20:] if len(normalize(s))>=length and s not in training);pt=normalize(sentence)[:length];key=list(range(width));random.Random(369771+j).shuffle(key);ct=encrypt(pt,key);f=P/f'beam-control-{length}-input.txt';f.write_text(ct+'\n')
 out=subprocess.check_output([str(P/'beam'),str(P),str(f),str(width),'10000'],text=True);(P/f'beam-control-{length}-result.txt').write_text(out);candidates=[]
 for line in out.splitlines():
  sc,raw,plain=line.split();seq=[int(x) for x in raw.rstrip(',').split(',')];read=[seq.index(i) for i in range(width)];assert encrypt(plain,read)==ct;candidates.append(dict(score=float(sc),chunk_order=seq,readout_columns=read,plaintext=plain))
 ranks=[i for i,c in enumerate(candidates) if c['plaintext']==pt];row=dict(length=length,width=width,source_sentence=sentence,excluded_from_train=True,plaintext=pt,ciphertext=ct,planted_readout_columns=key,candidates=candidates,exact_best=candidates[0]['plaintext']==pt,truth_ranks=ranks,all_candidates_reencrypt_exact=True);rows.append(row);(P/'beam-controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(length,width,row['exact_best'],ranks,flush=True)

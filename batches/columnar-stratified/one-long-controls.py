from controls import P,normalize,encrypt
from pathlib import Path
import json,random,subprocess
sentences=[l[9:] for l in Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().splitlines() if l.startswith('# text = ')];training={l[9:] for l in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines() if l.startswith('# text = ')};rows=[]
for j,(length,width) in enumerate([(55,18),(65,16),(85,21),(100,11),(115,19)]):
 sentence=next(s for s in sentences[j*20:] if len(normalize(s))>=length and s not in training);pt=normalize(sentence)[:length];key=list(range(width));random.Random(369977+j).shuffle(key);ct=encrypt(pt,key);f=P/f'one-long-control-{length}-input.txt';f.write_text(ct+'\n')
 out=subprocess.check_output([str(P/'one-long'),str(P),str(f),str(width),'10000'],text=True);(P/f'one-long-control-{length}-result.txt').write_text(out);candidates=[]
 for line in out.splitlines():
  sc,k,plain=line.split();seq=[int(x) for x in k.rstrip(',').split(',')];read=[seq.index(i) for i in range(width)];assert encrypt(plain,read)==ct;candidates.append(dict(score=float(sc),chunk_order=seq,readout_columns=read,plaintext=plain))
 candidates.sort(key=lambda c:c['score'],reverse=True);ranks=[i for i,c in enumerate(candidates) if c['plaintext']==pt];row=dict(length=length,width=width,source_sentence=sentence,excluded_from_train=True,plaintext=pt,ciphertext=ct,planted_readout_columns=key,exact_best=candidates[0]['plaintext']==pt,truth_ranks=ranks,all_retained_reencrypt_exact=True,candidates=candidates);rows.append(row);(P/'one-long-controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(length,width,row['exact_best'],ranks,flush=True)

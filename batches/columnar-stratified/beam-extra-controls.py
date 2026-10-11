from controls import P, encrypt, normalize
from pathlib import Path
import json,random,subprocess
rows=[]
a=json.loads((P/'beam-controls.json').read_text());c=next(x for x in a if x['length']==85)
ct=''.join('.' if i in [15,19] else ch for i,ch in enumerate(c['ciphertext']));f=P/'beam-control-85-erased.txt';f.write_text(ct+'\n');out=subprocess.check_output([str(P/'beam'),str(P),str(f),'17','10000'],text=True);(P/'beam-control-85-erased-result.txt').write_text(out)
key=c['planted_readout_columns'];expected=['']*85;at=0
for col in key:
 for pos in range(col,85,17):expected[pos]=ct[at];at+=1
expected=''.join(expected)
lines=out.splitlines();ranks=[i for i,l in enumerate(lines) if l.split()[2]==expected];rows.append(dict(kind='two-erasures',length=85,width=17,expected=expected,true_ranks=ranks,exact_best=bool(ranks and ranks[0]==0)))
test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu');train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu');training={l[9:] for l in train.read_text().splitlines() if l.startswith('# text = ')};sentences=[l[9:] for l in test.read_text().splitlines() if l.startswith('# text = ') and l[9:] not in training];selected=[];text=''
for s in sentences[40:]:
 selected.append(s);text+=normalize(s)
 if len(text)>=400:break
pt=text[:400];key=list(range(20));random.Random(369520).shuffle(key);ct=encrypt(pt,key);f=P/'beam-control-400.txt';f.write_text(ct+'\n');out=subprocess.check_output([str(P/'beam'),str(P),str(f),'20','10000'],text=True);(P/'beam-control-400-result.txt').write_text(out);lines=out.splitlines();ranks=[i for i,l in enumerate(lines) if l.split()[2]==pt];rows.append(dict(kind='heldout-multi-sentence',length=400,width=20,source_sentences=selected,excluded_from_train=True,plaintext=pt,ciphertext=ct,planted_readout_columns=key,true_ranks=ranks,exact_best=bool(ranks and ranks[0]==0)))
(P/'beam-extra-controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print([(r['kind'],r['exact_best'],r['true_ranks']) for r in rows],flush=True)

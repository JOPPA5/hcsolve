from pathlib import Path
import json,random,subprocess,unicodedata
P=Path(__file__).parent
def normalize(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
def encrypt(s,key):return ''.join(s[i] for col in key for i in range(col,len(s),len(key)))
def parse(out):
 rows=[]
 for line in out.splitlines():
  w,score,key,pt=line.split();rows.append(dict(width=int(w),score=float(score),readout_columns=[int(x) for x in key.rstrip(',').split(',')],plaintext=pt))
 return rows
if __name__=='__main__':
 test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu');train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu')
 sentences=[l[9:] for l in test.read_text().splitlines() if l.startswith('# text = ')];training={l[9:] for l in train.read_text().splitlines() if l.startswith('# text = ')};rows=[]
 for j,(length,width) in enumerate([(115,19),(110,22),(100,16)]):
  sentence=next(s for s in sentences[j*25:] if len(normalize(s))>=length and s not in training);pt=normalize(sentence)[:length];key=list(range(width));random.Random(369515+j).shuffle(key);ct=encrypt(pt,key)
  f=P/f'control-{length}-{width}.txt';f.write_text(ct+'\n');out=subprocess.check_output([str(P/'solver'),'batches/scoring-sol61/frequency',str(f),str(width),str(width)],text=True);(P/f'control-{length}-{width}-result.txt').write_text(out);c=parse(out)[0];assert encrypt(c['plaintext'],c['readout_columns'])==ct
  row=dict(length=length,width=width,source_sentence=sentence,excluded_from_train=True,plaintext=pt,planted_key=key,ciphertext=ct,found=c,exact=c['plaintext']==pt,matches=sum(a==b for a,b in zip(pt,c['plaintext'])),reencryption_exact=True);rows.append(row);(P/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(length,width,row['exact'],row['matches'],c['plaintext'],flush=True)

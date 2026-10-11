from pathlib import Path
import json, random, subprocess, unicodedata
P=Path(__file__).parent
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
def encrypt(pt,key,mode):
 ct=[];w=len(key)
 for i,ch in enumerate(pt):
  k=key[i] if i<w else ord((pt if mode<3 else ''.join(ct))[i-w])-97
  p=ord(ch)-97;c=(p+k if mode%3==0 else (k-p if mode%3==1 else p-k))%26
  ct.append(chr(97+c))
 return ''.join(ct)
def parse(out):
 a=[]
 for line in out.splitlines():
  m,w,s,k,t=line.split();a.append(dict(mode=int(m),primer_length=int(w),score=float(s),primer=k,plaintext=t))
 return a
sentences=[l[9:] for l in Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().splitlines() if l.startswith('# text = ')]
train={l[9:] for l in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines() if l.startswith('# text = ')}
if __name__=='__main__':
 rows=[]
 for length,width in [(55,3),(115,5)]:
  sentence=next(s for s in sentences if len(norm(s))>=length and s not in train);pt=norm(sentence)[:length]
  for mode in range(6):
   rng=random.Random(369881+mode+length);key=[rng.randrange(26) for _ in range(width)];ct=encrypt(pt,key,mode)
   path=P/f'control-{length}-{mode}.txt';path.write_text(ct+'\n')
   out=subprocess.check_output([str(P/'solver'),'batches/scoring-sol61/frequency',str(path),'6','12',str(mode)],text=True)
   (P/f'control-{length}-{mode}-results.txt').write_text(out);candidates=parse(out);candidate=next(c for c in candidates if c['primer_length']==width)
   assert encrypt(candidate['plaintext'],[ord(c)-97 for c in candidate['primer']],mode)==ct
   row=dict(length=length,mode=mode,primer_length=width,source_sentence=sentence,excluded_from_train=True,plaintext=pt,ciphertext=ct,planted_primer=key,exact_at_true_length=candidate['plaintext']==pt,matches=sum(a==b for a,b in zip(pt,candidate['plaintext'])),candidates=candidates)
   rows.append(row);(P/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(length,mode,row['exact_at_true_length'],row['matches'],flush=True)

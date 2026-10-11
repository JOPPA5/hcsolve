from pathlib import Path
from collections import Counter
import unicodedata,json,random,hashlib
w=Path(__file__).resolve().parent;root=w.parents[1]
alpha='abcdefghijklmnopqrstuvwxyz{|'
def norm(s,N=26):
 s=s.lower().replace('ß','ss')
 if N==28:s=s.replace('č','{').replace('š','|')
 return ''.join(c for c in unicodedata.normalize('NFD',s) if c in alpha[:N])
models={'sk':root/'batches/scoring-sol61','de':root/'batches/scoring-sol61/german','cs':root/'batches/czech-scoring'}
train={'sk':root/'ciphers/hcp-393/work/sk_snk-ud-train.conllu','de':models['de']/'source/de_gsd-ud-train.conllu','cs':models['cs']/'source/cs_cac-ud-train.conllu'}
test={'sk':root/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu','de':models['de']/'source/de_gsd-ud-test.conllu','cs':models['cs']/'source/cs_cac-ud-test.conllu'}
rows=[];reports=[]
for li,lang in enumerate(models):
 trtext=train[lang].read_text();trainset={norm(s[9:]) for s in trtext.splitlines() if s.startswith('# text = ')}
 core=set((models[lang]/'core-words.txt').read_text().splitlines()) if lang!='cs' else set()
 freq={26:Counter(),28:Counter()}
 for s in trtext.splitlines():
  f=s.split('\t')
  if len(f)>3 and f[0].isdigit():
   for N in (26,28):freq[N][norm(f[1],N)]+=1
   core.add(norm(f[1]))
 for N in (26,28):
  vocab=set(freq[N]) | core
  (w/f'{lang}-vocab-{N}.tsv').write_text(''.join(f'{s}\t{freq[N][s]}\n' for s in sorted(vocab) if s and all(c in alpha[:N] for c in s)))
 blocks=test[lang].read_text().strip().split('\n\n');pool=[]
 for b in blocks:
  text=next((s[9:] for s in b.splitlines() if s.startswith('# text = ')),None)
  if text and norm(text) not in trainset and not any(c.isdigit() for c in text) and '\tPROPN\t' not in b:
   pool.append({'text':text,'id':next((s[12:] for s in b.splitlines() if s.startswith('# sent_id = ')),'unknown')})
 random.Random(396345+li).shuffle(pool)
 for N in (26,28):
  for length in (55,65):
   exact=[p for p in pool if len(norm(p['text'],N))==length]
   entry=exact[0] if exact else next(p for p in pool if len(norm(p['text'],N))>=length)
   pt=norm(entry['text'],N)[:length];key=list(alpha[:N]);random.Random(396345+li*100+N+length).shuffle(key)
   ct=''.join(key[alpha.index(c)] for c in pt)
   label=f'control-{lang}-{N}-{length}'
   (w/(label+'.txt')).write_text(ct+'\n')
   rows.append({'label':label,'lang':lang,'N':N,'length':length,'source':str(test[lang].relative_to(root)),'source_sentence':entry,'whole_sentence':len(norm(entry['text'],N))==length,'training_sentence_excluded':True,'plaintext_raw':pt,'plaintext_folded':pt.replace('{','c').replace('|','s'),'encryption_key':''.join(key),'ciphertext':ct})
 reports.append({'lang':lang,'eligible_heldout_sentences':len(pool),'modeldir':str(models[lang]),'train':str(train[lang]),'test':str(test[lang]),'train_sha256':hashlib.sha256(train[lang].read_bytes()).hexdigest(),'test_sha256':hashlib.sha256(test[lang].read_bytes()).hexdigest()})
(w/'controls.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(w/'provenance.json').write_text(json.dumps(reports,indent=2)+'\n')
ct345=''.join((root/'ciphers/hcp-345/work/transcription.txt').read_text().split());ct396=''.join((root/'ciphers/hcp-396/work/transcription.txt').read_text().split())
assert len(ct345)==65 and len(ct396)==55
for label,ct in [('345',ct345),('396-C',ct396),('396-O',ct396[:30]+'o'+ct396[31:])]:
 for direction,text in [('forward',ct),('reverse',ct[::-1])]:
  (w/f'target-{label}-{direction}.txt').write_text(text+'\n')
print([(r['label'],r['whole_sentence'],r['plaintext_raw']) for r in rows])

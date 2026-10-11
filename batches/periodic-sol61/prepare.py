from pathlib import Path
from collections import Counter
import json,random,unicodedata,hashlib
w=Path(__file__).resolve().parent;root=w.parents[1]
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower().replace('ß','ss')) if 'a'<=c<='z')
resources={'sk':('ciphers/hcp-393/work/sk_snk-ud-train.conllu','ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu','batches/scoring-sol61'),'de':('batches/scoring-sol61/german/source/de_gsd-ud-train.conllu','batches/scoring-sol61/german/source/de_gsd-ud-test.conllu','batches/scoring-sol61/german'),'cs':('batches/czech-scoring/source/cs_cac-ud-train.conllu','batches/czech-scoring/source/cs_cac-ud-test.conllu','batches/czech-scoring')}
# Independent Python table encoder, rather than copying the C++ inverse formula.
def tables(mode):
 if mode=='vigenere':return [[(p+k)%26 for p in range(26)] for k in range(26)]
 if mode=='variant':return [[(p-k)%26 for p in range(26)] for k in range(26)]
 if mode=='beaufort':return [[(k-p)%26 for p in range(26)] for k in range(26)]
 rows=[]
 for k in range(13):
  second=list(range(13,26));second=second[-k:]+second[:-k] if k else second
  row=[None]*26
  for a,b in zip(range(13),second):row[a]=b;row[b]=a
  rows.append(row)
 return rows
def enc(s,mode,key):
 t=tables(mode);return ''.join('.' if c=='.' else chr(97+t[key[i%len(key)]][ord(c)-97]) for i,c in enumerate(s))
assert enc('geheimnis','porta',[5,2,12])=='opvztnfte'
assert enc('attackatdawn','vigenere',[11,4,12,14,13])=='lxfopvefrnhr'
controls=[];provenance=[]
old=set(c['source_sentence']['text'] for c in json.loads((root/'batches/short-masc/controls.json').read_text()))
for li,(lang,(tr,te,model)) in enumerate(resources.items()):
 train=(root/tr).read_text();trainset={norm(l[9:]) for l in train.splitlines() if l.startswith('# text = ')}
 freq=Counter(c for l in train.splitlines() if l.startswith('# text = ') for c in norm(l[9:]))
 (w/f'{lang}-frequencies.tsv').write_text(''.join(f'{chr(97+i)}\t{freq[chr(97+i)]}\n' for i in range(26)))
 pool=[]
 for block in (root/te).read_text().strip().split('\n\n'):
  raw=next((l[9:] for l in block.splitlines() if l.startswith('# text = ')),None)
  if raw and norm(raw) not in trainset and raw not in old and not any(c.isdigit() for c in raw) and '\tPROPN\t' not in block:
   pool.append({'text':raw,'id':next((l[12:] for l in block.splitlines() if l.startswith('# sent_id = ')),'unknown'),'normalized':norm(raw)})
 random.Random(619369+li).shuffle(pool);casefile=[]
 for j,length in enumerate((55,85,100,115)):
  matches=[p for p in pool if len(p['normalized'])==length]
  if matches:sentences=[matches[0]]
  else:
   pair=next(([a,b] for a in pool for b in pool if a['id']!=b['id'] and len(a['normalized'])+len(b['normalized'])==length),None)
   assert pair,(lang,length);sentences=pair
  text=''.join(p['normalized'] for p in sentences);assert len(text)==length
  for m,mode in enumerate(('vigenere','beaufort','variant','porta')):
   period=(3,9,15,12)[j];rng=random.Random(619369+li*1000+j*100+m);key=[rng.randrange(13 if mode=='porta' else 26) for i in range(period)]
   cipher=enc(text,mode,key);holes=[16,19] if length==85 else [];cipher=''.join('.' if i in holes else c for i,c in enumerate(cipher));truth=''.join('.' if i in holes else c for i,c in enumerate(text))
   label=f'control-{lang}-{mode}-{length}-T{period}';(w/(label+'.txt')).write_text(cipher+'\n');casefile.append(f'{label}\t{mode}\t{cipher}\t24\t2500')
   controls.append({'label':label,'lang':lang,'mode':mode,'length':length,'period':period,'key':key,'ciphertext':cipher,'plaintext':truth,'complete_source_sentences':sentences,'erasure_positions':holes,'training_sentence_injection':False,'prefix_truncation':False})
 (w/f'controls-{lang}.tsv').write_text('\n'.join(casefile)+'\n')
 provenance.append({'lang':lang,'train':tr,'test':te,'model':model,'train_sha256':hashlib.sha256((root/tr).read_bytes()).hexdigest(),'test_sha256':hashlib.sha256((root/te).read_bytes()).hexdigest(),'eligible_test_sentences':len(pool)})
(w/'controls.json').write_text(json.dumps(controls,ensure_ascii=False,indent=2)+'\n');(w/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
cases=[]
for number in (369,345,396,393,367,374):
 path=root/f'ciphers/hcp-{number}/work/transcription.txt';tokens=path.read_text().lower().split();header=[]
 if number==393:header=[tokens.pop(0)];assert header==['3100']
 assert all(len(s)==5 and all(c.isalpha() or c=='?' for c in s) for s in tokens)
 readings=[('literal',tokens)]
 if number==396:
  alt=tokens[:];assert alt[6]=='cscnu';alt[6]='oscnu';readings=[('C',tokens),('O',alt)]
 for reading,groups in readings:
  for omit in (-1,*range(len(groups))):
   body=''.join(g for i,g in enumerate(groups) if i!=omit).replace('?','.')
   for direction,ct in [('forward',body),('reverse',body[::-1])]:
    label=f'target-{number}-{reading}-omit{omit}-{direction}';(w/(label+'.txt')).write_text(ct+'\n')
    cases.append({'label':label,'cipher':number,'reading':reading,'omit_group_zero_based':omit,'removed_group':groups[omit] if omit>=0 else None,'direction':direction,'ciphertext':ct,'source':str(path.relative_to(root)),'excluded_numeric_header':header,'conditional_generic_indicator':omit>=0,'restarts':24 if omit==-1 else 4,'proposals_per_restart':2500 if omit==-1 else 1000,'erasure_count':ct.count('.')})
(w/'targets.json').write_text(json.dumps(cases,indent=2)+'\n');(w/'targets.tsv').write_text(''.join(f"{c['label']}\tall\t{c['ciphertext']}\t{c['restarts']}\t{c['proposals_per_restart']}\n" for c in cases))
(w/'audit.json').write_text(json.dumps({'requested_ciphers':[369,345,396,393,367,374],'ordinary_prior_periodic_results_found':False,'read_existing_332':['exact_periodic.cpp','reciprocal.cpp','NOTES.md'],'332_scope_not_repeated':'Old exhaustive 1–4 and heuristic 1–10, quadgrams only; reused formula family, improved combined scorer here on different targets.','unrelated_periodic_ic':'Unknown two-ring Kryha control, no target runs, not ordinary periodic substitution','target_readings':7,'target_cases':len(cases),'variant_equivalence':'Variant plaintext family equals Vigenere under negation of every residue; emit converted keys, no duplicate optimization.'},indent=2)+'\n')
print('prepared',len(controls),'fresh controls,',len(cases),'target cases')

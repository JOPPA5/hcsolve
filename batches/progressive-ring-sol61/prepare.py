from pathlib import Path
import random,json,hashlib,unicodedata
b=Path(__file__).resolve().parent;r=b.parents[1];source=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def prep(block):
 out=[]
 for line in block.splitlines():
  f=line.split('\t')
  if len(f)>4 and f[0].isdigit():
   s=''.join(digits[int(c)] if c.isdigit() and c.isascii() else c for c in f[1]);s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
   if s:out.append('q'+s+'q' if f[3]=='PROPN' else s)
 return ''.join(out)+'x'
train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';trainset={prep(x) for x in train.read_text().strip().split('\n\n')};pool=[]
for block in source.read_text().strip().split('\n\n'):
 text=prep(block)
 if text not in trainset:pool.append((text,next((s[9:] for s in block.splitlines() if s.startswith('# text = ')),'')))
long=''.join(x[0] for x in pool);p385=long[8000:8385];short=next(((t,s) for t,s in pool if len(t)==115),None)
if not short:short=next(( (a[0]+z[0],[a[1],z[1]]) for a in pool for z in pool if a!=z and len(a[0])+len(z[0])==115))
records=[]
for n,p,provenance in [(385,p385,{'prepared_test_stream_offset':8000,'prefix_truncation':True}),(115,short[0],{'complete_source_sentence_or_sentences':short[1],'prefix_truncation':False})]:
 assert len(p)==n;rng=random.Random(26115385+n);P=rng.sample(range(26),26);O=rng.sample(range(26),26);ipos={c:i for i,c in enumerate(P)};opos={v:c for c,v in enumerate(O)};cipher=''.join(chr(97+opos[(ipos[ord(c)-97]+i)%26]) for i,c in enumerate(p));decoded=''.join(chr(97+P[(O[ord(c)-97]-i)%26]) for i,c in enumerate(cipher));assert decoded==p
 rec={'label':f'control{n}','length':n,'plaintext':p,'ciphertext':cipher,'input_slots':P,'output_positions':O,'seed':26115385+n,'preparation':'same generic TRAIN preparation: accents stripped, PROPN Q delimiters, digits spelled, sentence X markers','provenance':provenance};records.append(rec);folder=b/rec['label'];folder.mkdir(exist_ok=True);(folder/'cipher.txt').write_text(cipher+'\n')
(b/'controls.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');models={f:str(r/'ciphers/hcp-350/work'/f) for f in ['ring-unigrams.tsv','ring-4grams.tsv','ring-5grams.tsv']};(b/'manifest.json').write_text(json.dumps({'model_files':models,'model_hashes':{f:hashlib.sha256(Path(p).read_bytes()).hexdigest() for f,p in models.items()},'TRAIN_source':str(train),'TRAIN_sentence_fraction':.8,'TEST_source':str(source),'TEST_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'excluded_prepared_sentences_found_in_any_TRAIN':True,'schedule':'d_i=i mod26','phase_zero_sign_positive':'initial offset absorbed into arbitrary output ring; negative sign equivalent under reflecting both rings','profile_starts':3000,'profile_steps':10000,'profile_retained':300,'MASC':'8*30000 4gram','joint':'8*100000 4gram from highest language score only'},indent=2)+'\n')

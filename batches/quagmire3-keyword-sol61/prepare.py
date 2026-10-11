from pathlib import Path
import json,unicodedata,random,hashlib,string
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';corpus=R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def normalize(s):
 s=''.join(digits[int(c)] if c.isascii() and c.isdigit() else c for c in s);return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
sentences=[];words=[]
for line in corpus.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():words.append((f[1],f[2],f[3]))
bound=int(.8*len(sentences));train=sentences[:bound];heldout=sentences[bound:];alphabets={}
for sentence in train:
 for form,lemma,pos in sentence:
  for raw in [form,lemma]:
   word=normalize(raw)
   if 3<=len(word)<=24 and len(set(word))>=3:
    alphabet=''.join(dict.fromkeys(word+string.ascii_lowercase));assert len(alphabet)==26;alphabets.setdefault(alphabet,word)
alphabets=sorted(alphabets.items());(P/'alphabets.tsv').write_text(''.join(word+' '+a+'\n' for a,word in alphabets));eligible=[(a,w) for a,w in alphabets if len(set(w))>=7]
def prep(sentence):return ''.join(('q'+s+'q' if pos=='PROPN' else s) for form,lemma,pos in sentence if (s:=normalize(form)))+'x'
heldout=[prep(s) for s in heldout]
def enc(p,alphabet,shifts):
 A={c:i for i,c in enumerate(alphabet)};return ''.join(alphabet[(A[c]+shifts[i%len(shifts)])%26] for i,c in enumerate(p))
for T,offset,seed in [(3,1180,334333061),(9,1350,334399061)]:
 rng=random.Random(seed);a,word=rng.choice(eligible);shifts=[rng.randrange(1,26) for _ in range(T)];plain=''.join(heldout[offset:])[:150];assert len(plain)==150;ct=enc(plain,a,shifts);erased=''.join('?' if i in [70,94] else c for i,c in enumerate(ct));folder=P/f'controlT{T}';folder.mkdir(exist_ok=True);(folder/'cipher.txt').write_text(erased+'\n');(folder/'planted.json').write_text(json.dumps(dict(keyword=word,alphabet_slots=a,absolute_shifts=shifts,period=T,heldout_offset=offset,training_sentence_boundary=bound,seed=seed,plaintext=plain,full_ciphertext=ct,erased_ciphertext=erased,expected_readable_plaintext=''.join('?' if i in [70,94] else c for i,c in enumerate(plain)),erasure_positions0=[70,94]),indent=2)+'\n')
manifest=dict(keyword_source='normalized TRAIN forms andlemmas only, length3..24 and>=3distinctletters; exactalphabetdedup',alphabet_count=len(alphabets),control_keyword_pool='TRAIN candidatealphabets whosekeyword>=7distinctletters, randomindependentseed',training_sentences=bound,heldout_sentences=len(heldout),corpus_sha256=hashlib.sha256(corpus.read_bytes()).hexdigest(),alphabet_list_sha256=hashlib.sha256((P/'alphabets.tsv').read_bytes()).hexdigest(),frozen_models={str(n):hashlib.sha256((M/f'ring-{n}grams.tsv').read_bytes()).hexdigest() for n in [4,5]},frozen_unigram_sha256=hashlib.sha256((M/'ring-unigrams.tsv').read_bytes()).hexdigest(),source_sha256=hashlib.sha256((R/'ciphers/hcp-334/source/cryptogram.jpg').read_bytes()).hexdigest());(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(manifest['alphabet_count'],[json.loads((P/f'controlT{T}/planted.json').read_text())['keyword'] for T in [3,9]])

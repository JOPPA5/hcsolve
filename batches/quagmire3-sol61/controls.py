from pathlib import Path
import random,json,unicodedata,subprocess,time,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def prep(tokens):
 out=[]
 for word,pos in tokens:
  word=''.join(digits[int(c)] if c.isascii() and c.isdigit() else c for c in word);word=''.join(c for c in unicodedata.normalize('NFD',word.lower()) if 'a'<=c<='z');out.append('q'+word+'q' if word and pos=='PROPN' else word)
 return ''.join(out)+'x'
sentences=[];words=[];corpus=R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
for line in corpus.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  fields=line.split('\t')
  if fields[0].isdigit():words.append((fields[1],fields[3]))
bound=int(.8*len(sentences));heldout=[prep(x) for x in sentences[bound:]]
def enc(plain,A,shifts):
 inv={v:i for i,v in enumerate(A)};return ''.join('?' if c=='?' else chr(97+inv[(A[ord(c)-97]+shifts[i%len(shifts)])%26]) for i,c in enumerate(plain))
def dec(ct,A,shifts):
 inv={v:i for i,v in enumerate(A)};return ''.join('?' if c=='?' else chr(97+inv[(A[ord(c)-97]-shifts[i%len(shifts)])%26]) for i,c in enumerate(ct))
quad={g:float(v) for g,v in (line.split() for line in (M/'ring-4grams.tsv').read_text().splitlines())}
def score(p):return sum(quad.get(p[i:i+4],-4) for i in range(len(p)-3) if '?' not in p[i:i+4])
results=[]
for T,offset,seed in [(3,900,334330061),(9,1050,334390061)]:
 plain=''.join(heldout[offset:])[:150];rng=random.Random(seed);A=rng.sample(range(26),26);shifts=[rng.randrange(26) for _ in range(T)]
 while shifts[0]==0:shifts=[rng.randrange(26) for _ in range(T)]
 ct=enc(plain,A,shifts);erased=''.join('?' if i in [70,94] else c for i,c in enumerate(ct));expected=''.join('?' if i in [70,94] else c for i,c in enumerate(plain));assert dec(ct,A,shifts)==plain and enc(dec(erased,A,shifts),A,shifts)==erased
 folder=P/f'controlT{T}';folder.mkdir(exist_ok=True);cipher=folder/'cipher.txt';cipher.write_text(erased+'\n');fixture=dict(plaintext=plain,expected_readable_plaintext=expected,full_ciphertext=ct,erased_ciphertext=erased,alphabet_positions=A,absolute_shifts=shifts,period=T,seed=seed,heldout_sentence_offset=offset,training_sentence_boundary=bound,erasure_positions0=[70,94]);(folder/'planted.json').write_text(json.dumps(fixture,indent=2)+'\n');output=folder/'search.txt';start=time.monotonic()
 if not output.exists():
  with output.open('w') as f,(folder/'progress.txt').open('w') as log:subprocess.run([str(P/'search'),str(M/'ring-4grams.tsv'),str(cipher),str(T),'384','30000',str(seed+771)],stdout=f,stderr=log,check=True)
 lines=output.read_text().splitlines();sc,moves=lines[0].split();key=[int(x) for x in lines[1].split(',') if x];keyshifts=[int(x) for x in lines[2].split(',') if x];candidate=lines[3];assert sorted(key)==list(range(26));assert dec(erased,key,keyshifts)==candidate and enc(candidate,key,keyshifts)==erased;assert abs(score(candidate)-float(sc))<.02
 agreement=sum(c==d for c,d in zip(candidate,expected) if d!='?');r=dict(**fixture,recovered_alphabet_positions=key,recovered_absolute_shifts=keyshifts,candidate_plaintext=candidate,matching_readable_letters=agreement,readable_letters=148,exact_readable_plaintext=agreement==148,score=float(sc),true_erased_score=score(expected),proposals=int(moves),seconds=time.monotonic()-start,blind_seed=seed+771,truth_used_for_search=False,independent_cipher_inverse_exact=True,unknown_plaintext_positions_not_claimed=True);results.append(r);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');(P/'results.json').write_text(json.dumps(results,indent=2)+'\n');print(T,agreement,r['score'],r['true_erased_score'],r['seconds'],flush=True)
(P/'manifest.json').write_text(json.dumps(dict(model='C_i=A^-1((A(P_i)+R[i modT]) mod26); same unknown bijective26alphabet',canonicalization='only subtract A[a] from allalphabetpositions; R unchanged, R0 notfixed',periods=[3,9],restarts=384,proposals_per_restart=30000,phase='position indices retained across two erasures',score='frozen TRAIN4gram; windows containing erasure omitted',corpus_sha256=hashlib.sha256(corpus.read_bytes()).hexdigest(),frozen_model_sha256=hashlib.sha256((M/'ring-4grams.tsv').read_bytes()).hexdigest(),source_sha256=hashlib.sha256((R/'ciphers/hcp-334/source/cryptogram.jpg').read_bytes()).hexdigest()),indent=2)+'\n')

from pathlib import Path
import json,random,unicodedata,subprocess,time,concurrent.futures,sys
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
five={s:float(v)for s,v in [l.split()for l in (M/'ring-5grams.tsv').read_text().splitlines()]}
quad={s:float(v)for s,v in [l.split()for l in (M/'ring-4grams.tsv').read_text().splitlines()]}
def encrypt(text,slots,O,phase,sign=1):
 I={letter:i for i,letter in enumerate(slots)};inv={pos:c for c,pos in enumerate(O)};d=0;out=[]
 for i,c in enumerate(text):out.append(chr(97+inv[(I[ord(c)-97]+d)%26]));d=(d+sign*steps[(phase+i)%17])%26
 return ''.join(out)
def decrypt(ct,slots,O,phase):
 out=[];d=0
 for i,c in enumerate(ct):out.append(chr(97+slots[(O[ord(c)-97]-d)%26]));d=(d+steps[(phase+i)%17])%26
 return ''.join(out)
def parse(lines):return dict(language_score=float(lines[0].split()[0]),plaintext_joined=lines[0].split()[1],input_slots=[int(x)for x in lines[1].split(',')if x],output_positions=[int(x)for x in lines[2].split(',')if x])
def verify(r,cts,phase):
 assert sorted(r['input_slots'])==list(range(26));assert sorted(r['output_positions'])==list(range(26))
 texts=[];at=0
 for ct in cts:
  text=r['plaintext_joined'][at:at+len(ct)];at+=len(ct);assert encrypt(text,r['input_slots'],r['output_positions'],phase)==ct;assert decrypt(ct,r['input_slots'],r['output_positions'],phase)==text;texts.append(text)
 assert at==len(r['plaintext_joined']);order=5 if r.get('objective')=='standalone frozen5gram' else 4;table=five if order==5 else quad;independent=sum(table.get(t[i:i+order],-order)for t in texts for i in range(len(t)-order+1));assert abs(independent-r['language_score'])<.08,(independent,r['language_score']);r.update(plaintext_messages=texts,independent_reencryption_exact_both=True,independent_inverse_exact_both=True,independent_boundary_score=independent,quadgram_windows=sum(len(t)-3 for t in texts),scoring_windows=sum(len(t)-order+1 for t in texts))
def pipeline(label,cts,phase,truth=None):
 folder=P/label/f'phase{phase}';folder.mkdir(parents=True,exist_ok=True);cf=folder/'cipher.txt';cf.write_text('\n'.join(cts)+'\n');start=time.monotonic()
 def command(binary,args,out):
  f=folder/out
  if not f.exists():
   with f.with_suffix('.partial').open('w')as stream:subprocess.run([str(P/binary)]+list(map(str,args)),stdout=stream,check=True)
   f.with_suffix('.partial').rename(f)
  return f.read_text().splitlines()
 ic=command('pair_profile',[cf,phase,1,3000,M/'ring-unigrams.tsv'],'profile.txt');batch=command('pair_masc',[M,cf,phase,1,folder/'profile.txt'],'masc.txt');assert len(batch)==len(ic)*4;rows=[]
 for j,line in enumerate(ic):
  assert int(batch[4*j].split()[0])==j;r=parse(batch[4*j+1:4*j+4]);r.update(profile_candidate_index=j,profile_score=float(line.split()[0]));verify(r,cts,phase);rows.append(r)
 rows.sort(key=lambda x:x['language_score'],reverse=True);(folder/'reranked.json').write_text(json.dumps(rows,indent=2));top=rows[0];seed=folder/'seed.txt';seed.write_text(' '.join(map(str,top['input_slots']+top['output_positions']))+'\n');r=parse(command('pair_refine',[M,cf,phase,1,seed],'refine.txt'));verify(r,cts,phase);r.update(label=label,phase=phase,sign=1,lengths=list(map(len,cts)),seconds=time.monotonic()-start,profile_candidates=len(rows),seed_profile_rank=top['profile_candidate_index'],seed_language_rank=0,seed_language_score=top['language_score'],model='shared two mixed rings, shared original17 phase, reset displacement and step index at each message; one press per letter',assumptions='shared historical keys/phase and original fixed17 schedule unproved for targets')
 if truth is not None:r.update(exact_plaintext_both=r['plaintext_messages']==truth,matches_per_message=[sum(a==b for a,b in zip(t,u))for t,u in zip(r['plaintext_messages'],truth)],truth_used_for_selection=False)
 (folder/'result.json').write_text(json.dumps(r,indent=2));print(label,phase,r['language_score'],r.get('exact_plaintext_both'),r.get('matches_per_message'),r['seconds'],flush=True);return r

def prepare(tokens):
 digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];out=[]
 for word,pos in tokens:
  w=''.join(digits[int(c)]if c.isdigit()and c.isascii()else c for c in word);w=''.join(c for c in unicodedata.normalize('NFD',w.lower())if'a'<=c<='z')
  if w:out.append('q'+w+'q'if pos=='PROPN'else w)
 return ''.join(out)+'x'
def controls():
 sentences=[];words=[];source=R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
 for line in source.read_text().splitlines()+['']:
  if not line:
   if words:sentences.append(words);words=[]
  elif not line.startswith('#'):
   f=line.split('\t')
   if f[0].isdigit():words.append((f[1],f[3]))
 bound=int(.8*len(sentences));heldout=[prepare(s)for s in sentences[bound:]];results=[]
 for j,(phase,sign,offsets)in enumerate([(4,1,[900,1000]),(10,-1,[1200,1300])]):
  texts=[''.join(heldout[o:])[:385]for o in offsets];assert all(len(t)==385 for t in texts);rng=random.Random(77061100+j);slots=rng.sample(range(26),26);O=rng.sample(range(26),26);cts=[encrypt(t,slots,O,phase,sign)for t in texts];label=f'control{j}';folder=P/label;folder.mkdir(exist_ok=True);plant=dict(input_slots=slots,output_positions=O,phase=phase,sign=sign,plaintext_messages=texts,ciphertext_messages=cts,heldout_sentence_offsets=offsets,training_boundary=bound,seed=77061100+j);(folder/'plant.json').write_text(json.dumps(plant,indent=2))
  refslots=slots if sign==1 else[slots[(-i)%26]for i in range(26)];refO=O if sign==1 else[(-x)%26 for x in O];assert [decrypt(c,refslots,refO,phase)for c in cts]==texts
  continued=encrypt(''.join(texts),slots,O,phase,sign)[385:];plant['continued_wrong_second_message_equal_positions']=sum(a==b for a,b in zip(continued,cts[1]));(folder/'plant.json').write_text(json.dumps(plant,indent=2));results.append(pipeline(label,cts,phase,texts));(P/'control-results.json').write_text(json.dumps(results,indent=2))
def refine5(r,truth=None):
 folder=P/r['label']/f"phase{r['phase']}";seed=folder/'seed5.txt';seed.write_text(' '.join(map(str,r['input_slots']+r['output_positions']))+'\n');out=folder/'refine5.txt'
 if not out.exists():
  with out.with_suffix('.partial').open('w')as stream:subprocess.run([str(P/'pair_refine5'),str(M),str(folder/'cipher.txt'),str(r['phase']),'1',str(seed)],stdout=stream,check=True)
  out.with_suffix('.partial').rename(out)
 v=parse(out.read_text().splitlines());v.update(objective='standalone frozen5gram',label=r['label'],phase=r['phase'],sign=1,seed_selection='unchanged operative fourgram winner; no truth based choice',truth_used_for_selection=False);verify(v,(folder/'cipher.txt').read_text().split(),r['phase'])
 if truth is not None:v.update(exact_plaintext_both=v['plaintext_messages']==truth,matches_per_message=[sum(a==b for a,b in zip(t,u))for t,u in zip(v['plaintext_messages'],truth)])
 (folder/'result5.json').write_text(json.dumps(v,indent=2));print('fivegram',r['label'],r['phase'],v['language_score'],v.get('matches_per_message'),flush=True);return v
if __name__=='__main__':controls()

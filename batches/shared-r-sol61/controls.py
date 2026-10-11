from pathlib import Path
import json,random,unicodedata,hashlib,re
w=Path(__file__).resolve().parent;root=w.parents[1]
normalize=lambda s: ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
train=root/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';test=root/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu'
trainset={normalize(s[9:]) for s in train.read_text().splitlines() if s.startswith('# text = ')}
pool=[]
for block in test.read_text().split('\n\n'):
 lines=block.splitlines();text=next((s[9:] for s in lines if s.startswith('# text = ')),None);sid=next((s[12:] for s in lines if s.startswith('# sent_id = ')),None)
 if text and normalize(text) not in trainset and not any(c.isdigit() for c in text) and not any('\tPROPN\t' in s for s in lines):pool.append(dict(text=text,id=sid,norm=normalize(text)))
print('eligible independently held-out sentences',len(pool))
def canonical(k):i=k.index(1);return k[i:]+k[:i]
def aligned(k,n):i=k.index(n);return k[i:]+k[:i]
def enc(s,k,n):
 labels=aligned(k,n);rows=[s[i:i+len(k)] for i in range(0,len(s),len(k))]
 return ''.join(row[c] for value in range(1,len(k)+1) for c,label in enumerate(labels) if label==value for row in rows if c<len(row))
def dec(s,k,n):
 labels=aligned(k,n);cells=[None]*len(s);at=0
 for value in range(1,len(k)+1):
  c=labels.index(value)
  for j in range(c,len(s),len(k)):cells[j]=s[at];at+=1
 assert at==len(s);return ''.join(cells)
reference=json.loads(root.joinpath('batches/historical-context/r-example-verification.json').read_text());s=reference['published_plaintext'];verified=[]
for stage in reference['stages']:
 labels=stage['physical_column_labels'];previous=s;s=enc(s,labels,7);assert s==stage['output'] and dec(s,labels,7)==previous
 verified.append(dict(width=len(labels),exact_published_output=True))
w.joinpath('primary-verification.json').write_text(json.dumps(dict(independent_encoder='explicit row grid, ascending label',stages=verified,gauge='cyclic physical array rotations produce identical aligned keys',source_target_solution=False),indent=2))
records=[]
for case,start in enumerate([15,120]):
 selected=[];raw='';i=start
 while len(normalize(raw))<200:
  selected.append(pool[i]);raw+=' '+pool[i]['text'];i+=1
 long=normalize(raw)[:200];short_entry=next(s for s in pool[i+20:] if len(s['norm'])>=50);short=short_entry['norm'][:50]
 rng=random.Random(614395+case);keys=[]
 for width in [21,19,20]:
  k=list(range(1,width+1));rng.shuffle(k);keys.append(canonical(k))
 alignments=[[3,13],[6,16]][case];messages=[]
 for j,p in enumerate([long,short]):
  n=alignments[j];stages=[];s=p
  for k in keys:s=enc(s,k,n);stages.append(s)
  back=s
  for k in reversed(keys):back=dec(back,k,n)
  assert back==p
  messages.append(dict(plaintext=p,ciphertext=s,alignment=n,intermediates=stages,raw_test_sentences=selected if j==0 else [short_entry]))
 label=f'heldout-pair-{case}';records.append(dict(label=label,keys=keys,convention='constant',messages=messages))
 w.joinpath(label+'.input.txt').write_text('\n'.join(str(m['alignment'])+' '+m['ciphertext'] for m in messages)+'\n')
 w.joinpath(label+'.keys.txt').write_text('\n'.join(' '.join(map(str,k)) for k in keys)+'\n')
w.joinpath('controls.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));w.joinpath('corpus-provenance.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [train,test]},indent=2))
# Conditional constraints only; no target plaintext/key is assumed.
j=json.loads(root.joinpath('ciphers/hcp-395/work/joint-indicator-constraints.json').read_text());scenarios=[]
for row in j:
 for convention,limit in [('constant',19),('progressive',18)]:
  pairs=[p for p in row['possible_pairs'] if max(p)<=limit]
  if pairs:scenarios.append(dict(reading396=row['reading396'],indicator_group=row['position'],convention=convention,alignment_pairs=pairs))
w.joinpath('target-conditional-scenarios.json').write_text(json.dumps(scenarios,indent=2))
print('two fresh 200/50-letter shared-key controls, independent primary example checks PASS')

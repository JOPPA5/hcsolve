from pathlib import Path
import json, itertools, unicodedata, random, heapq
P=Path(__file__).parent
example=json.loads(Path('batches/historical-context/r-example-verification.json').read_text())
base=[x['physical_column_labels'] for x in example['stages']]
models=[]
for n,weight in [(3,.15),(4,.4),(5,.8)]:
 lines=Path(f'batches/scoring-sol61/frequency/model{n}.tsv').read_text().splitlines()
 models.append((n,weight,float(lines[0].split()[1]),dict((s,float(v)) for s,v in (line.split() for line in lines[1:]))))
def score(s):return sum(weight*sum(m.get(s[i:i+n],floor) for i in range(len(s)-n+1) if '.' not in s[i:i+n]) for n,weight,floor,m in models)
def align(k,n):
 j=k.index(n);return k[j:]+k[:j]
def enc(s,k):return ''.join(s[i] for col in sorted(range(len(k)),key=k.__getitem__) for i in range(col,len(s),len(k)))
def dec(s,k):
 out=['']*len(s);at=0
 for col in sorted(range(len(k)),key=k.__getitem__):
  for i in range(col,len(s),len(k)):out[i]=s[at];at+=1
 return ''.join(out)
keys=[]
for order in itertools.permutations(range(3)):
 for progressive in [False,True]:
  bound=min(len(base[b])-j if progressive else len(base[b]) for j,b in enumerate(order))
  for n in range(1,bound+1):
   ks=[align(base[b],n+j if progressive else n) for j,b in enumerate(order)]
   keys.append((order,progressive,n,ks))
def solve(ct):
 best=[]
 for order,prog,n,ks in keys:
  pt=ct
  for k in reversed(ks):pt=dec(pt,k)
  sc=score(pt);item=(sc,order,prog,n,pt,ks)
  if len(best)<10:heapq.heappush(best,item)
  elif sc>best[0][0]:heapq.heapreplace(best,item)
 return [dict(score=sc,stage_order=order,progressive=prog,n=n,plaintext=pt,physical_labels=ks) for sc,order,prog,n,pt,ks in sorted(best,reverse=True)]
def normalize(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
if __name__ == '__main__':
 test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text()
 train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text()
 sentences=[l[9:] for l in test.splitlines() if l.startswith('# text = ')];trainset={l[9:] for l in train.splitlines() if l.startswith('# text = ')}
 controls=[]
 for i,(length,prog,n) in enumerate([(115,False,11),(100,True,7)]):
  sentence=next(s for s in sentences[i*20:] if len(normalize(s))>=length and s not in trainset)
  pt=normalize(sentence)[:length];ks=[align(k,n+j if prog else n) for j,k in enumerate(base)]
  ct=pt
  for k in ks:ct=enc(ct,k)
  candidates=solve(ct);assert candidates[0]['plaintext']==pt
  controls.append(dict(source_sentence=sentence,excluded_from_train=True,plaintext=pt,ciphertext=ct,physical_labels=ks,candidates=candidates,exact_best=True))
 (P/'controls.json').write_text(json.dumps(controls,indent=2,ensure_ascii=False))
 rows=[]
 for num in [396,345,393,367,374,369,371,399,395,363,364]:
  path=Path(f'ciphers/hcp-{num}/work/transcription.txt') if num!=363 else Path('ciphers/hcp-363/work/transcription-raw.txt')
  gs=[''.join(c if 'a'<=c<='z' else '.' for c in g.lower()) for g in path.read_text().split()]
  variants=[('literal',''.join(gs))]
  if num in [396,345,393,367,374,369,364]:variants += [(f'omit-{i+1}',''.join(g for j,g in enumerate(gs) if i!=j)) for i in range(len(gs))]
  if num==396:
   alt=gs[:];alt[6]='o'+alt[6][1:];variants += [('O-literal',''.join(alt))]+[(f'O-omit-{i+1}',''.join(g for j,g in enumerate(alt) if i!=j)) for i in range(len(alt))]
  for tag,raw in variants:
   for reverse in [False,True]:
    ct=raw[::-1] if reverse else raw;best=solve(ct)
    for c in best:
     reen=c['plaintext']
     for k in c['physical_labels']:reen=enc(reen,k)
     assert reen==ct
    row=dict(cipher=num,variant=tag,reverse=reverse,ciphertext=ct,tested=len(keys),candidates=best,whole_reencryption_exact=True)
    rows.append(row)
  (P/'targets.json').write_text(json.dumps(rows,indent=2));print(num,len(rows),max((r['candidates'][0] for r in rows if r['cipher']==num),key=lambda x:x['score']/len(x['plaintext']))['plaintext'],flush=True)
 (P/'summary.json').write_text(json.dumps(dict(cases=len(rows),keys_per_case=len(keys),all_retained_reencrypt_exact=True,controls_exact=2,historical_key_reuse_is_unproven=True),indent=2))

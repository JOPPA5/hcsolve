from pathlib import Path
import json, random, subprocess, unicodedata

p=Path(__file__).parent
alpha26='abcdefghijklmnopqrstuvwxyz'; alpha28=alpha26+'{|'
def norm(s,N):
    s=s.lower()
    if N==28:s=s.replace('č','{').replace('š','|')
    return ''.join(c for c in unicodedata.normalize('NFD',s) if c in (alpha26 if N==26 else alpha28))
test=[l[9:] for l in (p/'source/cs_cac-ud-test.conllu').read_text().splitlines() if l.startswith('# text = ')]
train=set(l[9:] for l in (p/'source/cs_cac-ud-train.conllu').read_text().splitlines() if l.startswith('# text = '))
rows=[]
for N in [26,28]:
    alpha=alpha26 if N==26 else alpha28
    for j,n in enumerate([115,85]):
        sentence=next(s for s in test[20*j:] if len(norm(s,N))>=n and s not in train)
        text=norm(sentence,N)[:n]; key=list(alpha); random.Random(334700+N+j).shuffle(key)
        ct=''.join(key[alpha.index(c)] for c in text)
        erased=[15,19] if n==85 else []
        ct=''.join('.' if i in erased else c for i,c in enumerate(ct))
        truth=''.join('.' if i in erased else c for i,c in enumerate(text)).replace('{','c').replace('|','s')
        f=p/f'control-{N}-{n}.txt'; f.write_text(ct+'\n')
        r=subprocess.run([str(p/f'mono{N}'),str(p),str(f),'40'],text=True,capture_output=True,check=True)
        (p/f'control-{N}-{n}-result.txt').write_text(r.stdout+'\n'+r.stderr)
        fields=r.stdout.split(); found=fields[2]; k=list(fields[1]); matching=[]
        for a in range(N):
            for b in range(a,N):
                kk=k[:];kk[a],kk[b]=kk[b],kk[a]
                candidate=''.join('.' if c=='.' else kk[alpha.index(c)] for c in ct).replace('{','c').replace('|','s')
                if candidate==truth:matching.append([a,b])
        row=dict(N=N,length=n,source_sentence=sentence,excluded_from_train=sentence not in train,plaintext_encoded=text,folded_erased_truth=truth,planted_key=''.join(key),found=found,exact_folded=found==truth,matched_known=sum(a==b for a,b in zip(found,truth) if b!='.'),blind_swap_neighborhood_contains_truth=bool(matching),diagnostic_matching_swaps=matching)
        rows.append(row);(p/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
        print(N,n,row['exact_folded'],row['matched_known'],bool(matching),flush=True)

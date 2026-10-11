from pathlib import Path
import json, random, subprocess, unicodedata, hashlib
P=Path(__file__).parent
train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu')
test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu')
def norm(text):return ''.join(c for c in unicodedata.normalize('NFD',text.lower()) if 'a'<=c<='z')
def signature(key):
    unique=sorted(set(key));return tuple(unique.index(c) for c in key)
words={}
for line in train.read_text().splitlines():
    fields=line.split('\t')
    if len(fields)<3 or not fields[0].isdigit():continue
    for raw in fields[1:3]:
        word=norm(raw)
        if 3<=len(word)<=24 and len(set(word))<len(word) and len(set(word))>=2:
            sig=signature(word)
            if sig not in words:words[sig]=word
keys=sorted(words.values());(P/'keywords.txt').write_text('\n'.join(keys)+'\n')
def order(n,key):
    return [row+col for ch in sorted(set(key)) for row in range(0,n,len(key)) for col,c in enumerate(key) if c==ch and row+col<n]
def enc(pt,key):return ''.join(pt[i] for i in order(len(pt),key))
def attack(name,ct):
    path=P/f'{name}.txt';path.write_text(ct+'\n')
    raw=subprocess.check_output([str(P/'search'),str(P/'keywords.txt'),'ciphers/hcp-350/work/ring-4grams.tsv','ciphers/hcp-350/work/ring-5grams.tsv',str(path)],text=True)
    (P/f'{name}-candidates.tsv').write_text(raw);out=[]
    for line in raw.splitlines():
        score,key,pt=line.split('\t');assert enc(pt,key)==ct
        out.append(dict(score=float(score),keyword=key,rank_signature=signature(key),plaintext=pt,whole_reencrypt_exact=True))
    return out
training={l[9:] for l in train.read_text().splitlines() if l.startswith('# text = ')}
sentences=[l[9:] for l in test.read_text().splitlines() if l.startswith('# text = ') and l[9:] not in training]
teststream='x'.join(norm(s) for s in sentences)
rng=random.Random(369625);controls=[]
pool=[k for k in keys if 6<=len(k)<=15]
for j,n in enumerate([55,65,115,400]):
    key=rng.choice(pool);pt=teststream[36000+j*500:36000+j*500+n];assert len(pt)==n
    ct=enc(pt,key);candidates=attack(f'control{n}',ct)
    r=dict(length=n,plaintext=pt,ciphertext=ct,planted_keyword=key,candidates=candidates,exact_best=candidates[0]['plaintext']==pt,truth_used_for_search=False)
    controls.append(r);(P/'controls.json').write_text(json.dumps(controls,indent=2)+'\n');print('control',n,r['exact_best'],flush=True)
manifest=dict(keywords=len(keys),source='TRAIN forms/lemmas only; numeric rank patterns deduplicated',train_sha256=hashlib.sha256(train.read_bytes()).hexdigest(),test_sha256=hashlib.sha256(test.read_bytes()).hexdigest(),keyword_sha256=hashlib.sha256((P/'keywords.txt').read_bytes()).hexdigest(),target_scope='whole literal bodies, forward/reverse; no indicator omission; nonletters erased with phase preserved')
(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
if not all(r['exact_best'] for r in controls):raise SystemExit('No target run under failed controls')
targets=[]
for num in [363,393,369,345,396,367,374,371,399,395]:
    path=Path(f'ciphers/hcp-{num}/work')/('transcription-raw.txt' if num==363 else 'transcription.txt');groups=path.read_text().lower().split();header=groups.pop(0) if groups[0].isdigit() else None
    ct=''.join(''.join(c if 'a'<=c<='z' else '.' for c in g) for g in groups)
    for rev in [False,True]:
        working=ct[::-1] if rev else ct;candidates=attack(f'target{num}-reverse{int(rev)}',working)
        r=dict(cipher=num,whole_reverse=rev,excluded_numeric_header=header,original_ciphertext=ct,candidates=candidates)
        for c in candidates:assert (enc(c['plaintext'],c['keyword'])[::-1] if rev else enc(c['plaintext'],c['keyword']))==ct
        targets.append(r);(P/'targets.json').write_text(json.dumps(targets,indent=2)+'\n');print('target',num,rev,candidates[0]['score'],candidates[0]['plaintext'],flush=True)

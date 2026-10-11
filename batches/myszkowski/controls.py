from pathlib import Path
import json, random, subprocess, unicodedata
p=Path(__file__).parent
def encrypt(s,k):
    return ''.join(s[i] for rank in sorted(set(k)) for row in range((len(s)+len(k)-1)//len(k)) for col in range(len(k)) if k[col]==rank for i in [row*len(k)+col] if i<len(s))
def normalize(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
# Primary ACA published mechanism test (distinct from recovery controls).
aca_plain='incompletecolumnarwithpatternwordkeyandlettersundersamenumbertakenoffbyrowfromtoptobottom'
aca_key=[1,0,2,0,2,0]
aca_cipher='NOPEE OUNRI HATRW RKYNL TESNE SMNME TKNFB RWRMO TBTOI LLWTO ATDER OOTOC MTCMA TPEND EDERU RAUBA EFYFO POTM'.replace(' ','').lower()
assert encrypt(aca_plain,aca_key)==aca_cipher
(p/'aca-vector.json').write_text(json.dumps(dict(source='https://www.cryptogram.org/downloads/aca.info/ciphers/Myszkowski.pdf',published_example=True,plaintext=aca_plain,key=aca_key,ciphertext=aca_cipher,exact=True),indent=2))
test=Path('ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu'); train=Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu')
sentences=[l[9:] for l in test.read_text().splitlines() if l.startswith('# text = ')]
training=set(l[9:] for l in train.read_text().splitlines() if l.startswith('# text = '))
rows=[]
for j,(n,w) in enumerate([(100,8),(85,7)]):
    original=next(s for s in sentences[j*10:] if len(normalize(s))>=n and s not in training)
    pt=normalize(original)[:n];rng=random.Random(374880+j);k=[rng.randrange(4) for _ in range(w)]
    distinct=sorted(set(k));k=[distinct.index(x) for x in k];assert len(set(k))<w
    ct=encrypt(pt,k);erasures=[15,19] if n==85 else []
    ct=''.join('.' if i in erasures else c for i,c in enumerate(ct))
    f=p/f'control-{n}.txt';f.write_text(ct+'\n')
    out=subprocess.check_output([str(p/'solver'),'batches/scoring-sol61/frequency',str(f),'8',str(p/'keyword-patterns.txt')],text=True)
    (p/f'control-{n}-result.txt').write_text(out)
    candidates=[]
    for line in out.splitlines()[1:]:
        sc,key,plain=line.split();candidates.append(dict(score=float(sc),key=[ord(x)-97 for x in key],plaintext=plain))
    truth=encrypt(''.join(chr(97+i%26) for i in range(n)),k)
    positions=[ord(c)-97 for c in truth] # Not used: plaintext position erasures computed independently below.
    erased_plain=set(); at=0
    for rank in sorted(set(k)):
        for row in range((n+w-1)//w):
            for col in range(w):
                pos=row*w+col
                if k[col]==rank and pos<n:
                    if at in erasures:erased_plain.add(pos)
                    at+=1
    expected=''.join('.' if i in erased_plain else c for i,c in enumerate(pt))
    ranks=[i for i,c in enumerate(candidates) if c['plaintext']==expected]
    row=dict(length=n,width=w,source_sentence=original,excluded_from_train=original not in training,plaintext=pt,planted_key=k,ciphertext=ct,erased_plain_positions=sorted(erased_plain),expected=expected,exact_best=candidates[0]['plaintext']==expected,true_in_top100=bool(ranks),diagnostic_truth_ranks=ranks,found=candidates[0],tested=out.splitlines()[0])
    rows.append(row);(p/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(n,row['exact_best'],ranks,flush=True)

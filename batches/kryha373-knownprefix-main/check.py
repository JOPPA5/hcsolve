"""Conditional fixed-ring compatibility, not a general Kryha exclusion."""
from pathlib import Path
import json, unicodedata, random, hashlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
keypath = ROOT / 'ciphers/hcp-350/work/kryha-decipherment/key.json'
key = json.loads(keypath.read_text())
pinv = [key['P'].index(i) for i in range(26)]
out = key['O']
ctpath = ROOT / 'batches/kryha373-collation-sol61/ciphertext650.txt'
ptpath = ROOT / 'batches/kryha373-collation-sol61/plaintext-typed.txt'
ct = ctpath.read_text().strip().lower()
published_prefix = ptpath.read_text().split('6.000')[0]

def letters(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if 'a' <= c <= 'z')

def checks(pt, cipher):
    rows = []
    for swap in (False, True):
        pc, oc = (out, pinv) if swap else (pinv, out)
        d = [(oc[ord(c)-97] - pc[ord(p)-97]) % 26 for p,c in zip(pt,cipher)]
        for sign in (1,-1):
            for m in range(2,53):
                n = len(d)-m
                if n <= 0: continue
                matched = sum((d[i+m]-d[i]) % 26 == sign*179 % 26 for i in range(n))
                rows.append(dict(swapped=swap,sign=sign,period=m,matched=matched,comparisons=n,exact=matched==n))
    return rows

# Independent physical walk: choose random stops, advance literal adjacent distances.
rng = random.Random(373179)
stops = sorted(rng.sample(range(52),23)); offset = rng.randrange(23)
stops = stops[offset:] + stops[:offset]; disp = rng.randrange(26)
controlpt = letters(published_prefix)
controlct = ''
for i,p in enumerate(controlpt):
    coordinate = (pinv[ord(p)-97]+disp) % 26
    controlct += chr(97+out.index(coordinate))
    a,b = stops[i%23],stops[(i+1)%23]
    while True:
        disp += key['adjacent_distances'][a]; a=(a+1)%52
        if a == b: break
controls = checks(controlpt,controlct)
assert any(r['exact'] and r['period']==23 and not r['swapped'] and r['sign']==1 for r in controls)
targets = []
for omit_handwritten_d in (False, True):
    prepared_prefix = published_prefix.replace('Ústredni','Ústreni') if omit_handwritten_d else published_prefix
    for glyph53 in ('l','i'):
        for glyph90 in ('e','a'):
            variantct = list(ct)
            variantct[52]=glyph53
            variantct[89]=glyph90
            variantct=''.join(variantct)
            for marker in ('','j','x'):
                for mergej in (False,True):
                    text = prepared_prefix.replace('j','i').replace('J','I') if mergej else prepared_prefix
                    p = letters(text.replace(',',marker))
                    for omit in (0,5):
                        rows = checks(p,variantct[omit:])
                        ranked = sorted(rows,key=lambda r:(-r['matched']/r['comparisons'],-r['comparisons']))
                        targets.append(dict(omit_handwritten_d=omit_handwritten_d,glyph53=glyph53,glyph90=glyph90,marker=marker,natural_j_to_i=mergej,omitted_prefix=omit,length=len(p),exact=[r for r in rows if r['exact']],best=ranked[:5]))
summary = dict(
    scope='Only transferred350 rings, ordinary full-wheel179 advance, periods2..52, stated source/preparation alternatives. Unknown rings, errorful source/preparation and selective extra presses are outside this test.',
    published_context_not_new_plaintext=True,
    source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (keypath,ctpath,ptpath)},
    control=dict(plaintext=controlpt,ciphertext=controlct,stops=stops,exact=[r for r in controls if r['exact']]),
    targets=targets,
)
(HERE/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(dict(prefix_length=len(controlpt),control_exact=summary['control']['exact'],target_exact_count=sum(len(x['exact']) for x in targets))))

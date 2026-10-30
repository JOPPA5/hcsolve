# Independent decoder (reviewer). Key taken from finished family card hcp-1545 (labels: H=CH glyph, F=shallow v).
import json, sys, collections
K = dict(zip("12345678bcdfghmnpqrst", "YUOIEAJL PSTVKRNMBZHCD".replace(" ","")))
K.update({"H":"CH","F":"F","?":"[?]"})
fam = json.load(open(sys.argv[2]))
for k,v in fam.items():
    kk = 'H' if k=='ř' else k
    assert K[kk]==v, (k,v,K[kk])
rows = json.load(open(sys.argv[1]))['rows']
cnt = collections.Counter(); out=[]
for r in rows:
    s=''.join(K.get(ch,ch) for ch in r['cipher'])
    for ch in r['cipher']:
        if ch in K: cnt[ch]+=1
    out.append(s)
print('\n'.join(out))
print('units', sum(cnt.values()), 'unused key labels', sorted(set(K)-set(cnt)), 'unknown chars', sorted({c for r in rows for c in r['cipher'] if c not in K and not c in " ,.-"}))

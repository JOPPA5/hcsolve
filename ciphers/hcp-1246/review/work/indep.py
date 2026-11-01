# independent decode: own glyph-class->letter table from hcp-1216 graphic-key.json names, own row strings for the disputed rows,
# plus a check that the literal letters of the normalized text cover the ledger.
import json,re,unicodedata,os
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
k=json.load(open(base+'hcp-1216/work/graphic-key.json'))
fam={v for v in k.values() if len(v)==1}
L=[l.split() for l in open(base+'hcp-1246/work/ledger.txt',encoding='utf8') if l.strip() and not l.startswith('#')]
toks=[t for l in L for t in l[1:] if t!='.']
import collections
c=collections.Counter(t.strip('[]:') for t in toks)
print(len(L),'rows',len(toks),'signs');print(sorted(c.items()))
print('tokens outside family:',[x for x in c if x.lower() not in fam and x!='H'])
lit=''.join(t.strip('[]:').lower() for l in L for t in l[1:] if t!='.')
strip=lambda s:''.join(ch for ch in unicodedata.normalize('NFD',s.lower()) if ch.isalpha() and ord(ch)<128)
n=strip(open(base+'hcp-1246/work/normalized.txt',encoding='utf8').read())
import difflib
s=difflib.SequenceMatcher(None,lit,n,autojunk=False)
for op,a,b,c2,d in s.get_opcodes():
    if op!='equal': print(op,repr(lit[max(0,a-8):a]),'['+lit[a:b]+'] -> ['+n[c2:d]+']')

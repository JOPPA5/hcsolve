import re,difflib,unicodedata as u
L=[l.split() for l in open('../../work/ledger-opus.txt',encoding='utf-8') if l.strip() and not l.startswith('#')]
tok=[t for r in L for t in r[1:]]
print('rows',len(L),'tokens',len(tok),'letters',sum(map(len,[t.strip('[]') for t in tok if t[0] not in '?.' and not t.isdigit()])))
lit=''.join(t.strip('[]').lower() for r in L for t in r[1:] if t[0] not in '?.')
base=lambda s:''.join(c for c in u.normalize('NFD',s) if not u.combining(c)).lower()
n=open('../../work/normalized-opus.txt',encoding='utf-8').read().replace('Under the stamp:','')
n=re.sub(r'\[Csókolja\?\].*?\.','',n,flags=re.S)
n=re.sub(r'[^\w]','',n)
a,b=base(lit),base(n)
for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(a[max(0,i-8):i]),repr(a[i:j]),'->',repr(b[k:l]),repr(a[j:j+6]))

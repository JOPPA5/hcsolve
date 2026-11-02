# Reviewer's independent decoder: own key table, own parser; aligns literal against the normalized text.
import difflib,unicodedata,re,sys
KEY=dict(zip("= 6 / E + P I J S L II O F ) T X V Z".split(),"a b d e f h i j k l n o r s t u v z".split()))
KEY.update({'III':'m','C':'g','CY':'gy','NY':'ny','LY':'ly','CS':'cs','E*':'e','I_':'i','is':'is','{O}':'','{blot}':''})
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if c.isalpha() and ord(c)<128)
out=[];toks=0;unk=0
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    for t in l.split()[1:]:
        t=t.rstrip("'\""); toks+=1
        if t not in KEY: unk+=1;print('UNKNOWN',t)
        out.append(KEY.get(t,'?'))
lit=''.join(out)
norm=open('../../work/normalized.txt',encoding='utf-8').read().split('\n')[0]
n=strip(re.sub(r'[\[\]]','',norm))
print('tokens',toks,'unknown',unk,'lit',len(lit),'norm',len(n))
print(lit)
for op,a,b,c,d in difflib.SequenceMatcher(None,lit,n,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(lit[max(0,a-8):a]),'['+lit[a:b]+'] -> ['+n[c:d]+']',repr(lit[b:b+8]))
from collections import Counter
print(Counter(out).most_common())

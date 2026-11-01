# Independent decode of the solver ledger; map typed here from the HCP1216 table, not imported from decode.py
import re,unicodedata as u,sys
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1267/'
M=dict(zip("A B C D E G H I J K L M N O T V Y Z".split(),"a b c d e g h i j k l m n o t v y z".split()))
M.update({'6':'b','+':'f','F':'r',')':'s','X':'u','CS':'cs'})
rows={};bad=set();cnt={}
for l in open(B+'work/ledger.txt',encoding='utf8'):
    if l[0]=='#' or not l.strip():continue
    k,r=l.split(None,1);out=''
    for t in re.findall(r'"[^"]*"|\S+',r):
        if t[0]=='"':continue
        if t[0]=='{':continue
        c=re.sub(r"[\[\]?:']","",t)
        if c not in M: bad.add(t);continue
        cnt[c]=cnt.get(c,0)+1;out+=M[c]
    rows[k]=out
txt=''.join(v for k,v in rows.items() if k[0]!='S')
print('unmapped',bad,'signs',sum(cnt.values()));print(sorted(cnt.items(),key=lambda x:-x[1]))
n=open(B+'work/normalized.txt',encoding='utf8').read().split('Under the stamp')[0]
for w in ['hogy','mert','kelet','ido','jo']:print(w,txt.count(w))
s=''.join(c for c in u.normalize('NFD',n.lower()) if c.isalpha())
import difflib
for op,a,b,c,d in difflib.SequenceMatcher(None,txt,s,autojunk=False).get_opcodes():
    if op!='equal':print(op,repr(txt[max(0,a-6):a]),repr(txt[a:b]),'->',repr(s[c:d]))

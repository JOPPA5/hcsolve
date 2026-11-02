#!/usr/bin/env python3
# Independent reviewer decode of hcp-1155: own key (from hcp-1174/1179 tables plus own derivation), own tokeniser.
import re,collections,unicodedata,datetime
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1155/'
K=dict(zip("0 0, 1 1. 1: 1' :1 .1 1, 2 2, 2. 3 3, 3. 4 4, 4. 5 5, 5. 6 6, 6. 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á ü u b c C é d r v f g Y h l L j n N k s S m t p z".split()))
rows=[];
for l in open(R+'work/transcription.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    t,b=l.split(':',1) if not l.startswith('IV ') else ('IV',l[3:].lstrip(' ')[1:] if False else l.split(':',1)[1])
    rows.append((t.strip(),b))
txt=[];c=collections.Counter();flag=0
for t,b in rows:
    if t=='IV': pass
    w=''
    for tok in re.findall(r"\S+|\|",b) :
        if tok=='|': w+=' ';continue
        if tok.endswith('~'): flag+=1;tok=tok[:-1]
        c[tok]+=1; w+=K[tok]
    txt.append(w); print(t.ljust(4),w)
print('signs',sum(c.values()),'distinct',len(c),'flag',flag)
print(sorted(c.items(),key=lambda x:-x[1]))
# Compare with hcp-1174 key
F1174={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','2,':'C','2.':'é','3':'d','3,':'r','3.':'v','4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'S','8':'m','8,':'t','9':'p','9,':'z'}
print('1174 conflicts',[k for k in F1174 if K[k]!=F1174[k]])
F1179={'1,':'b','5.':'l'}; print('1179 vs here',{k:(F1179[k],K[k]) for k in F1179})
print(datetime.date(1916,2,15).strftime('%A'),datetime.date(1916,2,20).strftime('%A'),datetime.date(1916,2,22).strftime('%A'))
def fold(s):
    s=s.replace('cs','C').replace('sz','S').replace('gy','Y').replace('ny','N').replace('ly','L').lower().replace('c','c')
    s=''.join(ch for ch in unicodedata.normalize('NFD',s) if not unicodedata.combining(ch))
    return re.sub(r'[^a-z]','',s)
sol=open(R+'SOLUTION.md',encoding='utf-8').read()
a=sol.index('Édes Margitkám!'); b=sol.index('Sokszor üdvözöl')
body=sol[a:b].replace('III','').replace('IV','')
tail=sol[b:sol.index('Open address')]
tail=tail.replace('Sokszor üdvözöl [open] és [open]','').replace('Mezőkövesd. 1916. II/22. [place and date open]','')
dec=fold(''.join(txt).replace('C','cs').replace('S','sz').replace('Y','gy').replace('N','ny').replace('L','ly'))
sl=fold(body+tail)
print(len(dec),len(sl))
import difflib
for op in difflib.SequenceMatcher(None,dec,sl,autojunk=False).get_opcodes():
    if op[0]!='equal': print(op[0],repr(dec[op[1]-8:op[2]+8]),repr(sl[op[3]-8:op[4]+8]))

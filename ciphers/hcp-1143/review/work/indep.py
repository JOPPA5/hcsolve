# independent decode: own table typed from SOLUTION.md's grid; parses transcription with no use of decode.py
import re,sys
T={'0':'o','0,':'ö','1':'i','1,':'b','1.':'a','1:':'e',"1'":'á',':1':'ü','.1':'u','2':'c','2,':'cs','2.':'é',
'3':'d','3,':'r','3.':'v','4':'f','4,':'g','4.':'gy','5':'h','5,':'l','5.':'ly','6':'j','6,':'n','6.':'ny',
'7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
from collections import Counter
c=Counter();bad=[];n=0
for l in open('work/transcription.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): 
        if l.startswith('## '):print('\n'+l.strip())
        continue
    s,w=l.rsplit(' | ',1);out=''
    for t in re.findall(r'\{.*?\}|\S+',s):
        n+=1
        if t[0]=='{':
            sg=t[1:-1].split('|')[0];out+='['+T.get(sg,'?')+']';bad.append((w.strip(),t));c[sg]+=1
        else: out+=T[t];c[t]+=1
    print(out,end=' ')
print('\n',n,bad);print(sorted(c.items(),key=lambda x:x[1]))

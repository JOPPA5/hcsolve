# Independent decoder (reviewer): own key table typed from hcp-1174/1148 reading, own tokeniser; no import of solver code.
import re,sys,collections
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1139/'
L={'o':'0','ö':'0,','i':'1','a':'1.','e':'1:','á':"1'",'b':'1,','u':'.1','ü':':1','c':'2','cs':'2,','é':'2.','d':'3','r':'3,','v':'3.','g':'4,','gy':'4.','h':'5','l':'5,','j':'6','n':'6,','ny':'6.','k':'7','s':'7,','sz':'7.','m':'8','t':'8,','p':'9','z':'9,'}
R={v:k for k,v in L.items()}
cnt=collections.Counter(); out=[]
for l in open(base+'work/transcription.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    s=''
    for t in l.split():
        if t=='|': s+=' '; continue
        cnt[t]+=1
        s+= R.get(t,'['+t+']')
    out.append(s)
print('\n'.join(out)); print(sum(cnt.values()),len(cnt)); print(sorted(cnt.items(),key=lambda x:-x[1]))

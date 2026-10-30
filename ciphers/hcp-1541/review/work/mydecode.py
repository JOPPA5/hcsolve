import sys, re, collections
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch'}
txt=open(sys.argv[1]).read()
cnt=collections.Counter(); unk=collections.Counter(); out=[]
for line in txt.splitlines():
    o=''; i=0
    while i<len(line):
        m=re.match(r'\[U0\d\]',line[i:])
        if m: o+={'[U01]':'g','[U02]':'(e)','[U03]':'(t?si)'}[m.group()]; unk[m.group()]+=1; i+=len(m.group()); continue
        ch=line[i]
        if ch in K: o+=K[ch]; cnt[ch]+=1
        elif ch in ' ,.?-': o+=ch
        else: o+='#'; unk[ch]+=1
        i+=1
    out.append(o)
print('\n'.join(out)); print(sum(cnt.values()),'keyed units; unknown:',dict(unk)); print('unused key entries:',[k for k in K if cnt[k]==0])

# independent: own transcription (mine.txt), own key, 0 -> [dt]; compares with solver output sign by sign
import re,subprocess,sys
k={'3':'l','2':'i','B':'b','7':'s','0':'0','E':'e','r':'r','9':'o','A':'a','1':'h','5':'u','M':'m','6':'n','K':'k','W':'w','8':'g','c':'c','Z':'z','p':'p','4':'f','v':'v'}
uml={'5':'ü','9':'ö'}
out=[]
for l in open('ciphers/hcp-1340/review/work/mine.txt'):
    r=''; i=0; l=l.rstrip('\n')
    while i<len(l):
        ch=l[i]
        if i+1<len(l) and l[i+1]=='^': r+=uml[ch]; i+=2; continue
        r+=k.get(ch,ch); i+=1
    out.append(r)
sol=subprocess.run(['python3','-I','ciphers/hcp-1340/work/decode.py'],capture_output=True,text=True).stdout.splitlines()[1:17]
sol=[s.split(None,1)[1] for s in sol]
diff=0;signs=0
for a,b in zip(out,sol):
    print(a)
    aw=a.split(); bw=b.split()
    if len(aw)!=len(bw): print('  WORDCOUNT',aw,bw);diff+=1;continue
    for x,y in zip(aw,bw):
        px='^'+re.escape(x).replace('0','[dt]')+'$'
        signs+=len(re.sub(r'\W','',x))
        if not re.match(px,y):
            print('  DIFF',x,'vs',y);diff+=1
print('words differing',diff,'signs',signs, 'zeros',sum(l.count('0') for l in out))

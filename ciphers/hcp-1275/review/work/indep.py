import re,collections,difflib
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/'
K={'=':'a','#':'e','6':'b','/':'d','+':'f','Z':'g',"'":'h','i':'i','T':'j','$':'k','~':'l','W':'m','N':'n','Q':'o','F':'r',')':'s','G':'t','X':'u','^':'v','Y':'y','%':'z','C':'C','.':'.',',':',','?':'?','M':'m',':':':'}
mine={}
for l in open(B+'review/work/my_reading.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,b=l.split(); mine[a]=''.join(K[c] for c in b).replace('o:','ö').replace('u:','ü').replace('C','cs')
led={}
for l in open(B+'work/ledger-opus.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,*t=l.split()
    s=''
    for x in t:
        x={'O:':'ö','U:':'ü',"O'":'ó',"I'":'í'}.get(x,x)
        s+= '?' if x[0] in '{[' else x.lower()
    led[a]=s
n=d=0
for k in led:
    a,b=mine[k],led[k]
    for tag,i,j,p,q in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if tag=='equal': n+=j-i
        else: d+=1; print(k,tag,repr(a[i:j]),'ledger',repr(b[p:q]), '@',b[max(0,p-5):q+5])
print('equal',n,'diffs',d)
t=''.join(led.values()); c=collections.Counter(x for x in t if x.isalpha()); N=sum(c.values())
print(N,sorted(c.items(),key=lambda x:-x[1])); print('IC',sum(v*(v-1) for v in c.values())/N/(N-1))
print('tokens',sum(len(l.split())-1 for l in open(B+'work/ledger-opus.txt',encoding='utf-8') if l[0]!='#' and l.strip()))

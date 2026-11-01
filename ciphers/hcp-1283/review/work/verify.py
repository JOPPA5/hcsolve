"""Independent review script hcp-1283 (Claude Opus 5.5, reviewer). Own key dict, written from the hcp-1216 table,
not imported from the solver; decodes work/ledger.txt, compares with the literal block in SOLUTION.md, then applies
the reviewer's sign corrections and prints the result. Run: python3 -I ciphers/hcp-1283/review/work/verify.py"""
import os,re,collections,unicodedata
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
K={'A':'a','6':'b','C':'c','D':'d','E':'e','+':'f','G':'g','H':'h','P':'p','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n',
   'O':'o','F':'r',')':'s','T':'t','X':'u','V':'v','Y':'y','Z':'z','CS':'cs','!':'!','?':'?'}
rows={};toks=[]
for l in open(D+'/work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split();out=''
    for x in t:
        b=x.strip('[]').split(':')[0]; toks.append(b)
        out+=K[b]
        if ':' in x: out+={'a':"'",'d':'"'}[x.strip('[]').split(':')[1]]
    rows[lab]=out
sol=open(D+'/SOLUTION.md',encoding='utf-8').read()
blk=sol.split('## Literal decipherment')[1].split('```')[1]
claim={}
for l in blk.strip().splitlines():
    if l.startswith('stamp'):
        for i,p in enumerate(l.split(':',1)[1].split('|'),1): claim['S%d'%i]=p.strip()
    else: a,b=l.split(' ',1); claim[a]=b.strip()
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r"[\[\]{}?'\"]",'',s)
bad=[k for k in rows if norm(rows[k])!=norm(claim[k])]
print('rows',len(rows),'tokens',len(toks),'mismatch vs SOLUTION literal block:',bad)
print('unmapped tokens: none (KeyError otherwise); frequencies:',collections.Counter(toks).most_common())
txt=''.join(norm(rows[k]) for k in rows)
print(txt)
print('\nReviewer corrections to sign readings:')
print(' r15 ...senkivel+!+e -> senkivel+d+e   (de lesz meg ez jobban is)')
print(' r16 meg->még, r18 emeg->emég, r15 nek->nék: dot present, ledger omits it')
print(' r17-18 kimegye harasztira sziva e még a tanyai levegöt -> kimegy-e Harasztira, szív[j]a-e még a tanyai levegőt?')

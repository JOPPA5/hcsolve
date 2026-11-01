"""Reviewer's own decode. rows.txt below = reviewer's sign-class reading from own crops, in shape names, not the solver's ledger.
Key taken from the table in ciphers/hcp-1216/SOLUTION.md. Run: python3 -I indep_decode.py"""
import re,unicodedata,difflib,collections,subprocess,os
KEY={'2b':'a','six':'b','4':'d','3b':'e','plus':'f','loopd':'g','1h':'h','4p':'p','idot':'i','invT':'j','Sk':'k','wave':'l','3s':'m','2s':'n','loop':'o','loopdots':'ö',
 'F':'r','bowl':'s','gam':'t','x':'u','xdots':'ü','chev':'v','ydesc':'y','zx':'z','zchev':'z','opp':'cs','dig3':'3'}
R='''bowl zx 3b F 3b F 3b gam 3b 4 3b bowl 3b loopd ydesc 3b gam
wave 3b 2s F 3b 3s 3b 2s ydesc 3b 3s chev 2b F chev 2b
chev 2b F gam bowl loop F 2b idot gam 3s 3b loopd
Sk 2b 4p gam 2b 3s 3s 3b wave ydesc 3b gam Sk loopdots
bowl zx loopdots 2s loopdots Sk bowl 2b invT 2s 2b wave gam loop
3s 2b gam F 3b plus 3b zchev 3b 3s Sk idot 1h loop loopd ydesc
2s 3b 3s 3s 3b loopd ydesc xdots 2s Sk six 3b F 3b 2s ydesc
six 3b 1h 3b loopdots 2s F 3b six idot zchev loop 3s 2b 4 loop wave
loopd loop gam 3s 2b invT 4 Sk xdots wave 4 loopdots Sk idot wave loop 2s
Sk 2b 2s 2b Sk 3b loopd ydesc 3b gam 3b six loopdots wave 2b plus 3b 2s ydesc
Sk 3b 4p 3b 3s 3b wave 3b wave 2b gam loop gam wave 3b chev 3b
wave 3b zx loopdots wave 2b 4p six loop wave 3b bowl 3s 3b loopd
idot F loop 3s 1h loop loopd ydesc 3s 2b loopd 2b 2s 2b Sk
2s idot 2s opp Sk 3b 4 chev 3b 3s loop gam wave 3b
3s 3b 2s 2s idot 3b 4 3b bowl 3b 3s 3b loopd ydesc 3b 2s
wave loop F 3b 3s 3b loopd 2s 3b 3s 3s 3b loopd ydesc
wave 3b 4 3b chev 2b loopd ydesc dig3 1h 3b gam
3s x wave chev 2b wave 3b 3s 3b loopd ydesc 3b Sk
3s 2b invT 4 1h loop wave 2s ? 4p six loop chev 3b six
six 3b idot F loop Sk 3s 3b F gam 3s 2b
bowl xdots F loopd loop bowl 4 loop loopd loop 3s chev ? 2s
idot bowl gam 3b 2s chev 3b
wave 3b 3b 4 3b
bowl 3b 3s opp loop
Sk loop wave loop 3s
bowl zchev 2b 3s gam 2b
wave 2b 2s bowl zchev loop gam
x 3b F idot'''.split('\n')
mine=[''.join(KEY.get(t,'?') for t in r.split()) for r in R]
for i,m in enumerate(mine): print(i+1,m)
D=os.path.dirname(os.path.abspath(__file__))+'/../..'
sol=[];
for l in open(D+'/work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    t=l.split()[1:]
    sol.append(t)
SP={'K8':'k','D1':'d','Z9':'z','CS':'cs','A?':'?','3':'3','O:d':'ö','U:d':'ü','U:x':'ü','N:x':'n','M:k':'m'}
sol=[''.join(SP.get(x,x.lower()) for x in t) for t in sol]
print('rows',len(mine),len(sol))
for i,(a,b) in enumerate(zip(mine,sol)):
    if a!=b: print('DIFF',i+1,a,b)
lit=''.join(sol)
print('signs',sum(len(l) for l in sol),collections.Counter(lit).most_common())
norm=open(D+'/work/normalized.txt',encoding='utf-8').read().replace('Stamp box:','')
def fold(s):
    s=s.lower().replace('ő','ö').replace('ű','ü')
    s=''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn' or c in '̈') 
    s=unicodedata.normalize('NFC',s)
    return re.sub(r'[^a-zöü0-9]','',s)
A=fold(lit.replace('?','a')); B=fold(norm)
print(len(A),len(B))
for op,i,j,k,l in difflib.SequenceMatcher(None,A,B,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(A[max(0,i-6):i]),repr(A[i:j]),'->',repr(B[k:l]),'next',repr(A[j:j+5]))

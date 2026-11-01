"""Reviewer's decoder for HCP1281. Shape codes typed from the reviewer's own crops (crops/), key from the sign table
in ciphers/hcp-1216/SOLUTION.md. Not a blind reading: the ledger had been seen first. Compares with work/ledger.txt.
Run from the repo root: python3 -I ciphers/hcp-1281/review/work/my_decode.py"""
import os,re
K={'2b':'a','6':'b','cs':'cs','d':'d','3b':'e','+':'f','g':'g','J':'j','S':'k','w':'l','3s':'m','2s':'n','o':'o','o:':'ö',
   'T':'h','i':'i','F':'r',')':'s','G':'t','x':'u','v':'v','y':'y','z':'z'}
R={
'01':') z 3b F 3b G 3b G 3b d 3b ) J o w 2b 2s S 2b 3s',
'02':'S i v 2b 2s o 3s T o g y 2b w 3b g J o 6 S 3b d',
'03':'v 3b 6 3b 2s G 2b w 2b w J 2b ) o F 2b i 3s',
'04':'2s 3b T 2b F 2b g x d J o 2s F 2b 3s 3b d 3b',
'05':') 3b 3s T G 3b g 2s 2b T 2s 3b 3s G 3b G 3b 3s',
'06':'G i ) z G 3b w 3b G 3b 3s 3b G S 3b d v 3b )',
'07':') 2b 3s o: 2s 2s 3b w d 2b w 3b g 2s 2b g y o 6',
'08':') 2b J 2s 2b w 2b G o 3s F 2b ?3bx ) w 3b g',
'09':'2s 2b g y o 6 6 o ) ) z x ) 2b g o 3s',
'10':'#2 o F 2b S 3b ) ) 3b ) 3b w 3b F S 3b z',
'11':'G 3b 3s ?2s, v 2b g y i ) #1/4 #1 #0 o F 2b S o F',
'12':'3b F S 3b z G 3b 3s T 2b z 2b i g 2b',
'13':'z 2b 2s ) 2b J 2s 2b w o 3s T o g y',
'14':'2s 3b 3s 3s 3b T 3b G G 3b 3s 3b w 3s 3b F G',
'15':'6 i z o 2s y o: G 2s 2b T i g 2s 3b 3s',
'16':'w 2b G 2s o 2s G 2b g 2b G 3b z 2s 2b g y',
'17':'d o w o g 2b z 3b 2s 3b T o: ) z i',
'18':'v 3b 3s 2s 3b S d 3b 6 i z G 2b G 2b z 2b F 3b',
'19':'3s 3b 2s y T o g y #3 #0 o F 2b 3s x w',
'20':'v 2b v i ) z o 2s G w 2b G J o S 3b g y',
'21':'2b z 2b z T o w 2s 2b T d 3b w x G 2b 2s',
'22':'+ o g o 3s o: G o S S o F + o g o 3s',
'23':'G i ) z G 3b w 3b G 3b 3s 3b G 3b z 3b w 6 3b z 2b F o 3s ) o F 3s 2b F 2b d o g i 3s 2b d o',
'24':'+ ?G 3b F i',
'S1':'cs o S o w','S2':'J 2b ) z 2b 3s','S3':'G 2b w 2b 2s','S4':') z o F','S5':') i F i g','S6':'T x + 3b F i','S7':'+ 3b',
}
def dec(s):
    o=[]
    for t in s.split():
        if t[0]=='#': o.append(t[1:])
        elif t[0]=='?': o.append('['+K.get(t[1:].rstrip(','),t[1:])+']')
        else: o.append(K[t])
    return o
L={}
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../work/ledger.txt')
for l in open(p,encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a,*t=l.split(); L[a]=t
def flat(t):
    o=[]
    for x in t:
        if x=='gy': o+=['g','y']
        elif x=='ű': o.append('u')
        elif re.fullmatch(r'\d+',x) and len(x)>1: o+=list(x)
        else: o.append(x)
    return o
import difflib
tot=same=0
for r,s in R.items():
    a=dec(s); b=flat(L[r]); tot+=len(b)
    m=difflib.SequenceMatcher(None,a,b,autojunk=False)
    same+=sum(x.size for x in m.get_matching_blocks())
    d=[(''.join(a[i:j]),''.join(b[k:l])) for op,i,j,k,l in m.get_opcodes() if op!='equal']
    print(r,''.join(a),'' if not d else '  DIFF mine/ledger: %s'%d)
print('ledger tokens (gy split):',tot,'matching:',same,'gy tokens in ledger:',sum(t.count('gy') for t in L.values()))

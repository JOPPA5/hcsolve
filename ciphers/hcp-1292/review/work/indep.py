"""Reviewer's independent decode of the disputed rows: sign tokens read by the reviewer from
crops in this directory -> own key dict (family key from hcp-1216 table), then compare to solver ledger."""
import re,difflib,os
K=dict(aa='a',b6='b',bowlL='c',dd='d',e3='e',plus='f',loop_d='g',hh='h',ii='i',invT='j',sec='k',wave='l',
 m3='m',n2='n',o='o',o2='ö',FF='r',bowlR='s',gam='t',x='u',x2='ü',chev='v',zz='z',gy='gy',cs='cs',a_='á',e_='é')
T={ # reviewer's tokens
'08':'m3 e3 loop_d a_ gam e_?'.replace(' e_?','').split(),
'20e':'hh o gy'.split(),
'21':'invT e3 wave hh o gy bowlR e3 m3 ii plus e_ wave chev aa bowlR x gam aa bowlR n2 aa sec'.split(),
'28e':'b6 e3 cs x2 wave e3 gam bowlR zz aa chev aa e_ n2 e3 wave'.split(),
'29s':'wave o2 gam e3 m3'.split(),
'29e':'plus o m3 bowlR zz o FF o wave'.split(),
'30s':'bowlR zz o FF o FF n2 ii dd e3 cs aa sec'.split(),
'31s':'bowlR zz aa chev a_ gam'.split()}
for k,v in T.items(): print(k,''.join(K.get(t,t) for t in v))
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../work/')
led=''
for l in open(D+'ledger.txt',encoding='utf-8'):
    if l[0]!='#' and l.strip(): led+=l.split(None,1)[1].strip()
led=re.sub(r'[{}|~\[\]]','',led)
print('alphabet',sorted(set(led)))
n=open(D+'normalized.txt',encoding='utf-8').read().lower()
n=re.sub(r'plain address side.*','',n,flags=re.S);n=re.sub(r'under the stamp:|blacked out','',n)
n=re.sub(r'[^a-záéíóöőúüű]','',n)
fold=str.maketrans('áéíóőúű','aeioöuü')
a,b=led.translate(fold),n.translate(fold)
for t,i,j,x,y in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if t!='equal': print(t,repr(a[max(0,i-5):i]),repr(a[i:j]),'->',repr(b[x:y]))

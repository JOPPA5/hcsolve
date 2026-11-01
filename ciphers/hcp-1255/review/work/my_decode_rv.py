"""Independent transcription (reviewer's eye, sign classes) decoded with the hcp-1216 family key; diff against solver ledger.
Run: python3 -I ciphers/hcp-1255/review/work/my_decode_rv.py"""
import os
K=dict(b2='a',six='b',cs='cs',tp='d',b3='e',fx='f',g='g',gy='gy',i='i',j='j',sec='k',w='l',s3='m',s2='n',o='o',r='r',bowl='s',t='t',x='u',v='v',y='y',z='z')
# tp = tall+short pair (d/h/p: letter given after ':'), s2 = two equal strokes; '?' = unreadable
R="""
sec b3 v b3 bowl j o w b2 s2 sec b2 s3 six b3 cs b3 bowl
bowl o r b2 i t sec o bowl z o s2 b2 t t b3 w
s3 b3 g sec b2 tp:p t b2 s3 s3 b3 w y b3 t b3 tp:p b3
tp:d o bowl z i v b3 w v b2 r t b2 s3 i g b2
z b2 s2 ? bowl b2 j s2 b2 w o s3 tp:h o gy s2 b3 s3
v i gy b2 z o t s3 b2 g b2 r b2 tp:d b3
b2 z s3 b3 g s2 y x g t b2 t tp:h o gy s3 b2 r
s3 x w o six b2 v b2 s2 i t s2 i s2 bowl b3 s3 i
x t bowl b2 g b3 tp:d b3 bowl j o w b2 s2 sec b2 s3
v b2 bowl b2 r s2 b2 tp:p o sec v b3 t w b3 s2 w b3 s2
w b3 s2 w b2 s2 w b3 s3 b3 gy b3 sec b2 z t tp:h i
bowl z b3 b3 tp:d b3 bowl b2 tp:p b2 s3 i bowl w b3 s3 b3 gy
b3 z b3 w six b3 z b2 r o s3 bowl o r b2 i s3
i bowl t b3 s2 v b3 w b3 b2 v i bowl z o s2 t
w b2 t b2 bowl r x tp:d v o z w o s3 b2 t b2
v o w six o w bowl i r i g tp:h x t i bowl z
t b3 w o j b3 fx b3 r i b3 tp:d b3 bowl j o w b2 s2
s3 b2 r sec b3 bowl o r b3 j b2 r b2 z i s2:d i
t o six b3 t s2 b3 s3 i r o sec s3 b2 j tp:d
v b2 bowl b2 r s2 b2 tp:p six o v b2 six b2 s2
""".strip().split('\n')
here=os.path.dirname(os.path.abspath(__file__))
led=[l.split()[1:] for l in open(os.path.join(here,'../../work/ledger-opus.txt'),encoding='utf-8') if l.strip() and l[0]!='#']
for n,(r,l) in enumerate(zip(R,led),1):
    mine=[]
    for t in r.split():
        c,_,v=t.partition(':')
        mine.append(v or ('?' if c=='?' else K[c]))
    sol=[x.split(':')[0].replace('[E]','E').lower() for x in l]
    d=[(i+1,s,m) for i,(s,m) in enumerate(zip(sol,mine)) if s!=m]
    print(f'{n:02d}',''.join(mine),'len',len(mine),len(sol),'DIFF(pos,solver,mine)',d if d else '-')

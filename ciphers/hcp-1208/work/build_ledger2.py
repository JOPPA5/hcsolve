"""One-off, 2026-11-02, after review 1: rewrite ledger-round1.txt as sign-class tokens.
Classes come from review/work/redecode.py (the reviewer's independent class list) with this card's
corrections; every letter is asserted against the corrected solver reading, so a mismatch stops it."""
import os,re
W=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(W,'../review/work/redecode.py'),encoding='utf-8').read()
R=dict((l.split()[0],l.split()[1:]) for l in re.search(r'R="""(.*?)"""',src,re.S).group(1).splitlines())
KEY=dict(re.findall(r"'(\w+)':'(\w)'",src.split('R="""')[0]))
FIX={ # corrected letter rows (review findings 1,2,3,8 and the solver's row 14 re-reading)
'14':'E S H O G Y E L M E H T E K E M A G A:a','15':'H O Z E:a D E S E M M I V E L M E:a G',
'19':'H E T E L M E G Y E K E Z E L','20':'B E Z A R O M S O R A I M','21':'M A R A D O K S I R I G H U:2'}
R['14']='B3 RB TS LOOP OPEN DESC B3 WAVE S3 B3 TS GAM B3 FIVE B3 S3 B2 FIVE B2'.split()
R['15'][-1]='FIVE'
R['21'][-3]='FIVE'
out=['# HCP1208 sign ledger, round 2. One token per written sign: a SIGN CLASS, not a letter (classes and key in decode.py).',
'# CLASS:mark = accent seen (d diaeresis, 2 double acute, a acute). CLASS=x = word-sense choice inside a near-homograph class',
'# (TS is h unless =p; FIVE is k unless =g; OPEN is g). Classes: reviewer list review/work/redecode.py, checked and corrected',
'# by the solver from work/hires; rows 14, 15 and 21 g signs are drawn as the 5-shape. Round 1 letters: ledger-round1.txt.']
for l in open(os.path.join(W,'ledger-round1.txt'),encoding='utf-8'):
    if not l.strip() or l[0]=='#': continue
    k,*t=l.split()
    if k in FIX: t=FIX[k].split()
    c=R[k]; assert len(c)==len(t),(k,len(c),len(t))
    r=[]
    for a,b in zip(c,t):
        b,_,m=b.partition(':'); b=b.lower()
        if KEY[a]==b: x=a
        elif (a,b) in (('TS','p'),('FIVE','g')): x=a+'='+b
        else: raise SystemExit(f'{k}: {a} is {KEY[a]}, reading has {b}')
        r.append(x+(':'+m if m else ''))
    out.append(k+' '+' '.join(r))
open(os.path.join(W,'ledger.txt'),'w',encoding='utf-8').write('\n'.join(out)+'\n')

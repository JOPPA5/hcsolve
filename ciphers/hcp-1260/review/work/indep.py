"""Reviewer's independent decode of hcp-1260. my_rows = my own sign-class reading from
crops (band*.png, dh/r22/misc sheets), tokens named by SHAPE, not by letter. Compares with solver ledger.
Run: python3 -I indep.py (from this directory)"""
import re,os,collections
K=dict(BB='a',SIX='b',OPP='cs',TL='d',EE='e',CR='f',G='g',TR='h',DOT='i',INV='j',SEC='k',W='l',MMM='m',NN='n',LOOP='o',LOOPDD='ö',LOOPTT='ő',F='r',BOWL='s',GAM='t',XP='u',XDD='ü',CHEV='v',Y='y',ZX='z')
R="""01 BOWL ZX EE F EE GAM EE GAM EE TL EE BOWL INV LOOP W BB NN
02 SEC BB MMM EE G Y EE GAM W EE NN F EE MMM EE NN Y EE MMM NN EE
03 TR BB F BB G XP TL INV LOOP NN F BB MMM TR LOOP G Y DOT INV EE NN
04 F DOT GAM SEC BB NN DOT F LOOP SEC MMM DOT GAM MMM BB G BB MMM DOT BOWL
05 F EE BOWL GAM EE W EE SEC TR EE BB NN Y DOT F BB DOT TL EE G EE BOWL
06 CHEV BB G Y LOOP SEC TL EE NN EE OPP LOOP TL EE W SEC LOOP ZX LOOP NN
07 F BB INV GAM BB EE TL EE BOWL EE MMM TR LOOP G Y TR LOOP G Y
08 CHEV LOOP W NN BB INV LOOP SIX SIX TR EE EE F LOOPDD W NN EE MMM
09 DOT F LOOP SEC MMM BB INV TL BOWL ZX LOOP CHEV BB W CR LOOP
10 G LOOP MMM EE W DOT NN GAM EE ZX NN DOT EE ZX GAM BB ZX
11 XDD G Y EE GAM MMM EE F GAM NN EE MMM BB SEC BB F LOOP SEC
12 EE F LOOPDD W DOT F BB BOWL SIX BB NN GAM BB F G Y BB W
13 NN DOT TL EE DOT GAM W EE BOWL ZX NN EE MMM BOWL LOOP SEC BB
14 F BB BB ZX DOT TL LOOPTT TR LOOP G Y BOWL ZX LOOP CHEV BB W
15 SIX EE BOWL ZX EE W TR EE GAM EE MMM BB G BB CHEV BB W
16 EE TL EE BOWL EE MMM MMM DOT GAM BB W DOT G CHEV BB
17 F LOOP SEC TR LOOP G Y MMM XP W BB GAM LOOP GAM
18 CHEV BB BOWL BB F NN BB TL F EE MMM EE W EE MMM
19 INV LOOP W TR LOOP G Y BOWL ZX LOOP W G BB W
20 INV BB BB ZX EE G EE BOWL EE G F EE MMM EE W EE MMM
21 INV LOOP W EE ZX EE W ZX BB F LOOP MMM BOWL LOOP
22 F BB DOT MMM MMM BB F BB TL LOOP SEC BOWL DOT F DOT G TR XDD SEC EE TL EE BOWL EE CR EE F DOT
C1 DOT BOWL GAM EE NN CHEV EE
C2 W EE CHEV EE EE TL EE
C3 BOWL EE MMM BOWL DOT F DOT G
C4 TR XDD SEC EE TL CHEV EE
C5 INV EE CHEV DOT BOWL ZX LOOP NN GAM
C6 W BB GAM BB BOWL F BB
C8 CHEV BB""".splitlines()
mine={}
for l in R:
    a,*t=l.split(); mine[a]=''.join(K[x] for x in t)
sol={}
S={'F':'r',')':'s','X':'u','6':'b','+':'f','CS':'cs','O':'ö','OO':'ő','U':'ü','UU':'ű'}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split()
    if a=='C7': continue
    sol[a]=''.join(S.get(x.rstrip('?'),x.rstrip('?')) for x in t)
n=0
for a in sorted(mine):
    f='same' if mine[a]==sol[a] else 'DIFF'
    print(a,f,mine[a],'' if f=='same' else '| solver: '+sol[a]); n+=len(mine[a])
print('letters',n); print(sorted(collections.Counter(''.join(mine.values())).items()))

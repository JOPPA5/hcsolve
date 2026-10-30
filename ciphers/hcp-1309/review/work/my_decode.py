"""Independent reviewer decode of HCP1309. Transcription below typed by the reviewer from review/work/crops
(not copied from work/ledger.txt), in the reviewer's own sign names; key table retyped from hcp-1216/SOLUTION.md.
LS = long+short stroke class (d/h/p). Then compares with the solver's command output.
Run from repo root: python3 -I ciphers/hcp-1309/review/work/my_decode.py"""
import re, subprocess, sys, collections, unicodedata
KEY=dict(b2='a',six='b',lb='c',b3='e',plus='f',gsign='g',invT='j',sect='k',wave='l',m3='m',n2='n',loop='o',
 gam='t',cross='u',fsign='r',rb='s',chev='v',desc='y',dot='i',ztail='z',opp='cs',LS='?')
T='''
01 rb ztail b3 fsign b3 gam b3 gam b3 LS b3 rb invT loop wave b2 sect b2 m3 sect dot
02 chev b2 n2 loop m3 LS loop gsign desc invT loop b3 gsign b3 rb b3 gsign
03 six b3 n2 gam b2 wave invT b2 rb loop fsign b2 dot m3 gam cross
04 LS b2 gam loop m3 LS loop gsign desc m3 b2 fsign b3 wave
05 invT loop gam b3 m3 rb ztail b3 n2 gam m3 dot LS b2 invT fsign loop wave
06 b3 rb m3 loop rb gam fsign b2 sect loop rb LS b2 wave loop gam b2 LS
07 LS loop wave gsign loop ztail loop m3 b3 rb dot gam gam dot rb wave b2
08 sect loop m3 b3 fsign loop wave m3 b3 gsign six loop chev b3 n2 n2 b3 m3 dot fsign
09 LS b2 gam loop sect m3 b3 fsign gam opp b2 sect rb ztail loop m3 six b2
10 gam loop n2 gam cross LS loop sect gam loop six b3 gam sect b3 LS chev b3 rb invT loop
11 wave b2 n2 sect b2 m3 LS loop gsign desc m3 cross wave b2 gam loop gam
12 chev b2 rb b2 fsign n2 b2 LS b3 n2 six b3 n2 chev loop wave gam b2 m3
13 LS b3 rb gam b3 n2 six b3 wave chev b2 wave
14 gam loop wave gam loop wave gam loop gam b3 m3 b2 LS b3 wave cross gam b2 n2 gam
15 sect b3 LS chev b3 rb invT loop wave b2 n2 sect b2 m3 dot fsign invT loop n2
16 LS loop gsign desc m3 dot cross invT rb b2 gsign b2 fsign loop sect
17 rb ztail b2 wave b2 rb six b2 b3 LS b3 rb b3 six b3 opp b3 rb
18 rb loop fsign b2 dot gam chev b2 fsign chev b2 lb ztail dot m3
19 LS loop wave b3 rb plus b3 fsign dot
S1 dot rb gam b3 n2 chev b3
S2 wave b3 wave b3 b3 LS b3
S3 rb b3 m3
S4 opp loop sect loop
S5 wave loop m3 rb ztail b2 m3
S6 gam b2 wave b2 n2 rb ztail loop fsign
'''
mine={}; cnt=collections.Counter()
for l in T.strip().splitlines():
    k,*s=l.split(); cnt.update(s); mine[k]=''.join(KEY[x] for x in s)
out=subprocess.run([sys.executable,'-I','ciphers/hcp-1309/work/decode.py'],capture_output=True,text=True).stdout
theirs={}
for l in out.splitlines():
    m=re.match(r'\s*(\d\d|S\d) (\S+)$',l)
    if m: theirs[m[1]]=m[2]
def norm(s):
    s=re.sub(r'\{[^}]*\}|[\[\]]','',s)
    s=unicodedata.normalize('NFD',s); return ''.join(c for c in s if not unicodedata.combining(c))
bad=0
for k in mine:
    a,b=mine[k],norm(theirs[k])
    ok=len(a)==len(b) and all(x==y or (x=='?' and y in 'dhp') or (x=='?' and y=='n' and k=='06') for x,y in zip(a,b))
    bad+=not ok; print(('same ' if ok else 'DIFF ')+k,a,'' if ok else b)
print('rows',len(mine),'diffs',bad,'signs',sum(cnt.values()),'types',len(cnt)); print(cnt.most_common())
print('letter-level unknown (LS class) count',cnt['LS'])

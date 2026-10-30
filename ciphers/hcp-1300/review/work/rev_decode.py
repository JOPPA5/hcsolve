"""Reviewer's independent decode of HCP1300. Sign classes are my own reading of review/work/crops,
key is the class table of ciphers/hcp-1216/SOLUTION.md. Does not import or read the solver's decode.py;
the ledger is opened only afterwards, for the comparison.
Run from repo root: python3 -I ciphers/hcp-1300/review/work/rev_decode.py"""
import os,re,difflib,unicodedata,collections
W=os.path.dirname(os.path.abspath(__file__)); S=os.path.join(W,'..','..','work')
KEY=dict(zip('=#6()D+QHITK~MNOFSGXAYZ','aeb()dfghijklmnorstuvyz'))  # '(' ')' pair = cs; X tilted cross = u; + upright = f
KEY['?']='?'
R="""
SZ#F#G#G#GG#D#STO~=NK=M
+OTG=GOMSOF=IMS=TN=~=G
G=~K#~GXD=GNOMHOQY#N
=G=A=SZIQ#QY=~G=~=NN#M
H#G#H=Z=M#FGIGOT=NAI
~=QA=NHOQYS=T=GG#SGA#F#
~=KOD=M#F=S#MM#H#GH=
Z==Z#M6#FH#DIQHIQYT#
#~#D#S#MN=QYONSZ#F#G
N#KM=F6#SZ#~NIM=Q=A=~
#D#S#MK#DA#S#M#NIS=FF#
K#F#M=TOIS G#NHOQY?M=Q=
SZ#F#~M?#?AIFQ=IS()=KSZ=
MOMOMF=NYI~TON=KOF
#N~#SSZ#K=~#Q6O~DOQ=66
+#FXI=AI~=QON6=FMOSG
IS=N=K#FZ#MM=Q=M#FG
6ODOQI=Z=GXD=GHOQY
M=Q=SZ#F#GK#DA#S#M
#NM=Q=GMINDIQTO66=N
SZ#F#GNIN#MM#QXNNI
GXDOM#N=ZG()=K=Z#FG
IFG=MHOQYM=TD#QYM=
SIK+#FISZ#6TOAOAK#()#QG#GGI#S=NQ#M=KKOF+?#H
N#~H=QY#N=Z#Q#SZAI~=Q#~OGISM#QMONDOMNOM
M=Q=A=QYS#NKI=+#NYK#H#GA=FOMSIK#FGKIA=NOK
HOZZ=OFX~OKHOQY#Q#SS#Q#S#NIS=+A=QYOK
""".split('\n')[1:-1]
# row 12 keeps one blank token '  ' mis-split guard
R=[r.replace(' ','') for r in R]
BOX="ISG#NA# ~#M#F# DOKOKSI FIQHXI M=DOT= X#FI".split()
def dec(r):
    o=r.replace('()','Ç'); return ''.join('cs' if c=='Ç' else KEY[c] for c in o)
mine=[dec(r) for r in R]+[dec(r) for r in BOX]
led=[]
for l in open(os.path.join(S,'ledger.txt'),encoding='utf-8'):
    if not l.strip() or l.startswith('#'): continue
    lab,*t=l.split()
    led.append(''.join({'XF':'f','ZP':'z','X':'u','{#}':'?','{sz?}':'+?'}.get(x,x.lower()) for x in t))
print('row  reviewer / ledger differences')
for i,(a,b) in enumerate(zip(mine,led)):
    if a!=b:
        print(i+1,a,'\n  ',b)
        for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            if op!='equal': print('     ',op,repr(a[i1:i2]),'->',repr(b[j1:j2]))
txt=''.join(mine).replace('?','')
c=collections.Counter(txt); n=len(txt)
print('\nletters',n,'IC %.4f'%(sum(v*(v-1) for v in c.values())/(n*(n-1))))
print(' '.join(f'{k}{v}' for k,v in c.most_common()))
print('classes of key unused:',sorted(set(KEY.values())-set(c)-set('()?')))
# which normalisation edits exist? compare stripped normalized text with ledger literal
norm=open(os.path.join(S,'normalized.txt'),encoding='utf-8').read().lower()
norm=''.join(ch for ch in unicodedata.normalize('NFD',norm) if ch.isalpha())
lit=''.join(led).replace('?','').replace('+','')
print('\nedits literal -> normalized (accents stripped):')
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,lit,norm,autojunk=False).get_opcodes():
    if op!='equal': print(f'  {lit[max(0,i1-5):i1]}[{lit[i1:i2]}=>{norm[j1:j2]}]{lit[i2:i2+5]}')

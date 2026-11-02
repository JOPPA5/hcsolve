"""Reviewer's independent decode of HCP1226. My transcription uses my own sign names (not the solver's tokens),
read from my crops in review/work/ (the ledger had been seen, so this is independent in code, not blind)."""
import os,re,difflib,collections
K=dict(aa='a',bb='b',cc='c',dd='d',ee='e',ff='f',gg='g',hh='h',ii='i',jj='j',kk='k',ll='l',mm='m',nn='n',oo='o',rr='r',ss='s',tt='t',uu='u',vv='v',yy='y',zz='z')
# compact form: plain letters = sign name, X = cs digraph sign, # = scribble
M="""01 szeretetedesegyetlenre
02 menyembeXessoraitmeg
03 kahtammitkoszonokszе
04 hensajnalatomatkelki
05 fejeznemhogynemjonmulat
06 sagbaheigyisjoXakazafo
07 hogyviszontlathatom
08 higyjeeledesemmikorso
09 raitolvasomkimondhatat
10 lanerzesfogtaelszive
11 metmiterzekenmagairant
12 aztleirninemlehetlegjob
13 benszetnemmarkeblemreolel
14 niedesemahiczinyszajatosze
15 viszaXokolnihesafnosezt
16 megsokatehetemijameg
17 edesemmikorjonhalehetki
18 megyekelejeb#azalloma
19 sonkedvesemekeresetmin
20 digharanXnakveszemmertXak
21 maganakelekesorulaszivem
22 hamagaszavaitteljesithe
23 temlegjobszeretnemmar
24 haszavaithalhatomes
25 teljesithetnemdemajd
26 eljoazazidomitaligaligvarokamitarokonaitil
27 letimodorommeglesznekelegetalanamugyismegaztirja
28 megedesemhogymiXodafoglakozastmondmajdrokonin
E1 ak
S1 istenve
S2 leedes
S3 semabol
S4 dogvi
S5 szont
S6 latasra
S7 feri""".replace('е','e')
mine={l.split()[0]:l.split()[1] for l in M.splitlines()}
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','work')
led={}
for l in open(D+'/ledger.txt',encoding='utf-8'):
    if not l.strip() or l[0]=='#':continue
    p=l.split();s=''
    for t in p[1:]:
        b=t.split(':')[0]
        s+={'CS':'X','H/d':'h','J?':'f','D?':'d','j?':'j','+?':'f','F':'r',')':'s','X':'u','6':'b','+':'f','D':'d','#':'#','?':'?'}.get(b,b.lower())
    led[p[0]]=s
n=0
for k in led:
    if led[k]!=mine[k]:
        print('DIFF',k,'\n  ledger',led[k],'\n  mine  ',mine[k])
tot=sum(len(v) for v in led.values()); print('ledger tokens',tot,'mine',sum(len(v) for v in mine.values()))
t=''.join(mine[k] for k in mine)
print('edesem',t.count('edesem'),'viszontlat',t.count('viszontlat'),'teljesithe',t.count('teljesithe'),'szavait',t.count('szavait'),'hogy',t.count('hogy'))
print(sorted(collections.Counter(t).items(),key=lambda x:-x[1]))

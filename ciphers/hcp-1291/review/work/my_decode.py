"""Reviewer's independent transcription (shape classes read from review/work crops) and diff to the solver's ledger.
Run: python3 -I ciphers/hcp-1291/review/work/my_decode.py"""
import os, difflib
H=os.path.dirname(os.path.abspath(__file__))
K=dict(bar2='a',six='b',sdt='d',bar3='e',plus='f',loop='g',tst='h',dotc='i',invT='j',sect='k',wave='l',s3='m',s2='n',curs='o',ffF='r',rbowl='s',gam='t',cross='u',chev='v',desc='y',zcr='z',odots='ö')
A={'=':'bar2','6':'six','D':'sdt','E':'bar3','+':'plus','g':'loop','H':'tst','i':'dotc','j':'invT','k':'sect','l':'wave','m':'s3','n':'s2','o':'curs','r':'ffF','s':'rbowl','t':'gam','u':'cross','v':'chev','y':'desc','z':'zcr','Ö':'odots'}
# one character = one sign class; D = short+tall, H = tall+short (h/p); ? = faint/probable; # = overwritten
R={
'01':'szErEtEttEDEsjol=nk=m','02':'EgyEtlEnrEmEnyEmkiv=nom','03':'Hogy?lEgjo66EgEssEg6EnEs','04':'kEDvE6Ent=l=lj=so r=im',
'05':'nEH=r=gu?onHogyijEnrit','06':'=nirokDEugyElv=gyok','07':'+ogl=lv=HogynEmju','08':'tokHozz=mostsok',
'09':'k=ton=von=tv=Esugy','10':'Elv=gyok+gl=v=Hogy','11':'=ligv=roHogylE','12':'+EkHEEHEz=l=HHozis',
'13':'m=rnEgyEDszE+ogokHoz','14':'z==zErtkErEm?=g=t','15':'EDEsEmlEgyEnElnE','16':'zEssElir=nt=mmErt',
'17':'jo66=nszErEtnEkin','18':'k=66mminH#=Hirnimi?t','19':'HogykEnytElEnv=gyok','20':'ijEnritk=nirni',
'21':'kiv=nokjomul=t=st','22':'szErEtÖkEDvEssE+Er','S1':'istEnvE','S2':'lEEDEsEm','S3':'m=r=Dok','S4':'sirig','S5':'HukEDvEs','S6':'s?+Er?'}
R['04']=R['04'].replace(' ','')
R['18']='k=66minH#=Hirnimin t'.replace(' ','')
R['22']=R['22'].replace('+Er','+Er')
def dec(r):
    o=''
    for c in r:
        if c in '?#': o+='('+c+')'
        else: o+=K[A[c]] 
    return o
LED={}
for l in open(os.path.join(H,'../../work/ledger.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split(); s=''
    M={'H~':'h','D~':'d','P~':'p','J?':'?','M?':'?','E+N':'#','N?':'n','|':'|','[E]':'?','I~':'?','O:diaeresis':'ö'}
    for x in t: s+=M.get(x,x.lower())
    LED[a]=s
for k,r in R.items():
    me=dec(r).replace('(?)','?').replace('(#)','#'); so=LED[k].replace('p','h')
    print(k,me, '' if me==so else '   <> solver '+so)
print('sign count me',sum(len(v) for v in R.values()),' solver',sum(len(v) for v in LED.values()))

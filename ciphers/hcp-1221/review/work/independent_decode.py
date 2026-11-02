"""HCP1221 reviewer: independent transcription (typed from review/work crops, one letter class per sign,
digraph signs as multi-char tokens separated by spaces only where needed) compared with the solver ledger decoded by my own table."""
import re,unicodedata,os,sys
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
# my own reading, sign classes as letters; accents dropped; [x]=not fully visible; h and p share class H; D=tick left; 8=digit-like
MINE={'01':'szeretetedesjolan','02':'kamneHaragudjonHogy','03':'ojritkanirokmert','04':'nagyonelvagyok','05':'foglalvameeste',
'06':'8oraigdolgozok','07':'mertaHolHolgo','08':'zoksurgosamun','09':'kaesojkesoidegen','10':'Haznalnemle','11':'Hetojkesonfel',
'12':'lennimegmostnem','13':'tudokirnisemi','14':'ujsakotmertcsak','15':'szombatonegyezek','16':'amesterrelHat','17':'jolakaeknalmiuj',
'18':'sagvasarnaHbemegyek','19':'Hestremegnezemlatogatomaesti'.replace('aesti','aHesti'),'20':'eket','S1':'istenve','S2':'leavi','S3':'szont','S4':'latas','S5':'igmely','S6':'barso','S7':'kalesz'}
T={'F':'r',')':'s','X':'u','6':'b','+':'f','H':'H','P':'H','CS':'cs','8':'8','*':'','I?':'i'}
tot=dif=0
for line in open(os.path.join(ROOT,'work/ledger.txt'),encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lab,*tk=line.split(); s=''
    for t in tk:
        b=t.split(':')[0]
        if b.startswith('{'): s+=b.strip('{}').lower(); continue
        s+=T.get(b,b.lower())
    tot+=len(tk)
    m=MINE[lab]
    if s!=m:
        dif+=1; print('DIFF',lab,'ledger',s,'mine',m)
print('rows',len(MINE),'signs in ledger',tot,'rows differing',dif)

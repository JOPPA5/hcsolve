"""Round 2 reviewer check. (1) own sign map over work/ledger.txt tokens, own output; (2) compare with the row
transcription I read on r2/ crops (cs = C); (3) align normalized.txt with the literal letters and list every
letter the normalized text adds, drops or changes, so undisclosed supply shows up."""
import re,difflib,unicodedata,os,subprocess
R=os.path.dirname(os.path.abspath(__file__))+'/../../'
MAP={'F':'r',')':'s','X':'u','6':'b','+':'f','+?':'f','H':'h','H/d':'d','D/p':'p','J?':'j','D?':'d','O?':'o','D':'d','CS':'C','#':'e'}
rows={}
for l in open(R+'work/ledger.txt',encoding='utf-8'):
    if not l.strip() or l[0]=='#':continue
    p=l.split();rows[p[0]]=''.join(MAP.get(t.split(':')[0],t.split(':')[0].lower()) for t in p[1:])
print('tokens',sum(len(v) for v in rows.values()),'rows',len(rows))
mine={'26':'eljoazazidomitaligaligvarokamitarokonaitil','27':'letimodorommeglesznekelegetalanamugyismegaztirja',
'28':'megedesemhogymiCodafoglakozastmondmajdrokonin','E1':'ak','S1':'istenve','S2':'leedes','S3':'semabol','S4':'dogvi','S5':'szont','S6':'latasra','S7':'feri',
'01':'szeretetedesegyetlenre','02':'menyembeCessoraitmeg','13':'benszetnemmarkeblemreolel','18':'megyekelejebeazalloma','20':'digharanCnakveszemmertCak','21':'maganakelekesorulaszivem'}
for k,v in mine.items():
    if rows[k].replace('C','C')!=v:print('DIFF',k,rows[k],v)
lit=''.join(rows[k] for k in rows).replace('C','cs')
n=open(R+'work/normalized.txt',encoding='utf-8').read()
n=re.sub(r'\[sense of.*?\]','',n)
s=''.join(c for c in unicodedata.normalize('NFD',n.lower()) if c.isalpha())
sm=difflib.SequenceMatcher(None,lit,s,autojunk=False)
for op,a,b,c,d in sm.get_opcodes():
    if op!='equal':print(op,repr(lit[a:b]),'->',repr(s[c:d]),'| ctx',lit[max(0,a-10):a]+'|'+lit[b:b+8])

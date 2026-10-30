"""Reviewer's independent decode. Glyph-class names below are my own reading from review/work crops
   (hires address side), typed row by row, not derived from work/ledger.txt.
   Usage: python3 -I ciphers/hcp-1308/review/work/own_decode.py"""
import os,re,difflib
KEY=dict(bb='a',six='b',bo='cs',lb='c',ds='d',bbb='e',pl='f',rs='g',ts='h',lp='i',T='j',ks='k',w='l',ss='m',nn='n',o='o',oo='ö',ps='p',F='r',rb='s',G='t',x='u',xx='ü',ch='v',y='y',z='z')
R="""
01 rb z bbb F bbb G bbb G bbb ds bbb rb T o w bb nn ks bb ss
02 six bbb bo bbb rb rb o F bb lp G ss bbb rs ks bb ps G bb ss
03 ss bbb T bbb F G pl o rs bb ds T bb ks oo rb z oo
04 nn bbb G bbb ss bbb G bbb ds bbb rb bbb ss ks oo rb z oo
05 nn oo ss ts o rs y pl bbb w ts bb rs y bbb z bbb ks bbb w
06 bb ch bbb G bbb T G bb F rb bb ks ks bb w G x ds o ss
07 bbb ds bbb rb bbb ss ts o rs y ss bb rs bb rb z bbb F bbb G
08 bbb nn rs bbb ss bbb rb bbb rs y rb z bbb F bbb G oo rb z lp ch
09 bo bb ks bbb rs y rs o nn ds o w ss lp nn ds lp rs
10 ts lp rs y T bbb bbb ds bbb rb bbb ss bb z bbb w bbb G bbb ss
11 G oo w ks oo nn y bbb six six bbb nn bbb w G x ds nn bbb ks
12 ch bb w nn lp ss lp nn G ss bb rs bb G o w bbb ds bbb
13 rb bbb ss bb w lp rs ch bb F o ss bb z G bb ps bbb F
14 lb z z bbb G ts o rs y rs y bb ks F bb six six bb nn
15 w bb G ts bb rb rb bb ss rb z bbb ps rb z bbb ss bbb lp G
16 bb T oo ch oo ts o nn bb ps bb six bb nn ss bb T ds
17 bbb nn y ts bbb six w bbb rb z bbb pl o F rs bb w o ss
18 bbb rb bb ks o F ss bb T ds ks bbb F bbb ch bb rs y ks bbb G
19 nn bb ps rb z bb six bb ds rb bb rs o G bbb rb w bbb
20 ss bbb rs y bbb ks ss bbb F G ss bbb rs bb F o ks
21 rb z bb w bb rb six bb lp rb w bb G nn lp bb ks bb
22 F o ss bbb rs y rb z bbb F w bbb rs bb
23 w bb six bbb rb x rs y lp rb bb ks bb F bbb F o ks
24 rb z xx w bbb lp ss ts bbb z lp rb ts bb z bb ss bbb nn lp bbb rb G x ds T bb bb z G ss bb rs bb lp rb bbb ds bbb
25 rb bbb ss ts o rs y ts bb ss bb rs bb bbb w T oo nn bb F o ks rb z bb w bb six o w nn bbb ss nn bb rs y o nn ss bbb
26 rs y bbb ks bb F bb bb ks oo F nn y bbb ks bo bb ks ts bb ss x rb z bb T bbb z bbb w six bbb z bb F o ss
27 rb o F bb lp ss ss bb F bb ds o ks rb z bbb F bbb
28 ks bbb ds ch bbb rb pl bbb F lp
S1 xx ds ch o z w oo ss
S2 G bb ch o six o w
S3 bo o ks T bb lp bbb F G
S4 ch bb rs y o rb lp
S5 F lp rs ts xx
S6 lp ss bb ds o T bb
S7 pl bbb F lp
"""
own={}
for l in R.strip().splitlines():
    k,*t=l.split(); own[k]=''.join(KEY[g] for g in t)
led=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','work','ledger.txt')
K2={'F':'r',')':'s','X':'u','6':'b','+':'f','CS':'cs'}
n=d=0
for l in open(led,encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    k,*t=l.split(); s=''
    for tok in t:
        b,_,m=tok.partition(':'); b=b.rstrip('~') or b
        c=K2.get(b,b.lower()); c={'o':'ö','x':'ü'}.get(c,c) if m=='d' and b in('O','X') else c
        s+=c
    n+=len(t)
    if s!=own[k]:
        d+=1; print(k,'SOLVER',s); print(k,'OWN   ',own[k])
        print('   diff:',[(s[a:b],own[k][c:e]) for op,a,b,c,e in difflib.SequenceMatcher(None,s,own[k],autojunk=False).get_opcodes() if op!='equal'])
print(n,'solver signs;',d,'rows differ')
print(''.join(own[k] for k in own))

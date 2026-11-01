"""Reviewer's independent HCP1253 decode. Own transcription (own sign names), own key. Run: python3 -I review/work/decode_review.py"""
import re,os
K=dict(aa='a',six='b',cc='cs',dd='d',eee='e',cr='f',g='g',gy='gy',hp='h',ii='i',jj='j',kk='k',ww='l',mmm='m',nn='n',oo='o',ff='r',rb='s',lb='s',gam='t',xx='u',ch='v',zz='z',amb='?')
R="""
01 lb rb zz eee ff eee gam eee gam eee' dd eee rb jj oo ww aa' nn kk aa' mmm
02 kk ii ch aa nn oo mmm hp oo gy jj oo eee g eee rb zz eee' g
03 six eee nn gam aa ww aa' ww jj aa rb oo ff aa ii mmm
04 hp oo gy mmm xx ww aa gam nn aa kk oo dd aa
05 hp aa zz aa ff eee mmm eee' ww eee mmm jj oo ww
06 six eee jj oo" nn hp eee' nn gam eee kk eee nn ch aa
07 ff oo mmm hp aa nn eee mmm jj oo" nn ww eee eee' dd eee
08 rb eee mmm eee' rb ii' ff jj aa mmm eee g hp aa ww eee
09 kk eee ww ww eee nn eee ch ii nn nn ch aa ww aa
10 mmm ii gam rb zz ii ch eee rb eee nn ww eee
11 ch ii rb zz eee mmm ii gam nn ii nn cc
12 lb eee mmm ii xx jj rb aa g mmm xx nn kk aa mmm
13 nn ii nn cc aa mmm ii gam amb eee mmm ii rb nn aa
14 gy oo kk eee ff eee rb eee kk mmm eee ff gam cc aa kk
15 ww eee nn gam lb zz eee ff eee gam nn eee' kk dd oo ww g oo zz
16 nn ii eee' rb mmm aa ff kk eee zz dd oo" dd ii aa
17 mmm xx nn kk aa eee rb ii gam hp oo nn nn eee mmm
18 aa kk aa ff oo kk dd oo ww g oo zz nn ii
19 mmm aa rb xx jj rb aa g ii gam nn ii nn cc xx gy aa nn eee' zz ii rb
20 ff eee' g ii ii rb gam eee nn ch eee eee' dd eee rb eee mmm
S1 amb oo kk oo ww oo mmm
S2 rb zz aa mmm gam aa ww aa nn
S3 rb zz oo ff ii mmm aa
S4 hp oo jj aa eee' rb
S5 ii ff ii g hp xx"
S6 kk eee dd ch eee rb eee
S7 cr eee ff ii
"""
out={}
for l in R.strip().splitlines():
    lab,*t=l.split(); out[lab]=''.join(K[x.rstrip("'\"")] for x in t)
    print(lab,out[lab])
# compare with solver's printed ledger reduced to base letters
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
T={'F':'r',')':'s','(':'s','6':'b','+':'f','X':'u','H':'h','D':'d','GY':'gy','CS':'cs','#':'?','CS?':'?','D?':'h','T?':'jj'[0]}
for l in open(D+'/work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split(); s=''.join(T.get(x.split(':')[0],x.split(':')[0].lower()) for x in t)
    if s!=out[lab]: print('DIFF',lab,'solver',s,'review',out[lab])

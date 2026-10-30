# Independent decoder: my own sign-class transcription (reviewer, read from sheet*.png), mapped by the family key.
# Sign-class names are mine; key checked against hcp-1216 legend. Run: python3 -I own_decode.py
import re,sys,os
K=dict(aa='a',six='b',lb='c',dd='d',eee='e',plus='f',gl='g',th='h',di='i',jt='j',sec='k',wv='l',mmm='m',nn='n',lp='o',tp='p',fr='r',rb='s',gam='t',x='u',chv='v',low='y',zc='z',gy='gy')
R={'01':'sec eee dd chv eee rb eee dd eee rb jt lp wv aa ^nn sec aa mmm six . rb lp fr aa',
'02':'di gam mmm eee gl sec aa tp gam aa mmm mmm eee # wv low nn eee sec nn aa',
'03':'gy lp nn lp fr x wv lp sec . eee rb sec eee fr eee mmm aa zc di rb',
'04':'fr eee nn fr th lp gy eee zc fr lp zc rb aa rb lp sec aa di gl',
'05':'nn low # di wv jt lp nn rb zc aa mmm lp mmm fr aa . aa mmm di eee nn',
'06':'gl eee mmm di wv wv eee gam aa wv di gl chv aa fr lp mmm aa chv di',
'07':'rb zc lp nn gam wv aa gam aa rb fr chv di rb zc lp ^nn gam sec di chv aa',
'08':'nn lp sec di wv low eee nn six lp wv dd lp gl rb aa gl lp gam',
'09':'sec di chv aa nn lp sec mmm di nn gam eee sec eee tp eee nn wv aa gam th aa',
'10':'gam lp di rb gam eee nn chv eee wv eee eee dd eee rb eee mmm th lp nn',
'11':'eee rb plus','b1':'lb rb lp','b2':'sec lp wv','b3':'di aa th plus'}
led={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.strip() and l[0]!='#':
        p=l.split();led[p[0]]=''.join('#' if t=='#' else '.' if t=='.' else t.split(':')[0].lstrip('^').lower() for t in p[1:])
n=0;bad=0
from collections import Counter
c=Counter()
for k,v in R.items():
    s=''
    for t in v.split():
        if t in('#','.'): s+=t
        else: s+=K[t.lstrip('^')];c[K[t.lstrip('^')]]+=1
    print(k,s,'' if s==led[k] else 'DIFF '+led[k]);bad+=s!=led[k]
print('rows differing',bad,'letters',sum(c.values()));print(sorted(c.items()))

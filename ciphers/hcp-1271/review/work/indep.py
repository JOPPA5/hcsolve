"""Reviewer's own transcription (descriptive sign names, typed from review/work crops, not from ledger.txt)
and key taken from hcp-1216 legend; compares with solver's ledger. Run: python3 -I review/work/indep.py"""
import os
D=os.path.dirname(os.path.abspath(__file__))
K={'b2':'a','six':'b','lb':'c','oppb':'cs','sT':'d','b3':'e','gl':'g','gy':'gy','Ts':'h','ix':'i','invT':'j','sec':'k','wv':'l',
   's3':'m','s2':'n','lp':'o','Fr':'r','rb':'s','gam':'t','x':'u','chv':'v','y':'y','zz':'z'}
R="""sT Fr b2 gl b2 oppb ix wv b2 gl lp s3 sec ix
chv b2 s2 lp s3 Ts lp gy b2 wv b3 gl invT lp six six
sec b3 sT chv b3 six b3 s2 gam b2 wv b2 wv invT b2 rb lp
Fr b2 ix s3 b3 sT b3 rb b3 s3 gam x sT b2 gam lp s3
Ts lp gy b3 s2 s3 b2 Fr s3 b2 s3 x s2 sec b2
six b2 sT b3 s3 lp rb gam s3 b2 rb s3 x Ts b3 wv y
six b3 gam b3 Ts b2 gam b2 lb zz ix s3 b3 s3
ix rb s3 b3 gl chv b2 wv gam lp zz ix sec
lb zz ix s3 b3 s3 ix rb b3 rb Ts b3 sT ix gl
ix sT b3 lb zz ix s3 b3 zz b3 rb lp Fr b2 ix gam
sec b3 sT chv b3 rb invT lp wv b2 s2 sec b2 s3
invT lp s3 x wv b2 gam b2 rb gam sec ix chv b2
s2 lp sec Ts lp wv s2 b2 Ts Fr b2 gl lp s2
sT lp wv invT lp s2 s2 b3 Ts b2 Fr b2 s3
sec ix rb zz ix s2 gam b3 s2 gl lp s2 sT lp wv
lp s2 Fr ix rb gam b3 s2 chv b3 b2 chv ix rb zz lp s2 gam
wv b2 gam b2 rb Fr b2 oppb lp sec lp wv lp s3 b3 zz b3 Fr rb zz b3""".splitlines()
mine=[''.join(K[t] for t in r.split()) for r in R]
led=[]
import re
for l in open(os.path.join(D,'../../work/ledger.txt'),encoding='utf-8'):
    if l[:2].isdigit():
        M={'F':'r',')':'s','X':'u','6':'b','H':'h','/':'d','GY':'gy','CS':'cs','{s}':''}
        s=''
        for t in l.split()[1:]:
            t=t.rstrip('!').split(':')[0]; s+=M.get(t,t.lower())
        led.append(s)
n=sum(len(r.split()) for r in R); print(n,'signs (reviewer; o-arm of row 17 not counted as a sign)')
for i,(a,b) in enumerate(zip(mine,led),1):
    print(f'{i:02} {a}', '' if a==b else f'   <> solver {b}')

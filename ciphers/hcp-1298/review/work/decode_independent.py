# independent decoder, reviewer: own table typed from HCP1216 legend, ignores work/key.json and decode.py
import re,sys
T=dict(zip("2BAR 3BAR SIX LBOWL TICKSTROKE CROSS SHOOK DOTLOOP INVT SECTION WAVE 3STROKE 2STROKE LOOP HP FSIGN RBOWL GAMMA XCROSS CHEVRON TAILX".split(),"a e b c d f g i j k l m n o h r s t u v z".split()))
T.update(GYLOOP='gy',LRBOWL='cs')
T['XCROSS::']='ű'
n=0;out={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    k,*t=l.split();s=''
    for x in t:
        n+=1
        if x[0]=='[':s+='·';continue
        if x.isdigit():s+=x;continue
        q=x.endswith('?');s+=T[x.rstrip('?')]+('?' if q else '')
    print(k,s);out[k]=s
print(n)

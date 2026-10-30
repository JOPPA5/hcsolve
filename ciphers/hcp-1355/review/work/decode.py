# Independent decoder: own transcription typed from review crops, table-built key, no solver files read.
import string,collections,datetime
L="""Nz Efbsftu kvtu
Cffo gps b tuspmf
J bn hpjoh up
Fbsmz Tfswjdf
Tvoebz Npsjoh
Xjui Mpwf Gspn zpvs
Hjsm""".split("\n")
a=string.ascii_lowercase; t=str.maketrans(a,a[-1]+a[:-1])
tot=0
for l in L:
    tot+=sum(c.isalpha() for c in l); print(l.ljust(24),l.lower().translate(t).upper())
print('letters',tot)
txt=''.join(c for c in ' '.join(L).lower() if c.isalpha())
print(sorted(collections.Counter(txt).items()))
print('absent cipher letters',[c for c in a if c not in txt])
E_="etaoinshrdlcumwfgypbvkjxqz"
fr=dict(zip(E_,[12.7,9.1,8.2,7.5,7,6.7,6.3,6.1,6,4.3,4,2.8,2.8,2.4,2.4,2.2,2,2,1.9,1.5,1,.8,.15,.15,.1,.07]))
sc=[]
for s in range(26):
    sc.append((round(sum(fr[a[(a.index(c)-s)%26]] for c in txt)/len(txt),2),s))
print(sorted(sc,reverse=True)[:4])
print(datetime.date(1907,3,30).strftime('%A'))
def easter(y):
    a_=y%19;b=y//100;c=y%100;d=b//4;e=b%4;f=(b+8)//25;g=(b-f+1)//3;h=(19*a_+b-d-g+15)%30;i=c//4;k=c%4;l=(32+2*e+2*i-h-k)%7;m=(a_+11*h+22*l)//451
    return (y,(h+l-7*m+114)//31,(h+l-7*m+114)%31+1)
print(easter(1907))

"""Independent check: reviewer's own row-by-row reading (made from enlarged crops, spelled here
in a private sign alphabet) decoded with the HCP1216 table re-keyed from that card's SOLUTION.md.
Run from repo root: python3 -I ciphers/hcp-1244/review/work/verify.py"""
import datetime, re, subprocess, sys, collections
T={'aa':'a','bb':'b','ch':'cs','dd':'d','ee':'e','gg':'g','hp':'h','ii':'i','jj':'j','kk':'k','ll':'l','mm':'m','nn':'n','oo':'o',
   'rr':'r','ss':'s','tt':'t','uu':'u','vv':'v','yy':'y','zz':'z','gy':'gy'}
R="""kk ee dd vv ee ss jj oo ll aa nn kk aa mm
tt uu dd aa tt oo mm hp oo gy ss zz ee
rr ee nn ch ee ss ee nn mm ee gg ee rr kk ee zz
tt uu nn kk aa gy oo nn gy oo ss ii aa ll oo
mm aa ss oo nn vv aa rr tt rr aa nn kk aa hp aa ee ss
aa nn yy mm ee dd ee ss jj oo ll aa nn kk aa mm
kk ii oo nn tt oo zz tt ee ee mm aa rr mm aa
gg aa tt ee nn aa mm ee ss tt ee rr uu rr ll aa
nn yy aa ii tt oo ll aa nn nn yy ii vv ii
zz ee tt hp oo gy bb oo rr ii gg ee ll aa zz
tt aa mm ii ss tt ee nn vv ee ll aa vv ii ss zz oo nn tt
ll aa tt aa ss rr aa dd ee ss oo kk aa ll ee ss zz aa zz
ee ll ee gg ll ee ss zz kk ii bb ii rr nn ii
aa dd oo ss ss oo hp ss ee mm mm aa rr aa dd tt
aa ch oo kk ss oo hp aa ss ee mm aa rr tt
hp aa ch oo kk oo tt kk aa hp bb aa bb aa mm
ch aa kk aa dd dd vv ii ss ss zz aa mm ii nn dd jj aa rr tt
ss zz ee rr ee tt ee tt tt ee ll""".splitlines()
mine=[''.join(T[t] for t in r.split()) for r in R]
out=subprocess.run([sys.executable,'-I','ciphers/hcp-1244/work/decode_opus.py'],capture_output=True,text=True).stdout
theirs=[]
for l in out.splitlines():
    m=re.match(r'\s*(\d\d|A1) (\S+)$',l)
    if m: theirs.append(m.group(2))
import unicodedata
def base(s):
    s=s.replace('[','').replace(']','')
    return ''.join(c for c in unicodedata.normalize('NFD',s) if not unicodedata.combining(c))
print('rows',len(mine),len(theirs))
d=0
for i,(a,b) in enumerate(zip(mine,theirs),1):
    ok=a==base(b); d+=not ok
    print(i,'OK ' if ok else 'DIFF',a,'' if ok else base(b))
print('differences',d)
c=collections.Counter(t for r in R for t in r.split()); print('signs',sum(c.values()),sorted(c.items(),key=lambda x:-x[1]))
# Easter 1912 (anonymous Gregorian algorithm)
Y=1912;a=Y%19;b,c2=divmod(Y,100);d2,e=divmod(b,4);f=(b+8)//25;g=(b-f+1)//3;h=(19*a+b-d2-g+15)%30;i,k=divmod(c2,4);l=(32+2*e+2*i-h-k)%7;m=(a+11*h+22*l)//451;mo=(h+l-7*m+114)//31;da=(h+l-7*m+114)%31+1
print('Easter',datetime.date(Y,mo,da))

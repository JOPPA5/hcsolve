"""Independent review decode of HCP1266. Run: python3 -I my_decode.py  (from this directory).
Glyph-name transcription made by the reviewer from review/work/crops, not copied from work/ledger.txt
(p! = short+long form read p; h! = tall+short form read d; X? = overwritten sign; dots = ö)."""
import re, collections
K=dict(bars2='a',six='b',lbowl='c',shortlong='d',bars3='e',cross='f',zig='g',tick='h',tick2='p',loopi='i',invT='j',
 sect='k',wave='l',s3='m',s2='n',loop='o',loopd='ö',lod='ő',F='r',rbowl='s',gam='t',ex='u',chev='v',ydesc='y',zt='z',
 pbang='P',hbang='D',over='?')
R='''
rbowl zt bars3 F bars3 gam bars3 gam bars3 shortlong bars3 rbowl invT loop wave bars2 s2
sect bars2 s3 s2 bars3 tick bars2 F bars2 zig ex shortlong invT loop s2
tick loop zig ydesc rbowl loop sect bars2 loopi F loop sect shortlong bars3
s2 bars2 zig ydesc loop s2 bars3 wave chev bars2 zig ydesc loop sect
cross loop zig wave bars2 wave chev bars2 bars2 chev bars2 rbowl ex gam bars2 wave
s3 bars2 chev loop gam bars2 s3 loop F chev loop rbowl loopi chev loopi
zt loopi gam bars2 s2 shortlong bars3 wave ex gam bars2 s2 sect bars2 pbang loop s3
pbang loopi F loop rbowl zt bars2 rbowl zt wave loop gam
tick loop wave s2 bars2 tick2 gam bars3 rbowl zt bars3 s3 wave bars3
cross bars3 sect bars3 zt lod loopi chev loopi zt rbowl zig bars2 gam
bars3 rbowl s3 bars2 F lbowl rbowl ex gam loopd gam loop sect loopd s2
ex gam bars2 zt loop sect loopi rbowl bars3 chev bars3 wave
s3 bars3 zig sect bars3 zt shortlong bars3 s3 bars2 zt ex invT
invT loopd chev loopd gam bars3 shortlong bars3 rbowl bars3 s3 bars2 tick bars3
gam bars3 s2 s3 bars3 zig loopi wave bars2 sect loop s3
shortlong bars3 invT loopd chev loopd tick bars3 gam F bars2 sect loop rbowl
tick2 bars2 wave loop gam bars2 hbang bars3 bars2 lbowl zt loopi s3 bars3 gam
s3 bars3 zig s2 bars3 s3 gam ex shortlong loop s3
s3 bars3 zig loopi F s2 loopi s3 bars2 invT shortlong wave bars3 zig
sect loop zt bars3 wave bars3 six six six loop chev bars3 six six bars3 s2
loopi rbowl gam bars3 s2 chev bars3 over shortlong bars3 rbowl bars3 s3
zig loop s2 shortlong loop wave
invT loop s2 s2 bars3
tick bars2 F bars2 s3
s3 loopi s2 bars3 s2
loopd s2 F bars3
lbowl rbowl loop sect loop wave loop s3
'''.strip().split('\n')
out=[''.join(K[g] for g in r.split()) for r in R]
c=collections.Counter(g for r in R for g in r.split())
led=[]
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        l=l.split()
        led.append(''.join({'F':'r',')':'s','X':'u','6':'b','+':'f','8':'k','DP':'P','HD':'D','?':'?','O:diaeresis':'ö','O:double-acute':'ő'}.get(t,t.lower()) for t in l[1:]))
n=0
for i,(a,b) in enumerate(zip(out,led)):
    print(f'{i+1:02d} {a}', '' if a==b else '  <> '+b); n+=a!=b
print('rows',len(out),len(led),'differing',n,'signs',sum(c.values()),'types',len(c))
print(' '.join(out).count('?'),'unassigned')

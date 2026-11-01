"""Reviewer's independent decode: own sign-name transcription read from review/work crops; own key.
Run from cipher dir: python3 -I review/work/indep.py"""
K=dict(bar2='a',six='b',lbowl='c',dt='d',bar3='e',cross='f',gl='g',gy='gy',ht='h',dotc='i',invT='j',sect='k',wave='l',
 s3='m',s2='n',loop='o',F='r',rbowl='s',gam='t',x='u',chev='v',lowy='y',zx='z',loopd='ö',xd='ü',one='|',seven='7',tw='?2')
R={
'01':'dotc gl bar2 zx bar2 s2 rbowl bar2 invT',
'02':'s2 bar2 wave loop s3 bar2 sect bar3 F bar3 rbowl zx gam wave bar2',
'03':'s2 lowy x s2 sect bar2 gam loop s2 s2 bar3 sect bar3 dt bar3 rbowl bar3 s3',
'04':'bar3 chev bar3 wave bar2 ht bar2 wave bar2 wave wave bar2 wave',
'05':'bar2 F bar3 s3 bar3 s2 lowy bar3 dotc loop rbowl zx bar3',
'06':'dt loopd wave gam bar3 sect sect bar3 dt chev bar3 rbowl bar3 s3',
'07':'bar2 s3 x wave bar2 gam rbowl bar2 gl six bar2 loop sect',
'08':'chev bar3 gam wave bar3 s2 wave bar3 s3 bar3 gy bar3 sect',
'09':'ht bar2 dt bar3 wave x gam bar2 one s3 bar3 s2 s2',
'10':'bar2 sect loop F bar3 rbowl gam bar3 F bar3 loop sect chev bar3 gam',
'11':'wave bar3 s2 rbowl zx bar3 ht gam bar3 s3 six bar3 F',
'12':'seven bar3 s2 wave bar3 rbowl zx bar3 gy rbowl zx xd',
'13':'F bar3 gam dotc s3 x wave bar2 gam rbowl bar2 gl dotc rbowl',
'14':'dt bar3 rbowl zx bar3 F bar3 gam s2 bar3 s3 s2 bar2 tw loop gy sect bar2 s2',
'15':'cross bar3 wave invT loop s2 s2 bar3 bar2 zx s3 x wave bar2 gam rbowl bar2 gl six bar2',
'16':'dotc rbowl gam bar3 s2 chev bar3 wave bar2 chev dotc rbowl zx loop s2 gam wave bar2 gam bar2 rbowl F bar2 cross bar3 F dotc',
's1':'xd dt chev loopd zx','s2':'wave loop s3 bar2 gam bar2','s3':'chev loop wave six loop wave','s4':'ht xd sect bar3 dt chev bar3 rbowl','s5':'lbowl bar3 cross bar3 F dotc'}
led={}
for l in open('work/ledger-opus.txt',encoding='utf8'):
    if l.strip() and l[0]!='#':
        a,*t=l.split(); led[a]=t
import unicodedata
def lt(t):
    b=t.lstrip('*').split(':')[0]; m={'F':'r',')':'s','X':'u','6':'b','+':'f','(':'c','GY':'gy','7':'7','|':'|','H~':'?2'}
    v=m.get(b,b.lower()); return {'o':'ö','u':'ü'}[v] if ':' in t else v
for a,s in R.items():
    me=[K[x] for x in s.split()]; th=[lt(t) for t in led[a]]
    print(a,''.join(me), 'SAME' if me==th else 'DIFF ledger='+''.join(th))

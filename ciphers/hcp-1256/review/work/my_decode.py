"""Reviewer's independent reading of HCP1256 (shape codes typed from review crops, not copied from ledger-opus.txt).
Key taken only from the sign table in ciphers/hcp-1216/SOLUTION.md. Run: python3 -I review/work/my_decode.py (from the cipher dir)."""
import difflib,re
K={'=':'a','#':'e','2':'n','3':'m','~':'l','^':'v','x':'z','+':'f','T':'j','L':'t','F':'r','6':'b',')':'s','S':'k','@':'o','|':'h','d':'d','!':'i','X':'u','Q':'g','Y':'y','C':'cs','"':'̈','?':'?','[':'[',']':']'}
R="""01 )x#F#L#L#d#)T@~=2S=3
02 S!^=2@3|@QY=~#QT@66
03 S#d^#6#2L=~=~T=)@F=!3
04 |@QY3X~=L@L^=)=F2=|
05 T@66=23!2L#23#FL#23=F
06 #Q#)x#~=F^X~@S#6#=|=)L
07 6#3#FL#QY#L~#2)x@F=
08 S@xL=L@3L@~!)3#Q^=QY@S
09 +@)xL^==3#2Y!6#+=Q#FT@)S=
10 |=x=3#2L#)3@)L2!2C)#2S!3
11 6=FT@6=F=L@LS@"2Y#2)x#
12 F#x|#L#SC=S|@QY|#x6#
13 S#FX"~#)2#S#33@)L3=F
14 @T=26=F=LF=2!2C)xX"S
15 )#Q#3^@~L=3)=2d@F
16 2=~+#~@F=!Q6#)x#Q#LL
17 ^#~#=xL~#|#L3@2d=2!
18 |@QY3!2d#F@"~6#)x#~X2S
19 =xL!)3@2L=|@QY3!#FL2#3
20 3#QY#SQY=SF=66=2|@xx=
21 |#F)x##2=xL3@2dL=3XQY!)LXd@3|@QY2#3#FF=6#)x#~
22 Q#L2!#d#)#3=S#F+#2YS#|#LT@"^@"|#L#23#SSX"~d@"3^=
23 )=F2=|+@Q@3~#^#L#L2!3=Q=3)x@36=L@2^#LL#3FX|=L!)C=S
24 S@~Q@x|=))=S=S@F3=TdC=SF#2d6#T@"^@"S!)L^=2S!F=TF=
25 )x=2d#S@x@S|=x=3#22!|=^=~=3!S@"x6#2#3T@"2
S1 ????#2^#
S2 ~##d#)#3
S3 =6@~d@Q
S4 ^!)x@L
S5 ~=L#)!Q
S6 ?=F)@S=
S7 ?#)x!3=d@
S8 T=+#F!"""
dec=lambda s:''.join(K[c] for c in s).replace('̈','"') 
mine={l.split()[0]:dec(l.split()[1]) for l in R.splitlines()}
import unicodedata
sol={}
import subprocess,sys
for l in open('review/work/solver-literal.txt',encoding='utf-8'):
    p=l.split()
    if len(p)==2 and re.match(r'^(S?\d+)$',p[0]): sol[p[0]]=p[1]
n=0;tot=0
for k,m in mine.items():
    s=unicodedata.normalize('NFD',sol[k]).replace('̈','"').replace('{?}','?').replace('{-}','?').replace('[','').replace(']','')
    if k=='S1': s='????'+s[3:]
    sm=difflib.SequenceMatcher(None,s,m,autojunk=False)
    ops=[o for o in sm.get_opcodes() if o[0]!='equal']
    tot+=len(m)
    if ops:
        n+=1
        print(k,[ (o[0],s[o[1]:o[2]],m[o[3]:o[4]]) for o in ops]); print('   sol ',s); print('   mine',m)
print('rows differing',n,'of',len(mine),'letters',tot)

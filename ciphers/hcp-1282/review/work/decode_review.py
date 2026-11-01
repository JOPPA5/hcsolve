#!/usr/bin/env python3
"""Reviewer's independent decode of HCP1282. Own shape-coded transcription from review crops
(not derived from work/ledger.txt). Shapes: 2 two bars,3 three bars,6 six,^ chevron,F F-sign,
G gamma,S section/cursive-S,~ wave,) right bowl,o loop,O dotted loop,Q double-ticked loop,
x cross,U dotted x,z crossed diag,i crossed curve,T inverted T,+ plain cross read j,f plain cross with F arm read f,y descender,g open
loop,Y gy,M three strokes,N two strokes,D long+short (d/h/p by sense: D=d,H=h,P=p),
C left bowl,I cap sign,/ short stroke(punct),? hidden.
"""
K={'2':'a','3':'e','6':'b','^':'v','F':'r','G':'t','S':'k','~':'l',')':'s','o':'o','O':'ö','Q':'ő',
'x':'u','U':'ü','z':'z','i':'i','T':'j','+':'j','f':'f','y':'y','g':'g','Y':'gy','M':'m','N':'n','D':'d','H':'h','P':'p',
'C':'c','I':'I','/':'|','?':'#','#':'[blob]'}
R="""S3D^3)3Y3G~3NF3M3Ny3M
Si^2NoMHoY2~3gTo66
S3D^363NG2~2~T2)o
F2iMHoYG3~iSiD3T3
Mix+)2gONNOSf3~3Mi
SOzGUNSN2Y^2~Goz2)
GOFG3NG/I~oN2Ho~N2P
M3Y^2FNi3~Q)zOF^2F
i3Y3~oS3~O^2FFoD2
63/IFM2P3Dig M2)2MoD
~3)zHoYMi~3)z63~Q
~OS32TO^QGiGS2#2
MiMiNS3Gi~3GM2)SU~OM
63N3g3))3g3S^2YxNS/3N""".split('\n')+["D3ziNGx~6o~DogN2S3F","z3MM2g2MM3FG6iz3~","M3G6iFoMoNN3S3D3)3M",
"63C)U~3G)z2^2M2DoMiF2)","62Ni)HoYN3MF63NN3Mi)?3N","^3~3 3D3)3MgoND o~+ON".replace(' ',''),
"N3H2F2M2SiON F3#3P3DQ)ziv^3~goNDo~".replace(' ','').replace('v','^')]
for n,r in enumerate(R,1):
    print(f"{n:02d}",''.join(K[c] for c in r.replace(' ','')))

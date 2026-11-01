"""Reviewer's independent decode of HCP1265. Rows are the reviewer's own reading of crops in review/work/crops,
in a glyph alphabet that does not reuse the solver's ledger tokens. Prints a diff against the solver's literal rows.
Glyphs: 2 two bars,3 three bars,F r,G gamma,L inverted T,W wave,N two strokes,M three strokes,H tall+short,
D short+long,O loop,I dotted loop,S section,V chevron,X plain cross,Z crossed diagonal,B six,Y y-loop,g zigzag,
Q opposed bowls,) right bowl,+ upright cross,? unresolved overwritten sign"""
import subprocess,sys,re,difflib,os
K=dict(zip("23FGLWNMHDOISVXZBYg)+Q",["a","e","r","t","j","l","n","m","h","d","o","i","k","v","u","z","b","y","g","s","f","cs"]))
R="""01 )Z3F3G3G3D3)LOW2NS2M
02 SIV2NOMHOgY2W3gLOBB
03 S3DV3B3NG2W2WL2)OF2IM
04 GXD2GOMHOgYM2IFG2M2Z
05 IWONS2N2SM3gIg3FG3M
06 HOgYM2LD2NY3FONV2gY
07 2FOS)Z2W2)B2V2gYB3
08 F3NYB3MO)G2ZONGOF3
09 S3D3SHOgY3gYSIQSIFX
10 H2ZSODH2)2SHOgYN3ZZ3S
11 SIV2W2HOgYD33ZGH2gY
12 LXSM3FG3ZI)G3NF3W3)3
13 2Z3g3)ZN3MLO3WOF3
14 )3MIG)Z2MIG2NI2ZLO
15 HOgYSIM3NGH2F2)ZGI
16 F2W3g2W2B)ZIVL23ZG
17 2LOG2NY2IW3V3gOG
18 B2FIg2ZHOgY2FOS)Z2
19 W2)B2)3NINQFO)ZW3V3
20 gO)I?3SIV3WMIND3N
21 N2H?2W2WSOSM3FG3gY
22 H3LF3L2FXNS3B3D3WNI
23 OMONDG2HOgYN2gYONLOWN3ZSILOW2NS2MQ2SVI
24 gY2ZONM2g2F2DF2g2QIW2gOMN3HOgYM3g+2Z
25 ON2S3D3WN3M)OS2GGOFODOSXgY2NIWON2N2SVIgY3
26 W3N3MGXDOMHOgYING3ZS3DN3S
S1 I)G3NV3
S2 W3
S3 DF2g2MQO
S4 SOWOM
S5 )Z2MG2
S6 W2N)ZO
S7 IM2DOL2
S8 +3FI"""
sol=subprocess.run([sys.executable,'-I','ciphers/hcp-1265/work/decode.py'],capture_output=True,text=True,cwd='/Users/tomaspavuk/Desktop/hcsolve').stdout
srows={m[0]:m[1] for m in re.findall(r'^\s*(\d\d|S\d) (\S+)$',sol,re.M)}
n=0
txt=[]
for l in R.splitlines():
    lab,g=l.split(); p=''.join(K.get(c,'?') for c in g); n+=len(g); txt.append(p)
    s=unicodedata_strip=__import__('unicodedata').normalize('NFD',srows[lab]); s=''.join(c for c in s if ord(c)<0x300).replace('[deleted]','')
    print(lab,'OK' if p==s else f'DIFF mine={p} solver={s}')
print(n,'signs (reviewer; deleted S2 tail not counted)')
t=''.join(txt)
for w in ['hogy','jolankam','aroks','leveg','ilon','nem','jo']: print(w,t.count(w))

# Independent reviewer decoder: own visual transcription (reviewer-typed from enlarged crops),
# family key from ciphers/hcp-1545/work/key.json convention. [..] = signs restored from context.
import re
K={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','8':'L','q':'Z','g':'K','f':'V','h':'R','t':'D','r':'H',
   'c':'S','s':'C','n':'M','m':'N','p':'B','b':'P','d':'T','y':'J','7':'J','ř':'CH','v':'F'}
ROWS="""fh581 t4g cht5sg3 n375 q86d5, q6 th6r1 8[4c]d5g
76g t6h4 c5 m1m4 c r86f4sg32? 76 7c5n, p3r2t4g,
p385cd cf5 r86f1 74q bh5n3r8, gd5h5 nm5 m1m4
bh4c83 f584s5 m5fr3t. 2 m6c 74q p84q4 c5 t3p6
f6m3sm4 6 c m4 h3qnm3q5m4 bh6s5. d6g5 76
fqb3n4m6n m6 83mcg1 h3g fd5d3 t3p5,
gt1 n375 cht5sg3 qt5 t8583 m6 qg32cg6ř.
cg3t6. 6 d1 r5q32mg5 řf48g1 fqt1 d6g
h1ř85 bhř674. 76g dh6f4 6m2cg6 m1m57c4
t832r5 f5s5h1? n27 q4f3d 75 m6h6nm5 75tm3-
df6hm1. fs5h6 řd58 7c5n m6fcd4f4d4 f5s5h
g3msd5hd f h2t38v4m5, qthq58 7c5n
c5 fc6g bh484c t832r3 f 2h6t5. d4c4s fh581ř
b2c b3c486 b5b32c cf5n2 75t4m5n2 cht5sg2."""
def dec(s):
    out=[];i=0
    while i<len(s):
        ch=s[i]
        if ch=='[': out.append('['); i+=1; continue
        if ch==']': out.append(']'); i+=1; continue
        out.append(K.get(ch,ch)); i+=1
    return ''.join(out)
for r in ROWS.splitlines(): print(dec(r))

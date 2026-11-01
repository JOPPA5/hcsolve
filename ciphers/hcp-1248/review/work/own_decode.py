"""Reviewer's independent decode of HCP1248. Rows below are the reviewer's own sign-class
reading from review/work crops (accents and dots ignored; ? = writer's blot; literals dropped),
in a private alphabet. Key taken from the HCP1216 sign table. Compares with solver's ledger.
Run: python3 -I ciphers/hcp-1248/review/work/own_decode.py"""
import os,re,difflib,unicodedata
K={'3':'e','2':'a','W':'m','N':'n','L':'t','J':'j',')':'s','S':'k','Q':'o','I':'i','G':'g','D':'y','F':'r','B':'b','P':'f','H':'h','T':'d','A':'l','X':'u','Z':'z','R':'v','C':'cs','?':'?'}
R='''3T3)3GD3LA3NF3W3ND3WN3LXN
JQNP3AHQGD3GD)Z3LF3S3L
A2HQLI)IFQST3HIFL3A3NJQL
3GDJQQLA3L3WN2GDQNQFXA
N3SH2W2G2N2SI)W3GL3L)Z3N3
3NA3)Z2R2)XL2)QSN2S2
)ZXF3LIWXA2L)2G3)H2W2G2
N2SS3TR3RQAN23AJQNNI2S
SQFB3A3HN3SF3NT3ZQN3S2ZL
3AQF3IG3GF3WHQGDQJJ2N
WXA2L)2GB2W3GN3WRQAL
3)PQG2AW2)INCFQF2HQGD
WIJ3NA3H3L3GDH3)LIWX
A2L)2GA3)ZN3SR2GD3ZF3N
I)N2GDQ?QN)Z3F3LN3WH2
3AJQNN3W3FLXGD)3WWXA2L
H2LXNSW2)S3H3GDXLW3FL
ILN2GDQNN3H3Z)Z2B2TITQL
S2HNIWQ)LI)C2SXGDS2HN3S
F3NT3ZQA3NN3SL3H2LS3
F3WHQGDGDQF)2NGQNTQA
J2W3G2TQAGQLW3FL
IGB3S3AJ3A3NL3NIHQGD
F3NT3ZQ2S2FQSA3NNI3Z3AB3Z2LQW)QF2IW
W2F2TQSB)QF2ILR2FQS3TR3))3P3FI
I)L3NR3
A33T3)3W
2BQATQG
RI)ZQNL
A2L2)F
HXS3TR3)
)3P3FI'''.split('\n')
def plain(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if c.isalpha() or c=='?')
led=[l.split()for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../work/ledger.txt'),encoding='utf-8') if l.strip() and l[0]!='#']
M={'F':'r',')':'s','6':'b','+':'f','H':'h','CS':'cs','BLOT':'?'}
n=0
for r,l in zip(R,led):
    mine=''.join(K[c] for c in r); n+=len(r)
    t=''
    for x in l[1:]:
        if x[0]=='#' or x=='DOT': continue
        b=x.split(':')[0]; t+=M.get(b,b.lower())
    print(l[0],mine,'' if mine==t else '<> solver '+t)
print(n,'reviewer signs')

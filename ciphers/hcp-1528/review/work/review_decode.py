# Independent reviewer decoder for HCP 1528 (pc_hcp_209). Key typed by hand from family
# cards (not loaded from solver's key.json). Transcription is the reviewer's own reading
# of source/picture.jpg from 4-6x crops in review/work/. '?' = sign not secured,
# '[..]' = hidden under tree/engraving.
KEY = {'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L',
       'b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M',
       'p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH'}
ROWS = [
 "fh581 t4g q6 th6r1 84cd5g. b3c85ř8 7c5n cf5 cht5sg3 6 q2cd68 7c5n",
 "75cd5 t3n6. 75 n4 74q 3 r3tm5 85b5, 6fc6g t3c2t b84s5 6 ghg? m5-",
 "7c32 2b8m5 f b3h6tg2. f b3mt584 q5bd6n c5 85g6h5, qt6 n4 t3f384",
 "74q 74d4 t3 2h6t2. 73 n4 m1m4 m5n3s f5h2c5 m5fr3t. 6p1 n5 cht5sg3",
 "cd3m683 g5 nm5, p1ř q6 q6tm32 s5m2 m5řd58. 4? p18 p1ř c4 fc6g bh68",
 "gt1q nm5 d6g r86f6 p38586, 6p1 nm5 [..] p183 n5 cht5sg3 6cb3m",
 "m6 řf484 bh4c83, b383q483 cf32 h2sg2",
 "m6 r86f2, p186 p1 nm5 74cd5 p385cd4",
 "bh5cd686. r5qg1 c5 f5 cf4m5ř p6f[..]",
 "6 f1h4t, bh3c4n, c85sm6 76mg3f6",
 "n5 2sd4f5 b3h2s5m4. m5b3c84",
 "n4 fc6g q5 cf4m 3b5d d6g3f1",
 "84cd5g, 76g3 b3c85tm5, gd5h1 nm5",
 "q6hn32d48. cht5sm1 b3qth6f6",
 "d4c4s t832r1ř, f6cm4f1ř b2c",
 "b3c486 d4 df27 b5b32c,",
 "gd5h1 cd685 fh585",
 "fqb3n4m6.",
]
def dec(s):
    out=[];i=0
    while i<len(s):
        if s.startswith('[..]',i): out.append('[..]');i+=4;continue
        ch=s[i]; out.append(KEY.get(ch,ch)); i+=1
    return ''.join(out)
n=0
for r in ROWS:
    print(dec(r)); n+=sum(1 for c in r if c in KEY)
print('signs decoded with key:',n)

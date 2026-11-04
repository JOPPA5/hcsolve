# Independent reviewer decoder for hcp-1045: own transcription (read from review/work crops), A=2..Z=26 without J.
import string
alpha=[c for c in string.ascii_uppercase if c!='J']
key={n+2:c for n,c in enumerate(alpha)}
# words as lists of numbers; 'U' suffix = umlaut, 'D' = doubled; read independently from block_full.png / corner_rm38.png
text = """23 15 | 3 10 19 20 | 5 21 | 9 6 21 20 ?
12 10 6 3 6 18 | 7 18 10 20 26 !
6 3 6 14 | 5 6 10 6 14 6 | 11 2 18 20 6 | 6 18 9 2 12 20 6 14 | 21U 3 6 18
23 2 19 | 10 19 20 | 5 6 14D | 5 2 19 26 | 7 21U 18 | 6 10 14 | 7 15 18 20 23 2U 18 6 14 5 6 19 | 8 6 26 2 14 11 6 ?
10 19 20 | 5 2 19 | 5 10 6 | 7 18 6 21 5 6 | 2 21 7 | 13 6 10 14 6 | 8 6 19 21 14 5 9 6 10 20 ?
13 10 20 | 8 18 21 19 26 | 19 21 19 10"""
U={'A':'Ä','O':'Ö','U':'Ü'}
for line in text.splitlines():
    out=[]
    for w in line.split('|'):
        s=''
        for t in w.split():
            if t in '?!': s+=t; continue
            n=int(t.rstrip('UD')); c=key[n]
            if 'U' in t: c=U[c]
            if 'D' in t: c*=2
            s+=c
        out.append(s)
    print(' '.join(out))

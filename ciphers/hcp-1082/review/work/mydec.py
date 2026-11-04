import sys,re
# independent: key built as 3 rows of digits 1..0
rows={'':'ABCDEFGHIJ',"'":'KLMNOPQRST','"':'UVWXYZ????'}
src=sys.argv[1]
n=0
for line in open(src):
    if line.startswith('#') or not line.strip(): continue
    out=[]
    for g in line.split('|'):
        w=''
        for t in g.split():
            m=re.fullmatch(r"(\d)('|\")?",t); d=int(m.group(1)); mk=m.group(2) or ''
            w+=rows[mk][(d-1)%10]; n+=1
        out.append(w)
    print(' '.join(out))
print('signs',n)

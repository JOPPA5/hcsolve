import re,subprocess,sys
K=dict(zip("2bar 3bar six lbowl rbowl d Ccurl tallhi tallhlo loop loopdd loopdot invT wave m3 n2 sect F gamma X Xdd chev crossd gy BLOT OVERWRITTEN".split(),
 "a e b c s d g h p o ö i j l m n k r t u ü v z gy ? #".split()))
mine={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l[0]=='#':continue
    p=l.split();mine[int(p[0])]=[K[t] for t in p[1:]]
out=subprocess.run(['python3','-I','../../work/decode_opus.py'],capture_output=True,text=True).stdout
theirs={}
for l in out.splitlines():
    m=re.match(r'(\d\d) (\S+)$',l)
    if m:theirs[int(m[1])]=m[2]
tot=0
for r in sorted(mine):
    a=''.join(mine[r]);tot+=len(mine[r])
    b=re.sub(r'\{blot\}','?',theirs[r]).replace('[ü]','?').replace('[d]','?').replace('[h]','?').replace('[n]','#').replace('.','').replace('F','r').replace('ú','u')
    print(r,'OK ' if a==b else 'DIFF',a,'' if a==b else '| '+b)
print('signs',tot)

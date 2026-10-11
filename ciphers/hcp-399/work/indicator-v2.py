from pathlib import Path
p=Path(__file__).parent
s=''.join(c for c in (p/'transcription-v2.txt').read_text() if c.isalpha())
def digits(n):return ''.join(str((n+i)%10) for i in range(5)) if n<10 else f'{n:02}0{n+1:02}'
print('Necessary repeated-letter constraints only; unknown daily homophone table.')
valid=[]
for pos in range(0,len(s),5):
 g=s[pos:pos+5];ns=[]
 for n in range(1,23):
  d=digits(n)
  if all(g[i]!=g[j] or d[i]==d[j] for i in range(5) for j in range(5)) and all(len({g[i] for i in range(5) if d[i]==v})<=3 for v in set(d)): ns.append(n)
 print(pos//5+1,g,','.join(map(str,ns)) or 'NONE')
 if ns:valid.append(pos//5+1)
(p/'indicator-positions-v2.txt').write_text(' '.join(map(str,valid)))

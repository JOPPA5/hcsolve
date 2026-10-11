"""Rebuild independent controls and run bounded alternative-system attacks.
The control text is synthetic; target guesses are never labelled plaintext.
"""
from pathlib import Path
import subprocess,random,json
p=Path(__file__).resolve().parent
plain=(p/'control-plain.txt').read_text().strip()
for mode,key in [('beaufort',[7,13,2]),('porta',[7,3,10])]:
 out=''
 for i,c in enumerate(plain):
  x=ord(c)-97;k=key[i%3]
  y=(k-x)%26 if mode=='beaufort' else 13+(x+k)%13 if x<13 else (x-13-k)%13
  out+=chr(97+y)
 (p/(mode+'-control.txt')).write_text(out)
plain40=plain[:40]
(p/'columnar-control-plain.txt').write_text(plain40)
(p/'columnar-control.txt').write_text(''.join(plain40[col::5] for col in [2,0,4,1,3]))
alphabet=list('abcdefghijklmnopqrstuvwxyz');random.Random(91832).shuffle(alphabet)
(p/'mono-control-key.txt').write_text(''.join(alphabet))
(p/'mono-control.txt').write_text(''.join(alphabet[ord(c)-97] for c in plain))
for exe in ['reciprocal','columnar','mono']:
 subprocess.run(['c++','-O3','-std=c++17',str(p/(exe+'.cpp')),'-o',str(p/exe)],check=True)
checks={}
for mode in ['beaufort','porta','columnar','mono']:
 exe='reciprocal' if mode in ['beaufort','porta'] else mode
 args=[str(p/exe),str(p),str(p/(mode+'-control.txt'))]+([mode] if exe=='reciprocal' else [])
 out=subprocess.check_output(args,text=True)
 (p/(mode+'-control-results.txt')).write_text(out)
 expected=plain40 if mode=='columnar' else plain
 checks[mode]={'plaintext_recovered':any(l.split()[3]==expected for l in out.splitlines()),'expected':expected}
 for f in sorted(p.glob('target-*.txt')):
  if '-result' in f.name:continue
  for rev in ([False,True] if mode=='columnar' else [False]):
   args=[str(p/exe),str(p),str(f)]+([mode] if exe=='reciprocal' else [])+(['reverse'] if rev else [])
   out=subprocess.check_output(args,text=True)
   (p/(mode+'-'+f.stem+('-reverse' if rev else '')+'-results.txt')).write_text(out)
(p/'alternative-control-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))

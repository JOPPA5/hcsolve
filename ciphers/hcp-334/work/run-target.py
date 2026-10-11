from pathlib import Path
import subprocess
p=Path(__file__).parent;groups=(p/'transcription.txt').read_text().split()
for off in range(5):
 g=groups.copy();g[18]='FWXX'[:off]+'?'+'FWXX'[off:];ct=''.join(g).lower();f=p/f'target-phase-{off}.txt';f.write_text(ct)
 out=subprocess.check_output([str(p/'vigenere-erasures'),str(p),str(f)],text=True);(p/f'target-phase-{off}-results.txt').write_text(out)
 print('completed phase',off,flush=True)

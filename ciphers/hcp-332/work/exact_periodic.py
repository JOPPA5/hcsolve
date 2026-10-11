from pathlib import Path
import subprocess
p=Path(__file__).resolve().parent
subprocess.run(['c++','-O3','-std=c++17',str(p/'exact_periodic.cpp'),'-o',str(p/'exact_periodic')],check=True)
for mode in ['vigenere','beaufort','porta']:
 control='control-cipher.txt' if mode=='vigenere' else mode+'-control.txt'
 out=subprocess.check_output([str(p/'exact_periodic'),str(p),str(p/control),mode],text=True)
 assert out.splitlines()[2].split()[4]==(p/'control-plain.txt').read_text()
 (p/('exact-'+mode+'-control-results.txt')).write_text(out)
 for f in sorted(p.glob('target-*.txt')):
  if '-result' in f.name:continue
  out=subprocess.check_output([str(p/'exact_periodic'),str(p),str(f),mode],text=True)
  (p/('exact-'+mode+'-'+f.stem+'-results.txt')).write_text(out)
 print(mode,'period-3 exact control recovered')

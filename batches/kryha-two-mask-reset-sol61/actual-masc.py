from pathlib import Path
import subprocess
b=Path(__file__).resolve().parent;r=b.parents[1]
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
 for ix in (5,6):
  name=f'{variant}-row{ix}';subprocess.run(['python3',str(b/'project.py'),str(b/f'{name}-input.json'),f'{name}-profile.txt',f'{name}-projected.txt','100'],check=True)
  with (b/f'{name}-masc.txt').open('w') as f:subprocess.run([str(b/'masc'),str(b/'dummy-pair.txt'),str(b/'zero-schedule.txt'),str(r/'batches/kryha-mask-sol61'),str(r/'ciphers/hcp-350/work'),str(b/f'{name}-projected.txt')],stdout=f,check=True)
  subprocess.run(['python3',str(b/'neighbors.py'),str(b/f'{name}-input.json'),f'{name}-masc.txt',f'{name}-projected.txt',f'{name}-neighbors.json'],check=True);print(name,'complete',flush=True)

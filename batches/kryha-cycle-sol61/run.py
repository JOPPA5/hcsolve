from pathlib import Path
import subprocess,sys
b=Path(__file__).resolve().parent;kind=sys.argv[1] if len(sys.argv)>1 else '2';workers=[]
for m in (20,27,30):workers.append((m,subprocess.Popen([str(b/'cycle'),str(b/f'control-m{m}.txt'),str(m),kind,'32','20000'],stdout=open(b/f'order{kind}-m{m}.tsv','w'),stderr=open(b/f'order{kind}-m{m}.log','w'))))
for m,p in workers:print(m,p.wait(),flush=True)

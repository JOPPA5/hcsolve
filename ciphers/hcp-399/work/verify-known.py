from pathlib import Path
import json,subprocess
p=Path(__file__).parent
for f in sorted(p.glob('control-*-key.json')):
 keys=json.loads(f.read_text());name=f.name.removesuffix('-key.json');keyfile=p/(name+'-key.txt')
 keyfile.write_text(str(len(keys))+'\n'+'\n'.join(str(len(k))+' '+' '.join(map(str,k)) for k in keys))
 ct=p/(name+'.txt');out=subprocess.check_output([str(p/'verify-known'),str(ct),str(keyfile)],text=True).strip();plain=(p/(name[:11]+'-plain.txt')).read_text();assert out==plain,name
 print(name,'C++ known-key decipherment exact',len(out))

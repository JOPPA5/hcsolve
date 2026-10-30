import sys,json,re
from pathlib import Path
C=Path(sys.argv[1])
key=json.loads(Path(sys.argv[2]).read_text())  # sister key (hcp-1545)
key={k:v.upper() for k,v in key.items()}
out=[]
for line in (C/'work/transcription.txt').read_text().splitlines():
    s='';
    for m in re.finditer(r'⟦U\d+⟧|.',line):
        t=m.group(); s+=key.get(t,t) if not t.startswith('⟦') else t
    out.append(s)
print('\n'.join(out))
print(sorted(set(re.sub(r'⟦U\d+⟧|[ .,!?\-\n]','',(C/'work/transcription.txt').read_text()))-set(key)), file=sys.stderr)

from pathlib import Path
import json,hashlib,string
p=Path(__file__).resolve().parent.parent
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest, name
s=(p/'work/transcription.txt').read_text()
a=string.ascii_uppercase
out=s.translate(str.maketrans(a,a[1:]+a[:1]))
print(out,end='')
print('Letters:',sum(c in a for c in s))

from pathlib import Path
import json
from exact_cover import solve
q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';g=(Path(__file__).resolve().parents[2]/'ciphers/hcp-364/work/transcription.txt').read_text().split();c=''.join(x for i,x in enumerate(g) if i!=2)
out=solve(q+'?',c,[16,17],20000,3);Path(__file__).with_name('tight-raw16-17.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

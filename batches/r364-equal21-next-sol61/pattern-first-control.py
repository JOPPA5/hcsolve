from pathlib import Path
import json
from closed import solve
b=Path(__file__).resolve().parent;v=json.loads((b/'control-input.json').read_text());r=solve(v['plaintext'],[v['ciphertext']],seconds=60,pattern_first=True);(b/'pattern-first-control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))

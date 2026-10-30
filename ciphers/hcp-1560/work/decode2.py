#!/usr/bin/env python3
"""hcp-1560 round-2 decoder (stdlib only, read-only).
Applies the fixed family key (work/key.json, = ciphers/hcp-1520/work/key.json + v=F)
to the corrected manual transcription work/transcription-r2.txt and prints the literal plaintext.
Signs in {braces} are damaged (under ink blots) but read; they are decoded and shown in [brackets].
"""
import json,re,sys
from pathlib import Path
W=Path(__file__).resolve().parent
key=json.loads((W/'key.json').read_text())
fam=json.loads((W.parents[2]/'ciphers/hcp-1520/work/key.json').read_text()) if (W.parents[2]/'ciphers/hcp-1520/work/key.json').exists() else None
if fam is not None: assert key=={c:p.upper() for c,p in dict(fam,v='f').items()},'key differs from family key'
src=(W/'transcription-r2.txt').read_text()
out=[];units=letters=damaged=ch=0;used=set()
for line in src.splitlines():
    s=''
    for m in re.finditer(r'\{[^}]*\}|.',line):
        t=m.group()
        if t.startswith('{'):
            p=''.join(key[c] for c in t[1:-1]);s+='['+p+']';damaged+=len(t)-2;units+=len(t)-2;letters+=len(p);used|=set(t[1:-1])
        elif t in key:
            s+=key[t];units+=1;letters+=len(key[t]);used.add(t);ch+=t=='H'
        else:
            assert t in ' .,!?-',('unmapped sign',t);s+=t
    out.append(s)
print('\n'.join(out))
print(f'VERIFY: {len(out)} rows; {units} cipher units ({damaged} damaged but read); {letters} letters; CH={ch}; classes used={len(used)}/23; unmapped=0',file=sys.stderr)

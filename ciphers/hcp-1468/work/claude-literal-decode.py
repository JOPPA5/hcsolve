#!/usr/bin/env python3
"""Decode the literal transcription letter by letter (standard International Morse).
Checks source hashes. Output is LITERAL; it is not a claimed plaintext."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest, name
codes = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.',
         '---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
M = {c: chr(65+i) for i, c in enumerate(codes)}
for line in (p/'work/claude-literal-transcript.txt').read_text().splitlines():
    if line.startswith('#') or not line.strip():
        continue
    label, body = line.split(':', 1)
    body = body.split('(')[0]
    out = []
    for t in body.split():
        out.append(' ' if t == '/' else M.get(t, t))
    print(f'{label:10s} {"".join(out)}')
print('Source hashes OK. Literal letters only; see NOTES.md for intended readings and open points.')

#!/usr/bin/env python3
"""Decode only new, manually frozen slots; keep uncertain digits visible."""
import hashlib
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p / 'source' / name).read_bytes()).hexdigest() == digest
audit = json.loads((p / 'work/ten05-position-audit.json').read_text())
clear = 0
for group in audit['groups']:
    slots = group['slots']
    assert all(n is None or 1 <= n <= 26 for n in slots)
    clear += sum(n is not None for n in slots)
    print(group['where'] + ': ' + ''.join('?' if n is None else chr(91-n) for n in slots))
    candidate = group['provisional_middle']
    print('Provisional middle code only:', candidate, '->', chr(91-candidate))
    print('Provisional literal:', ''.join(chr(91-(candidate if n is None else n)) for n in slots))
    print(group['reason'])
assert clear == 4
print('4 newly frozen numeric positions; existing 69 + 4 = 73 clear positions.')
print('Source hashes passed. Manual transcription, not full-message/pixel proof.')

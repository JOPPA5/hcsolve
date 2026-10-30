#!/usr/bin/env python3
"""Round-2 decoder for hcp-1549. Standard library only, read-only.
Reads work/transcription-r2.json and work/key.json; prints
 1. the LITERAL reading (exactly what the glyphs give; [X] = restored letter under an ink blot),
 2. the EDITORIAL base reading (literal + the listed, explicitly marked writer-slip repairs),
 3. counts."""
import json, re
from pathlib import Path
W = Path(__file__).resolve().parent
key = json.loads((W / 'key.json').read_text())
assert key == json.loads((W.parents[1] / 'hcp-1520/work/key.json').read_text()), 'family key differs'
rec = json.loads((W / 'transcription-r2.json').read_text())
U = rec['uncertainties']
def dec(s): return ''.join(key[c].upper() if c in key else c for c in s)
lit = []; known = ch = restored = 0
for r in rec['rows']:
    out = ''
    for part in re.split(r'(\{U1\})', r['cipher']):
        if part == '{U1}':
            g = U['U1']['glyphs']
            p = ''.join('[' + dec(m[1]) + ']' if m[1] else dec(m[2]) for m in re.finditer(r'\{(.)\}|(.)', g))
            assert p == U['U1']['plain_literal']; out += p
            restored += len(re.findall(r'\{.\}', g)); known += len(re.sub(r'\{.\}', '', g))
        else:
            assert all(c in key or c in ' ,.!?-' for c in part), (r['id'], part)
            out += dec(part); known += sum(c in key for c in part); ch += part.count('H')
    lit.append(out)
literal = '\n'.join(lit)
# Editorial repairs of writer slips (each must apply exactly once), shown with <...> in output.
REPAIRS = [('ZVASTE', 'ZV<L>ASTE'),      # zvlaste: L omitted by writer
           ('HTEL JSEM ZASLATI', '<CH>TEL JSEM ZASLATI'),  # CH tilde omitted
           ('RUZNERO', 'RUZNE<H>O'),       # R written for H
           ('ROZPRAVU DU', 'ROZPRAVU <T>U'),# D written for T
           ('ABY SO O', 'ABY S<E> O')]     # O written for E (faint mark above)
ed = literal
for a, b in REPAIRS:
    assert ed.count(a) == 1, a; ed = ed.replace(a, b)
print('=== LITERAL ([X] = restored under ink blot) ===\n' + literal)
print('\n=== EDITORIAL BASE (<X> = editorial repair of a writer slip) ===\n' + ed)
print(f'\nCHECKED: {len(rec["rows"])} rows; {known} plainly read cipher units ({ch} of them CH); '
      f'{restored} restored units (U1); 0 bounded alternatives; {len(REPAIRS)} editorial repairs.')

#!/usr/bin/env python3
"""Source-bound manual geometry audit, with a deliberately limited Pigpen check.
Does not turn pixels into letters and does not claim an established key.
"""
import hashlib,json,itertools
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED={'address.jpg': '7a54e02489a958e54293b6cbdfdcdcc29ef6166d02c5a7fa0f7c4b2ac095fd64', 'metadata.md': '0d799c33f63caeb7b67023dfef803acdeb0cc006207cfd7fd868c46b3053287c', 'picture.jpg': 'd0ab8297410a28a74b38d35ba20daeb1cdae000263b455d4f731356c1b80cb2c'}
# Conventional A-I/J-R grids with S-V/W-Z crosses. Indices name visible outlines.
GRID=['corner_br','cup','corner_bl','open_left','square','open_right','corner_tr','cap','corner_tl']
CROSS=['angle_down','angle_right','angle_left','angle_up']
def key_for(order=(0,1,2,3)):
    groups=[GRID,[s+'_dot' for s in GRID],CROSS,[s+'_dot' for s in CROSS]]
    ordered=list(itertools.chain.from_iterable(groups[i] for i in order))
    return dict(zip(ordered,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
def render(rows,key):
    words=[]
    for row in rows:
        word=''
        for g in row['glyphs']:
            if g.get('canceled'): word+='{CANCELED}'; continue
            vals=[key.get(r,'?') for r in g['readings']]
            word+=vals[0] if len(vals)==1 else '['+'/'.join(vals)+']'
        words.append(word)
    return ' / '.join(words)
def main():
    for name,sha in EXPECTED.items():
        actual=digest(BASE/'source'/name)
        assert actual==sha,(name,actual)
        print('SHA256',name,actual)
    t=json.loads((BASE/'work/transcript.json').read_text())
    records=[g for r in t['rows'] for g in r['glyphs']]
    assert [g['id'] for g in records]==list(range(1,30))
    print('Manual geometry records:',len(records),'active:',sum(not g.get('canceled',False) for g in records))
    print('Coordinates refer to original picture; the script verifies hashes, not pixel readings.')
    for r in t['rows']:
        print('GROUP',r['word'], ' '.join(f"{g['id']}:{'|'.join(g['readings'])}@{g['box']}" for g in r['glyphs']))
    print('Conventional reference key (NOT established):')
    print(render(t['rows'],key_for()))
    print('Right-facing T positions 11 and 24 have no entry in this reference key.')
    print('Group-order sensitivity only (24 orders; no completeness or language-negative claim):')
    for order in itertools.permutations(range(4)):
        print(''.join(map(str,order)),render(t['rows'],key_for(order)))
    print('NO PLAINTEXT ESTABLISHED. Geometry alternatives and canceled glyph remain unresolved.')
if __name__=='__main__': main()

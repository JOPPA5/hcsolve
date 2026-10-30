#!/usr/bin/env python3
"""Read-only audit/decoder of a MANUAL transcript; never OCR or glyph truth."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    audit = json.loads((HERE/'audit-sha256.json').read_text())
    for path, expected in audit['originals_and_references'].items():
        assert sha(REPO/path) == expected, f'Source/reference hash mismatch: {path}'
    for name, expected in audit['records'].items():
        assert sha(HERE/name) == expected, f'Record hash mismatch: {name}'
    guard = json.loads((REPO/'batches/easy-2026-10-28/cz230-next-source-sha256.json').read_text())
    assert len(guard) == 9
    for path, expected in guard.items():
        assert sha(REPO/path) == expected, f'Batch original mismatch: {path}'
    key = json.loads((HERE/'key.json').read_text())
    canonical = json.loads((REPO/'ciphers/hcp-1520/work/key.json').read_text())
    assert key == {**canonical, 'F':'f'}
    assert len(key) == 23 and len(set(key.values())) == len(key)
    inverse = {v:k for k,v in key.items()}  # whole fixed key, never learned per token
    raw = (HERE/'transcription.txt').read_text()
    inv = json.loads((HERE/'inventory.json').read_text())
    assert raw.splitlines() == [r['transcription'] for r in inv['rows']]
    reconstructed = []
    for n,(line,row) in enumerate(zip(raw.splitlines(),inv['rows']),1):
        assert row['line'] == n
        bx = row['bbox_upright']
        assert row['bbox_original'] == [bx[1],674-bx[2],bx[3],674-bx[0]]
        count=0; word=1; inch=0
        for offset,c in enumerate(line):
            if c==' ': word+=1; inch=0; continue
            inch+=1
            if c in key:
                count+=1
                reconstructed.append(dict(id=f'L{n:02d}-R{count:03d}',line=n,recognized_unit_index=count,word_index=word,transcript_character_in_word=inch,transcript_offset_zero_based=offset,cipher=c,plaintext=key[c],whole_row_bbox_original=row['bbox_original']))
        assert count == row['recognized_units']
    assert reconstructed == inv['glyphs'], 'Inventory indices or literal units disagree'
    assert 'unknown_spans' not in inv and inv['resolved_spans'][0]['length'] == 5
    assert all(c in key or c in ' .,!?-\n' for c in raw), 'Unmapped symbol in transcription'
    literal = ''.join(key.get(c,c) for c in raw)
    assert literal == (HERE/'literal.txt').read_text(), 'Recorded literal mismatch'
    # Re-encode the entire literal, treating CH as one Czech unit.
    out=[]; i=0
    while i<len(literal):
        if literal[i:i+2]=='ch': out.append(inverse['ch']); i+=2
        else: out.append(inverse.get(literal[i],literal[i])); i+=1
    assert ''.join(out) == raw, 'Whole-key inverse failed'
    units=len(reconstructed); letters=sum(len(g['plaintext']) for g in reconstructed)
    print(f'OK: 9 immutable batch originals; {len(audit["originals_and_references"])} original/reference/manifest hashes; {len(audit["records"])} record hashes')
    print(f'OK: 14 rows; {units} recognized cipher units; {letters} recognized base letters; {sum(g["cipher"]=="H" for g in reconstructed)} CH units; 0 unknown spans')
    print('OK: all inventory indices, recorded literal equality, and whole fixed-key greedy-CH inverse')
    print('These checks do not prove image transcription (manual, checked in review).\n')
    print(literal,end='')

if __name__ == '__main__':
    main()

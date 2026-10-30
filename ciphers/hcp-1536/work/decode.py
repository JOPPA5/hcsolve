"""Read-only verifier/decoder of a manual image transcription; this is not OCR.

The source hashes bind the supplied images to the manually authored record.
They do not prove that a human reading of every glyph is correct.
"""
from pathlib import Path
import json, hashlib

HERE=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((HERE/'record-sha256.json').read_text())
for name,want in manifest.items():
    assert sha(HERE/name)==want, f'record changed: {name}'
record=json.loads((HERE/'transcription.json').read_text())
key=json.loads((HERE/'key.json').read_text())
assert sha(HERE/'key.json')==record['key_sha256']
for name,want in record['source_sha256'].items():
    assert sha(HERE.parent/'source'/name)==want, f'source changed: {name}'
inverse={v:k for k,v in key.items()}
assert len(inverse)==len(key)
flags={}
for uid,u in record['uncertainties'].items():
    for pos in u['positions']: flags[(u['row'],pos)]=uid
count=0;spans=0;ch_count=0;out=[]
for row in record['rows']:
    plain=[];source=[]
    for pos,tok in enumerate(row['tokens'],1):
        assert tok['position']==pos, f'{row["id"]}: missing position {pos}'
        if tok['kind']=='span':
            assert tok['glyph_count'] is None
            assert tok['id'] in record['uncertainties']
            p='⟦'+tok['id']+':unknown-length⟧'
            source.append('['+tok['id']+']');spans+=1
        else:
            s=tok['symbol'];source.append(s)
            if tok['kind']=='glyph':
                p=key[s]; assert inverse[p]==s, 'tokenwise exact roundtrip failed';count+=1
                ch_count += (p=='ch')
            else:
                assert s in ' .,', f'unexpected unkeyed symbol: {s!r}'
                p=s
        if (row['id'],pos) in flags: p='['+p+']'
        plain.append(p)
    assert ''.join(source)==row['transcription'], f'{row["id"]}: transcript mismatch'
    out.append((row['id'],''.join(plain).upper()))
print('MANUAL TRANSCRIPTION, NOT OCR. Source and record hashes verified.')
print(f'{len(out)} rows; {count} keyed glyph tokens ({ch_count} CH signs, {count-ch_count} other signs), emitting {count+ch_count} base letters; all indexed positions verified; exact tokenwise roundtrip passed.')
for uid,u in record['uncertainties'].items():
    row=[r for r in record['rows'] if r['id']==u['row']][0]
    assert ''.join(row['tokens'][q-1]['symbol'] for q in u['positions'])==u['symbols'], uid
    print(f"{uid} ({u['row']} positions {u['positions']}, {u['status']}): shown in [brackets] below")
for row,s in out:print(f'{row}: {s}')
print('Unencrypted date: 26./IX.1903. Address and printed publisher text are separately recorded in SOLUTION.md.')

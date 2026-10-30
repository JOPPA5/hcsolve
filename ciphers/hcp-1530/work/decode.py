#!/usr/bin/env python3
"""HCP 1530 (pc_hcp_211) - read-only decoder, v2 (after review 1).
Applies work/key.json to the manual transcription work/v2/transcription-v2.json.
Signs restored from context (not seen on the scan) are printed in [brackets];
faint signs are listed separately. The v1 partial decoder is kept as decode-v1-partial.py."""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parents[1];W=R/'work'
for fn,dg in json.loads((W/'source-sha256.json').read_text()).items():
    assert hashlib.sha256((R/fn).read_bytes()).hexdigest()==dg,'hash mismatch '+fn
key=json.loads((W/'key.json').read_text());inv={v:k for k,v in key.items()};assert len(inv)==len(key)==23
rec=json.loads((W/'v2'/'transcription-v2.json').read_text())
cnt=Counter();faint=[];units=letters=ch=0;plain_rows=[]
for row in rec['rows']:
    out=[];raw=[];prev_restored=False
    for p in row['parts']:
        if 'cipher' in p:
            c=p['cipher'];pl=key[c];assert pl==p['plain'] and inv[pl]==c
            units+=1;letters+=len(pl);ch+=pl=='CH';cnt[p['certainty']]+=1;raw.append(c)
            r=p['certainty']=='restored'
            if r and not prev_restored: out.append('[')
            if prev_restored and not r: out.append(']')
            out.append(pl);prev_restored=r
            if p['certainty'] in('faint','probable'): faint.append(f"{row['id']}:{c}={pl}({p['certainty']})")
        else:
            if prev_restored: out.append(']');prev_restored=False
            t=p.get('ordinary',p.get('literal'));raw.append(t);out.append(t)
    if prev_restored: out.append(']')
    assert ''.join(raw)==row['cipher']
    plain_rows.append(row['id']+' '+''.join(out))
print('\n'.join(plain_rows))
assert (len(rec['rows']),units,ch,letters)==(14,464,6,470),(units,ch,letters)
assert cnt['restored']==2
print(f'\n{units} cipher units (6 CH) -> {letters} letters; {cnt["clear"]} clear, {cnt["faint"]+cnt["probable"]} faint/probable, {cnt["restored"]} restored from context (in brackets).')
print('Faint/probable signs:',', '.join(faint))
print('No unassigned sign. Verified 3 source hashes and exact per-sign inverse-key round trip.')

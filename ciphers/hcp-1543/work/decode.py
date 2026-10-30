#!/usr/bin/env python3
"""Read-only reproducibility check. Transcription is human/AI visual evidence, not OCR."""
from pathlib import Path
import csv, hashlib, io, json, re
R=Path(__file__).resolve().parents[1];W=R/'work';ROOT=R.parents[1]
manifest=json.loads((W/'sha256.json').read_text())
for group,base in [('source',R),('references',ROOT),('record',R)]:
    for rel,want in manifest[group].items():
        assert hashlib.sha256((base/rel).read_bytes()).hexdigest()==want,(group,rel,'hash mismatch')
key=json.loads((W/'key.json').read_text());rec=json.loads((W/'transcription.json').read_text());aliases=rec['aliases'];unknown=rec['uncertainties']
ref={k:v.upper() for k,v in json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text()).items()}
assert key==ref,'Family key differs from hashed earlier-key reference'
inverse={v:k for k,v in key.items()};assert len(inverse)==len(key),'Non-injective base key'
assert all(target in key and alias not in key for alias,target in aliases.items())
# Actual independent direction: tokenize complete plaintext chunks by descending
# plaintext-value length, then use the whole inverse key. CH is a digraph here;
# this convention cannot distinguish hypothetical adjacent C and H source units.
values=sorted(inverse,key=len,reverse=True)
def encode_chunk(plain):
    result=[];i=0
    while i<len(plain):
        match=next((v for v in values if plain.startswith(v,i)),None)
        if match is not None:result.append(inverse[match]);i+=len(match)
        else:
            assert not plain[i].isalpha(),('unencodable plaintext',plain[i]);result.append(plain[i]);i+=1
    return ''.join(result)
rows=[];positions=[];global_slot=0;known=0
for rn,row in enumerate(rec['rows'],1):
    rid=f'R{rn:02}';assert row['id']==rid
    tokens=re.findall(r'\{[^}]+\}|.',row['cipher']);plain=[];canonical=[];chunk=[];chunk_plain=[];slot=0;row_known=0
    def check_chunk():
        assert encode_chunk(''.join(chunk_plain))==''.join(chunk),('inverse mismatch',rid)
        chunk.clear();chunk_plain.clear()
    for token in tokens:
        canon=aliases.get(token,token)
        if token in unknown:
            check_chunk();value=unknown[token]['literal'];plain.append(value);slot+=1;global_slot+=1
            positions.append([str(global_slot),rid,str(slot),token,'',value,str(unknown[token]['unit_length']) if unknown[token]['unit_length'] is not None else ''])
        elif canon in key:
            value=key[canon];plain.append(value);chunk.append(canon);chunk_plain.append(value);slot+=1;global_slot+=1;known+=1;row_known+=1
            positions.append([str(global_slot),rid,str(slot),token,canon,value,'1'])
        else:
            assert token in ' .,-',('unrecognized token',rid,token)
            plain.append(token);chunk.append(token);chunk_plain.append(token)
    check_chunk();text=''.join(plain);assert text==row['plaintext'],('saved row plaintext mismatch',rid)
    assert slot==row['record_slots'] and row_known==row['known_units'];rows.append(text)
saved=list(csv.reader(io.StringIO((W/'positions.csv').read_text())))
assert saved[0]==['record_slot','row','row_slot','shape_label','canonical_label','base_plaintext','unit_length']
assert saved[1:]==positions,'position inventory mismatch'
out='\n'.join(rows)+'\n';assert (W/'plaintext.txt').read_text()==out,'plaintext file mismatch'
print(out,end='')
print(f'CHECKS OK: {len(rows)} rows; {known} read units; {global_slot-known} editorial restorations shown as [C]; {global_slot} sign positions.')
print('Verified original/reference/record hashes, every index, saved plaintext, and canonical whole-chunk inverse. Alias shapes 7/y and ř/H collapse; CH uses greedy digraph convention. These checks do not certify visual transcription or key provenance independently.')

#!/usr/bin/env python3
"""Verify source bytes and indexed manual transcription, then decode. Read-only by default.
This proves record/key consistency, not the truth of the manual image reading.
"""
from pathlib import Path
import argparse,hashlib,json,sys
W=Path(__file__).resolve().parent
P=argparse.ArgumentParser(); P.add_argument('--write-derived',action='store_true'); args=P.parse_args()
key=json.loads((W/'key.json').read_text()); inv={v:k for k,v in key.items()}
assert len(inv)==len(key), 'non-invertible key'
for name,sha in json.loads((W/'source-sha256.json').read_text()).items():
 assert hashlib.sha256((W.parent/'source'/name).read_bytes()).hexdigest()==sha, f'changed original: {name}'
for name,sha in json.loads((W/'record-sha256.json').read_text()).items():
 assert hashlib.sha256((W/name).read_bytes()).hexdigest()==sha, f'changed record: {name}'
for name,sha in json.loads((W/'reference-sha256.json').read_text()).items():
 assert hashlib.sha256((W.parents[2]/name).read_bytes()).hexdigest()==sha, f'changed reference: {name}'
rows=json.loads((W/'manual-records.json').read_text())['rows']
assert [r['row'] for r in rows]==list(range(1,14))
index=['row\tglyph_index\tword_index\tshape\tplain_base']; plains=[]; indexed=[]; count=0
for row in rows:
 units=[key.get(c,c) for c in row['cipher']]
 assert ''.join(units)==row['expected_plain'], f'decode mismatch row {row["row"]}'
 assert ''.join(inv.get(u,u) for u in units)==row['cipher'], f'tokenwise roundtrip mismatch row {row["row"]}'
 assert all(c in key or c in ' .,-?' for c in row['cipher']), 'unrecorded token'
 i=0; seq=[]
 for word,part in enumerate(row['cipher'].split(' '),1):
  for ch in part:
   if ch in key:
    i+=1; index.append(f"{row['row']}\t{i}\t{word}\t{ch}\t{key[ch]}");seq.append(f'{i:02}:{ch}')
 count+=i; plains.append(row['expected_plain'])
 indexed.append(f"## Row {row['row']:02}\n\n![Row {row['row']}]({row['crop']})\n\nCipher: `{row['cipher']}`\n\nIndices: `{' '.join(seq)}`\n\nLiteral: {row['expected_plain']}\n")
assert (W/'indexed-transcription.tsv').read_text()=='\n'.join(index)+'\n', 'indexed record mismatch'
text='\n'.join(plains)+'\n'
assert count==289
assert (W/'plaintext-literal.txt').read_text()==text, 'literal display mismatch'
if args.write_derived:
 from PIL import Image
 im=Image.open(W.parent/'source'/'picture.jpg').rotate(-90,expand=True)
 im.save(W/'upright.png')
 for row in rows:
  box=row['crop_box_upright'];im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3)).save(W/row['crop'])
 (W/'plaintext-literal.txt').write_text(text)
 (W/'transcription-index.md').write_text('# Indexed manual transcription\n\nGlyph indices count cipher shapes only, excluding spaces and punctuation. Row crops overlap to retain tall strokes. All coordinates refer to clockwise rotated picture; no unknown spans asserted.\n\n'+'\n'.join(indexed))
print(text,end='')
print(f'VERIFIED: 3 originals; 13 ordered rows; {count} indexed glyphs; exact tokenwise roundtrip. Image reading remains manual.',file=sys.stderr)

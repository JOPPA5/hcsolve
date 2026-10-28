"""Authoring helper: records the solver's manual glyph readings, not OCR."""
from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json,csv
from collections import Counter
p=Path(__file__).resolve().parent; root=p.parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','H':'CH','v':'F'}
(p/'key.json').write_text(json.dumps(key,indent=2)+'\n')
texts=[
'fh581 t4g q6 th6r1 84cd5g! q6hn32-',
'd48 nm5 fc6g. 6m2mg6 n4 2hs4d5',
'c84p486, q5 f h47m2 bh475t5',
't3 bh6r1! gt4q c6n6 m5f5h4,',
'q5 c5 n4 b3 m4 cd1cg6 6 q6',
'c5 m6 m4 f584s5 d5c4n, m5n6',
'nm5 c6n6 h6t6! - t3b4c q6c82,',
'76gn485 c5 n4 dh3H2 2f38m4',
'f m6rh3n6t5m5 bh6s4.',
'sdfhd h3g2 m5p t685, 76g3',
'76 7c5n n2c58 s5g6d4 m6',
't3b4c, d3 74cd5 dhf6d4',
'm5p2t5! d4c4s fh581H, t832-',
'r1H f6cm4f1H b2c 3t b5b32c5.',
'cg3t6, q5 n4 b3c8686 76r3t1 p5q f1qm6n2!',
'p18 p1H q6t68, 6p1 r3tm5 phq3 bh47586 t3 bh6r1!',
'gt1q fc6g m5n674 n4d4 76r3t4',
'bh3 nm5 cf5r3 f1qm6n2, m5f4n,',
'n3r2-84 c5 3tf6q4d4, d3r3 q6t6d4..']
# Literal shape label H is the special CH unit, including its upper mark; no separate accent decoding.
rows=[]; im=Image.open(root/'source'/'picture.jpg').transpose(Image.Transpose.ROTATE_90);im.save(p/'oriented-native.png');mi=Image.open(root/'source'/'picture.jpg').transpose(Image.Transpose.ROTATE_180);mi.save(p/'margin-oriented-native.png')
base=[583,609,635,661,687,713,738,764,791,816,842,868,896,922,947,975]
for i,cipher in enumerate(texts):
 if i<16:
  rid=f'B{i+1:02d}';frame='picture-ROTATE_90';b=base[i]; box=[260 if i<12 else (250 if i==12 else (195 if i==13 else 30)),b-23,644,b+13];src=im; fn=f'line{i+1:02d}.png'
 else:
  rid=f'M{i-15:02d}';frame='picture-ROTATE_180';box=[[95,455,555,508],[95,491,535,537],[95,525,557,566]][i-16];src=mi;fn=f'margin{i-15:02d}.png'
 plain=''.join(key.get(c,c) for c in cipher)
 row={'id':rid,'frame':frame,'box':box,'crop':fn,'cipher':cipher,'literal':plain,'assigned_units':sum(c in key for c in cipher)}
 rows.append(row);src.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3)).save(p/fn)
meta={'method':'Manual visual transcription from source/picture.jpg. Lossless ROTATE_90 frame is 674x1024; ROTATE_180 frame is 1024x674 for margin. Whole-row crops can overlap at ascenders and descenders; row boxes are not individual glyph pixel boxes. Known-key transfer, not automatic OCR. Spaces and punctuation are editorial segmentation of visible writing; literal means unaccented base-letter substitution, with source spelling retained.','source_sha256':{f.name:sha(f) for f in (root/'source').iterdir() if f.is_file()},'rows':rows,'excluded_spans':[{'row':'B09','frame':'picture-ROTATE_90','box':[569,775,618,811],'reason':'Canceled overink after PRACI. At least three apparent sign positions are visible: first a solid blot, second an f-form (V) with upper loop and descender, third a looped ascender compatible with h/R or 8/L but uncertain. The whole word and exact original unit count remain unknown. Excluded from active-unit totals; no replacement unit or total-original denominator is assigned.'}],'ordinary':['Picture margin date: 13./X.1903.','Address side: Velectena Slecna / slecna Anna Ticha / ucitelka v / Zirovnici / u Pocatek. Modern accents editorial. No ciphertext identified on address side.'],'marks':['B13 terminal arrow points toward margin continuation; ordinary arrow, not a cipher unit.','Margin-entry arrow points to M01; ordinary arrow.','B15 BEZ is underlined, not additional letters.','M03 ends with two small dots and, slightly above the line after them, a distinct upright u-like sign in the same ink. It does not match the key 2/U shape. Its meaning is unknown; it is excluded from the cipher-unit index and not silently decoded as U.','Small pen marks above individual ordinary units are not used to manufacture accented plaintext. H labels the established special CH glyph including its upper mark.'],'reading_notes':['B02 6m2mg6 literally ANUNKA, not ANINKA.','B04 gt4q literally KDIZ versus M01 gt1q literally KDYZ: the B04 third sign has the two-arm, footed I/4 form. Preserve KDIZ literally; editorial Czech normalises it to kdyz.','B04 punctuation after PRAHY is an exclamation mark with visible upper stroke, not a dot.','M01 76r3t4 literally JAHODI whereas B15 76r3t1 literally JAHODY. Preserve final I/Y difference; editorial version corrects JAHODI to jahody.','B08 dh3H2 literally TROCHU; CH is one cipher unit, two plaintext base letters.','B05/B06 ZA / SE joins to zase; no hyphen visibly supplied at B05 end.','B09 canceled overink not reconstructed.']}
counts=Counter(c for row in rows for c in row['cipher'] if c in key)
meta['counts']={'active_rows':len(rows),'active_units':sum(counts.values()),'base_letters':sum(counts[c]*len(key[c]) for c in counts),'CH_units':counts['H'],'unknown_active_units':0,'observed_assigned_classes':len(counts),'class_counts':dict(sorted(counts.items()))}
meta['excluded_marks']=[{'row':'M03','frame':'picture-ROTATE_180','box':[526,524,552,551],'description':'Distinct upright u-like mark after two dots; same ink, not matching the established 2/U class. Meaning unknown, excluded from active cipher-unit counts.'}]
(p/'transcription.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
(p/'transcription.txt').write_text('\n'.join(r['id']+' '+r['cipher'] for r in rows)+'\n')
(p/'literal.txt').write_text('\n'.join(r['id']+' '+r['literal'] for r in rows)+'\n')
with (p/'indexed-units.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['ordinal','row','row_unit','glyph_label','plain','frame','row_box']);i=0
 for row in rows:
  j=0
  for c in row['cipher']:
   if c in key:
    i+=1;j+=1;w.writerow([i,row['id'],j,c,key[c],row['frame'],','.join(map(str,row['box']))])
refs=['ciphers/hcp-1520/work/key.json','batches/easy-2026-10-28/published-anna-ticha-key.txt','batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/public-reference-199/provenance.json']
(p/'reference-sha256.json').write_text(json.dumps({f:sha(root.parent.parent/f) for f in refs},indent=2)+'\n')
(p/'record-hashes.json').write_text(json.dumps({f:sha(p/f) for f in ['transcription.json','key.json','indexed-units.csv','transcription.txt','literal.txt','reference-sha256.json']+[r['crop'] for r in rows]+['oriented-native.png','margin-oriented-native.png','build_records.py','decode.py','review1-source-controls.png','review1-u-mark-box-check.png']+[f'review1-source-control-{i}.png' for i in range(1,6)]},indent=2)+'\n')
print((p/'literal.txt').read_text())

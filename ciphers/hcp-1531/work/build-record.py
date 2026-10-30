#!/usr/bin/env python3
"""Explicit record generator; not invoked by the read-only decoder."""
from pathlib import Path
import json,hashlib,csv
R=Path(__file__).resolve().parents[1]; W=R/'work'
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH'}
boxes=[(580,37,973,79),(584,69,973,104),(585,94,975,132),(582,120,970,157),(578,148,975,185),(576,176,972,211),(576,202,972,239),(575,231,968,268),(573,254,970,291),(673,425,954,464),(669,459,956,495),(662,485,958,522),(662,515,960,549),(567,539,959,576),(517,568,955,603),(478,590,950,629),(479,613,720,642)]
cipher=[
'fh5832 b2c2 q6 th6r1 84cd5g. bh3-',
'n4m, q5 m53tb3f5t58 7c5n cf5n2',
'cht5sg2 t3c2t. f c3p3d2 h3qp38586',
'c5 n4 r86f6 6 dh6b486 nm5 6q t3',
'fs5h57cg6. p186 d3 n686 řh4bg6,',
'm6c85tg5n gd5h5 7c5n f m5t584',
'6 f b3mt584 n2c48 285rm32d4.',
'bh4c83 n4 d3 f584s5 m5fr3t,',
'b3m5f6tq bh6f5 m1m4 7c5n',
'q6rhm4d bh6s4, gd5h32',
'm4gt3 q6 nm5 m52t586.',
'bc6m[4] 75 74q h3q5bc6m3,',
'3t5c82 75 s3 m57th4f5.',
's3 t586 n375 cht5sg3? d4c4s',
'fh581ř b3qth6f2 3t b5b32c5, gd5h1',
'f t2ř2 m53c4c8m5 gh6d5 th6r32 df374',
'r86f4mg2 84p6.'
]
rows=[];pos=[];ordinal=0
for i,(b,c) in enumerate(zip(boxes,cipher),1):
 rid=f'R{i:02}';plain=''.join(key.get(x,x) for x in c);idx=0
 for x in c:
  if x in key:
   idx+=1;ordinal+=1;pos.append([ordinal,rid,idx,x,key[x]])
 rows.append({'id':rid,'box_source_xyxy':b,'cipher':c,'plaintext':plain,'active_units':idx})
record={'method':'Manual visual source transcription using supplied family key. Printed labels are glyph classes. No OCR. Coordinates refer to the original 1024x674 picture.jpg. Boxes can overlap ascenders; ordinal positions do not claim individual glyph pixel coordinates.', 'rows':rows,'unknowns':[],'restorations':[{'row':'R12','row_ordinal':5,'shape':'Final unit of opening PSAN[I] lies under the photograph shadow: a closed bowl with a long descender and a possible further faint oval are seen; the sign cannot be identified visually and possibly two signs stand there. 4/I (PSANI) is restored from context (neuter noun needed for je jiz rozepsano), not read.'}],'review_corrections':['R05 ordinal 2: peaked Lambda-form is the writer s/C (as in VELICE R08 and PRACI R10), not 1/Y; reads VCEREJSKA (review 1 finding 1).','R16 NEOSISLNE: 4th sign is the open c/S (as in TISIC), not s/C; 3rd sign read as 3/O, possibly the hooked s/C; sister card hcp-1532 has m5cs4c8m5 NESCISLNEKRATE (review 1 finding 4).'], 'ordinary':['11./XI.1903 at picture center-left.','Address side: Velectena Slecna / slecna Anna Ticha / ucitelka v / Zirovnici / u Pocatek (ordinary script, editorial accent removal).'],'marks':['No canceled cipher units identified.','R01 PRO-/R02 MIN continuation retained.','R05 CHRIPKA and R15 VRELYCH and R16 DUCHU use the special CH glyph, labelled ř by convention.','R10 last-but-one unit of first word is classified 4/I, yielding ZAHRNIT; not normalized to ZAHRNUT.','R16 NEOSISLNE KRATE retained literally (intended nescislnekrate); 3rd sign possibly s/C.','R13 ODESLU 3rd sign under shadow looks 6-like; E read from context.']}
for name,data in [('key.json',key),('transcription.json',record)]: (W/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (W/'positions.csv').open('w') as f:
 wr=csv.writer(f);wr.writerow(['global_ordinal','row','row_ordinal','glyph','plaintext']);wr.writerows(pos)
for name,files in [('source-sha256.json',['source/picture.jpg','source/address.jpg','source/metadata.md']),('record-sha256.json',['work/key.json','work/transcription.json','work/positions.csv'])]:
 (W/name).write_text(json.dumps({f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in files},indent=2)+'\n')
print('\n'.join(r['plaintext'] for r in rows));print('Units',ordinal,'CH',sum(c.count('ř') for c in cipher),'base letters',sum(len(key[x]) for c in cipher for x in c if x in key))

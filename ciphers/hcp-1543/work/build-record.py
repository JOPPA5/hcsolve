#!/usr/bin/env python3
"""Regenerate manual solver transcription artifacts; never edits source/."""
from pathlib import Path
import csv, hashlib, json, re
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[1]; W=R/'work'; ROOT=R.parents[1]
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','y':'J','H':'CH'}
aliases={'7':'y','ř':'H'}
raw=[
'h3qn486 n6 6m4sg3, fh581 t4g q6 th6r1 84cd5g. bh686',
'7c4 c4 tm5c 74q 3tb3f5t,6fc6g 76 d5bhf5 tm5c 7c5n',
'84cd5g df27 t3cd68. p18 d5bhf5 fs5h6 3t5c86m',
'q rh6t{U1}5 6 t3c58 fs5h6 f5s5h t3 bh6r1,gt1',
'c5 74q m5t3h2s3 f683. hn32d4 nm5,q5 n375',
'cht5{U2}g3 3b5d cd2m5. bh4 f3t486 7c4 c3p5',
'ř3h3p2 d2 c3t3f32 f3t32,gd5h5 76 m5f5h4n.',
'c5dh4 c5 s3 m57f4s5 th6r32cg2. d4c4s',
'fh581ř,f6cm4 f1ř b2c b3c486 d4 cd685',
'fqb3n4m674s4 b5b32c.',
'c85sm5 76mg3f5',
'f1h4t,bh3c4n,',
'n375 b3-',
'h2s5m4.'
]
ys=[(42,80),(76,109),(103,143),(135,175),(168,205),(202,239),(235,276),(273,314),(312,353),(349,389),(384,418),(413,448),(445,477),(473,499)]
unknowns={'{U1}':{'kind':'editorial_restoration','candidate_labels':['s'],'literal':'[C]','unit_length':1,'note':'R04: one-sign-wide blot between HRAD (t = D read) and E. C restored from context only (Z HRADCE, the recipient town Jindrichuv Hradec); no stroke of the sign recovered.'},'{U2}':{'kind':'editorial_restoration','candidate_labels':['s'],'literal':'[C]','unit_length':1,'note':'R06: one heavy struck/overwritten sign (closed bowl with a long oblique stroke) between SRDE and KO. Its shape does NOT match the family s = C; C restored from context only (SRDECKO = srdecko). Any hacek reading of the stroke is speculative.'}}
rec={'method':'Manual visual transcription from source/picture.jpg rotated clockwise 90 degrees. Shape labels are mnemonic identifiers, not plaintext letters. Known key transfer; no target solution supplied. Spaces approximate manuscript gaps; no accent values inferred by the decoder. Indexed row boxes overlap ascenders. All fourteen message rows, both sides and margins inspected.','aliases':aliases,'uncertainties':unknowns,'ordinary':['Picture date 17.VIII.1903.','Address: Velectena Slecna / slecna Anna Ticha, / ucitelka t.c. / v Jindrichove Hradci / u slecny K. Jankove, ucitelky. (Accents present in ordinary handwriting; this list is descriptive.)','Printed picture artist text: 1903. [artist signature]; landscape decoration. No extra cipher text identified in margins or address side.'],'marks':['Separate short marks occur over CH-like units in R07 and R09 and over PUS in R09. They are recorded descriptively, not used to manufacture accent values.','Both blotted positions are one sign wide; their letters are editorial restorations printed in square brackets.'],'rows':[]}
positions=[];idx=0
rec['paleographic_choices']=[{'row':'R01','cipher_word':'6m4sg3','chosen_label':'s g','plaintext':'ANICKO','security':'clear after review 1','discarded_alternative':'6m4g3 ANIKO / ANIZO (earlier record omitted the narrow s sign)','evidence':'At 3-8x a narrow upright s (C) with small top hook stands between 4 (I) and the closed-loop g (K); same form as s in VCERA (R03, R04) and NEDORUCOVALO (R05). Review 1 finding 1.'}]
for rn,(rawrow,(ya,yb)) in enumerate(zip(raw,ys),1):
    rid=f'R{rn:02}'; tokens=re.findall(r'\{[^}]+\}|.',rawrow); plain=[];local=0; known=0
    for token in tokens:
        canon=aliases.get(token,token)
        if token in unknowns:
            local+=1;idx+=1; value=unknowns[token]['literal'];plain.append(value)
            positions.append([idx,rid,local,token,'',value,unknowns[token]['unit_length']])
        elif canon in key:
            local+=1;idx+=1;known+=1;plain.append(key[canon]);positions.append([idx,rid,local,token,canon,key[canon],1])
        else: plain.append(token)
    rec['rows'].append({'id':rid,'box_upright_xyxy':[29,ya,649,yb],'cipher':rawrow,'plaintext':''.join(plain),'known_units':known,'record_slots':local})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
with (W/'positions.csv').open('w') as f:
    writer=csv.writer(f);writer.writerow(['record_slot','row','row_slot','shape_label','canonical_label','base_plaintext','unit_length']);writer.writerows(positions)
(W/'plaintext.txt').write_text('\n'.join(x['plaintext'] for x in rec['rows'])+'\n')
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);im.save(W/'picture-upright.png');indexed=im.copy();d=ImageDraw.Draw(indexed)
for row in rec['rows']:
    box=row['box_upright_xyxy'];d.rectangle(box,outline='red');d.text((1,box[1]),row['id'],fill='red');im.crop(box).resize((1860,(box[3]-box[1])*3)).save(W/(row['id']+'.png'))
indexed.save(W/'indexed.png')
refs=['ciphers/hcp-1520/work/key.json','batches/easy-2026-10-28/published-anna-ticha-key.txt','batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/public-reference-199/provenance.json']
manifest={'source':{str(x.relative_to(R)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted((R/'source').iterdir()) if x.is_file()},'references':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in refs},'record':{str(x.relative_to(R)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [W/'key.json',W/'transcription.json',W/'positions.csv',W/'plaintext.txt']}}
(W/'sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
print((W/'plaintext.txt').read_text());print('Known units:',sum(x['known_units'] for x in rec['rows']),'record slots:',idx,'editorial restorations:',2)

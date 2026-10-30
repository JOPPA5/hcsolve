"""Authoring helper (review 1, Claude Opus 5.5, 2026-10-29): writes the corrected,
completed transcription into work/transcription.json, transcription.txt,
literal-czech.txt and glyph-index.csv. Writes only inside work/."""
from pathlib import Path
from collections import Counter
import json, csv, io
W=Path(__file__).resolve().parent
key=json.loads((W/'key.json').read_text())
ROWS={
'H01':'fh581 b6s 6 b2c2 q6 th6r5 h3qd3n485 bc6mg3 df3y5, y5r3q 3pc6r nm5 f584s5 3p86q48.',
'H02':'cg3t6, q5 d5 m5n3r2 q6 m5 f6cm4f5 qb2c3f6d4? 3tb3f4n t3b4c5n t85 n3qm3cd4 s3 m5y-',
'H03':'th4f5: n6n y4d4 bh4cd4 d1t5m t3 cd6f4d58cg5r3 f5m5sg2 f r3d582 n3m3b382. 3p5tf6n',
'H04':'c m5g384g6 s85m1 f1p3h2, gd5h4 nm5 t2dg84f5 qf32. t32f6n fc6g, q5 c5 f5m5sg2 f1rm2.',
'M01':'b3c486n 6n3hg6, 6p1 ct5848 n5 6m2ms5,',
'M02':'q5 y4 n6n f6cm4f5 h6t 6 6p1 b48m5',
'M03':'q685f68 gf5d4mg2 m6c4 p86q4s4 86cg1.',
'M04':'d4c4s. b3qth6f2 6 t832r1H b2c b3c486',
'M05':'f5sm5 df2y b5b32♡.',
}
NONCIPHER=' ,.-?:♡'
rec=json.loads((W/'transcription.json').read_text())
counts=Counter(); positions=[]; lit_lines=[]; ct_lines=[]
for row in rec['rows']:
    ct=ROWS[row['id']]; lit=''; rk=0
    for off,ch in enumerate(ct,1):
        if ch in key:
            counts[ch]+=1; rk+=1; lit+=key[ch]
            positions.append([str(len(positions)+1),row['id'],str(rk),'1',str(off),ch,key[ch]])
        else:
            assert ch in NONCIPHER, ch; lit+=ch
    row['elements']=[ct]; row['cipher_with_unknown_markers']=ct; row['literal']=lit; row['mapped_units']=rk
    lit_lines.append(row['id']+' '+lit); ct_lines.append(row['id']+' '+ct)
rec['method']+=' Review-1 revision (Claude Opus 5.5, 2026-10-29): postmark spans U01-U05 read through the overprint; four ordinary signs corrected on enlargements (H01 b6s, H02 qb2c3f6d4, M03 gf5d4mg2, M03 p86q4s4). The terminal heart is a drawn non-cipher mark (♡), not a mapped unit.'
rec['resolved_spans']=[dict(s, status='resolved') for s in rec.pop('unknown_spans')]
res={'U01':'b3c (POS-) of b3c486n POSILAM; first sign under heavy postmark dots and c blackened by a dot, shapes fit but partly context-supported','U02':'q685f (ZALEV-) of q685f68 ZALEVAL, legible through dots','U03':'s (C) completing d4c4s TISIC','U04':'b3q (POZ-) of b3qth6f2 POZDRAVU; third sign the 9-like q = Z','U05':'sm (CN) of f5sm5 VECNE','U06':'drawn heart after b5b32 (PEPOU); not a cipher sign; editorial Pepouš rests on sister cards'}
for s in rec['resolved_spans']: s['reading']=res[s['id']]; s.pop('glyph_count',None)
rec['counts']={'physical_rows':9,'mapped_units':sum(counts.values()),'CH_units':counts['H'],'mapped_letters':sum(counts[k]*len(key[k]) for k in counts),'observed_classes':len(counts),'unknown_spans':0,'noncipher_marks':1,'class_counts':dict(sorted(counts.items()))}
rec['marks']=['The postmark is postal overprint over the margin rows; the signs beneath were read through it (U01-U05).','M05 ends with a drawn heart after PEPOU, recorded as non-cipher mark ♡; editorial Pepouš.','H represents the established complete marked CH unit.']
rec['odd_readings']=['H04 t32f6n literally DOUVAM (editorial doufám); a stroke at x-height on the 4th sign may be an F crossbar or a ligature, undecided.','H02 qb2c3f6d4 ZPUSOVATI (colloquial zpusovat, to cover with kisses).','M01 6n3hg6 AMORKA (amorek, Cupid).','H03 n3m3b382 MONOPOLU; hotel not externally identified.']
rec['uncertain_assigned']=[]
(W/'transcription.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
(W/'transcription.txt').write_text('\n'.join(ct_lines)+'\n')
(W/'literal-czech.txt').write_text('\n'.join(lit_lines)+'\n')
buf=io.StringIO(); w=csv.writer(buf,lineterminator='\n')
w.writerow(['global_index','row','row_index','element_index','offset_in_element','class','literal']); w.writerows(positions)
(W/'glyph-index.csv').write_text(buf.getvalue())
print(rec['counts'])

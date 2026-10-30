"""Manual photograph readings; authoring writes only this card's work/. No OCR."""
from pathlib import Path
from collections import Counter
from PIL import Image,ImageDraw
import csv,json,hashlib
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
kp=R/'ciphers/hcp-1520/work/key.json';key=json.loads(kp.read_text());(W/'key.json').write_bytes(kp.read_bytes())
# Strings use the unchanged pre-target family labels. Unknown spans do not stand for one invented glyph.
manual=[
('H01','original',[53,501,978,552],['fh581 t4g 6 b2c2 q6 th6r5 h3qd3n485 bc6mg3 df3y5, y5r3q 3pc6r nm5 f584s5 3p86q48.']),
('H02','original',[50,531,978,583],['cg3t6, q5 d5 m5n3r2 q6 m5 f6cm4f5 q82c3f6d4? 3tb3f4n t3b4c5n t85 n3qm3cd4 s3 m5y-']),
('H03','original',[50,557,979,611],['th4f5: n6n y4d4 bh4cd4 d1t5m t3 cd6f4d58cg5r3 f5m5sg2 f r3d582 n3m3b382. 3p5tf6n']),
('H04','original',[50,585,979,636],['c m5g384g6 s85m1 f1p3h2, gd5h4 nm5 t2dg84f5 qf32. t32f6n fc6g, q5 c5 f5m5sg2 f1rm2.']),
('M01','ccw90',[25,810,493,852],[{'unknown':'U01'},'486n 6n3hg6, 6p1 ct5848 n5 6m2ms5,']),
('M02','ccw90',[25,837,493,878],['q5 y4 n6n f6cm4f5 h6t 6 6p1 b48m5']),
('M03','ccw90',[25,863,493,908],[{'unknown':'U02'},'68 g f5d4mg5 m6c4 p86q4c4 86cg1.']),
('M04','ccw90',[25,889,493,937],['d4c4',{'unknown':'U03'},'. ',{'unknown':'U04'},'th6f2 6 t832r1H b2c b3c486']),
('M05','ccw90',[25,917,306,967],['f5',{'unknown':'U05'},'5 df2y b5b32',{'unknown':'U06'},'.'])]
unknowns=[
{'id':'U01','row':'M01','frame':'ccw90','box':[33,812,89,852],'glyph_count':'unknown','reason':'Postmark interferes with the initial prefix before visible486n. Possible b3c traces are observations, not supplied letters.'},
{'id':'U02','row':'M03','frame':'ccw90','box':[32,860,109,907],'glyph_count':'unknown','reason':'Postmark obscures initial material before the visible68 ending. Expected word completions are not inserted.'},
{'id':'U03','row':'M04','frame':'ccw90','box':[94,890,116,933],'glyph_count':'unknown','reason':'Overprinted ink after d4c4; do not supply a final C from an expected TISIC.'},
{'id':'U04','row':'M04','frame':'ccw90','box':[120,890,167,934],'glyph_count':'unknown','reason':'Postmark crosses the prefix before visible th6f2. Possible b3q traces remain unresolved.'},
{'id':'U05','row':'M05','frame':'ccw90','box':[67,918,122,959],'glyph_count':'unknown','reason':'Postmark masks internal strokes between visible f5 and final5. No h/m or ending is filled from a closing formula.'},
{'id':'U06','row':'M05','frame':'ccw90','box':[266,922,292,958],'glyph_count':'unknown','unit_count_may_be_zero':True,'reason':'Heart-shaped closing ink follows b5b32. No separate certain c/S is read. It may be an ornamental mark with zero additional cipher units, or substitute/merge a character; no S is supplied from a familiar name. It is not asserted to be active ciphertext.'}]
p=Image.open(C/'source/picture.jpg');q=p.transpose(Image.Transpose.ROTATE_90);q.save(W/'picture-ccw.png');frames={'original':p,'ccw90':q};rows=[];pos=[];counts=Counter();known=0
for rid,frame,box,elements in manual:
 lit='';cipher='';rknown=0
 for ei,e in enumerate(elements,1):
  if isinstance(e,dict):mark='<UNK:'+e['unknown']+'>';lit+=mark;cipher+=mark
  else:
   cipher+=e;lit+=''.join(key.get(c,c) for c in e)
   for offset,c in enumerate(e,1):
    if c in key:
     known+=1;rknown+=1;counts[c]+=1;pos.append([known,rid,rknown,ei,offset,c,key[c]])
    else:assert c in ' ,.-?:'
 crop=rid+'.png';frames[frame].crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3),Image.Resampling.NEAREST).save(W/crop)
 rows.append({'id':rid,'frame':frame,'row_box':box,'crop':crop,'elements':elements,'cipher_with_unknown_markers':cipher,'literal':lit,'mapped_units':rknown})
for frame,name in [('original','indexed-original.png'),('ccw90','indexed-margin.png')]:
 im=frames[frame].copy();d=ImageDraw.Draw(im)
 for row in rows:
  if row['frame']==frame:d.rectangle(row['row_box'],outline='red');d.text((row['row_box'][0],row['row_box'][1]-11),row['id'],fill='red')
 for span in unknowns:
  if span['frame']==frame:d.rectangle(span['box'],outline='blue');d.text((span['box'][0],span['box'][1]-10),span['id'],fill='blue')
 im.save(W/name)
record={'method':'Manual source-linked glyph reading, not OCR. H rows use original1024x674; M rows use lossless90CCW674x1024. Whole-row/context boxes may overlap; glyph indices count resolved units only, not absolute original ordinals after unknown-length spans.','source_sha256':{str(p.relative_to(R)):sha(p) for p in sorted((C/'source').iterdir()) if p.is_file()},'rows':rows,'unknown_spans':unknowns,'counts':{'physical_rows':len(rows),'mapped_units':known,'CH_units':counts['H'],'mapped_letters':sum(counts[c]*len(key[c]) for c in counts),'observed_classes':len(counts),'unknown_spans':len(unknowns),'unknown_units':'unknown','original_total':'unknown','class_counts':dict(sorted(counts.items()))},'date_evidence':{'portal_metadata':'1903-02-19','handwritten_diplomatic_preferred':'19./II.1903','certainty':'Roman month remains a visual QA point. The long leading stroke is tentatively a separator, followed byII; metadata is not used to manufacture missing strokes. No proven disagreement or agreement claimed.','postal':'Numerals not securely transcribed; no postal month/date supplied.'},'marks':['The postmark is postal overprint, not cancellation of the handwritten cipher. Affected spans remain active unknown ink.','M05 heart-shaped terminal ink is retained asU06 with uncertain alphabetic status, not treated as a mapped S.','No small-mark accent rule applied. H represents the established complete marked G10/CH unit.'],'odd_readings':['H02 q82c3f6d4 literally zlusovati; no expected verb substituted.','H04 t32f6n literally douvam: source f has a tall loop/descender like other V signs. The supplied shallow-v/F photo control is distinct; no F assignment from expected DOUFAM.','M03 p86q4c4 literally blazisi; small roundc/S is preferred but s/C is a bounded visual alternative at word position6.','M01 6n3hg6 literally amorka; no personal identity inferred.','H03 n3m3b382 literally monopolu; no external hotel identification.'],'uncertain_assigned':[{'row':'M03','word':'p86q4c4','word_unit':6,'preferred_class':'c','preferred_literal':'s','alternative_class':'s','alternative_literal':'c','note':'Small terminal shape is a visual c/s checkpoint; no contextual replacement made.'}]}
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');(W/'transcription.txt').write_text(''.join(r['id']+' '+r['cipher_with_unknown_markers']+'\n' for r in rows));(W/'literal-czech.txt').write_text(''.join(r['id']+' '+r['literal']+'\n' for r in rows))
with (W/'glyph-index.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['global_known_index','row','row_known_index','element_index','offset_in_element','class','literal']);w.writerows(pos)
print((W/'literal-czech.txt').read_text());print(record['counts'])

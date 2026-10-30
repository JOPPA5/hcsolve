"""Manual pixel reading, not OCR. Authoring helper writes only this card's work/."""
from pathlib import Path
from collections import Counter
from PIL import Image,ImageDraw
import json,csv,hashlib
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
# Copy the fixed pre-target key verbatim, without a target-derived assignment.
keypath=R/'ciphers/hcp-1520/work/key.json';key=json.loads(keypath.read_text());(W/'key.json').write_bytes(keypath.read_bytes())
# Unknown entries are active ink spans of unknown original glyph count, not one invented cipher unit.
manual=[
('R01',(27,872,649,909),['bh3n4m, th6r32cg2, q5 t3c2t m53t5c86',{'unknown':'U01'},' yc5n t3b4c. y5cd']),
('R02',(27,894,649,933),['qt5 3t cdh5t1 b6m c4n28g6, cf6',{'unknown':'U02'},' n5r3 ph6dh6, y5n2q']),
('R03',(27,916,649,958),['f bh6qtm1H Hf484H t586n cb385sm',{'unknown':'U03'},'. tm5c f5s5hm4n']),
('R04',(27,939,649,981),['f86g5n 3ty5t5. q4dh6 3t5c82 bc6mg',{'unknown':'U04'},'. d4c4s fh581H, t832r1H']),
('R05',(27,962,649,1003),['b2c cf5 y5t4m5 6m2ms5 q6c486 cd685 fqb3n4m6y4s4 b5b32c.'])]
unknowns=[
{'id':'U01','row':'R01','box':[430,875,443,900],'glyph_count':'unknown','description':'Smudged ink after m53t5c86 / neodesla. Possible 8/L-like lobes, but class and original count not asserted. No contextual ending inserted.'},
{'id':'U02','row':'R02','box':[389,896,422,926],'glyph_count':'unknown','description':'Blotted material after cf6 / sva. Tall-loop ink and dark lower smear cannot be reliably segmented/classified. No G or any new assignment from an expected word.'},
{'id':'U03','row':'R03','box':[405,918,429,950],'glyph_count':'unknown','description':'Smudged terminal material after cb385sm / spolecn, before a separate dot. Exact glyph count and values unresolved.'},
{'id':'U04','row':'R04','box':[389,941,407,970],'glyph_count':'unknown','description':'Smudged terminal material after bc6mg / psank, before a separate dot. Possible 3/O-shaped trace, not counted as a resolved unit.'}]
rows=[];positions=[];counts=Counter();nknown=0
im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90);im.save(W/'upright.png');indexed=im.copy();draw=ImageDraw.Draw(indexed)
for rid,box,elements in manual:
 literal='';cipher='';rowknown=0
 for element_index,element in enumerate(elements,1):
  if isinstance(element,dict):
   marker='<UNK:'+element['unknown']+'>';literal+=marker;cipher+=marker
  else:
   cipher+=element;literal+=''.join(key.get(c,c) for c in element)
   for offset,c in enumerate(element,1):
    if c in key:
     nknown+=1;rowknown+=1;counts[c]+=1
     positions.append([nknown,rid,rowknown,element_index,offset,c,key[c]])
    else:assert c in ' ,.-'
 row={'id':rid,'frame':'picture-ROTATE_90','box':list(box),'elements':elements,'cipher_with_unknown_markers':cipher,'literal':literal,'known_units':rowknown,'crop':rid+'.png'};rows.append(row)
 im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3),Image.Resampling.NEAREST).save(W/row['crop'])
 draw.rectangle(box,outline='red',width=1);draw.text((3,box[1]),rid,fill='red')
for span in unknowns:draw.rectangle(span['box'],outline='blue',width=1);draw.text((span['box'][0],span['box'][1]-10),span['id'],fill='blue')
indexed.save(W/'indexed.png')
record={'method':'Manual source-image transcription. Lossless 90-degree counterclockwise transpose gives674x1024. Row boxes overlap at sloping ascenders/descenders. CSV indexes enumerate resolved units only, not physical whole-card ordinals after unknown spans. Unknown spans are active ink retained as opaque markers and have unknown original glyph counts. No OCR, no automatic cancellation or grammar filling.','source_sha256':{str(p.relative_to(R)):sha(p) for p in sorted((C/'source').iterdir()) if p.is_file()},'rows':rows,'unknown_spans':unknowns,'counts':{'physical_rows':len(rows),'mapped_units':nknown,'CH_units':counts['H'],'mapped_base_letters':sum(counts[c]*len(key[c]) for c in counts),'observed_assigned_classes':len(counts),'unknown_spans':len(unknowns),'unknown_units':'unknown','all_original_units':'unknown','class_counts':dict(sorted(counts.items()))},'marks':['R04 q4dh6 / zitra is underlined; line adds no cipher unit.','H denotes the established marked G10/CH form including its upper stroke, not a grammar-inferred letter or automatic accent restoration.','Smudged spans are retained as active unknown ink, not declared canceled.'],'ordinary':['Picture ordinary date:29.III.1903.','Picture red printed verse beginning V mem srdci pouze jedno prani; ordinary Czech print, not substituted.','Address ordinary handwriting to Anna Ticha, ucitelka v Zirovnici u Pocatek; no cipher.','Address Dopisnice heading, postal stamp and overlapping PRA(G)/Zirovnice-Serowitz postmarks, bottom-left emblem and S.73; no decipherment of unclear postal numerals.'],'reading_notes':['R02 first qt5 literally ZDE: compact q/Z bowl and open hook compared with same-card ZE/ZITRA; g/K in SIMULKA/DRAHOUSKU has a looped descender. Earlier gt5/KDE was a visual class error, not a writer slip.','R02 b6m/pan contrasts b/P with ph6dh6/bratra initial p/B.','R02 c4n28g6 reads simulka without supplied diacritics or verified identity; the named string is not a biographical identification.','R03 marked CH forms in prazdnych and chvilich, two more in R04 vrelych/dlouhych.','R05 6m2ms5 contains the angular s/C before final5/E: anunce, not a supplied letter.','R05 q6c486 / zasila retains I/4; no Y normalisation.']}
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text(''.join(x['id']+' '+x['cipher_with_unknown_markers']+'\n' for x in rows))
(W/'literal.txt').write_text(''.join(x['id']+' '+x['literal']+'\n' for x in rows))
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['global_known_index','row','row_known_index','element_index','offset_in_known_element','shape_label','literal']);w.writerows(positions)
print((W/'literal.txt').read_text());print(record['counts'])

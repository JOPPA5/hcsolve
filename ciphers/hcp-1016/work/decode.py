#!/usr/bin/env python3
"""Decode a manual, coordinate-indexed shape transcript; not image OCR."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
KEY={'SE':'A','S':'B','SW':'C','E':'D','O':'E','W':'F','NE':'G','N':'H','NW':'I','SE.':'K','S.':'L','SW.':'M','E.':'N','O.':'O','W.':'P','NE.':'Q','N.':'R','NW.':'S','I':'T','check':'U','up.':'Z'}
rows=[
 ('1',438,[423,455,490,525,558,594,655,694,724,755,786], 'SW. O NW E. O NW. | S. NW O S O'),
 ('2',486,[363,406,439,465,500,533,563,594,674,705,728,749,778,814,843,871,901], 'N O N. up. NW NE O E. | SW. SE O check NW. SW N O E.'),
 ('3',518,[219,259,282,309,338,399,431,464,532,565,583,614,647,708,739,775,808,841,866,886,917,944,977], 'SE. O. SW. SW. O | NW SW N | O NW E. O E. | SE. N. SE O W I NW NE O. E.'),
 ('4',562,[144,185,214,249,286,316,347,416,449,482,560,595,628,664,697,786,817,850,881,915,947,978], 'NW. SW N S. check SW SE. | check E. E | O NW E. O E. | NW. check O NW. NW. O E.'),
 ('5',606,[110,145,174,205,236,266,294,321,341,359,382,410,443], 'NE check I O E. SE SW N I SE. check NW. NW.'),
 ('signature',613,[641,672,714,756], 'I N O O.'),
]
records=[]
for name,y,xs,s in rows:
 tokens=s.split(); n=0; out=[]
 for t in tokens:
  if t=='|':out.append(' ');continue
  alts=t.split('/'); plain=[KEY[a] for a in alts]
  out.append(plain[0] if len(plain)==1 else '['+'/'.join(plain)+']')
  records.append({'id':f'{name}.{n+1:02}','xy':[xs[n],y],'shape':t,'reading':plain,'box':[xs[n]-14,y-18,xs[n]+14,y+18]});n+=1
 assert n==len(xs),(name,n,len(xs))
 print(name+': '+''.join(out))
print('Date-like small marks between final text and signature: provisionally ordinary 1898, not included in Pigpen inventory.')
print('Symbols:',len(records),'(manual inventory; see opening-audit.md for resolved alternatives)')
for p in sorted((ROOT/'source').iterdir()):
 if p.is_file():print('SHA256',p.name,hashlib.sha256(p.read_bytes()).hexdigest())
if '--write-transcript' in __import__('sys').argv:
 (HERE/'transcript.json').write_text(json.dumps({'coordinate_system':'Original picture.jpg 1024 x 678, pixel x/y from upper left; boxes approximate, inspect original.','rows':records},indent=2)+'\n')

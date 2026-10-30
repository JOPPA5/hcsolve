"""Partial Pigpen reading from a manually segmented, hashed source inventory; not OCR."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
j=json.loads((P/'inventory.json').read_text())
for name,sha in j['source_sha256'].items():
 assert hashlib.sha256((P.parent/'source'/name).read_bytes()).hexdigest()==sha,name
# Classes as originally transcribed in the90CCW crop; read in reverse sequence
# and rotate each glyph180, yielding the ordinary pair-filled German key.
key={'BR':'R','BR.':'S','LBR':'P','LBR.':'Q','BL':'N','BL.':'O',
'TBR':'L','TBR.':'M','box':'I','box.':'K','TBL':'G','TBL.':'H',
'TR':'E','TR.':'F','TLR':'C','TLR.':'D','TL':'A','TL.':'B',
'up':'T','up.':'U','left':'V','left.':'W','right':'X','right.':'Y',
'down':'Z','down.':'[nonstandard dotted Z-shaped wedge]','I':'[detached stroke]'}
for row in ['second','upper']:
 records=[r for r in j['records'] if r['id'].startswith(row+'.')]
 print(row+':',''.join(key[r['shape']] for r in reversed(records)))
print('Margin, separate90-degree orientation: GE [three unresolved forms]; canceled hatch excluded.')
print('18 leading alphabetic positions supported: HASTDUDICHGUTAMMUS.')
print('40 provisional graphic units =32 body forms +3 detached strokes +5 margin forms.')
print('Not a full decipherment. Crossed/overprinted shape B remains provisional.')
for name,sha in j['source_sha256'].items():print('SHA256',name,sha)

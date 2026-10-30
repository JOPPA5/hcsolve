"""Bounded root-QA source-pixel comparison, not a contextual plaintext repair."""
from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json
W=Path(__file__).resolve().parent;C=W.parent
im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
items=[('R02-first','R02 first glyph in ?DE',[38,898,64,932]),('R01-ZE','R01 q/Z in ZE',[248,876,285,913]),('R04-ZITRA','R04 q/Z in ZITRA',[187,942,227,978]),('R02-SIMULKA','R02 g/K in SIMULKA',[304,898,338,934]),('R01-DRAHOUSKU','R01 g/K in DRAHOUSKU',[214,875,253,914])]
out=Image.new('RGB',(len(items)*280,340),'white');d=ImageDraw.Draw(out)
for i,(name,label,b) in enumerate(items):
 d.text((i*280+3,4),label,fill='black');z=im.crop(b).resize(((b[2]-b[0])*7,(b[3]-b[1])*7),Image.Resampling.NEAREST);out.paste(z,(i*280+3,26));z.save(W/('qg-'+name+'.png'))
out.save(W/'qg-root-control.png')
(W/'qg-root-control.json').write_text(json.dumps({'source':'source/picture.jpg','sha256':hashlib.sha256((C/'source/picture.jpg').read_bytes()).hexdigest(),'transform':'lossless90CCW;native674x1024;display7xnearestneighbour','panels':[{'id':n,'label':l,'box':b,'file':'qg-'+n+'.png'} for n,l,b in items]},indent=2)+'\n')

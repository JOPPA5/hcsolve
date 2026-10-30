"""Source-derived crop index for manual review; writes only work/."""
from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json
W=Path(__file__).resolve().parent;C=W.parent
im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
items=[
('U01','R01 smeared ending after neodesla',(407,872,449,905)),
('U02','R02 tall loop and blot after sva',(369,891,433,929)),
('U03','R03 smeared ending after spolecn',(385,914,439,955)),
('U04','R04 smeared ending after psank',(368,937,420,976)),
('b-p','R02 pan/simulka then meho bratra: b/P vs p/B',(190,892,566,934)),
('t-d','R04 odjede / underlined zitra: crossed t/D vs looped d/T',(108,937,306,978)),
('m-n-I-Y','R03 prazdnych / chvilich / delam: m/n,1/Y,4/I,CH',(51,914,330,959)),
('small-C','R05 jedine anunce / zasila: angular s/C and4/I',(103,961,347,1002)),
('closing','R05 stale vzpominajici pepous',(349,960,649,1003))]
out=Image.new('RGB',(1600,len(items)*240),'white');d=ImageDraw.Draw(out)
for i,(nm,label,b) in enumerate(items):
 d.text((5,i*240+4),label,fill='black');z=im.crop(b).resize(((b[2]-b[0])*4,(b[3]-b[1])*4),Image.Resampling.NEAREST);z.save(W/('control-'+nm+'.png'));out.paste(z,(5,i*240+24))
out.save(W/'controls.png')
(W/'controls.json').write_text(json.dumps({'source':'source/picture.jpg','source_sha256':hashlib.sha256((C/'source/picture.jpg').read_bytes()).hexdigest(),'frame':'lossless ROTATE_90,674x1024; boxes are context crops not claimed individual segmentation','display':'uniform4x nearest-neighbour, no denoising','items':[{'id':nm,'description':label,'box':list(b),'file':'control-'+nm+'.png'} for nm,label,b in items]},indent=2)+'\n')

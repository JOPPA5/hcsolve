"""Same-card source controls; boxes are original or explicitly upright-left coordinates."""
from pathlib import Path
import json
from PIL import Image,ImageDraw
W=Path(__file__).resolve().parent;C=W.parent
im=Image.open(C/'source/picture.jpg');left=im.crop((31,167,346,514)).rotate(-90,expand=True)
panels={
 'A3-A4-source-controls':[
 ('Target B02: b/P first, m/N third selected by same-card controls','original',[341,535,400,568]),
 ('B02 DAMAM: t/D then n/M controls','original',[536,535,621,572]),
 ('B01 PONEVADZ opening: b/P','original',[105,509,231,547]),
 ('T02 PREPSATI opening: b/P (also second b/P)','original',[43,50,146,88]),
 ('B02 ZNAM: m/N second, n/M fourth','original',[41,536,117,569]),
 ('B02 MODERNICH: n/M first, m/N sixth','original',[239,533,346,572]),
 ('B05 MNOU: n/M first, m/N second','original',[72,612,138,639]),
 ],
 'A1-source-controls':[
 ('Target L09 ZA[R|H]MOUCENEHO: overink prefix','left-upright',[101,237,294,276]),
 ('L09 SVEHO: r/H fourth; same row immediately before target','left-upright',[12,237,106,275]),
 ('L10 KTERY: h/R fourth','left-upright',[15,268,92,305]),
 ('L10 VRELOU: h/R second','left-upright',[189,272,266,310]),
 ('L04 PREJI: h/R second','left-upright',[140,86,198,123]),
 ('T05 DRAHA: h/R second versus r/H fourth','original',[202,125,289,163]),
 ]}
manifest={}
for name,items in panels.items():
 canvas=Image.new('RGB',(1260,len(items)*225),'white');d=ImageDraw.Draw(canvas)
 for i,(label,view,box) in enumerate(items):
  src=im if view=='original' else left;x=src.crop(box);x=x.resize((x.width*5,x.height*5),resample=Image.Resampling.NEAREST)
  canvas.paste(x,(12,i*225+28));d.text((12,i*225+8),label+f'; {view} box {box}',fill='black')
 canvas.save(W/(name+'.png'));manifest[name]=[{'label':a,'coordinate_view':b,'box':c,'scale':5,'resampling':'nearest'} for a,b,c in items]
(W/'source-control-boxes.json').write_text(json.dumps({'source':'../source/picture.jpg','left_upright':{'original_crop':[31,167,346,514],'rotation_clockwise':90},'panels':manifest},indent=2)+'\n')

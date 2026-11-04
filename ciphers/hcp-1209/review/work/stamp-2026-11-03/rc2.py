import sys
from PIL import Image, ImageOps, ImageChops
im=Image.open(sys.argv[1]).convert('RGB'); out=sys.argv[2]
x0,y0,x1,y1=[int(v) for v in sys.argv[3:7]]; name=sys.argv[7]; s=int(sys.argv[8])
c=im.crop((x0,y0,x1,y1)); r,g,b=c.split()
# ink green vs triangle blue-green: try several
outs={'r':r,'g':g,'b':b,'bmr':ImageChops.subtract(b,r),'gmb':ImageChops.subtract(g,b),'rmb':ImageChops.subtract(r,b)}
tiles=[]
for k,v in outs.items():
    v=ImageOps.autocontrast(v,cutoff=1).resize((c.width*s,c.height*s),Image.LANCZOS); tiles.append(v)
W=tiles[0].width; H=tiles[0].height
sheet=Image.new('L',(W,H*len(tiles)+5*len(tiles)),255)
for i,t in enumerate(tiles): sheet.paste(t,(0,i*(H+5)))
sheet.save(out+'/'+name+'.png')

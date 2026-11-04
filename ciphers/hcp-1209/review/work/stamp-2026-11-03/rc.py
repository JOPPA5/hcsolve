import sys
from PIL import Image, ImageOps, ImageChops
im=Image.open(sys.argv[1]).convert('RGB')
out=sys.argv[2]
def save(box,name,s,mode='rgb'):
    c=im.crop(box)
    if mode=='r': c=ImageOps.autocontrast(c.split()[0],cutoff=1)
    elif mode=='b': c=ImageOps.autocontrast(c.split()[2],cutoff=1)
    elif mode=='gmr':
        r,g,b=c.split(); c=ImageOps.autocontrast(ImageChops.subtract(r,g),cutoff=1)
    else: c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(out+'/'+name+'.png')
save((2720,160,3220,720),'box',2)
save((2720,160,3220,720),'box_r',2,'r')
rows=[('r1',230,330),('r2',310,410),('r3',380,480),('r4',450,560),('r5',530,640),('r6',600,700)]
for n,y0,y1 in rows:
    for m in ['rgb','r','gmr']:
        save((2780,y0,3150,y1),n+'_'+m,4 if m!='rgb' else 4,m)

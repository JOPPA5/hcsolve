# Side-by-side crops of the message block of each Wooster card, from the un-converted originals.
import glob,sys
from PIL import Image, ImageOps
for n,y0,y1 in [('1338',370,990),('1337',400,950),('1336',400,960),('1335',400,890),('1334',400,960),('1322',360,880)]:
    f=glob.glob(f'hcp-{n}/work/hires/*adr*')[0]
    im=Image.open(f).convert('RGB'); s=im.width/1014
    W,H=im.size
    print(n,im.size)
    c=im.crop((int(60*s),int(y0/1.76*s),int(520*s),int(y1/1.76*s)))
    c=ImageOps.autocontrast(c,cutoff=1).resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f'hcp-1339/work/crops/sister{n}.png')

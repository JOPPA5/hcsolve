"""Revision 2026-11-02: comparison crops of the writer's plain hand on sisters (read only). Run from ciphers/ with a Python that has PIL."""
from PIL import Image, ImageOps
import glob
def c(card,side_box,name,s=3):
    f=glob.glob(f'hcp-{card}/work/hires/*adr.jpg')[0]; im=Image.open(f).convert('RGB'); W=im.width/1024
    b=tuple(int(x*W) for x in side_box); r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
    ImageOps.autocontrast(r.split()[1],cutoff=.5).save(f'hcp-1272/work/crops2/{name}.png')
c(1245,(835,45,970,195),'s1245')

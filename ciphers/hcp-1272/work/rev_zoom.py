"""Revision 2026-11-02: high zoom of named stamp-note regions. Run from ciphers/hcp-1272 with a Python that has PIL."""
from PIL import Image, ImageOps, ImageChops, ImageFilter
im = Image.open('work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
G=im.split()[1]
d=ImageOps.invert(ImageOps.autocontrast(ImageChops.subtract(G.filter(ImageFilter.GaussianBlur(25)),G),cutoff=.3))
def z(n,b,s=8):
    d.crop(b).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS).save(f'work/crops2/z_{n}.png')
    r=im.crop(b).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS); r.save(f'work/crops2/z_{n}_c.png')
z('end',(2900,590,3040,740),7)
z('mid',(2740,620,2920,720),8)
z('left',(2640,620,2790,750),7)
z('last',(2780,690,3010,770),7)

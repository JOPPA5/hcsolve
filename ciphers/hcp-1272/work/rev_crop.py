"""Revision 2026-11-02: stamp-note crops. Run from ciphers/hcp-1272 with a Python that has PIL."""
from PIL import Image, ImageOps, ImageChops, ImageFilter
import sys
im = Image.open('work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
def c(name, box, s=4):
    r=im.crop(box); w,h=r.size
    r=r.resize((w*s,h*s),Image.LANCZOS)
    R,G,B=r.split()
    # plain
    r.save(f'work/crops2/{name}_rgb.png')
    ImageOps.autocontrast(G,cutoff=0.5).save(f'work/crops2/{name}_G.png')
    ImageOps.autocontrast(B,cutoff=0.5).save(f'work/crops2/{name}_B.png')
    # R-G: ink redness; the writing red ink vs pink smear
    d=ImageChops.subtract(G.filter(ImageFilter.GaussianBlur(25*s/4)),G)
    ImageOps.invert(ImageOps.autocontrast(d,cutoff=0.5)).save(f'work/crops2/{name}_loc.png')
c('full',(2680,260,3130,800),2)
c('l1',(2700,560,3120,650),4)
c('l2',(2700,630,3120,710),4)
c('l3',(2700,690,3120,770),4)
# wider to the left; second pass
c('w',(2560,520,3100,790),3)
c('a',(2580,600,2860,780),6)
c('b',(2800,600,3060,780),6)
# ink-vs-wash separation: project out the pink wash
import numpy as np
def sep(name,box,s=6):
    a=np.asarray(im.crop(box).resize(((box[2]-box[0])*s,(box[3]-box[1])*s),Image.LANCZOS)).astype(float)
    # darkness in each channel relative to local background
    from PIL import Image as I
    out={}
    for i,ch in enumerate('RGB'):
        p=I.fromarray(a[:,:,i].astype('uint8')); bg=np.asarray(p.filter(ImageFilter.GaussianBlur(30))).astype(float)
        out[ch]=bg-a[:,:,i]
    # red channel: wash barely absorbs red, ink somewhat; blue contains purple overprint
    for ch in out:
        v=np.clip(out[ch],0,None); v=255-255*v/np.percentile(v,99.7); I.fromarray(np.clip(v,0,255).astype('uint8')).save(f'work/crops2/{name}_d{ch}.png')
    m=(out['G']+out['R']*1.5+out['B']*0.5); v=np.clip(m,0,None); v=255-255*v/np.percentile(v,99.7); I.fromarray(np.clip(v,0,255).astype('uint8')).save(f'work/crops2/{name}_mix.png')
sep('a',(2580,620,2860,780),6)
sep('b',(2800,620,3060,780),6)

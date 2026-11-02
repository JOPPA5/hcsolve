"""Revision 2026-11-02: row 17 crops (green channel). Run from ciphers/hcp-1272 with a Python that has PIL."""
from PIL import Image, ImageOps
im = Image.open('work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
b=(60,1940,1000,2050)
r=im.crop(b); r=ImageOps.autocontrast(r.split()[1],cutoff=.3); r.resize((r.width*2,r.height*2),Image.LANCZOS).save('work/crops2/r17.png')
b=(380,1950,800,2045)
r=im.crop(b); r=ImageOps.autocontrast(r.split()[1],cutoff=.3); r.resize((r.width*4,r.height*4),Image.LANCZOS).save('work/crops2/r17z.png')

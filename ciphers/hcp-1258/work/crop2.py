"""Round-2 crops. Args: name,x0,y0,x1,y1,scale[,r]. Output: work/crops2/."""
import sys, os
from PIL import Image, ImageEnhance, ImageOps
here = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(here, 'hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-70_adr.jpg')).convert('RGB')
for spec in sys.argv[1:]:
    p = spec.split(','); n = p[0]; x0, y0, x1, y1 = map(int, p[1:5]); s = float(p[5])
    c = im.crop((x0, y0, x1, y1))
    if len(p) > 6: c = ImageOps.autocontrast(c.split()[0], cutoff=1)
    else: c = ImageEnhance.Contrast(c).enhance(1.6)
    c.resize((int(c.width*s), int(c.height*s)), Image.LANCZOS).save(os.path.join(here, 'crops2', n + '.png'))

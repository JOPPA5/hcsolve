# saturation-boosted colour view
import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def strip(name,x0,y0,x1,y1,s=3):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
    r=ImageEnhance.Color(r).enhance(2.2); r=ImageEnhance.Contrast(r).enhance(1.9); r=ImageEnhance.Brightness(r).enhance(1.1)
    r.save('rev2/%s.png'%name)
a=sys.argv[1:]
for i in range(0,len(a),6): strip(a[i],*map(int,a[i+1:i+6]))

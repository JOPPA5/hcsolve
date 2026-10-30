from PIL import Image, ImageEnhance
import os
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1319/'
im=Image.open(D+'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=3445/1024
# (row, y0,y1 in large coordinates)
rows=[(1,32,72),(2,68,110),(3,100,142),(4,134,178),(5,168,212),(6,202,246),(7,240,282),(8,276,322),(9,310,356),(10,345,392),(11,388,432),(12,415,452),(13,448,492),(14,488,525)]
for r,a,b in rows:
    for i,(x0,x1) in enumerate([(20,175),(165,320),(305,460)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c=ImageEnhance.Contrast(c).enhance(1.5)
        c.save(D+f'review/work/crops/r{r:02d}_{i}.png')

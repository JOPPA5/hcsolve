import sys
from PIL import Image
im=Image.open('hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=1.72
rows=[(70,135),(130,215),(200,265),(265,335),(335,420),(425,500),(490,560),(565,640),(625,700),(680,750),(765,840),(825,880),(875,950),(960,1020)]
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(50,350),(330,630),(600,890)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/r{i:02d}_{j}.png')
c=im.crop((2650,200,3250,750)).rotate(0); c.resize((c.width*2,c.height*2)).save('crops/stamp.png')
c.rotate(90,expand=True).resize((c.height*2,c.width*2)).save('crops/stamp_rot.png')

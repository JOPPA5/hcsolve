import sys
from PIL import Image
im=Image.open('hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg')
# rows in 2000-scale y ranges, overlapping
rows=[(50,115),(120,195),(205,270),(280,345),(345,420),(425,490),(490,560),(565,635),(630,720),(680,750),(760,830),(820,905),(905,965),(950,1030),(1030,1110),(1090,1200)]
f=1.72
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(70,640),(600,1170)]):
        c=im.crop((int(x0*f),int(a*f),int(x1*f),int(b*f)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/r{i:02d}{"ab"[j]}.png')
c=im.crop((int(1630*f),int(90*f),int(1900*f),int(380*f)));c=c.resize((c.width*3//2,c.height*3//2)); c.save('crops/stamp.png')

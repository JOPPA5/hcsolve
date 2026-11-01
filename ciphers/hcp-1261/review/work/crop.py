import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07_adr.jpg').convert('RGB')
# name,x0,y0,x1,y1(hires px)[,rot][,k]
for a in sys.argv[1:]:
    p=a.split(',');n=p[0];b=list(map(int,p[1:5]));r=int(p[5]) if len(p)>5 else 0;k=int(p[6]) if len(p)>6 else 2
    c=im.crop(b)
    if r:c=c.rotate(r,expand=True)
    c=c.resize((c.width*k,c.height*k),Image.LANCZOS);c.save('crops/%s.png'%n)

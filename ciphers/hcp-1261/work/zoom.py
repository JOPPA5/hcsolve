import sys
from PIL import Image
im=Image.open('hires/cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07_adr.jpg').convert('RGB')
S=3445/1024
# name x0 y0 x1 y1 (large coords) rot
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,*r=a.split(',')
    c=im.crop((int(int(x0)*S),int(int(y0)*S),int(int(x1)*S),int(int(y1)*S)))
    if r: c=c.rotate(int(r[0]),expand=True)
    k=min(int(__import__("os").environ.get("K","3")),1900//c.width)
    k=max(k,1)
    c=c.resize((c.width*k,c.height*k),Image.LANCZOS); c.save(f'crops/{n}.png')

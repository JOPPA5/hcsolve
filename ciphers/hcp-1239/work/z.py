import sys
from PIL import Image
im=Image.open('hires/cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105_adr.jpg').convert('RGB')
S=1.72
# name,x0,y0,x1,y1 display coords, zoom
J=[l.split() for l in open(sys.argv[1]) if l.strip()]
for n,a,b,c,d,z in J:
    a,b,c,d,z=[float(v) for v in (a,b,c,d,z)]
    k=im.crop((int(a*S),int(b*S),int(c*S),int(d*S)))
    k.resize((int(k.width*z),int(k.height*z)),Image.LANCZOS).save(f'z/{n}.png')

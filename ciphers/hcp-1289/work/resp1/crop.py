import sys
from PIL import Image
im=Image.open('work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg').convert('RGB')
for spec in sys.argv[1:]:
    n,a,b,c,d,s=spec.split(',')
    a,b,c,d,s=map(int,(a,b,c,d,s))
    x=im.crop((a,b,c,d));x.resize((x.width*s,x.height*s),Image.LANCZOS).save(f'work/resp1/{n}.png')
print(im.size)

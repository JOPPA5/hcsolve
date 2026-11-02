from PIL import Image
import sys,os
d=os.path.dirname(os.path.abspath(__file__))+'/'
im=Image.open(d+'hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_adr.jpg').convert('RGB')
s=1.72
a=sys.argv[1:]
c=im.crop((int(int(a[1])*s),int(int(a[2])*s),int(int(a[3])*s),int(int(a[4])*s)));z=int(a[5]);c=c.resize((c.width*z,c.height*z),Image.LANCZOS);c.save(d+f'crops/{a[0]}.png')

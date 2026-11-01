from PIL import Image,ImageOps
import sys
im=Image.open('work/hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr.jpg').convert('RGB')
for spec in sys.argv[1:]:
    n,a,b,c,d,z=spec.split(',')
    t=im.crop((int(a),int(b),int(c),int(d)));z=float(z)
    t=t.resize((int(t.width*z),int(t.height*z)),Image.BICUBIC);t=ImageOps.autocontrast(t,cutoff=0.5);t.save(f'review/work/crops/{n}.png')

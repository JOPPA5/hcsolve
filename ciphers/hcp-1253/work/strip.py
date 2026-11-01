from PIL import Image,ImageOps
im=Image.open('hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg').convert('L')
im=im.rotate(-4,resample=Image.BICUBIC,center=(0,0),fillcolor=200)
f=1.7225
import sys
# windows of three-row height, 3 horizontal panels
ys=[(330,470),(450,590),(570,710),(690,830),(810,950),(930,1070),(1050,1190),(1170,1310)]
xs=[(40,350),(330,640),(620,930)]
for i,(a,b) in enumerate(ys):
  for j,(c,d) in enumerate(xs):
    r=im.crop((int(c*f),int(a*f),int(d*f),int(b*f)))
    r=ImageOps.autocontrast(r,cutoff=1)
    r=r.resize((r.width*3,r.height*3),Image.LANCZOS)
    r.save(f'crops/v{i}{j}.png')

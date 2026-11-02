import sys
from PIL import Image,ImageOps
f=sys.argv[7] if len(sys.argv)>7 else 'adr'
im=Image.open('work/hires/cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38_%s.jpg'%f).convert('RGB')
x0,y0,x1,y1=map(int,sys.argv[1:5]);s=float(sys.argv[5])
c=im.crop((x0,y0,x1,y1));c=ImageOps.autocontrast(c,cutoff=1).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS)
c.save('review/work/'+sys.argv[6]+'.png')

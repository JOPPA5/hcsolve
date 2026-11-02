import sys
from PIL import Image,ImageOps
im=Image.open('hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg').convert('RGB')
x0,y0,x1,y1,n=map(int,sys.argv[1:6]);o=sys.argv[6]
c=im.crop((x0,y0,x1,y1));c=c.resize((c.width*n,c.height*n),Image.LANCZOS);ImageOps.autocontrast(c,cutoff=1).save('crops/'+o)

import sys
from PIL import Image
side,x0,y0,x1,y1,s,out=sys.argv[1:8]
x0,y0,x1,y1=map(int,(x0,y0,x1,y1));s=float(s)
im=Image.open(f'work/hires/cpc_1916-05-04_HU_Mezokovesd_HU_Szomolya_szomolya-33_{side}.jpg')
if len(sys.argv)>8: im=im.rotate(int(sys.argv[8]),expand=True)
c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('review/work/'+out)

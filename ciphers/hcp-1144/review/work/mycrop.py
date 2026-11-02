import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1144/work/hires/cpc_1916-05-19_HU_Mezokovesd_HU_Szomolya_szomolya-36_adr.jpg').convert('RGB')
for a in sys.argv[1:]:
    p=a.split(','); n=p[0]; x0,y0,x1,y1=map(int,p[1:5]); s=float(p[5]) if len(p)>5 else 1
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1144/review/work/crops/%s.png'%n)

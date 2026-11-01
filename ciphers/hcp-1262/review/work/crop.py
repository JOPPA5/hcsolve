import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1262/work/hires/cpc_1912--15_HU__HU_Jasz-Arokszalas_jolanka-100_adr.jpg').convert('RGB')
print(im.size)
# args: name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
    c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1262/review/work/crops/%s.png'%n)

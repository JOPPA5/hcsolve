import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/work/hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
print(im.size)
W=im.size[0]
s=W/1024  # coords in the 1024 px large view
rows=[(20,62),(62,105),(105,150),(145,190),(185,225),(222,268),(258,303),(295,335),(330,372),(372,412),(410,452),(450,495),(492,535),(530,572),(565,612)]
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(20,240),(225,450)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/review/work/crops/r{i:02d}{"ab"[j]}.png')
c=im.crop((int(810*s),int(80*s),int(945*s),int(240*s))).rotate(180); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/review/work/crops/stamp.png')
print(c.size)

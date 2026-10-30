from PIL import Image, ImageEnhance
import sys
p='ciphers/hcp-1294/work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg'
im=Image.open(p).convert('RGB')
S=3445/1024
rows={1:(15,60),2:(50,95),3:(85,130),4:(120,165),5:(160,205),6:(190,232),7:(228,272),8:(262,305),9:(298,342),10:(330,372),11:(362,405),12:(395,438),13:(428,470),14:(462,510),15:(510,550)}
for r,(a,b) in rows.items():
    for i,(x0,x1) in enumerate([(25,180),(165,320),(305,490)]):
        c=im.crop((int(x0*S),int(a*S),int(x1*S),int(b*S)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save('ciphers/hcp-1294/review/work/crops/r%02d_%d.png'%(r,i))

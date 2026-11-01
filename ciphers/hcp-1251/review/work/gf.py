from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1251/work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
C='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1251/review/work/c/'
def f(n,b,s):
    a=np.asarray(im.crop(b)).astype(float)
    d=a[...,1]-a[...,0]  # green minus red: paper negative, green ink positive, black ~0
    g=np.clip((d+45)/90,0,1)
    Image.fromarray((255*(1-g)).astype('uint8')).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS).save(C+n+'.png')
f('g4',(1440,280,1860,470),4)
f('g3',(1440,190,1860,360),4)
# k / g comparison
crops={'kivanok':(1130,640,1290,760),'kivanok_b':(1000,690,1300,800),'fogok':(2890,1880,3200,1980),'tartsak':(2800,1950,3120,2030),'draga_g':(1040,1290,1180,1420)}
for k,b in crops.items(): im.crop(b).resize(((b[2]-b[0])*4,(b[3]-b[1])*4),Image.LANCZOS).save(C+'k_'+k+'.png')

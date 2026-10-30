from PIL import Image
import sys
im=Image.open('hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(name,x0,y0,x1,y1,z=2):
    b=[int(v*s) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%name)
# main block in bands
bands=[(40,100,'a'),(90,180,'a2')]
c('r01_03',50,40,860,270);c('r04_06',50,260,890,450);c('r07_10',50,440,890,680)
c('r11_13',50,670,890,880);c('r14_15',50,870,920,1010);c('r16',50,960,1000,1060);c('r16b',850,960,1920,1060)
c('r17',50,1050,1000,1130);c('r17b',850,1040,1920,1130);c('r18',50,1110,1000,1220);c('r18b',850,1100,1920,1220)
c('stamp',1520,60,1810,380,3);c('edge',1750,960,1920,1190,3)

import sys
from PIL import Image
im=Image.open('hires/cpc_1912-07-07_HU__HU_Jasz-Arokszalas_jolanka-29_adr.jpg')
s=1.72
def c(n,x0,y0,x1,y1,z):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save('crops/'+n+'.png')
import os; os.makedirs('crops',exist_ok=True)
y=[(50,180),(150,290),(260,400),(380,510),(490,620),(600,730),(710,850),(830,960),(940,1070)]
for i,(a,b) in enumerate(y): c('a%d'%i,40,a,420,b,2.9); c('b%d'%i,400,a,830,b,2.6)
c('low1',40,1040,520,1240,2.3); c('low2',500,1040,1000,1240,2.3); c('low3',960,1070,1480,1240,2.2); c('low4',1460,1070,1920,1240,2.4)
c('stamp',1450,150,1720,390,4)

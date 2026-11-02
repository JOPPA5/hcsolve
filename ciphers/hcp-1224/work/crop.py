import sys
from PIL import Image
im=Image.open('hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_adr.jpg').convert('RGB')
def c(n,b,s):
    r=im.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save('crops/%s.png'%n)
y=70
# strips of ~ 3 rows, 
i=0
for y0 in range(70,2100,165):
    c('L%02d'%i,(60,y0,860,y0+185),2.4); c('R%02d'%i,(800,y0,1660,y0+185),2.4); i+=1
c('stamp',(2640,130,3080,630),3)
c('bottomR',(1500,1950,3200,2090),1.5)
print(i)

import sys
from PIL import Image
im=Image.open('hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
def c(n,b,s=3):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
# left block by rows: 6 strips, each two halves
y=60;h=350;i=0
while y<2100:
    for j,(x0,x1) in enumerate([(50,800),(750,1560)]):
        c(f's{i:02d}{"ab"[j]}',(x0,y,x1,y+h),2)
    y+=330;i+=1
c('stamp',(2600,200,3250,780),3)
c('lowR',(1500,1760,2500,2110),2)
c('lowR2',(2450,1760,3320,2110),2)
c('edge',(3180,1300,3330,2110),2)

from PIL import Image
import sys
im=Image.open('hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=2):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
ys=[60,300,540,780,1020,1260,1500,1740,1950]
for i in range(len(ys)-1):
    y0,y1=ys[i],ys[i+1]+40
    c(f'L{i}',(70,y0,860,y1)); c(f'R{i}',(780,y0,1570,y1))
c('stamp',(2700,120,3120,560),3)
c('bot1',(1500,1880,3250,2090),2)

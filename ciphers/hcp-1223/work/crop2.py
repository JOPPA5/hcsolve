from PIL import Image
im=Image.open('hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=3):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
x=100
for i in range(5):
    c(f'B{i}',(x+i*640,1880,x+i*640+700,2100))
c('r19',(90,1780,800,1900))
c('r8',(90,780,800,880))
c('r9',(90,860,1560,1000),2)
c('stamp2',(2740,270,3110,540),4)

from PIL import Image
im=Image.open('../../work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=2):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
# bands of ~4 rows, left and right halves
y=[50,330,610,900,1180,1470,1760,2110]
for i in range(len(y)-1):
    c(f'bL{i}',(60,y[i],830,y[i+1]+30))
    c(f'bR{i}',(780,y[i],1560,y[i+1]+30))
c('bot1',(1450,1890,2400,2100))
c('bot2',(2350,1890,3250,2100))
c('stamp',(2650,100,3150,520))

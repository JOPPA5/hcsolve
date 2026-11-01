from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
k=0.0
# bottom rows on unsheared: x ranges
def c(n,box,sc=2.4):
    x=im.crop(box); x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=1).save('crops/'+n)
c('bot1.png',(1500,1740,2300,2090))
c('bot2.png',(2250,1740,3050,2090))
c('bot3.png',(2900,1740,3340,2090))
c('stamp1.png',(2750,190,3320,450),2.8)
c('stamp2.png',(2750,430,3320,700),2.8)
c('edge.png',(3100,350,3340,1700),1.4)

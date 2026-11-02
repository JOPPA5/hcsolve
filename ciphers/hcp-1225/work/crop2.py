from PIL import Image
im=Image.open('hires/cpc_1912-02-29_HU__HU_Jasz-Arokszalas_jolanka-06_adr.jpg')
def c(n,b,s=3):
    x=im.crop(b); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/'+n+'.png')
c('stamp',(2760,40,3360,620),2)
c('addr1',(1800,80,2800,560),2)
c('addr2',(1600,620,3400,1750),1)
# row 4: y approx 150*3.365
c('r4',(780,420,1500,560),3)
c('r5',(1000,520,1700,660),3)
c('r6',(40,640,1000,800),2)
c('r7',(40,760,1000,900),2)
c('r12',(100,1370,800,1520),3)
c('r15',(60,1740,700,1900),3)
c('r16',(1200,1810,1800,1980),3)
c('r14',(780,1590,1350,1760),3)

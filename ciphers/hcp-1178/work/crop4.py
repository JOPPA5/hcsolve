from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=3):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s))).resize((int((x1-x0)*s*z),int((y1-y0)*s*z)),Image.LANCZOS)
    r=ImageEnhance.Contrast(r).enhance(1.8); r.save('crops/%s.png'%n)
c('t1n',495,10,730,48,2.5)
c('t2n',720,10,955,48,2.5)
c('v3',20,415,240,470,2.5)
c('v4',240,405,500,470,2.5)
c('g1',20,100,260,145,2.5)
c('g2',230,70,500,135,2.5)
c('g3',20,180,250,225,2.5)
c('g4',240,170,470,225,2.5)
c('i1',110,590,330,622,3.5)
c('dig1',110,560,300,600,4)
c('dig2',290,560,500,600,4)

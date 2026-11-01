from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
W,H=im.size; print(W,H)
s=W/1024
def c(n,x0,y0,x1,y1,z=2):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r=ImageEnhance.Contrast(r).enhance(1.5); r.save('crops/%s.png'%n); print(n,r.size)
c('bottom',100,555,960,620,2)
c('codeA',110,555,500,600,3)
c('l1',10,30,500,200,1)
c('l2',10,190,500,340,1)
c('l3',10,330,500,480,1)
c('l4',10,470,500,625,1)
c('topr',480,10,960,270,1)
c('addr',470,260,960,625,1)

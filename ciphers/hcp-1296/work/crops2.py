from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-06-11_HU__HU_Jasz-Arokszalas_jolanka-25_adr.jpg').convert('RGB')
p=Image.open('hires/cpc_1912-06-11_HU__HU_Jasz-Arokszalas_jolanka-25_pic.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,b,z=1.0,rot=0,src=im):
    x=src.crop(tuple(int(v*s) for v in b))
    if rot: x=x.rotate(rot,expand=True)
    x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS); x.save('crops/'+n+'.png')
c('j1',(20,340,240,372),2.2)   # mi ujsag
c('j2',(20,445,240,478),2.2)   # it ninos
c('j3',(20,575,300,610),1.8)   # fele tisztelem
c('j4',(400,60,470,300),3,-90)  # right part of side note
c('j5',(460,60,640,250),2.5)   # left postmark
c('j6',(720,60,920,260),2)     # right postmark
c('j7',(470,590,870,612),1.8)
c('j8',(440,555,970,590),1.3)
# contrast-boosted picture side
g=ImageOps.autocontrast(p.convert('L'),cutoff=1); g=ImageOps.equalize(g); g.resize((1400,898)).save('crops/pic_eq.png')

from PIL import Image, ImageOps
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
def c(n,b,z=3,red=False):
    cr=im.crop(tuple(int(x*s) for x in b))
    if red: cr=ImageOps.autocontrast(cr.split()[0])
    cr=cr.resize((cr.width*z,cr.height*z),Image.LANCZOS); cr.save(f'crops/y_{n}.png')
c('pm',(1270,160,1680,420),2)
c('kis',(30,960,300,1030),5,True)
c('sok',(30,925,330,985),4)
c('tail',(520,1000,860,1060),3)
c('yak',(640,470,820,520),5)
c('l14',(40,675,110,720),6)

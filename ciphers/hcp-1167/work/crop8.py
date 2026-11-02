from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
W,H=im.size
s=3468/1800
# column of line starts
cr=im.crop((int(15*s),int(200*s),int(240*s),int(950*s))); cr.save('crops/w_col.png'); print(cr.size)
def c(n,b,z):
    cr=im.crop(tuple(int(x*s) for x in b)); cr.resize((cr.width*z,cr.height*z),Image.LANCZOS).save(f'crops/w_{n}.png')
c('szoval',(95,595,230,650),5)
c('oka',(420,370,720,420),4) if False else None
c('es',(30,965,300,1020),4)
c('addrtop',(880,250,1400,400),2)
c('lehet',(40,395,330,450),4) if False else None

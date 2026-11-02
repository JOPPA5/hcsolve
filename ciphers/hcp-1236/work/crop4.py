from PIL import Image
a=Image.open('hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg').convert('RGB')
p=Image.open('hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_pic.jpg').convert('RGB')
s=3445/1024
def c(im,n,x0,x1,y0,y1,z=1,rot=0):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    if z!=1: r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    if rot: r=r.rotate(rot,expand=True)
    r.save(f'crops/{n}.png')
c(a,'addr',480,990,110,600)
c(a,'pm',480,960,25,265)
c(a,'r5end',400,500,145,185,3)
c(a,'r11g',190,290,395,450,3)
c(p,'poem',740,900,220,450,1,-90)

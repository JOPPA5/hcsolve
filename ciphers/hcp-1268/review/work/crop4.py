from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/work/hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=3445/1024
o='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/review/work/crops/'
def C(n,box,z=4):
    c=im.crop(tuple(int(v*s) for v in box))
    c=c.resize((c.width*z,c.height*z),Image.LANCZOS); c.save(o+n+'.png'); print(n,c.size)
C('z_r4e',(120,145,200,212),5)
C('z_r10a',(20,372,80,425),5)
C('z_r11a',(90,410,190,465),5)

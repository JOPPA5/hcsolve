from PIL import Image,ImageOps
im=Image.open('hires/cpc_1914-11-23_HU__HU_Budapest_jolanka-56_adr.jpg').convert('RGB')
def s(n,box,z=2,ac=True):
    c=im.crop(box)
    if ac:
        # green channel suppresses little; use red channel: green ink darker in red, black cancel dark too
        c=ImageOps.autocontrast(c.split()[0],cutoff=1)
    c.resize((c.width*z,c.height*z),Image.LANCZOS).save(f'crops/{n}.png')
s('r3a',(60,300,900,560)); s('r3b',(800,300,1680,560))
s('r5a',(60,480,900,760)); s('r5b',(800,480,1680,760))
s('r7a',(60,680,900,900)); s('r7b',(800,680,1680,900))
s('bot1',(60,1900,1000,2110)); s('bot2',(900,1900,2100,2110)); s('bot3',(2000,1900,3360,2110),z=1)
c=im.crop((3250,60,3421,2110));c=c.rotate(90,expand=True);c.save('crops/redge.png')
p=Image.open('hires/cpc_1914-11-23_HU__HU_Budapest_jolanka-56_pic.jpg').convert('L')
ImageOps.equalize(p).resize((1700,1081)).save('crops/pic_eq.png')

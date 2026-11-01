from PIL import Image, ImageEnhance, ImageOps
im=Image.open('hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg').convert('RGB')
f=1.72
def box(n,x0,y0,x1,y1,s,ch=None):
    c=im.crop((int(x0*f),int(y0*f),int(x1*f),int(y1*f)))
    if ch is not None:
        c=ImageOps.autocontrast(c.split()[ch],cutoff=1)
    c=c.resize((c.width*s//2,c.height*s//2),Image.LANCZOS); c.save(f'crops/{n}.png')
box('y1',640,60,850,120,5)
box('y2',80,985,640,1060,3)
box('y3',78,1095,360,1195,6,1)
box('y4',78,1095,360,1195,6,2)
box('y5',80,830,140,920,6)
box('y6',80,985,180,1050,8,1)
box('y7',1000,1100,1140,1200,5)

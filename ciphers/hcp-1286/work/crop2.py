from PIL import Image, ImageChops, ImageOps
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
r,g,b=im.split()
d=ImageChops.subtract(b,g,1,128)  # B-G
d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=(0.5,0.1)))
def c(src,name,x0,y0,x1,y1,s):
    bx=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    q=src.crop(bx); q=q.resize((int(q.width*s),int(q.height*s)),Image.LANCZOS); q.save('crops/%s.png'%name)
# band 130-430 (rows 3-9) segments
c(d,'p1',40,120,500,290,2.5); c(d,'p2',470,120,960,290,2.5)
c(d,'p3',40,270,500,440,2.5); c(d,'p4',470,270,960,440,2.5)
c(d,'p5',40,420,500,520,2.5); c(d,'p6',470,420,960,520,2.5)

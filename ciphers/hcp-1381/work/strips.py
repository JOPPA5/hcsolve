from PIL import Image, ImageOps, ImageFilter, ImageChops
im=Image.open('hires/pc_hcp_62_adr.JPG').convert('RGB')
c=im.crop((40,60,1010,1120)).rotate(90,expand=True)
print(c.size)
g=c.split()[1]
bg=g.filter(ImageFilter.GaussianBlur(12))
d=ImageOps.invert(ImageOps.autocontrast(ImageChops.subtract(bg,g),cutoff=(0,0.3)))
c.save('crops/full_rot.png'); d.save('crops/full_d.png')
# offset: y in new = old msg y +30(+?), x + 60
def strip(n,y0,y1,x0=250,x1=1060,s=3):
    for nm,src in (('r',c),('d',d)):
        src.crop((x0,y0,x1,y1)).resize(((x1-x0)*s//1,(y1-y0)*s),Image.LANCZOS).save(f'crops/L{n}_{nm}.png')
ranges=[(1,60,200),(2,200,300),(3,300,400),(4,400,510),(5,500,620)]

from PIL import Image, ImageOps, ImageFilter
import sys
im=Image.open('hires/pc_hcp_43_adr.JPG').convert('RGB')
def d(name,box,z=7):
    x0,y0,x1,y1=box
    r=im.crop((800-y1,300+x0,800-y0,300+x1)).rotate(90,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.BICUBIC)
    r=r.filter(ImageFilter.UnsharpMask(8,120,2))
    r=ImageOps.autocontrast(r,cutoff=0.3); r.save('crops/%s.png'%name)
d('w22',(245,150,460,250),6)
d('w23',(490,120,775,240),5)
s=im.crop((1380,180,1720,420)).rotate(100,expand=True); s=s.resize((s.width*3,s.height*3),Image.LANCZOS); s.save('crops/stamp_rot.png'); print(s.size)
d('w31',(10,225,300,370),4)

from PIL import Image, ImageOps, ImageFilter
import sys
r=Image.open('rot.png').convert('RGB')
s=1175/1053
def c(n,x0,y0,x1,y1,z=4):
    b=[int(v*s) for v in (x0,y0,x1,y1)]
    im=r.crop(b); 
    b_ch=im.split()[2]
    bg=b_ch.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(10))
    from PIL import ImageChops
    d=ImageChops.subtract(bg,b_ch)
    d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=(0,0.3)))
    w=(im.width*z,im.height*z)
    out=Image.new('RGB',(w[0],w[1]*2+6),'white')
    out.paste(im.resize(w,Image.LANCZOS),(0,0)); out.paste(d.convert('RGB').resize(w,Image.LANCZOS),(0,w[1]+6))
    out.save(n+'.png'); print(n,out.size)
c('l1a',390,855,690,925,3)
c('l1b',660,850,990,925,3)
c('l2',390,930,950,1020,2)
c('l3a',400,1020,700,1095,3)
c('l3b',680,1020,990,1100,3)
c('l4a',420,1085,700,1150,3)
c('l4b',660,1085,990,1160,3)
c('l5a',390,1145,720,1250,3)
c('l5b',700,1160,980,1260,3)
c('z_mpwf',670,850,860,925,6)
c('z_sign',790,860,880,925,9)
c('z_nh',640,1155,740,1235,8)
c('z_op',640,1085,790,1150,6)
c('z_ej',400,1030,560,1095,6)
c('z_nh2',650,1130,800,1230,6)
c('z_nz',390,860,480,925,6)
c('z_cpz',860,855,990,930,5)
c('z_O',650,1105,730,1150,10)
r.crop((90,110,420,460)).rotate(0).resize((990,1050)).save('z_post.png')

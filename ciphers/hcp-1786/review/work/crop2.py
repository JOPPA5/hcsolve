from PIL import Image, ImageOps
s=1785/1024
A=Image.open('work/hires/pc_hcp_467_adr.JPG').convert('RGB')
P=Image.open('work/hires/pc_hcp_467_pic.JPG').convert('RGB')
def c(box,z,name,im=A):
    b=[int(x*s) for x in box]; r=im.crop(b); r.resize((r.width*z,r.height*z),Image.BICUBIC).save('review/work/'+name)
c((60,185,150,225),8,'z_x65.png')
c((270,170,330,225),10,'z_nesmis.png')
c((400,175,480,225),10,'z_zlat.png')
c((60,320,110,355),10,'z_dnes.png')
c((225,222,270,262),10,'z_vzd.png')
c((165,322,200,355),10,'z_v.png')
c((400,405,445,445),10,'z_hotovo.png')
c((225,360,300,400),10,'z_seto.png')
# pencil: blue channel downsample then autocontrast
b=[int(x*s) for x in (395,55,670,300)]
r=P.crop(b).split()[0].resize(((b[2]-b[0])*2,(b[3]-b[1])*2),Image.LANCZOS)
ImageOps.autocontrast(r,cutoff=2).save('review/work/pencil_red.png')

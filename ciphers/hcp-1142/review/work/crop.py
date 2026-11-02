from PIL import Image
import sys
im=Image.open('../../work/hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg').convert('RGB')
S=3468/1024
def c(n,x0,y0,x1,y1,z=1.5):
    r=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save(n)
rows=[(18,58),(55,95),(90,127),(122,160),(155,192),(195,235),(230,265),(265,305),(305,345),(345,385),(380,420),(415,465),(465,505),(500,545),(540,615)]
for i,(a,b) in enumerate(rows,1):
    c(f'r{i:02}a.png',10,a,235,b); c(f'r{i:02}b.png',225,a,480,b)
c('x10a.png',10,345,240,405); c('x10b.png',235,345,480,405)
c('x13a.png',10,425,240,475);c('x13b.png',235,425,490,475)
c('x14.png',10,465,240,510);c('x15.png',235,500,490,545);c('x15a.png',10,500,240,545)
c('foot1.png',20,540,250,585,2.5);c('foot2.png',20,572,250,615,2.5);c('foot3.png',240,540,500,615,2.5)
c('stamp.png',650,20,940,310,1)
c('ty.png',130,350,220,400,5)
c('end.png',370,500,460,550,5)
c('word.png',170,578,350,612,5)
c('word2.png',300,578,480,612,5)
c('sig.png',360,540,450,580,5)
pm=im.crop((int(690*S),int(70*S),int(945*S),int(310*S)))
for a in (0,90,180,270):
    pm.rotate(a,expand=True).resize((700,700)).save(f'pm{a}.png')
pic=Image.open('../../work/hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_pic.jpg'); pic.thumbnail((1200,1200)); pic.save('pic.png')

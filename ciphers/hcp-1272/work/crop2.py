from PIL import Image
im=Image.open('hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
S=1.7225
def c(n,x0,y0,x1,y1,z=4):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%n)
c('z1end',640,55,830,175,3)      # row1 end + row2
c('z2a',40,150,260,200,3)
c('z4',200,250,560,320,3)
c('z4b',640,240,860,420,3)
c('z12',60,860,860,930,2)
c('z11',560,800,880,870,3)
c('z16a',40,1085,300,1135,4)
c('z17a',380,1130,800,1185,3)
c('z17b',40,1130,420,1185,3)
c('z8',380,560,960,620,2)
c('z10',380,720,800,780,3)

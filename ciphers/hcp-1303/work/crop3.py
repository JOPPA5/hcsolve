from PIL import Image, ImageOps
im=Image.open('hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(name,x0,y0,x1,y1,z=3,rot=0):
    b=[int(v*s) for v in (x0,y0,x1,y1)]
    r=im.crop(b); 
    if rot: r=r.rotate(rot,expand=True)
    r=ImageOps.autocontrast(r.resize((r.width*z,r.height*z),Image.LANCZOS),cutoff=1); r.save('crops/%s.png'%name)
c('e_edge',1800,940,1920,1190,4,-90)
c('e_tail',1450,1120,1920,1215,2)
c('e_tail2',1230,1100,1880,1195,3)
c('e_st4',1525,265,1810,375,5)
c('e_r4',560,250,880,340,4)
c('e_r1',560,40,860,120,4)
c('e_r8',600,520,890,590,4)
c('e_r9',50,640,420,720,4)
c('e_r18l',50,1125,240,1190,6)

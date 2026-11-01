from PIL import Image,ImageOps
im=Image.open('hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg').convert('L')
f=1.7225
for n,b,s in [('l1',(50,1085,330,1225),3),('l2',(320,1085,610,1225),3),('l3',(600,1075,890,1215),3),('l4',(600,1020,890,1140),3),('l5',(880,1060,1240,1200),3),('l6',(320,1000,610,1110),3),('l7',(50,1010,330,1120),3)]:
    r=im.crop(tuple(int(x*f) for x in b)); r=ImageOps.autocontrast(r,cutoff=1); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save(f'crops/{n}.png')
b=(1560,100,1810,400)
r=im.crop(tuple(int(x*f) for x in (1570,200,1800,280))); r=r.resize((r.width*4,r.height*4),Image.LANCZOS); r.save('crops/s4.png')

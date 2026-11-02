from PIL import Image
src='work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg'
im=Image.open(src).convert('RGB')
# merged view: multiply out black postmark by replacing dark neutral pixels with paper
px=im.load()
W,H=im.size
out=im.copy();p=out.load()
for y in range(H):
    for x in range(W):
        r,g,b=px[x,y]
        if b-g<14 and r<150: p[x,y]=(225,212,205)
out.save('work/crops/nopm.png')
ys=[(30,200),(130,300),(230,400),(330,500),(430,600),(530,700),(640,800),(740,900),(840,1010),(980,1140),(1090,1240),(1190,1350),(1290,1450),(1450,1610),(1550,1710),(1640,1800),(1740,1880),(1820,1970),(1920,2070),(2000,2150)]
for i,(u,v) in enumerate(ys,1):
    for n,(a,b) in enumerate([(20,620),(560,1160),(1100,1720)]):
        for tag,I in (('p',im),('q',out)):
            c=I.crop((a,u,b,v));c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS);c.save('work/crops/%s%02d%s.png'%(tag,i,'abc'[n]))

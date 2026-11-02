from PIL import Image
import glob,sys
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
# small-scale y bands
s=3421/1400
ys=[(40,145),(130,250),(240,350),(340,450),(440,560),(550,660),(650,770),(760,885)]
for i,(a,b) in enumerate(ys):
    for j,(x0,x1) in enumerate([(25,400),(380,770)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*2//1,c.height*2//1),Image.LANCZOS)
        c.save(f'crops/b{i}_{j}.jpg',quality=88)
c=im.crop((int(1140*s),int(60*s),int(1300*s),int(320*s))).rotate(-90,expand=True);c=c.resize((c.width*2,c.height*2));c.save('crops/stamp.jpg')
c=im.crop((int(770*s),int(220*s),int(1380*s),int(880*s)));c.save('crops/addr.jpg')
c=im.crop((int(25*s),int(840*s),int(1050*s),int(885*s)));c.save('crops/bottom.jpg')

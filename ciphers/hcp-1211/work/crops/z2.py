from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
s=3421/1400
Z={'e1':(640,840,860,885,4),'e2':(840,840,1040,885,4),'leg':(480,475,770,540,3),'nek':(395,575,780,640,3),'r12b':(280,625,780,680,2),'r7a':(30,335,380,400,3)}
for k,(a,b,c,d,z) in Z.items():
    r=im.crop((int(a*s),int(b*s),int(c*s),int(d*s)));r=r.resize((r.width*z,r.height*z),Image.LANCZOS);r.save(f'crops/z_{k}.jpg',quality=88)
r=im.crop((int(1140*s),int(60*s),int(1300*s),int(320*s))).rotate(-90,expand=True)
r=r.crop((150,100,r.width,330));r=r.resize((r.width*2,r.height*2));r.save('crops/z_st.jpg')

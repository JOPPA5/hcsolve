from PIL import Image
import glob,sys
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
s=3421/1400
# name:(x0,y0,x1,y1) in overview coords, scale
Z={'r3a':(120,145,330,205,3),'r4b':(240,195,750,250,2),'r6b':(330,285,800,350,2),'r7b':(380,340,650,395,3),
'r12a':(25,600,300,660,3),'r16a':(25,805,520,860,2),'r17a':(25,840,520,885,3),'r17b':(420,840,1040,885,3),'r5m':(120,250,300,310,3)}
for k,(a,b,c,d,z) in Z.items():
    r=im.crop((int(a*s),int(b*s),int(c*s),int(d*s)));r=r.resize((r.width*z,r.height*z),Image.LANCZOS);r.save(f'crops/z_{k}.jpg',quality=88);print(k,r.size)

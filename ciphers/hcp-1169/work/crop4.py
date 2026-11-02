from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.9267
B={'m0':(40,430,200,640,3.5),'m1':(150,990,600,1085,2.2),'m2':(470,1000,720,1085,4),'e1':(700,20,860,90,5),'e2':(60,700,480,790,2.4),'e3':(60,770,880,890,1.3),'e4':(60,880,880,1000,1.3),'e5':(640,540,800,630,5)}
for n,(x0,y0,x1,y1,f) in B.items():
    c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    c=c.resize((int(c.width*f),int(c.height*f)),Image.LANCZOS); c.save(f'crops/{n}.png')

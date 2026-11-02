from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.9267
B={'p0':(70,620,500,680,3),'p1':(70,700,480,810,2.5),'p2':(450,740,900,850,2.5),'p3':(70,840,480,960,2.5),'p4':(450,830,900,960,2.5),'p5':(50,950,500,1100,2.5),'p6':(470,950,960,1100,2.3),'q0':(90,30,300,125,4),'q1':(90,95,250,160,6),'q2':(630,700,900,830,4),'stamp':(1240,10,1720,180,2.2),'adr':(880,170,1730,1100,1.0)}
for n,(x0,y0,x1,y1,f) in B.items():
    c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    c=c.resize((int(c.width*f),int(c.height*f)),Image.LANCZOS); c.save(f'crops/{n}.png')

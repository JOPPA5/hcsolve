from PIL import Image, ImageOps
import numpy as np, glob
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1171/work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
def box(x0,y0,x1,y1,name,z=2,blue=False):
    c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS)
    if blue:
        a=np.asarray(c).astype(float); r=a[...,0];b=a[...,2]
        # brown ink/paper have r>>b; blue ink r<=b : use r channel (blue dark in red, brown lighter?) 
        g=r-0.0*b
        g=(g-g.min())/(g.max()-g.min())*255
        c=ImageOps.autocontrast(Image.fromarray(g.astype('uint8')))
    c.save('crops/'+name+'.png')
rows=[(20,60,'h'),(70,175,'a'),(165,270,'b'),(260,365,'c'),(355,460,'d'),(450,560,'e'),(550,650,'f'),(640,745,'g'),(740,850,'i'),(840,990,'j')]
for y0,y1,n in rows:
    box(30,y0,830,y1,'r_'+n,z=2); box(30,y0,830,y1,'rb_'+n,z=2,blue=True)
box(90,20,700,70,'head',z=3)
box(230,930,620,985,'sig',z=4)
box(800,90,1520,400,'stamp',z=1.5)
def z(x0,y0,x1,y1,n): box(x0,y0,x1,y1,'c_'+n,z=4); box(x0,y0,x1,y1,'b_'+n,z=4,blue=True)
z(40,920,420,975,'osul1'); z(40,880,780,945,'csok0')
z(40,905,440,950,'lan'); z(420,905,800,950,'leg')
z(40,860,430,912,'mind'); z(40,275,430,325,'mg1'); z(420,275,810,325,'mg2')
z(40,160,430,205,'jol1'); z(400,160,810,205,'jol2')
z(40,535,420,585,'neh1'); z(420,535,800,585,'neh2')
z(40,580,800,640,'mas')
z(40,720,420,770,'nem1')
z(40,440,420,490,'hagy');z(420,440,800,490,'hagy2')

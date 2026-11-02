from PIL import Image
import glob,sys
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.9267
# (name,y0,y1) in 1800-scale; split each in left/right halves
L=[('l01',25,85),('l02',85,140),('l03',130,185),('l04',170,225),('l05',210,265),('l06',255,305),('l07',290,345),('l08',335,395),('l09',385,440),('l10',430,485),('l11',480,530),('l12',525,575),('l13',565,620),('l14',605,640),('l15',630,700),('l16',690,770),('l17',750,850)]
for n,a,b in L:
    for part,(x0,x1) in {'a':(70,380),'b':(350,640),'c':(610,910)}.items():
        c=im.crop((int(x0*S),int(a*S),int(x1*S),int(b*S)))
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'crops/{n}{part}.png')

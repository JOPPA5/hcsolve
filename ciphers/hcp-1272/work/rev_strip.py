"""Revision 2026-11-02: deskewed row strips of the stamp note. Run from ciphers/hcp-1272 with a Python that has PIL."""
from PIL import Image, ImageOps, ImageChops, ImageFilter
im = Image.open('work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
G=im.split()[1]
d=ImageChops.subtract(G.filter(ImageFilter.GaussianBlur(25)),G)
d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=0.3))
# coordinates in w crop (scale 3, origin 2560,520): row (x0,y0)-(x1,y1) baseline
rows={'A':(340,130,1400,350),'B':(280,290,1400,440),'C':(270,420,1400,590),'D':(190,590,1320,690)}
for n,(x0,y0,x1,y1) in rows.items():
    X0,Y0,X1,Y1=2560+x0/3,520+y0/3,2560+x1/3,520+y1/3
    s=(Y1-Y0)/(X1-X0)
    W=int(X1-X0);H=70
    S=5
    out=Image.new('L',(W*S,H*S),255); px=out.load()
    src=d.resize((d.width,d.height)) ; 
    tmp=d.transform((W,H),Image.AFFINE,(1,0,X0,s,1,Y0-H*0.65),resample=Image.BICUBIC)
    tmp=tmp.resize((W*S,H*S),Image.LANCZOS); tmp.save(f'work/crops2/row{n}.png')
    tmp.crop((0,0,W*S//2+60,H*S)).save(f'work/crops2/row{n}1.png'); tmp.crop((W*S//2-60,0,W*S,H*S)).save(f'work/crops2/row{n}2.png')

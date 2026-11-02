import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1214/work/hires/*adr.jpg')[0]).convert('L')
s=3445/1400
B={'A_r1end':(500,50,570,115,10),'B_r7h':(405,320,470,380,10),'C_r10a':(460,445,510,485,10),'D_r12oe':(470,505,540,560,8),'E_pm':(980,70,1110,320,4)}
for k,(a,b,c_,d,f) in B.items():
    c=im.crop((int(a*s),int(b*s),int(c_*s),int(d*s))); c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*f//2,c.height*f//2),Image.LANCZOS); c.save(k+'.png'); print(k,c.size)

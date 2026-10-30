import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB'); S=3445/1024
L=[('r13end',375,395,425,425),('r13cmp',335,395,425,425),('r9a',135,270,185,300),('r9acute',285,250,330,295),('r11T',205,325,240,355),('r10d',335,300,370,335),('r18start',30,525,70,560),('r18h',200,525,250,565),('r18next',225,525,275,565),('s5',790,160,900,190),('s6',800,185,900,215),('corner',960,570,990,620),('pencil',430,25,760,75)]
W=[]
for n,l,t,r,b in L:
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)));z=5 if r-l<120 else 2.5
    x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS);ImageEnhance.Contrast(x).enhance(1.4).save(sys.argv[2]+'/z_'+n+'.png')

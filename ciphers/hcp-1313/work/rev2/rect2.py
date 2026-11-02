from PIL import Image, ImageDraw
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
enh=Image.open(W+'crops/enh_full.png')
def r(name,x0,y0,w,h,s=2.5):
    c=enh.crop((x0,y0,x0+w,y0+h)).resize((int(w*s),int(h*s)),Image.LANCZOS).convert('L')
    d=ImageDraw.Draw(c)
    for t in range(0,w,100): d.text((int(t*s)+2,2),str(x0+t),fill=0)
    c.save(W+'rev2/'+name+'.png')
r('e10',560,1180,700,170); r('e11',1100,1320,620,170); r('e12',60,1450,700,170); r('e12b',1100,1440,700,200); r('e13',60,1570,700,170)
r('addr',1750,500,1500,1600,1); r('stamp',2700,280,560,420,2)

from PIL import Image, ImageOps
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/rev2/'
im=Image.open(W+'pca0.png')
for n,b in {'p1':(100,90,900,300),'p2':(800,90,1600,330),'p3':(40,290,840,470),'p4':(800,290,1600,490)}.items():
    c=ImageOps.autocontrast(im.crop(b),cutoff=(0.5,8))
    c.resize((c.width*2,c.height*2),Image.BICUBIC).save(W+n+'.png')

from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
Z={'irok':(120,262,420,305,4),'szomb':(590,135,800,190,4),'vers':(440,250,790,312,4),'blot':(540,490,700,545,5),'marad':(600,800,730,850,5),
'imad1':(30,850,330,920,4),'imad2':(300,850,620,925,4),'lam':(520,365,690,425,5),'magyek':(30,195,300,240,4),'ketec':(30,235,420,285,3),'csok':(330,790,560,850,4),'ud':(60,730,400,790,4)}
for n,(a,b,c,d,z) in Z.items():
    x=im.crop((int(a*S),int(b*S),int(c*S),int(d*S)))
    x=x.resize((x.width*z,x.height*z),Image.BICUBIC)
    ImageEnhance.Contrast(x).enhance(1.4).save(f'crops/z_{n}.png')

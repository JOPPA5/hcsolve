from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
Z={'blot2':(640,485,760,545,6),'addig':(25,265,250,312,5),'post':(1200,270,1540,470,2)}
for n,(a,b,c,d,z) in Z.items():
    x=im.crop((int(a*S),int(b*S),int(c*S),int(d*S)))
    x=x.resize((x.width*z,x.height*z),Image.BICUBIC)
    ImageEnhance.Contrast(x).enhance(1.4).save(f'crops/z_{n}.png')
# red-channel view of the blot
x=im.crop((int(640*S),int(485*S),int(760*S),int(545*S))).split()[0].resize((260*6,130*6),Image.BICUBIC)
ImageEnhance.Contrast(x).enhance(2.2).save('crops/z_blot_r.png')

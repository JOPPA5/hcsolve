from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
Z={'blot':(640,490,740,535,8),'tam':(530,365,680,430,6),'marad':(600,800,730,850,7),'ad':(30,885,330,950,3.5),'udv':(30,715,330,770,3.5),'ha':(70,525,320,585,4),'addig':(30,270,250,310,4),'stamp':(1215,290,1540,480,3),'ism':(390,190,640,245,4),'date':(30,930,620,975,2.7)}
for n,(a,b,c,d,f) in Z.items():
    k=im.crop((int(a*S),int(b*S),int(c*S),int(d*S)))
    k=k.resize((int(k.width*f),int(k.height*f)),Image.LANCZOS)
    ImageEnhance.Contrast(k).enhance(1.4).save('z_'+n+'.png')

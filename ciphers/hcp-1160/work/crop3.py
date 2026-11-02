from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
R={'g1':(2130,40,2830,135,3),'g2':(1510,40,2000,135,4),'g3':(960,1225,1120,1310,6),'g4':(60,540,240,630,5),'g5':(1210,330,1330,400,6),'g6':(1020,240,1130,310,6),'g7':(1280,680,1400,770,6),'g8':(720,900,860,980,6),'g9':(1100,1320,1230,1430,6)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/%s.png'%k)

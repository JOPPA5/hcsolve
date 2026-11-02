from PIL import Image
import glob
im=Image.open(glob.glob('work/hires/*adr*')[0]).convert('RGB')
Z={'z18':(1100,1640,1700,1770,3),'z10':(440,990,960,1110,3),'z22a':(1500,2000,2350,2115,2),'z15':(300,1430,700,1570,4),'z12':(480,1170,960,1270,3),'z22b':(2350,1990,3270,2115,2),'z7':(1380,620,1640,740,4),'z14':(1180,1250,1640,1400,3),'z21end':(2800,1840,3280,1990,3)}
for k,(a,b,c,d,s) in Z.items():
    r=im.crop((a,b,c,d));r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'review/work/{k}.png')

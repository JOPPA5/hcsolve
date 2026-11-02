from PIL import Image, ImageEnhance
import sys
im=Image.open('hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')
Y={1:125,2:210,3:300,4:370,5:465,6:560,7:640,8:710,9:790,10:875,11:955,12:1040,13:1125,14:1215,15:1290,16:1365,17:1440,18:1525,19:1625,20:1730,21:1830,22:1915,23:1990}
s=3.3;W=int(560*s);H=int(190*s)
for r,y in Y.items():
    can=Image.new('RGB',(W,H*3+20),'white')
    for k,x in enumerate((70,600,1120)):
        dy=-int((x-70)*0.035)
        i=im.crop((x,y-95+dy,x+560,y+95+dy)).resize((W,H),Image.LANCZOS)
        i=ImageEnhance.Contrast(i).enhance(1.9)
        can.paste(i,(0,k*(H+10)))
    can.save(f'crops/r{r:02d}.png')

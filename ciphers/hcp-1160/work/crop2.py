from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
R={'e1':(1110,10,1450,110,4),'e2':(1190,15,1400,70,6),'e3':(1500,20,2200,90,3),'e4':(2150,20,2780,110,3),
'f1':(1440,120,1560,220,6),   # end L3 etc
'f2':(30,320,300,400,5),      # udo start? 
'f3':(70,1000,330,1090,5),    # 9 :1 
'f4':(1000,985,1290,1090,5),   # 8. -1
'f5':(1400,890,1640,970,5),   # ertem
'f6':(1060,300,1350,380,5),  # L3 row? 
'f7':(150,1190,330,1290,5),
'f8':(790,1190,950,1290,5)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/%s.png'%k)

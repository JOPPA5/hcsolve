import glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
B={'a1':(500,410,1040,540),'a2':(1000,410,1620,540),'b1':(20,1300,560,1420),
'c1':(20,1950,560,2080),'c2':(540,1950,1100,2080),'c3':(1060,1950,1640,2100),
'd1':(1560,1880,2060,2030),'d2':(2040,1880,2540,2030),'d3':(2520,1880,3020,2030),'d4':(2960,1880,3420,2030)}
for k,b in B.items():
    r=im.crop(b); r.resize((r.width*3,r.height*3),Image.LANCZOS).save('crops/'+k+'.png')

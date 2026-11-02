import glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
B={'h1':(20,1585,620,1690),'h2':(1090,1570,1640,1680),'h3':(20,1660,640,1770),'h4':(20,1840,640,1960),'h5':(600,1840,1120,1960),
'h6':(20,1170,560,1290),'h7':(20,840,640,950),'h8':(20,1720,640,1860),'h9':(620,1720,1200,1860)}
for k,b in B.items():
    r=im.crop(b); r.resize((r.width*3,r.height*3),Image.LANCZOS).save('crops/'+k+'.png')

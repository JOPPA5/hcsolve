from PIL import Image
import sys
im=Image.open('work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg').convert('RGB')
for name,(x0,y0,x1,y1) in {'z8':(330,510,640,590),'z8b':(600,510,930,590),'z12':(430,760,800,840),'z13':(440,830,640,915),'z14':(620,880,930,985),'z5':(330,300,620,400)}.items():
    c=im.crop((int(x0*1.72),int(y0*1.72),int(x1*1.72),int(y1*1.72)))
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'work/crops/{name}.png')

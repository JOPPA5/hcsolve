from PIL import Image, ImageOps, ImageEnhance
import sys
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
c=im.crop((90,340,790,1100)).rotate(90,expand=True)
# coordinates below in the 760x700 rotated frame
boxes={'l1':(0,10,690,135),'l2':(0,95,720,210),'l3':(0,175,690,300),'l4':(30,260,690,380),'l5':(20,360,720,480),'l6':(20,440,720,560),'l7':(10,510,700,640),'l8':(0,590,600,700),
'l2a':(0,95,420,210),'l2b':(200,95,720,210),'l3a':(0,175,350,300),'l3b':(320,175,690,300),'l4a':(30,260,350,380)}
for k,b in boxes.items():
    x=c.crop(b);x=x.resize((x.width*3,x.height*3),Image.LANCZOS)
    x=ImageEnhance.Contrast(x).enhance(1.5)
    x.save(f'work/crops/{k}.png')

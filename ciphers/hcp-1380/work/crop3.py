from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
c=im.crop((90,340,790,1100)).rotate(90,expand=True)
b={'y_take':(20,365,240,470),'y_amp':(570,180,680,290),'y_own':(480,520,660,610),'y_loving':(0,595,420,700),'y_special':(380,450,680,560),'y_req':(20,520,340,640),'y_J1':(420,30,560,125),'y_am':(540,30,680,90)}
for k,v in b.items():
    x=c.crop(v);x=x.resize((x.width*5,x.height*5),Image.BICUBIC);ImageEnhance.Contrast(x).enhance(1.5).save(f'work/crops/{k}.png')

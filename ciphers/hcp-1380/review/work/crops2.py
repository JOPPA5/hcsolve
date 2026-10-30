from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
c=im.crop((90,340,790,1100)).rotate(90,expand=True)
b={'a_l1':(0,15,380,120),'a_l1b':(380,15,720,130),'a_l2a':(0,105,250,195),'a_l2b':(220,100,470,190),'a_l2c':(470,100,740,200),
'a_l3a':(20,190,260,290),'a_l3b':(240,190,500,290),'a_l3c':(460,190,740,290),
'a_l4a':(40,280,280,380),'a_l4b':(270,300,520,380),'a_l4c':(460,280,730,400),
'a_l5':(20,370,400,470),'a_l5b':(380,370,740,480),
'a_l6':(20,450,380,560),'a_l6b':(360,450,730,570),
'a_l7':(20,530,360,640),'a_l7b':(340,540,720,640),'a_l8':(0,610,620,700)}
for k,v in b.items():
    x=c.crop(v);x=x.resize((x.width*4,x.height*4),Image.BICUBIC);ImageEnhance.Contrast(x).enhance(1.7).save(f'review/work/{k}.png')

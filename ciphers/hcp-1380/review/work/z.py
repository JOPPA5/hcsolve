from PIL import Image
im=Image.open('review/work/flat.png')
b={'t_sorry':(255,135,460,205),'t_wfsz':(60,135,250,205),'t_ipqf':(80,300,260,375),'t_xjmm':(480,300,750,390),'t_own':(380,570,690,650),'t_loving':(30,630,330,720),'t_girl':(370,630,600,720),'t_jo':(200,225,340,330),'t_efb':(190,45,480,130),'t_am':(590,50,720,120)}
for k,v in b.items():
    x=im.crop(v);x.resize((x.width*5,x.height*5),Image.BICUBIC).save(f'review/work/{k}.png')

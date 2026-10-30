from PIL import Image,ImageOps
im=Image.open('work/crops/all_ccw.png').convert('RGB')
boxes={'z_favo':(130,340,420,470),'z_ourite':(380,340,640,480),'z_hymns':(650,340,990,450),'z_love':(190,430,420,600),'z_first':(150,160,330,290),'z_some':(460,150,760,320),'z_date':(250,590,720,740),'z_dear':(490,60,800,190)}
for k,b in boxes.items():
    s=5 if b[2]-b[0]<300 else 4
    c=ImageOps.autocontrast(im.crop(b),cutoff=0.5).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.BICUBIC)
    c.save(f'work/crops/{k}.png')

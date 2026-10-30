from PIL import Image,ImageOps
im=Image.open('work/crops/all_ccw.png').convert('L')
boxes={'l1a':(170,40,600,170),'l1b':(480,40,1000,190),'l2a':(150,150,600,290),'l2b':(460,150,1000,320),'l3':(130,250,850,380),'l4a':(130,340,640,480),'l4b':(600,340,990,450),'l5a':(190,430,640,600),'l5b':(600,470,990,610),'l6a':(0,600,520,730),'l6b':(420,590,830,740)}
for k,b in boxes.items():
    c=ImageOps.autocontrast(im.crop(b),cutoff=1).resize(((b[2]-b[0])*3,(b[3]-b[1])*3),Image.LANCZOS)
    c.save(f'work/crops/{k}.png')

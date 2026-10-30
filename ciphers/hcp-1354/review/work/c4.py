from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
def cr(b,n,s=6,rot=0):
    c=ImageOps.autocontrast(im.crop(b),cutoff=1); c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
    if rot: c=c.rotate(rot,expand=True)
    c.save(n)
cr((340,1025,560,1110),'y_sudd.png',8)
cr((690,1400,860,1480),'y_sund.png',8)
cr((180,240,410,380),'y_stamp.png',5)
cr((90,1490,230,1640),'y_pen.png',4,-90)

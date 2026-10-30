from PIL import Image, ImageOps
c=Image.open('crops/message.png')
def s(n,b,k=6):
    d=c.crop(b); d=d.resize((d.width*k,d.height*k),Image.BICUBIC); d.save(f'crops/{n}.png')
s('w_mystery',(480,335,790,425),6)
s('w_will',(390,240,680,350),6)
s('w_for',(290,345,480,450),6)
s('w_amp',(380,555,680,640),6)

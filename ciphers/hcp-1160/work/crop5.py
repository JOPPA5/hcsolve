from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
x=im.crop((2750,20,3450,190)); x.resize((x.width*3,x.height*3),Image.LANCZOS).save('crops/i1.png')
x=im.crop((1460,30,3468,520)); x.save('crops/i2.png')

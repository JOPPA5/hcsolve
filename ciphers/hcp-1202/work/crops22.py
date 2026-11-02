import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
for b,y in enumerate(range(120,960,140)):
    strips=[im.crop((x,y,x+640,y+170)).resize((1472,391),Image.LANCZOS) for x in (150,750,1350)]
    out=Image.new('RGB',(1472,391*3+20),'white')
    for i,s in enumerate(strips): out.paste(ImageEnhance.Contrast(s).enhance(1.5),(0,i*400))
    out.save(D+f'/crops/A{b:02d}.png')
print(b)

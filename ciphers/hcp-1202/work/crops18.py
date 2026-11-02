import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
import PIL
# stacked strips per band: three width segments stacked vertically in one image
from PIL import Image
for b,y in enumerate(range(960,2100,125)):
    strips=[im.crop((x,y,x+640,y+170)).resize((1472,391),Image.LANCZOS) for x in (150,750,1350)]
    out=Image.new('RGB',(1472,391*3+20),'white')
    for i,s in enumerate(strips): out.paste(ImageEnhance.Contrast(s).enhance(1.5),(0,i*400))
    out.save(D+f'/crops/B{b:02d}.png')
print(b)

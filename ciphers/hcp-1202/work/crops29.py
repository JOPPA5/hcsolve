import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
for k,y0 in enumerate(range(1010,2000,235)):
    y1=y0+250
    for j,(a,b) in enumerate([(140,800),(760,1420),(1380,2040)]):
        c=im.crop((a,y0,b,y1)); c=c.resize((1400,int(1400*(y1-y0)/(b-a))),Image.LANCZOS)
        ImageEnhance.Contrast(c).enhance(1.6).save(D+f'/crops/H{k}_{j}.png')

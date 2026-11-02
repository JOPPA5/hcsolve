import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
for k,(y0,y1) in enumerate([(1800,1960),(1930,2090),(2040,2190)]):
    for j,(a,b) in enumerate([(1960,2540),(2500,3000),(2960,3430)]):
        c=im.crop((a,y0,b,y1)); s=1400/(b-a); c=c.resize((1400,int((y1-y0)*s)),Image.LANCZOS)
        ImageEnhance.Contrast(c).enhance(1.6).save(D+f'/crops/J{k}_{j}.png')

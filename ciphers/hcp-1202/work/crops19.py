import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
def st(name,x0,y0,y1,w=500):
    xs=list(range(x0,3440,w-40))
    H=int((y1-y0)*2.9)
    W=int(w*2.9)
    out=Image.new('RGB',(W,(H+10)*len(xs)),'white')
    for i,x in enumerate(xs):
        s=im.crop((x,y0,x+w,y1)).resize((W,H),Image.LANCZOS)
        out.paste(ImageEnhance.Contrast(s).enhance(1.6),(0,i*(H+10)))
    out.save(D+'/crops/'+name+'.png')
st('R1',2250,1900,2010)
st('R2',2000,1970,2080)
st('R3',2000,2040,2130)
st('R4',2000,2085,2185)

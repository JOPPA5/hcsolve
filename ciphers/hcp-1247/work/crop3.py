from PIL import Image, ImageOps
s=Image.open('crops/shear.png')
Y=[42,88,122,160,205,245,283,320,365,405,440,485,522,550,590,625,665,705,745,790,830,870,900,940,970,1015]
def strip(r,a,b,sc=2.6,pad=78):
    y=Y[r-1]*2
    c=s.crop((a,y-pad,b,y+pad)).resize((int((b-a)*sc),int(2*pad*sc)),Image.LANCZOS)
    c=ImageOps.autocontrast(c,cutoff=1); c.save(f'crops/r{r:02d}{"ab"[a>500]}.png')
for r in range(1,27):
    strip(r,80,860); strip(r,800,1640)

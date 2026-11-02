from PIL import Image,ImageOps
import sys
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/hires/cpc_1914-01-07_HU__HU_Jasz-Arokszalas_jolanka-46_adr.jpg'
im=Image.open(src).convert('RGB')
def crop(name,box,s=2):
    c=im.crop(box); c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
    c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/crops/'+name+'.png')
if len(sys.argv)>1:
    a=sys.argv; crop(a[1],tuple(int(x) for x in a[2:6]),int(a[6]) if len(a)>6 else 2); sys.exit()
# whole overview of block
y=50
i=0
while y<2150:
    crop(f'L{i:02d}',(60,y,830,y+300)); crop(f'R{i:02d}',(780,y,1600,y+300)); y+=260;i+=1
print(i)

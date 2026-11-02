import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1214/work/hires/*adr.jpg')[0]).convert('L')
s=3445/1400
# same-scale (4x of hires) crops of each umlaut: row2 ko:zel, row7 start, row10 ue, row12 boe, row16 toe
B={'r02':(465,70,560,145),'r07':(40,325,135,400),'r10':(200,450,295,525),'r12':(470,505,565,580),'r16':(195,665,290,740)}
W=int(95*s)*3;H=int(75*s)*3
m=Image.new('L',(W*2+10,(H+10)*3),255)
for i,(k,b) in enumerate(B.items()):
    c=ImageOps.autocontrast(im.crop(tuple(int(v*s) for v in b)),cutoff=1).resize((W,H),Image.LANCZOS)
    m.paste(c,((i%2)*(W+10),(i//2)*(H+10)))
m.save('umlauts.png');print(m.size)

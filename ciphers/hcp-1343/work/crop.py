import sys
from PIL import Image
im=Image.open('hires/pc_hcp_24_adr.JPG').convert('L')
print(im.size)
# top block rows
s=1785/1400
def c(n,b,z=3,rot=0):
    r=im.crop([int(x*s) for x in b])
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%n)
for i,y in enumerate([48,78,108,135,165,195]):
    y0=y-2;c('t%dL'%i,(45,y0,520,y0+38));c('t%dR'%i,(500,y0,1020,y0+38))
c('t6',(620,215,800,250),4)
ys=[305,340,375,408,440,472,505,530,560,590,625,650,685,712,745,775,805,835]
for i,y in enumerate(ys):
    c('b%02d'%i,(40,y,620,y+38))
c('side',(615,285,650,870),3,-90)

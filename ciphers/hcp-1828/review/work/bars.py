from PIL import Image, ImageDraw
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
s=1785/1014
# approx centres in 1014-wide coordinates: (label,x,y)
B=[('R1 D',229,163),('R8 D',373,491),('R9 D',392,544),
   ('R3 T',368,250),('R4 T',293,303),('R5 T1',233,348),('R5 T2',343,348),('R7 T1',199,444),('R7 T2',409,445),('R8 T',185,492),('R9 T',141,544),('R10 T',500,596)]
W=[]
for l,x,y in B:
    c=im.crop((int((x-26)*s),int((y-27)*s),int((x+26)*s),int((y+27)*s))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
    ImageDraw.Draw(c).text((3,3),l,fill=(255,0,0)); W.append(c)
w,h=W[0].size
sh=Image.new('RGB',(w*6,h*2),'white')
for i,c in enumerate(W): sh.paste(c,((i%6)*w,(i//6)*h))
sh.save('crops/bars.png')
E2=[('R2 ',342,207),('R4a',238,303),('R4b',0,0)]
C=[('R2 eye',0),]
def sheet(items,name):
    W=[]
    for l,x,y in items:
        c=im.crop((int((x-20)*s),int((y-24)*s),int((x+20)*s),int((y+24)*s))); c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
        ImageDraw.Draw(c).text((3,3),l,fill=(255,0,0)); W.append(c)
    w,h=W[0].size
    sh=Image.new('RGB',(w*6,h*2),'white')
    for i,c in enumerate(W): sh.paste(c,((i%6)*w,(i//6)*h))
    sh.save(name)
sheet([('R2e',0+342-30,207),('R4e1',262,304),('R4e2',415,304),('R6e',500,392),('R7e',118,440),('R9e',429,544),('R10e',127,592),
 ('R3x',395,250),('R6x1',277,398),('R6x2',382,398),('R7x',499,440),('R8x',121,491)],'crops/eyes.png')
a=im.crop((int(580*s),int(370*s),int(990*s),int(630*s))); a=a.resize((a.width*2,a.height*2),Image.LANCZOS); a.save('crops/addr.png')
b=im.crop((int(760*s),int(40*s),int(990*s),int(290*s))); b=b.resize((b.width*2,b.height*2),Image.LANCZOS); b.save('crops/stamp.png')

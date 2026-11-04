# Rotated strips for columns L11..L20 (reading order), with corrected manual lines.
import json
from PIL import Image, ImageDraw
import numpy as np
HI='ciphers/hcp-927/work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__adr.jpg'
im=Image.open(HI).convert('RGB')
pts={
 'L11':[(300,630),(1200,617),(1900,590)],
 'L12':[(300,557),(1200,537),(1900,520)],
 'L13':[(300,482),(1200,462),(1900,440)],
 'L14':[(300,420),(1200,405),(1900,380)],
 'L15':[(300,337),(1200,335),(1900,327)],
 'L16':[(300,266),(1200,270),(1900,270)],
 'L17':[(300,212),(1200,217),(1900,220)],
 'L18':[(300,155),(1200,160),(1900,165)],
 'L19':[(300,100),(1200,110),(1900,105)],
}
Y0,Y1=230,2150; HW=34; S=2
names=sorted(pts)
strips=[]
for n in names:
    ys,xs=zip(*pts[n]); f=np.polyfit(ys,xs,2)
    st=Image.new('RGB',(Y1-Y0,2*HW),'white')
    for y in range(Y0,Y1):
        xc=int(round(np.polyval(f,y)))
        st.paste(im.crop((xc-HW,y,xc+HW,y+1)).transpose(Image.ROTATE_90),(y-Y0,0))
    strips.append((n,st))
segs=[(230,900),(850,1520),(1470,2150)]
for g in range(0,len(strips),3):
    grp=strips[g:g+3]
    for si,(a,b) in enumerate(segs):
        W=(b-a)*S; Hh=(2*HW*S+18)*len(grp)+20
        cv=Image.new('RGB',(W,Hh),'white'); d=ImageDraw.Draw(cv)
        for y in range(a-a%50+50,b,50):
            d.line([((y-a)*S,0),((y-a)*S,12)],fill='red',width=2); d.text(((y-a)*S+3,0),str(y),fill='red')
        for r,(n,st) in enumerate(grp):
            top=20+r*(2*HW*S+18)
            cv.paste(st.crop((a-Y0,0,b-Y0,2*HW)).resize((W,2*HW*S)),(0,top))
            d.text((3,top+2*HW*S+2),n,fill='green')
        cv.save('ciphers/hcp-927/work/crops/M%s-%s_%d.png'%(grp[0][0],grp[-1][0],si))

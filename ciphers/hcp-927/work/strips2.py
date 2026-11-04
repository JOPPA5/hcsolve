# Rotated column strips (reading order right->left, each column read top->bottom shown left->right)
import json
from PIL import Image, ImageDraw
import numpy as np
HI='ciphers/hcp-927/work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__adr.jpg'
im=Image.open(HI).convert('RGB')
cols=json.load(open('ciphers/hcp-927/work/cols.json'))
lines=[]
for c in cols:
    xs=[e[3] for e in c['els']]; ys=[e[0] for e in c['els']]
    f=np.polyfit(ys,xs,1); lines.append((c['mx'],f))
for (xt,xb) in [(100,100),(155,165),(212,220),(266,270)]:
    f=np.polyfit([300,2100],[xt,xb],1); lines.append((xt,f))
lines.sort(key=lambda t:-t[0])
json.dump([list(f) for _,f in lines],open('ciphers/hcp-927/work/lines.json','w'))
Y0,Y1=230,2150; HW=34; S=2
strips=[]
for k,(mx,f) in enumerate(lines):
    st=Image.new('RGB',(Y1-Y0,2*HW),'white')
    for y in range(Y0,Y1):
        xc=int(round(np.polyval(f,y)))
        st.paste(im.crop((xc-HW,y,xc+HW,y+1)).transpose(Image.ROTATE_90),(y-Y0,0))
    strips.append(st)
segs=[(230,900),(850,1520),(1470,2150)]
for g in range(0,len(strips),4):
    grp=strips[g:g+4]
    for si,(a,b) in enumerate(segs):
        W=(b-a)*S; Hh=(2*HW*S+18)*len(grp)+20
        cv=Image.new('RGB',(W,Hh),'white'); d=ImageDraw.Draw(cv)
        for y in range(a-a%50+50,b,50):
            d.line([((y-a)*S,0),((y-a)*S,12)],fill='red',width=2); d.text(((y-a)*S+3,0),str(y),fill='red')
        for r,st in enumerate(grp):
            top=20+r*(2*HW*S+18)
            cv.paste(st.crop((a-Y0,0,b-Y0,2*HW)).resize((W,2*HW*S)),(0,top))
            d.text((3,top+2*HW*S+2),'L%d'%(g+r+1),fill='green')
        cv.save('ciphers/hcp-927/work/crops/L%02d-%02d_%d.png'%(g+1,g+len(grp),si))
print(len(lines))

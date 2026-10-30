from PIL import Image
import numpy as np
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
n=np.asarray(Image.open(O+'desk.png'))
L={3:(300,300),4:(385,385),5:(470,470),6:(540,565),7:(605,650),8:(675,715),9:(785,775),10:(875,885),11:(960,960),12:(1050,1050),13:(1150,1150),14:(1230,1230),15:(1310,1315),16:(1405,1410),17:(1505,1500),18:(1585,1590),19:(1675,1690),20:(1780,1785),21:(1865,1865),22:(1955,1955)}
H=75
for k,(a,b) in L.items():
    out=np.full((2*H+6,1500,),255,'uint8') if 0 else None
    X0,X1=60,1560
    cols=[]
    for x in range(X0,X1):
        yc=int(round(a+(b-a)*(x-100)/1300))
        cols.append(n[yc-H:yc+H,x])
    s=np.stack(cols,1)
    im=Image.fromarray(s)
    W=500
    can=Image.new('L',(1250,3*(int(2*H*2.5))+20),128)
    for i in range(3):
        t=im.crop((i*(W-10),0,i*(W-10)+W,2*H)).resize((1250,int(2*H*2.5)),Image.LANCZOS)
        can.paste(t,(0,i*(int(2*H*2.5)+10)))
    can.save(O+f'l{k:02d}.png')

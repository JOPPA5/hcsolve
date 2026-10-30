from PIL import Image
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
n=Image.open(O+'desk.png')
ys=[105,220,295,382,467,550,635,712,795,875,960,1050,1137,1225,1312,1400,1487,1582,1680,1770,1862,1962]
for i,y in enumerate(ys,1):
    H=66
    A=n.crop((60,y-H,780,y+H)).resize((1440,2*H*2),Image.LANCZOS)
    B=n.crop((720,y-H,1440,y+H)).resize((1440,2*H*2),Image.LANCZOS)
    c=Image.new('L',(1440,4*H*2+10),128); c.paste(A,(0,0)); c.paste(B,(0,2*H*2+10)); c.save(O+f'row{i:02d}.png')

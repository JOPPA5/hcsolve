from PIL import Image, ImageDraw
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
im=Image.open(W+'enh2_full.png')
ys={4:520,5:650,6:780,7:900,8:1030,9:1150,10:1270,11:1400,12:1530,13:1660}
for r,y in ys.items():
    for j,x in enumerate((60,440,820,1200)):
        dy=int((x-60)*0.045)
        c=im.crop((x,y-85+dy,x+500,y+85+dy)).resize((1300,442),Image.LANCZOS)
        ImageDraw.Draw(c).text((3,3),f'r{r} x{x}',fill=0)
        c.save(W+f's{r:02d}_{j}.png')

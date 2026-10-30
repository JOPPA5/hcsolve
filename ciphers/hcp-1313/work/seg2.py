from PIL import Image, ImageDraw
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
im=Image.open(W+'enh2_full.png')
ys={14:1790,15:1900,16:2000}
for r,y in ys.items():
    for j,x in enumerate((60,440,820,1200,1500)):
        dy=int((x-60)*0.03)
        c=im.crop((x,y-95+dy,x+500,y+95+dy)).resize((1300,494),Image.LANCZOS)
        ImageDraw.Draw(c).text((3,3),f'r{r} x{x}',fill=0)
        c.save(W+f's{r:02d}_{j}.png')

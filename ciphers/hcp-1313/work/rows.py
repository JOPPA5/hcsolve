from PIL import Image, ImageDraw
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
im=Image.open(W+'enh_full.png')
ys=[130,270,390,520,650,780,900,1030,1150,1270,1400,1530,1660,1790,1900,2010]
for i,y in enumerate(ys,1):
    out=Image.new('L',(1040,3*290),255)
    for j,x in enumerate((60,660,1260)):
        dy=int((x-60)*0.045)
        c=im.crop((x,y-100+dy,x+700,y+100+dy)).resize((1040,297),Image.LANCZOS)
        out.paste(c,(0,j*290))
        ImageDraw.Draw(out).text((2,j*290+2),f'x{x}',fill=0)
    out.save(W+f'row{i:02d}.png')

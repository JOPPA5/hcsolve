from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('RGB')
centers=[150,269,377,500,624,728,861,985,1113,1216,1313,1432]
for i,c in enumerate(centers,1):
    a=im.crop((60,c-85,1560,c+85)); 
    if i>=8: a=im.crop((60,c-85,1560,c+85))
    for j,(x0,x1) in enumerate([(0,780),(720,1500)]):
        b=a.crop((x0,0,x1,170)); b=ImageOps.autocontrast(b,cutoff=1)
        b.resize((b.width*2,b.height*2),Image.LANCZOS).save(f'review/work/r{i:02d}{"ab"[j]}.png')

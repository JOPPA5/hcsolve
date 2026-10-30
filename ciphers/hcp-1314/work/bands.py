from PIL import Image
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
n=Image.open(O+'desk.png')
for k,y in enumerate(range(240,2000,300)):
    for s,x in (('A',60),('B',740)):
        n.crop((x,y,x+720,y+360)).resize((1440,720),Image.LANCZOS).save(O+f'band{k}{s}.png')

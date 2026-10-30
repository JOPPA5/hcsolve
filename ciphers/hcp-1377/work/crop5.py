from PIL import Image
r=Image.open('reading.png')
b={'el':(325,545,520,640,5),'nl':(190,470,450,560,4)}
for k,(a,b1,c1,d,s) in b.items():
    c=r.crop((a,b1,c1,d)); c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
im=Image.open('hires/pc_hcp_58_adr.JPG').convert('RGB')
c=im.crop((1330,100,1680,450)).resize((1050,1050),Image.LANCZOS); c.save('crops/stamp.png')

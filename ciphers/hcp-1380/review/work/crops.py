from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
im.resize((im.width//2,im.height//2)).save('review/work/full.jpg')
c=im.crop((60,300,820,1140)).rotate(90,expand=True)
c.save('review/work/msg.png')
print(c.size)
for i in range(0,8):
    y=20+i*88-20
    x=c.crop((0,max(0,y),c.width,y+150)); x=x.resize((x.width*2,x.height*2),Image.LANCZOS); ImageEnhance.Contrast(x).enhance(1.6).save(f'review/work/r{i+1}.png')

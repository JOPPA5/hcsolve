from PIL import Image
im=Image.open('work/hires/pc_hcp_54_adr.JPG').rotate(90,expand=True).convert('RGB')
R={'z_nicely':(370,1250,620,1400),'z_usual':(900,1385,1110,1490),'z_going':(610,1160,860,1290),'z_L':(150,1540,250,1630)}
for k,b in R.items():
    c=im.crop(b);c.resize((c.width*7,c.height*7),Image.BICUBIC).save(f'review/work/{k}.png')

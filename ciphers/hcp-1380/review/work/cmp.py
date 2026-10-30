from PIL import Image
c=Image.open('review/work/flat.png')
# bn on this card, plus raw (no flat) at 8x
raw=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB').crop((60,300,820,1140)).rotate(90,expand=True)
raw.crop((590,45,720,120)).resize((130*7,75*7),Image.LANCZOS).save('review/work/raw_bn.png')
raw.crop((560,130,640,200)).resize((80*8,70*8),Image.LANCZOS).save('review/work/raw_be.png')
raw.crop((410,225,600,300)).resize((190*5,75*5),Image.LANCZOS).save('review/work/raw_dpef.png')
# postmark
im=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB').crop((1270,120,1480,350)); im.resize((630,690)).save('review/work/pm.png')

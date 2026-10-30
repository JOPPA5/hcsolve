from PIL import Image
raw=Image.open('work/hires/pc_hcp_61_adr.JPG').convert('RGB')
raw.crop((1350,170,1600,340)).resize((1000,680),Image.LANCZOS).save('review/work/pm2.png')
r=raw.crop((60,300,820,1140)).rotate(90,expand=True)
r.crop((490,125,640,215)).resize((150*7,90*7),Image.LANCZOS).save('review/work/raw_be2.png')

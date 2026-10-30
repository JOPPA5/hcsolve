from PIL import Image
r=Image.open('reading.png')
b={'l2':(100,130,860,260),'l3':(120,235,960,370),'l4':(170,350,950,490),'l5':(30,460,920,570),'l6':(20,540,900,690)}
for k,v in b.items():
    c=r.crop(v); c.resize((c.width*2,c.height*2),Image.LANCZOS).save(f'crops/{k}.png')

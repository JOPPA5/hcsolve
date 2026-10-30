from PIL import Image
r=Image.open('reading.png')
b={'cjlf':(125,240,320,385,5),'nz':(30,465,160,560,6),'gspn':(460,480,660,570,5),'zpvs':(710,475,920,565,5),'head':(190,35,820,140,3),'bn':(270,155,350,225,6)}
for k,(a,b1,c1,d,s) in b.items():
    c=r.crop((a,b1,c1,d)); c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')

from PIL import Image
r=Image.open('r2/r46.png')
for k,b,z in [('Z5',(1180,1370,1660,1560),4),('Z6',(1700,620,2000,790),4)]:
    c=r.crop(b); c.resize((c.width*z,c.height*z),Image.LANCZOS).save('r2/%s.png'%k)

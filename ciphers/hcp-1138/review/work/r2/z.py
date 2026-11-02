from PIL import Image
r=Image.open('r2/r46.png')
# row 10 akkorra zone; row 8-9 plain 9s; row 6 lehec 2
for k,b,z in [('Z1',(1080,1330,1500,1470),4),('Z2',(1880,1190,2560,1400),3),('Z3',(1830,1000,2100,1130),4),('Z4',(550,1120,800,1260),4)]:
    c=r.crop(b); c.resize((c.width*z,c.height*z),Image.LANCZOS).save('r2/%s.png'%k)

import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L')
reg=im.crop((0,0,1560,2298)).rotate(90,expand=True)  # CCW: rightmost col -> top row
reg.save(sys.argv[2]+'/rot.png')
w,h=reg.size
print(w,h)
# strips of height 200 overlapping
n=0
for y in range(0,h,190):
    for x0 in (0,1150):
        s=reg.crop((x0,y,min(w,x0+1250),min(h,y+220)))
        s=s.resize((s.width*1,s.height*1))
        s.save(sys.argv[2]+'/r%02d_%d.png'%(n,x0//1150))
    n+=1

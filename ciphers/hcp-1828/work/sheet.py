from PIL import Image, ImageDraw
im=Image.open('hires/pc_hcp_509_adr.JPG').convert('RGB')
# name, center x,y in hires; 90x90 box
X=[('R2 from r',560,350),('R3 with i',0,0)]
import sys
items={
'x':[('R2',555,360),('R3',735,445),('R4',785,540),('R6lineX',480,705),('R6ruinI',705,705),('R7or',105,760),('R7inI',870,775),('R8anyX',215,865),('R10for',205,1055),
     ('R4O',455,535),('R6O',870,700),('R9O',750,950),('R2',555,345)],
'y':[('R2',500,350),('R3a',0,0)]}
def sheet(lst,fn,box=62,sc=4,cols=5):
    w=box*2*sc; S=Image.new('RGB',(cols*w,((len(lst)+cols-1)//cols)*w),'white')
    for i,(n,x,y) in enumerate(lst):
        c=im.crop((x-box,y-box,x+box,y+box)).resize((w,w),Image.LANCZOS)
        ImageDraw.Draw(c).text((4,4),n,fill=(255,0,0))
        S.paste(c,((i%cols)*w,(i//cols)*w))
    S.save(fn)
sheet(items['x'][:-1],'crops/sheet_x.png')
T=[('R1d',395,290),('R3t',665,440),('R4t',505,540),('R5t get-e',235,615),('R5t',410,615),('R7t',368,775),('R7t',718,780),('R8t',325,865),('R8d send',685,865),('R9t',250,950),('R9d',680,950),('R10t',905,1060),
   ('R4c2bar',565,540),('R5c',600,615),('R7c',570,775),('R9c',870,950)]
sheet(T,'crops/sheet_t.png',box=50,sc=4,cols=6)
sheet([('R10 r',205,1055)],'crops/r10eye.png',box=50,sc=8,cols=1)
c=im.crop((290,420,560,510)).resize((1080,360),Image.LANCZOS);c.save('crops/v.png')

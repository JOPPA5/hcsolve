from PIL import Image,ImageOps
import sys
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/'
im=Image.open(B+'work/hires/pc_hcp_62_adr.JPG').convert('RGB')
c=im.crop((70,120,1000,1110)).rotate(90,expand=True).split()[1]
def sv(n,box,s=5,lo=130,hi=225):
    x=c.crop(box).point(lambda v:max(0,min(255,int((v-lo)*255/(hi-lo)))))
    x.resize((x.width*s,x.height*s),Image.BICUBIC).save(B+'review/work/'+n+'.png')
sv('z7',(590,700,760,800),6)
sv('z7b',(760,700,960,800),5)
sv('z2',(320,230,640,320),4)
sv('z2b',(640,230,960,320),4)
sv('z8a',(30,750,500,850),3)
sv('z8b',(500,780,970,870),3)
sv('z6',(290,620,640,720),4)
sv('z6b',(640,630,960,730),4)
sv('y7',(670,700,830,800),6)
sv('y6',(420,640,620,760),5)
sv('y3',(520,330,700,420),6,120,225)
sv('y3b',(690,340,860,440),5,120,225)
sv('y4',(310,410,600,540),4,120,225)
sv('y4b',(600,420,860,540),4,120,225)
sv('y2',(660,240,960,340),4,120,225)
sv('x78',(590,690,800,870),5,130,225)

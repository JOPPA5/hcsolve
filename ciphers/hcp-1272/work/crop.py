import sys
from PIL import Image
im=Image.open('hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
S=1.7225
def c(n,x0,y0,x1,y1,z=2):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%n)
# rows in display coords
tops=[60,115,165,220,280,345,405,465,525,590,640,690,755,810,870,925,985,1040,1090,1135]
for i in range(0,17,3):
    y0=tops[i]-10; y1=tops[min(i+3,19)]+15
    c('L%02d'%(i+1),40,y0,500,y1)
    c('R%02d'%(i+1),460,y0,960,y1)
c('B1',40,1090,700,1190); c('B2',650,1090,1300,1190); c('B3',1250,1090,1880,1190)
c('adr',1300,790,1880,860); c('stamp',1540,160,1820,460,3)

import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/crops/'
# display coords *1.72
def c(n,x0,y0,x1,y1,s=3):
    b=[int(v*1.72) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save(out+n+'.png')
ys=[(55,135),(135,215),(215,295),(295,375),(375,455),(455,535),(535,615),(615,695),(695,775),(775,855),(855,935),(935,1015),(1015,1095),(1095,1190)]
for i,(a,b) in enumerate(ys):
    c(f'L{i:02d}a',40,a,500,b,2) if False else None
    c(f'L{i:02d}a',40,a,500,b); c(f'L{i:02d}b',480,a,960,b)
c('corner',1560,80,1840,380,4)
ys=[72,118,152,205,236,295,348,408,462,520,562,622,672,712,755,800,855,912,970,1040,1100,1155]
for i,y in enumerate(ys,1):
    c(f'R{i:02d}a',40,y-42,500,y+42); c(f'R{i:02d}b',480,y-42,960,y+42)

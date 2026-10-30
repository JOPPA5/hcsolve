import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1289/work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1289/work/crops/'
S=1.72
def crop(name,x0,y0,x1,y1,z=2.5):
    b=tuple(int(v*S) for v in (x0,y0,x1,y1))
    c=im.crop(b); c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS); c.save(out+name+'.png')
if __name__=='__main__':
    # main block: 4 rows per band, two halves
    bands=[(40,110),(100,180),(170,250),(240,320),(310,390),(380,450),(440,520),(510,590),(580,650),(640,720),(710,790),(780,850),(840,920),(910,990),(980,1050)]
    for i,(a,b) in enumerate(bands):
        crop(f'b{i:02d}L',35,a,480,b); crop(f'b{i:02d}R',460,a,950,b)
    for i,(a,b) in enumerate([(1045,1120),(1100,1170),(1150,1215)]):
        for j,(x,y) in enumerate([(35,520),(500,1000),(980,1460),(1440,1920)]):
            crop(f'f{i}{j}',x,a,y,b)
    crop('stamp',1550,140,1810,420,3.5)

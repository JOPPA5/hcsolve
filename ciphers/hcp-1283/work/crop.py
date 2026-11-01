import sys
from PIL import Image
f='ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB')
k=3445/1024
def c(n,x0,y0,x1,y1,s=2):
    r=im.crop((int(x0*k),int(y0*k),int(x1*k),int(y1*k)))
    r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('ciphers/hcp-1283/work/crops/%s.png'%n); print(n,r.size)
if __name__=='__main__':
    # strips of 3 rows, left and right halves
    y=20;i=0
    while y<610:
        c('L%02d'%i,15,y,230,y+70,2); c('R%02d'%i,215,y,440,y+70,2); y+=60;i+=1
    c('stamp',790,40,930,215,4)
    c('bottom1',15,560,450,615,2); c('bottom2',440,560,880,615,2)

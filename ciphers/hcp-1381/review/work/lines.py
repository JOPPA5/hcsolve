from PIL import Image,ImageOps
B='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1381/'
im=Image.open(B+'work/hires/pc_hcp_62_adr.JPG').convert('RGB')
c=im.crop((70,120,1000,1110)).rotate(90,expand=True)
print(c.size)
r=c.split()[0]
def sv(n,box,s=3):
    x=r.crop(box); x=ImageOps.autocontrast(x,cutoff=(1,1))
    x.resize((x.width*s,x.height*s),Image.LANCZOS).save(B+'review/work/'+n+'.png')
L={'l2':(300,230,1040,350),'l3':(300,310,1040,430),'l4':(300,400,1040,540),'l5':(300,510,1040,640),'l6':(300,620,1040,740),'l7':(300,700,1040,810),'l8':(60,770,1040,890)}
for k,v in L.items():
    w=v[2]-v[0]
    # split in halves
    m=(v[0]+v[2])//2
    sv(k+'a',(v[0],v[1],m+30,v[3]),3); sv(k+'b',(m-30,v[1],v[2],v[3]),3)

from PIL import Image, ImageDraw
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
s=1785/1014
def z(n,x,y,r,f=6,ry=None):
    ry=ry or r
    c=im.crop((int((x-r)*s),int((y-ry)*s),int((x+r)*s),int((y+ry)*s)));c=c.resize((c.width*f,c.height*f),Image.BICUBIC);c.save(n);return c
L=[('R7e',59,436),('R10e',127,592),('R2e',314,207),('R4e2',415,304),('R7x',499,440),('R6x2',414,398)]
W=[z('/dev/null.png' if 0 else f'crops/z{l}.png',x,y,20,6,26) for l,x,y in L]
w,h=W[0].size
sh=Image.new('RGB',(w*6,h),'white')
for i,c in enumerate(W): sh.paste(c,(i*w,0))
sh=sh.resize((sh.width*2//3,sh.height*2//3)); sh.save('crops/lens.png')
z('crops/surname.png',780,395,150,3,45)
z('crops/sussex.png',800,590,100,3,35)
z('crops/jan.png',570,580,70,4,45)

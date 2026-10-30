from PIL import Image
d='ciphers/hcp-1340/'
a=Image.open(d+'work/hires/pc_hcp_21_adr.JPG'); p=Image.open(d+'work/hires/pc_hcp_21_pic.JPG')
def z(im,box,n,f=8):
    c=im.crop(box); c=c.resize((c.width*f,c.height*f),Image.BICUBIC); c.save(d+'review/work/z_'+n+'.png')
z(a,(790,620,890,740),'nett',7)
z(a,(800,480,890,540),'schatz',7)
z(a,(170,525,250,590),'hae')
z(a,(560,700,700,790),'braeut',6)
z(a,(450,640,560,700),'war')
z(p,(720,800,860,870),'gekuesst',6)
m=p.crop((1620,226,1717,840)).rotate(90,expand=True)
c=m.crop((60,0,200,97)); c.resize((c.width*7,c.height*7),Image.BICUBIC).save(d+'review/work/z_gruss.png')
z(p,(1600,110,1717,250),'corner',6)
z(p,(150,150,290,760),'leftmargin',2)
z(a,(950,340,1250,520),'addrmark',3)
z(p,(60,860,1700,1110),'plain',1)

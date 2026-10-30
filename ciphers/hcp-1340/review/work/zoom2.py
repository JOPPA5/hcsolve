from PIL import Image
d='ciphers/hcp-1340/'
a=Image.open(d+'work/hires/pc_hcp_21_adr.JPG'); p=Image.open(d+'work/hires/pc_hcp_21_pic.JPG')
def z(im,box,n,f=8):
    c=im.crop(box); c=c.resize((c.width*f,c.height*f),Image.BICUBIC); c.save(d+'review/work/z_'+n+'.png')
z(a,(790,715,880,790),'nett',7)
z(a,(453,715,560,775),'war',7)
z(a,(560,770,700,830),'braeut',6)
p.crop((150,150,290,760)).rotate(90,expand=True).resize((610*2,140*2)).save(d+'review/work/z_leftmargin.png')

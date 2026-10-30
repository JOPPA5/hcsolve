from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
a=im.crop((55,40,900,390)).rotate(180,expand=True)
def s(n,box,sc=8,rot=0):
    c=a.crop(box)
    if rot: c=c.rotate(rot,expand=True,fillcolor=(235,215,180))
    c=ImageEnhance.Contrast(c).enhance(1.5)
    c.resize((c.width*sc,c.height*sc),Image.BICUBIC).save('review/work/crops/'+n)
s('with.png',(745,265,845,340),10)
s('with_rot.png',(745,265,845,345),10,rot=25)
s('carrie.png',(690,295,830,350),8)
s('soun.png',(300,225,440,290),8)
s('side_end.png',(30,0,60,10),2)

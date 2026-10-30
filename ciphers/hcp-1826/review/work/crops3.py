from PIL import Image, ImageEnhance
P='review/work/crops/'
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
a=im.crop((55,40,900,390)).rotate(180,expand=True)
c=ImageEnhance.Contrast(a.crop((550,290,720,350))).enhance(1.5)
c.resize((c.width*7,c.height*7),Image.BICUBIC).save(P+'sig.png')
# comparison panel: corner word (rotated to level) vs X exemplars / with exemplar
w=a.crop((745,265,845,345)).rotate(25,expand=True,fillcolor=(235,215,180))
s=Image.open(P+'side_all.png')
# exemplars from level rows
ex={'that_S03':(610,195,790,245),'with_S11':(135,655,310,700),'want_T2':(40,70,185,105)}
pan=Image.new('RGB',(1100,1050),'white')
y=0
w2=ImageEnhance.Contrast(w).enhance(1.4).resize((w.width*6,w.height*6),Image.BICUBIC); pan.paste(w2,(0,0)); 
y=w2.height+10
for k,b in ex.items():
    src=s if k[-3]=='S' else a
    c=src.crop(b); c=c.resize((c.width*4,c.height*4),Image.BICUBIC); pan.paste(c,(0,y)); y+=c.height+8
pan=pan.crop((0,0,1100,y)); pan.save(P+'with_compare.png')
# postmark, stamp side and pencil name
pm=im.crop((1180,70,1450,360)); ImageEnhance.Contrast(pm).enhance(2).resize((810,870)).save(P+'postmark.png')
pi=Image.open('work/hires/pc_hcp_507_pic.JPG').convert('RGB')
n=pi.crop((60,300,240,740)).rotate(90,expand=True); ImageEnhance.Contrast(n).enhance(3).resize((n.width*2,n.height*2)).save(P+'pencil.png')

from PIL import Image
m=Image.open('rot.png').convert('RGB').crop((180,965,1080,1725))
print(m.size)
L={'a_head':(20,20,850,125),'b_l1':(170,110,800,210),'c_l2':(170,205,830,330),'d_l3':(190,300,760,430),
'e_l4':(230,400,830,530),'f_l5':(200,500,860,640),'g_l6':(150,580,860,690),'h_l7':(230,660,800,740)}
for k,b in L.items():
    c=m.crop(b); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(k+'.png')

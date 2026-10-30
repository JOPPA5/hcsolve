from PIL import Image
m=Image.open('msg.png').convert('RGB')
# seg coords -> msg: seg0 x/2,y/2; seg1 x/2+310; seg2 x/2+660
Z={'n_l1':(30,100,280,270,4),'pxo_el':(420,170,780,270,4),'el_l1':(640,190,800,270,6),
'x_wait':(170,420,560,540,4),'lett':(650,350,1030,440,4),'wait2':(380,430,620,520,5),
'ml':(30,620,300,740,4),'el_end':(860,640,1040,730,5),'hjsm':(830,720,1030,830,5),
'j':(170,330,330,440,4),'kvtu':(190,260,420,340,4),'come':(420,250,720,350,4),'back':(700,270,960,360,4),'line5':(240,540,1000,660,2)}
for k,(a,b,c,d,s) in Z.items():
    r=m.crop((a,b,c,d)); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'z_{k}.png')
# montage

from PIL import Image
o=Image.open('rot.png').convert('RGB')
m=o.crop((180,965,1080,1725))
L={'z1_px':(330,120,560,205,6),'z2_jt':(190,210,340,330,6),'z3_xbt':(320,220,480,300,6),'z4_jut':(210,520,410,640,5),
'z5_zpvs':(620,600,860,690,6),'z6_girl':(470,680,800,740,6),'z7_hrs':(300,320,450,370,7),'z8_cf':(460,300,600,430,6),'z9_oh':(590,410,830,510,5),'z10_gspn':(460,600,640,690,6)}
for k,(a,b,c,d,s) in L.items():
    x=m.crop((a,b,c,d)); x.resize((x.width*s,x.height*s),Image.LANCZOS).save(k+'.png')
# postmark in rotated frame
p=o.crop((60,60,420,420)).rotate(-90 ,expand=True); p=p.resize((p.width*3,p.height*3),Image.LANCZOS); p.save('z11_pm.png')

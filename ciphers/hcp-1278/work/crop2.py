from PIL import Image
im=Image.open('hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
f=1.72
B={'a16l':(40,1090,260,1200,4),'a16m':(240,1090,560,1200,3),'a16r':(540,1090,890,1200,3),'a15l':(40,1040,260,1120,4),'a14e':(600,985,880,1060,3),
'a07m':(280,510,480,575,4),'a12s':(40,850,300,915,4),'a08e':(620,575,880,650,3),'a09m':(240,650,560,710,3),'stamp':(1520,120,1830,450,3),'a03b':(40,190,260,262,4),'a02b':(280,120,480,195,4)}
for k,(l,t,r,b,s) in B.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)));c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
c=im.crop((int(1520*f),int(120*f),int(1830*f),int(450*f))).rotate(-90,expand=True);c.resize((c.width*2,c.height*2)).save('crops/stamp_rot.png')

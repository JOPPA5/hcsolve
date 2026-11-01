from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1263/work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg')
B={'r6':(620,560,1000,680),'r7':(740,640,1460,770),'r8a':(80,730,620,850),'r8b':(560,730,1100,850),'r8c':(1040,730,1600,850),
'r16':(800,1450,1480,1570),'r19':(780,1740,1540,1860),'r20':(80,1840,700,1960),'r21a':(100,1920,860,2070),'r21b':(800,1920,1660,2070),'r14':(480,1270,1300,1370),'r15':(80,1330,1000,1460)}
for k,b in B.items():
    c=im.crop(b); f=min(4,2000/c.width); c.resize((int(c.width*f),int(c.height*f)),Image.LANCZOS).save('crops/'+k+'.png')
# stack
names=['r6','r7','r8a','r8b','r8c','r16']
for g,ns in {'s1':['r6','r7','r8a'],'s2':['r8b','r8c','r16'],'s3':['r19','r20','r21a','r21b'],'s4':['r14','r15']}.items():
    ims=[Image.open('crops/'+n+'.png') for n in ns]; W=max(i.width for i in ims);H=sum(i.height+10 for i in ims)
    s=Image.new('RGB',(W,H),'white');y=0
    for i in ims: s.paste(i,(0,y)); y+=i.height+10
    s.save('crops/'+g+'.png')

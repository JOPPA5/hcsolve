from PIL import Image, ImageDraw
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_adr.jpg').convert('RGB')
def sheet(name,items,s=5,cols=3):
    t=[]
    for lab,b in items:
        r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
        c=Image.new('RGB',(r.width,r.height+24),'white'); c.paste(r,(0,24)); ImageDraw.Draw(c).text((4,4),lab,fill='black'); t.append(c)
    w=max(c.width for c in t)+10;h=max(c.height for c in t)+10
    rows=(len(t)+cols-1)//cols
    S=Image.new('RGB',(w*cols,h*rows),'white')
    for i,c in enumerate(t): S.paste(c,((i%cols)*w,(i//cols)*h))
    S.save('crops/'+name+'.png')
sheet('dh',[('R5 de?',(520,410,640,490)),('R6 de',(500,490,600,560)),('R8 he?',(750,670,860,755)),('R13 de',(260,1105,360,1190)),('R7 hogy',(1190,590,1290,690)),('R16 ed',(150,1370,250,1450)),('R18 nap',(690,1555,800,1640)),('R19 hogy',(420,1640,520,1760)),('R17 hogy',(330,1500,450,1600))],5)
sheet('r22',[('R22 a',(1100,1900,1700,2045)),('R22 b',(1650,1900,2300,2045)),('R22 c',(2250,1900,2700,2045))],3,1)
sheet('misc',[('R14 blot',(670,1170,780,1260)),('R14 od',(560,1160,700,1260)),('R20 first',(90,1800,190,1880)),('R20 over',(950,1730,1090,1860)),('R3 dj',(370,240,520,330)),('7',(2730,530,2800,610)),('R1 j',(880,90,1010,190)),('C5 j',(2720,430,2800,500)),('C1 ve+',(2840,190,3010,270)),('C4 ve',(2680,330,3010,420)),('R20/j R7 j',(200,590,300,680)),('R8 j',(420,670,520,760))],4)

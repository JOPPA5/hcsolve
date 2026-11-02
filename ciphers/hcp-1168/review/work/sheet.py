import sys,glob
from PIL import Image,ImageDraw
A=glob.glob('../../work/hires/*_adr.jpg')[0]
im=Image.open(A).convert('RGB')
def sheet(items,out,s=5,cols=4):
    t=[]
    for n,b in items:
        c=im.crop(b);c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
        d=ImageDraw.Draw(c);d.text((4,4),n,fill=(200,0,0));t.append(c)
    w=max(c.width for c in t);h=max(c.height for c in t);r=(len(t)+cols-1)//cols
    S=Image.new('RGB',(w*cols,h*r),'white')
    for i,c in enumerate(t):S.paste(c,((i%cols)*w,(i//cols)*h))
    S.save(out)
sheet([('7. viszonyok',(380,340,470,420)),('7. sokszor',(226,1975,316,2065)),('? szereto',(1955,1965,2045,2060)),('4. hogy L02',(860,150,950,235)),('4. egy L13',(300,1215,390,1300)),('4. egy L15',(845,1395,935,1480)),('4. hogy L06',(530,525,620,600)),('7 kedvesed',(2330,1975,2420,2065))],'cmp_sz.png')
sheet([('ud..o1 9',(575,1970,690,2075)),('o2 + 9,',(690,1970,830,2075)),('9 par L06',(1050,510,1140,600)),('9 pár L15',(1020,1400,1110,1490)),('0, belole',(190,1120,330,1200)),('0, szereto',(2150,1970,2260,2070)),('9 Arpad',(250,1450,330,1560)),('9 cipore',(560,1090,680,1190))],'cmp_oe.png',s=4)

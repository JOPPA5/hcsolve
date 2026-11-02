import glob
from PIL import Image, ImageEnhance, ImageDraw
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
def sheet(name,items,s=5,W=2000):
    tiles=[]
    for lab,b in items:
        r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.BICUBIC); r=ImageEnhance.Contrast(r).enhance(1.5)
        ImageDraw.Draw(r).text((4,4),lab,fill=(255,0,0)); tiles.append(r)
    rows=[[]]; x=0
    for t in tiles:
        if x+t.width>W: rows.append([]); x=0
        rows[-1].append(t); x+=t.width+10
    H=sum(max(t.height for t in r)+10 for r in rows)
    o=Image.new('RGB',(W,H),'white'); y=0
    for r in rows:
        x=0
        for t in r: o.paste(t,(x,y)); x+=t.width+10
        y+=max(t.height for t in r)+10
    o.save(name)
sheet('m1.png',[('lassan',(1270,330,1450,440)),('szolt',(380,600,560,710)),('uzlet',(2200,400,2540,520)),('Lubi',(1370,550,1600,650))])
sheet('m2.png',[('fiu',(60,450,280,530)),('utolert',(460,440,620,520)),('ertunk',(240,520,420,600)),('bubaj',(400,890,640,1000)),('hu',(620,1830,760,1890)) ,('kedvesed',(720,1890,860,1990))])
sheet('m3.png',[('igaz',(1300,1790,1560,1900)),('arad',(1230,1315,1540,1410)),('labad',(1450,1470,1700,1570)),('kezed',(570,735,680,795))],s=4)
sheet('m4.png',[('postmark',(2470,350,3180,860))],s=2)
sheet('m5.png',[('addr',(1650,480,2150,800))],s=2)

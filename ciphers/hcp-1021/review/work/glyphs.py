import sys, json
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('L')
t=json.load(open(sys.argv[2]))
order=list(range(29,0,-1))
boxes={g['id']:g['box'] for r in t['rows'] for g in r['glyphs']}
tiles=[]
for gid in order:
    x0,y0,x1,y1=boxes[gid]
    c=im.crop((x0-4,y0-5,x1+4,y1+8)).rotate(180)
    c=ImageOps.autocontrast(c,cutoff=1).resize(((c.size[0])*6,(c.size[1])*6),Image.LANCZOS)
    tiles.append((gid,c))
# 2 sheets
for s in range(3):
    part=tiles[s*10:(s+1)*10]
    W=sum(c.size[0]+20 for _,c in part); H=max(c.size[1] for _,c in part)+40
    sheet=Image.new('L',(W,H),255)
    from PIL import ImageDraw
    d=ImageDraw.Draw(sheet); x=0
    for gid,c in part:
        sheet.paste(c,(x,40)); d.text((x+5,5),str(gid),fill=0); x+=c.size[0]+20
    sheet.save(f"sheet{s}.png")

import sys
from PIL import Image
im=Image.open(sys.argv[1]); out=sys.argv[2]
rows={"T01":(26,57),"T02":(50,85),"T03":(74,111),"T04":(97,139),"T05":(122,164),
"B01":(507,540),"B02":(531,568),"B03":(556,593),"B04":(582,621),"B05":(608,639)}
xs=[(35,290),(280,535),(525,780),(770,985)]
for r,(y0,y1) in rows.items():
    tiles=[im.crop((a,y0,b,y1)) for a,b in xs]
    sc=4
    W=max(t.width for t in tiles)*sc; H=sum(t.height for t in tiles)*sc
    can=Image.new("RGB",(W,H),"white"); y=0
    for t in tiles:
        t=t.resize((t.width*sc,t.height*sc),Image.LANCZOS); can.paste(t,(0,y)); y+=t.height
    can.save(f"{out}/seg_{r}.png")

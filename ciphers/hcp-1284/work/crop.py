import sys
from PIL import Image
im=Image.open(sys.argv[1]); 
# rows: display y ranges; two halves
rows=[(70,115),(120,175),(180,235),(240,305),(310,370),(385,445),(440,490),(515,565),(575,640),(640,695),(710,770),(775,830),(835,895),(900,960),(960,1035),(1040,1095),(1095,1160),(1135,1205)]
for i,(a,b) in enumerate(rows,1):
    c=im.crop((int(50*1.72),int((a-8)*1.72),int(480*1.72),int((b+8)*1.72))); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'work/crops/r{i:02d}a.png')
    c=im.crop((int(440*1.72),int((a-8)*1.72),int((1400 if i>=17 else 950)*1.72),int((b+8)*1.72)));
    s=2 if i<17 else 1; c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(f'work/crops/r{i:02d}b.png')
c=im.crop((int(1520*1.72),int(120*1.72),int(1800*1.72),int(400*1.72))); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('work/crops/stamp.png')

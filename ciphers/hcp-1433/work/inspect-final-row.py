#!/usr/bin/env python3
"""Reproduce a diagnostic crop and color screen; no automatic transcription.
Run with a Python environment providing Pillow. Every coordinate is a manual
observation in the source rotated 180 degrees, not a recognized Morse token.
"""
from pathlib import Path
import hashlib,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
im=Image.open(root/'source/address.jpg').rotate(180)
box=(535,405,940,487)
raw=im.crop(box).convert('RGB')
raw.resize((1620,328)).save(root/'work/final-row-original.png')
# Red print has a stronger red-minus-blue component than the dark pen ink.
# This heuristic can also suppress pen edges and cannot restore hidden marks.
screen=raw.copy();pix=[]
for r,g,b in raw.getdata():
    strength=max(0,165-(r+g+b)/3)
    strength=max(0,strength-max(0,r-b-10)*3)
    v=round(255-min(255,strength*2.5));pix.append((v,v,v))
screen.putdata(pix)
screen.resize((1620,328)).save(root/'work/final-row-color-screen.png')
marks=[(555,427,'.'),(581,431,'-'),(608,438,'.'),(626,440,'.'),
       (654,441,'-'),(676,442,'-'),(697,446,'-'),(744,453,'.'),
       (770,456,'-'),(800,460,'.'),(823,462,'.'),(853,463,'.')]
view=raw.resize((1620,328));draw=ImageDraw.Draw(view)
for n,(x,y,kind) in enumerate(marks,1):
    a=(x-box[0])*4;b=(y-box[1])*4
    draw.rectangle((a-12,b-13,a+12,b+13),outline='blue',width=2)
    draw.text((a-13,b-32),f'{n} {kind}',fill='blue')
view.save(root/'work/final-row-mark-map.png')
(root/'work/final-row-observations.json').write_text(json.dumps({
 'status':'provisional manual mark inventory; no letter grouping established',
 'coordinates':'pixels after rotating original address.jpg 180 degrees',
 'marks':[dict(x=x,y=y,shape=k) for x,y,k in marks],
 'limitations':['long slashes intersect adjacent rows',
 'some points coincide with slash terminals',
 'red printed stationery overlaps the pen marks',
 'color screen is a heuristic and not independent evidence']},indent=2)+'\n')
print('Diagnostic views saved. No letters added to the frozen transcript.')

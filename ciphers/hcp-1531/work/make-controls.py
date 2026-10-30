#!/usr/bin/env python3
"""Explicit source-pixel crop generator; requires Pillow, unlike decode.py."""
from pathlib import Path
from PIL import Image,ImageDraw
import json
R=Path(__file__).resolve().parents[1];W=R/'work';im=Image.open(R/'source/picture.jpg');rec=json.loads((W/'transcription.json').read_text())
indexed=im.copy();d=ImageDraw.Draw(indexed)
for row in rec['rows']:
 b=row['box_source_xyxy'];d.rectangle(b,outline='red',width=1);d.text((b[0]-24,b[1]),row['id'],fill='red')
 cr=im.crop(b);cr.resize((cr.width*4,cr.height*4)).save(W/(row['id']+'.png'))
indexed.save(W/'indexed.png')
controls=[
 ('C01 R05 first word: s/C versus 1/Y; compare R14 CO and R09 NYNI',(583,143,724,184)),
 ('C02 R14 CO: triangular s/C shape',(568,536,613,577)),
 ('C03 R09 NYNI: digit1/Y control',(799,257,882,288)),
 ('C04 R05 BYLA: p/B class (not n/M)',(720,145,786,186)),
 ('C05 R07 ULEHNOUTI: h/H partly darkened by photograph',(799,204,956,241)),
 ('C06 R10 ZAHRNIT: penultimate 4/I retained',(673,423,823,464)),
 ('C07 R02 SVEMU: final 2/U comparison',(887,72,969,107)),
 ('C08 R08 MI: 4/I comparison',(659,231,687,267)),
 ('C09 R12 PSANI: photograph overlap',(661,483,800,523)),
 ('C10 R13 ODESLU: photograph overlap',(661,513,771,550)),
 ('C11 R16 NEOCISLNE KRATE: literal spelling',(558,590,792,626)),
 ('C12 R17 HLAVINKU LIBA: closing, not signature',(478,612,730,645)),
]
sc=4;gap=36;width=max((b[2]-b[0])*sc for _,b in controls);height=sum((b[3]-b[1])*sc+gap for _,b in controls)
out=Image.new('RGB',(width,height),'white');dr=ImageDraw.Draw(out);yy=0
for name,b in controls:
 dr.text((2,yy+3),name,fill='black');cr=im.crop(b).resize(((b[2]-b[0])*sc,(b[3]-b[1])*sc));out.paste(cr,(0,yy+gap));yy+=gap+cr.height
out.save(W/'focused-controls.png');(W/'focused-controls.json').write_text(json.dumps([{'label':n,'box_source_xyxy':b} for n,b in controls],indent=2)+'\n')

items=[('R05 V?EREJSKA unresolved 1/Y or s/C',(583,143,724,184)),('R05 BYLA: same row 1/Y',(720,145,786,186)),('R01 DRAHY: final1/Y',(770,37,837,79)),('R16 NEOCISLNE: C=s class',(558,590,729,626)),('R10 ZAHRNIT: prefinal4/I',(673,423,823,464)),('R10 KTEROU: final2/U',(864,426,954,465)),('R08 MI: final4/I',(659,231,687,267)),('R12 PSAN?: unresolved final unit',(661,483,800,523))]
scale=4;pw=720;ph=210;out=Image.new('RGB',(pw*2,ph*4),'white');d=ImageDraw.Draw(out)
for i,(label,b) in enumerate(items):
 x=(i%2)*pw;y=(i//2)*ph;d.text((x+3,y+4),label,fill='black');cr=im.crop(b).resize(((b[2]-b[0])*scale,(b[3]-b[1])*scale));out.paste(cr,(x,y+40))
out.save(W/'side-by-side-controls.png');(W/'side-by-side-controls.json').write_text(json.dumps([{'label':s,'box_source_xyxy':b} for s,b in items],indent=2)+'\n')

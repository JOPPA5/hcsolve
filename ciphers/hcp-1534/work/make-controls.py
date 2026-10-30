from pathlib import Path
from PIL import Image,ImageDraw
import json
p=Path(__file__).resolve().parent; src=p.parent/'source/picture.jpg'
im=Image.open(src).transpose(Image.Transpose.ROTATE_90)
for row in json.loads((p/'transcription.json').read_text())['rows']:
 im.crop(row['box']).save(p/(row['id']+'.png'))
controls=[('U02 unresolved overink before MNE',(365,80,434,112)),('S01 VASKERI first-vowel 6',(506,240,616,275)),('S04 DOUFAL shallow-v F',(552,324,628,360)),('L01 MILAVANE middle-vowel 6',(239,900,367,935)),('S05 ZE DO TE t/D',(492,353,631,386)),('S12 SOTVA looped d/T',(570,547,635,583)),('U07 SCHUZI CH glyph',(197,211,294,245))]
sheet=Image.new('RGB',(800,len(controls)*180),'white'); d=ImageDraw.Draw(sheet)
for i,(name,box) in enumerate(controls):
 d.text((10,i*180+4),f'{name}; upright box={box}',fill='black')
 crop=im.crop(box);crop=crop.resize((crop.width*4,crop.height*4),Image.Resampling.NEAREST)
 sheet.paste(crop,(10,i*180+24))
sheet.save(p/'focused-controls.png')

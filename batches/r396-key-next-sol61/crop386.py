from pathlib import Path
from PIL import Image
import json,hashlib
B=Path(__file__).resolve().parent;s=Path('batches/solved-context-main/386/cipher.jpg');im=Image.open(s);boxes={'386-row3':(244,386,862,424),'386-row4':(244,423,862,459),'386-row5':(244,458,862,495),'386-row6':(244,494,862,532)}
for name,box in boxes.items():
 x=im.crop(box);x.resize((x.width*3,x.height*3),Image.Resampling.NEAREST).save(B/f'{name}.png')
(B/'386-crop-manifest.json').write_text(json.dumps({'source':str(s),'sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'boxes':boxes,'zoom':'3x nearest-neighbor','note':'independent pixel support only, public Solved386 context not own plaintext/key solution'},indent=2)+'\n')

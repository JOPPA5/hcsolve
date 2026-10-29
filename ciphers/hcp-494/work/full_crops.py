from PIL import Image
from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
boxes={'gap':('0004.jpg',(1150,1910,2460,2140)), 'margin-full':('0004.jpg',(80,1880,630,2220)), 'passage2-full':('0004.jpg',(530,2250,2340,2630)), 'signature-full':('0004.jpg',(1210,3480,2310,3860)), '625-gloss':('0003.jpg',(180,1090,750,1390)), 'key255-alphabet':('key255.jpg',(80,240,2500,1270))}
for name,(src,box) in boxes.items():
 im=Image.open(p/'source/full'/src);im.crop(box).save(p/f'work/{name}.png')
(p/'work/full-crops.json').write_text(json.dumps(boxes,indent=2))

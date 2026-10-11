from PIL import Image
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;src=Path('ciphers/hcp-351/source/cryptogram.jpg');im=Image.open(src);boxes={'group3-11-12':(420,412,520,455),'group15-73':(530,451,720,495),'group18-86':(799,451,893,495),'group47-231':(550,555,653,602)}
for name,box in boxes.items():
 crop=im.crop(box);crop.save(B/f'{name}-native.png');crop.resize((crop.width*6,crop.height*6),Image.Resampling.NEAREST).save(B/f'{name}-6x.png')
(B/'manifest.json').write_text(json.dumps({'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'image_size':im.size,'boxes':boxes,'enlargement':'6x nearest-neighbor, no enhancement or retouch','inspection':'post-review and after disclosure of parent/reviewer readings; not blind'},indent=2)+'\n')

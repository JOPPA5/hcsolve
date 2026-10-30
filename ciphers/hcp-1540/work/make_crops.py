from pathlib import Path
from PIL import Image
import json,hashlib
W=Path(__file__).resolve().parent;C=W.parent
r=json.loads((W/'record.json').read_text());im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90);a=Image.open(C/'source/address.jpg');manifest=[]
for row in r['rows']:
 if row['id'].startswith('A'):
  box=row['crop_address_xyxy'];crop=a.crop(box);orientation='original address image'
 else:
  box=row['crop_upright_xyxy'];crop=im.crop(box);orientation='picture ROTATE_90 counterclockwise'
  if row['id'].startswith('M'):crop=crop.transpose(Image.Transpose.ROTATE_180);orientation+=' then crop ROTATE_180'
 crop=crop.resize((crop.width*3,crop.height*3),Image.Resampling.NEAREST);fn='indexed-'+row['id']+'.png';crop.save(W/fn)
 manifest.append({'row':row['id'],'file':fn,'box':box,'orientation':orientation,'enlargement':'3x nearest neighbor','sha256':hashlib.sha256((W/fn).read_bytes()).hexdigest()})
(W/'crop-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

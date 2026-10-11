from pathlib import Path
from PIL import Image
import hashlib,json
B=Path(__file__).resolve().parent;R=B.parents[1];source=R/'ciphers/hcp-364/source/cryptogram.jpg';im=Image.open(source);regions={'body':(225,430,965,525),'group8':(309,477,398,515),'group10':(496,477,578,515),'group11-12':(585,477,759,515),'reply':(229,174,924,250)};records=[]
for name,box in regions.items():
 crop=im.crop(box);crop.resize((crop.width*4,crop.height*4),Image.Resampling.NEAREST).save(B/f'{name}-color.png');crop.getchannel('B').resize((crop.width*4,crop.height*4),Image.Resampling.NEAREST).save(B/f'{name}-blue-channel.png');records.append(dict(region=name,box_left_top_right_bottom=box,scale=4,resampling='nearest original pixels',blue_channel='literal B component of each original pixel; no generated strokes'))
(B/'image-provenance.json').write_text(json.dumps(dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source_dimensions=im.size,regions=records),indent=2));print(im.size)

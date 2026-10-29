"""Acquire public METS-listed thumbnails and build contact sheets for triage.

Thumbnails cannot support a final glyph reading. Selected original pages must
be acquired separately before using their letters/numbers as evidence.
"""
from pathlib import Path
import argparse,concurrent.futures,hashlib,json,subprocess,xml.etree.ElementTree as E
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--collection',choices=['239','206'],default='239');args=ap.parse_args()
tag='darmstadt'+args.collection
METS=ROOT/f'source/arcinsys/{tag}-mets.xml'
ns={'m':'http://www.loc.gov/METS/'};href='{http://www.w3.org/1999/xlink}href'
r=E.parse(METS).getroot()
urls=[x.attrib[href] for x in r.findall('.//m:fileGrp[@USE="THUMBS"]//m:FLocat',ns)]
out=ROOT/f'source/arcinsys/{tag}-thumbs';out.mkdir(exist_ok=True)
def fetch(url):
 p=out/url.rsplit('/',1)[1]
 if not p.exists():
  data=subprocess.check_output(['curl','-fsSL','--max-time','45','--retry','1',url])
  p.write_bytes(data)
 with Image.open(p) as im: im.verify()
 return {'url':url,'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,urls))
(ROOT/f'work/{tag}-thumbnails.json').write_text(json.dumps(rows,indent=2)+'\n')
for first in range(0,len(rows),40):
 sheet=Image.new('RGB',(1600,1500),'white');draw=ImageDraw.Draw(sheet)
 for k,row in enumerate(rows[first:first+40]):
  im=Image.open(ROOT/row['file']);im.thumbnail((190,270))
  x=(k%8)*200;y=(k//8)*300
  sheet.paste(im,(x+(190-im.width)//2,y+20));draw.text((x+5,y+3),Path(row['file']).stem.rsplit('_',1)[1],fill='black')
 sheet.save(ROOT/f'work/{tag}-contact-{first:03d}.jpg',quality=92)
print(json.dumps({'thumbnails':len(rows),'contact_sheets':(len(rows)+39)//40,'source_bytes':sum((ROOT/r['file']).stat().st_size for r in rows)}))

"""Download selected immutable original pages from the already acquired METS."""
from pathlib import Path
import argparse,hashlib,json,subprocess,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
ns={'m':'http://www.loc.gov/METS/'};href='{http://www.w3.org/1999/xlink}href'
ap=argparse.ArgumentParser();ap.add_argument('--collection',choices=['239','206'],default='239');ap.add_argument('pages',type=int,nargs='+');args=ap.parse_args()
tag='darmstadt'+args.collection
r=E.parse(ROOT/f'source/arcinsys/{tag}-mets.xml').getroot()
urls=[x.attrib[href] for x in r.findall('.//m:fileGrp[@USE="DEFAULT"]//m:FLocat',ns)]
out=ROOT/f'source/arcinsys/{tag}-full';out.mkdir(exist_ok=True)
for page in args.pages:
 url=urls[page];p=out/url.rsplit('/',1)[1]
 if not p.exists():
  data=subprocess.check_output(['curl','-fsSL','--max-time','60','--retry','1',url]);p.write_bytes(data)
manifest=[]
for p in sorted(out.glob('*.jpg')):
 url=next(u for u in urls if u.rsplit('/',1)[1]==p.name)
 manifest.append({'url':url,'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/f'work/{tag}-full.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'total_original_pages':len(manifest)}))

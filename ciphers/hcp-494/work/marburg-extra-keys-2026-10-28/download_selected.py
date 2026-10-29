import urllib.request,json,hashlib,concurrent.futures
from pathlib import Path
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parent
selected={'1218':[28,35,43,58,77,115,141,147,157,165,180,189,198,205,214,233,249,258,269,275,281,315,325,337,352,375,381,392,395,416,475,501], '1220':[3,5,7,10,12,14,16,20,26,42,47,54,56,87,92,94,96], '1238':[3,5,7]}
tasks=[]
for x in json.loads((p/'deliveries.json').read_text()):
 key=x['key'];d=p/f'key{key}-full';d.mkdir(exist_ok=True)
 files=[a for a in x['files'] if a['use']=='DEFAULT']
 for i in selected[key]:tasks.append((key,i,files[i-1]['url'],d/f'{i:04}.jpg'))
def get(t):
 key,i,u,q=t
 try:
  b=q.read_bytes() if q.exists() else urllib.request.urlopen(u,timeout=60).read();q.write_bytes(b)
  return {'key':key,'page':i,'url':u,'path':str(q.relative_to(p)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 except Exception as e:return {'key':key,'page':i,'url':u,'error':str(e)}
r=list(concurrent.futures.ThreadPoolExecutor(6).map(get,tasks));(p/'selected-downloads.json').write_text(json.dumps(r,indent=2)+'\n')
for key in selected:
 rows=[a for a in r if a['key']==key and 'error'not in a];d=p/f'key{key}-selected-sheets';d.mkdir(exist_ok=True)
 for j in range(0,len(rows),6):
  batch=rows[j:j+6];im=Image.new('RGB',(1800,1800),'white');dr=ImageDraw.Draw(im)
  for k,a in enumerate(batch):
   tile=Image.open(p/a['path']);w,h=tile.size;tile=tile.crop((0,0,w,int(h*.45)));tile.thumbnail((890,560));xx=(k%2)*900;yy=(k//2)*600;im.paste(tile,(xx+(900-tile.width)//2,yy+30));dr.text((xx+10,yy+10),f'{key}:{a["page"]:04} TOP45%',fill='black')
  im.save(d/f'{j+1:03}-{j+len(batch):03}.jpg')
print('selected full scans',len(r),'errors',[a for a in r if 'error'in a],flush=True)

"""Reproduce source crops and a character-edit audit; not a decipherment model."""
from pathlib import Path
import hashlib, json, unicodedata
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parents[1]
claim=json.loads((p/'work/reading.json').read_text())
assert hashlib.sha256((p/'source/address.jpg').read_bytes()).hexdigest()==claim['source_sha256']['address.jpg']
im=Image.open(p/'source/address.jpg')
regions=[('Unresolved A15',(350,388,526,420)),('GY in hogy, A17',(148,446,202,477)),('f in foglalva, A09',(180,229,270,263)),('A16 start',(27,417,183,447)),('A15 prefix',(200,390,366,418))]
out=Image.new('RGB',(1300,200*len(regions)),'white');draw=ImageDraw.Draw(out)
for n,(label,box) in enumerate(regions):
 draw.text((8,n*200+5),label,fill='black')
 crop=im.crop(box)
 out.paste(crop.resize((crop.width*6,crop.height*6)),(8,n*200+20))
out.save(p/'work/gap-comparison-pass7.png')
# Unit-cost Levenshtein distance: a diagnostic of how much a conjecture changes,
# NOT a linguistic probability, glyph classifier, or evidence for a candidate.
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if c.isalpha())
def distance(a,b):
 row=list(range(len(b)+1))
 for i,x in enumerate(a,1):
  nxt=[i]
  for j,y in enumerate(b,1):nxt.append(min(nxt[-1]+1,row[j]+1,row[j-1]+(x!=y)))
  row=nxt
 return row[-1]
phrases=['úgy fogott meg','úgy fogyott meg','úgy fagyott meg','úgy fagytam meg','hogy ittam','hogy ittam még','úgy voltam','úgy folyt','nem fagytam meg','fogyott meg']
result={'input_alternatives':['ufogyitme','ufogyotme'],'warning':'Letter edit counts only; candidates selected manually, not exhaustive. No candidate is accepted. Accents and spaces ignored.','candidates':[{'phrase':v,'distances':{raw:distance(raw,norm(v)) for raw in ['ufogyitme','ufogyotme']}} for v in phrases]}
(p/'work/gap-candidates-pass7.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))

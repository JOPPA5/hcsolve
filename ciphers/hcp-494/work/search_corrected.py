"""Bounded diagnostic search, not a decipherment. No target plaintext used to train."""
from pathlib import Path
from collections import Counter
import itertools,json,math,re,unicodedata,hashlib
P=Path(__file__).resolve().parents[1];R=P.parents[1]
def norm(s):
 s=s.lower().replace('ſ','s').replace('ß','ss').replace('ꝛ','r').replace('ͤ','e')
 s=''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
 return re.sub('[^a-z]+',' ',s.replace('j','i').replace('v','u')).strip()
files=sorted((R/'ciphers/hcp-517/source/dta').glob('*.txt'))
texts=[norm(f.read_text().replace('¬\n','')) for f in files]
text=' '.join(texts);words=Counter(text.split());grams=[None]+[Counter(text[i:i+n] for i in range(len(text)-n+1)) for n in range(1,6)]
def score(s):
 s=norm(s);v=0.
 for i,c in enumerate(s):
  p=(grams[1][c]+0.5)/(len(text)+13.5)
  for n in range(2,min(5,i+1)+1):
   ctx=s[i-n+1:i];den=grams[n-1][ctx]
   if den:p=(grams[n][ctx+c]+2*p)/(den+2)
  v+=math.log(p)
 return v
alpha='abcdefghiklmnopqrstuwxyz'
pre='disgustirt und ';post=' in holstein'
def search(base):
 opts={base:0}
 for n in (1,2):
  for pos in itertools.combinations(range(5),n):
   for vals in itertools.product(alpha,repeat=n):
    w=list(base)
    for i,v in zip(pos,vals):w[i]=v
    w=''.join(w);opts[w]=min(opts.get(w,9),sum(a!=b for a,b in zip(base,w)))
 out=[]
 for w,edits in opts.items():
  forms=[w]+[w[:i]+' '+w[i:] for i in range(1,5) if w[:i] in words and w[i:] in words]
  for f in forms:out.append({'text':f,'changes':edits,'score':round(score(pre+f+post),4),'word_count':words[f]})
 out.sort(key=lambda x:x['score'],reverse=True)
 return {'base':base,'unique_strings':len(opts),'scored_forms':len(out),'best':out[:40], 'one_change_attested':[r for r in out if r['changes']<=1 and r['word_count']][:30]}
# Edit distance for suffix boundaries; all recorded words, no forced er- prefix.
def dist(a,b):
 row=list(range(len(b)+1))
 for i,x in enumerate(a,1):
  nr=[i]
  for j,y in enumerate(b,1):nr.append(min(nr[-1]+1,row[j]+1,row[j-1]+(x!=y)))
  row=nr
 return row[-1]
near=[]
for w,c in words.items():
 if c>=2 and 3<=len(w)<=10:
  d=dist('ertaz',w)
  if d<=2:near.append({'word':w,'distance':d,'count':c})
near.sort(key=lambda x:(x['distance'],-x['count']))
r={'training':'8 existing DTA texts, 1724-1748: later than the target; diagnostic only, not exact replication of Bourdeau LM', 'characters':len(text),'word_types':len(words),'sources':[{'path':str(f.relative_to(R)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files], 'searches':[search('ertaz'),search('ertad')], 'dictionary_neighbors':near, 'accepted':None}
(P/'work/corrected-search.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('chars',len(text),'word types',len(words))
for x in r['searches']:
 print(x['base'],x['unique_strings'],'strings',x['scored_forms'],'forms');print(json.dumps(x['best'][:12],ensure_ascii=False));print('one-change attested:',x['one_change_attested'])
print('neighbors',json.dumps(near[:40],ensure_ascii=False))

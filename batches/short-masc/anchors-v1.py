# Adapted from scoring-sol61/german/anchors-short.py and pairs.cpp (GPT-6.1 Sol).
# All words come from frozen dictionaries/TRAIN; no true words are injected.
from pathlib import Path
from collections import defaultdict
import sys,json,random,math
w=Path(__file__).resolve().parent
inp=Path(sys.argv[1]);lang=sys.argv[2];N=int(sys.argv[3]);prefix=Path(sys.argv[4]);ct=inp.read_text().strip();alpha='abcdefghijklmnopqrstuvwxyz{|'
def pat(s):
 d={};return tuple(d.setdefault(c,len(d)) for c in s)
index=defaultdict(list)
for line in (w/f'{lang}-vocab-{N}.tsv').read_text().splitlines():
 word,f=line.split('\t');f=int(f)
 if 6<=len(word)<=25:index[pat(word)].append((word,f))
anchors=[]
for length in range(25,5,-1):
 for offset in range(len(ct)-length+1):
  span=ct[offset:offset+length];matches=index[pat(span)]
  if len(matches)>200:continue
  for word,f in matches:
   mapping={alpha.index(c):alpha.index(a) for c,a in zip(span,word)}
   anchors.append((length*length+5*math.log1p(f),offset,word,mapping))
anchors.sort(key=lambda x:(-x[0],x[1],x[2]));selected=anchors[:1000];partials={}
for rank,offset,word,k in selected:partials[tuple(sorted(k.items()))]=rank
for i,a in enumerate(selected):
 for b in selected[i+1:]:
  if not (a[1]+len(a[2])<=b[1] or b[1]+len(b[2])<=a[1]):continue
  k=a[3].copy();inv={v:z for z,v in k.items()};ok=True
  for z,v in b[3].items():
   if (z in k and k[z]!=v) or (v in inv and inv[v]!=z):ok=False;break
   k[z]=v;inv[v]=z
  if ok:partials[tuple(sorted(k.items()))]=len(k)*100+len(a[2])+len(b[2])
ranked=sorted(partials.items(),key=lambda x:(-x[1],x[0]))[:2000];r=random.Random(396345);out=[]
for item,rank in ranked:
 k=dict(item);available=[i for i in range(N) if i not in k.values()];r.shuffle(available);key=[k.get(i,-1) for i in range(N)]
 for i in range(N):
  if key[i]<0:key[i]=available.pop()
 out.append(''.join(alpha[v] for v in key)+' '+''.join('1' if i in k else '0' for i in range(N)))
# Fresh blind starts hedge the dictionary's omissions. No control truth access.
for i in range(128):
 key=list(alpha[:N]);r.shuffle(key);out.append(''.join(key)+' '+'0'*N)
prefix.with_suffix('.seeds.txt').write_text('\n'.join(out)+'\n');prefix.with_suffix('.seeds.json').write_text(json.dumps({'anchors_total':len(anchors),'anchors_pairing_cap':1000,'compatible_partial_keys':len(partials),'generic_anchor_pair_seeds':len(ranked),'random_seeds':128,'true_words_injected':False,'top_anchors':[{'offset':a[1],'word':a[2]} for a in selected[:20]]},indent=2)+'\n')
print(prefix.name,len(anchors),len(partials),len(out))

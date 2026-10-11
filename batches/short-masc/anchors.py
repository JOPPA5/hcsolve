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
  matches=sorted(matches,key=lambda item:(-item[1],item[0]))[:8]
  for word,f in matches:
   mapping={alpha.index(c):alpha.index(a) for c,a in zip(span,word)}
   anchors.append((length*length+5*math.log1p(f),offset,word,mapping))
anchors.sort(key=lambda x:(-x[0],x[1],x[2]))
# Reserve a TRAIN-frequency pool separately from generic length priority.
freqwords={word:f for entries in index.values() for word,f in entries}
frequency=sorted(anchors,key=lambda a:(-freqwords[a[2]],-len(a[2]),a[1],a[2]))
unique={}
for a in anchors[:1000]+frequency[:1000]:unique[(a[1],a[2])]=a
selected=list(unique.values());partials={}
for rank,offset,word,k in selected:partials[tuple(sorted(k.items()))]=rank
pairing=selected[:250]+frequency[:250]
for i,a in enumerate(pairing):
 for b in pairing[i+1:]:
  if not (a[1]+len(a[2])<=b[1] or b[1]+len(b[2])<=a[1]):continue
  k=a[3].copy();inv={v:z for z,v in k.items()};ok=True
  for z,v in b[3].items():
   if (z in k and k[z]!=v) or (v in inv and inv[v]!=z):ok=False;break
   k[z]=v;inv[v]=z
  if ok:partials[tuple(sorted(k.items()))]=len(k)*100+len(a[2])+len(b[2])
singles={tuple(sorted(a[3].items())):a[0] for a in selected}
pairs=sorted(partials.items(),key=lambda x:(-x[1],x[0]))[:1000]
ranked=list(sorted(singles.items(),key=lambda x:(-x[1],x[0])))+[(key,rank) for key,rank in pairs if key not in singles]
r=random.Random(396345);out=[]
for item,rank in ranked:
 k=dict(item);available=[i for i in range(N) if i not in k.values()];r.shuffle(available);key=[k.get(i,-1) for i in range(N)]
 for i in range(N):
  if key[i]<0:key[i]=available.pop()
 out.append(''.join(alpha[v] for v in key)+' '+''.join('1' if i in k else '0' for i in range(N)))
# Fresh blind starts hedge the dictionary's omissions. No control truth access.
for i in range(128):
 key=list(alpha[:N]);r.shuffle(key);out.append(''.join(key)+' '+'0'*N)
prefix.with_suffix('.seeds.txt').write_text('\n'.join(out)+'\n');prefix.with_suffix('.seeds.json').write_text(json.dumps({'anchors_total':len(anchors),'anchors_pairing_cap':500,'compatible_partial_keys':len(partials),'generic_anchor_pair_seeds':len(ranked),'single_anchor_quota_preserved':len(singles),'version':3,'per_window_frequency_quota':8,'pairing_cap':500,'random_seeds':128,'true_words_injected':False,'top_anchors':[{'offset':a[1],'word':a[2]} for a in selected[:20]]},indent=2)+'\n')
print(prefix.name,len(anchors),len(partials),len(out))

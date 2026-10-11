from pathlib import Path
from collections import Counter
from itertools import permutations
import heapq, json
p=Path(__file__).parent
s=''.join((p/'transcription.txt').read_text().split())
words='som sme ste nie pri pre pro ako pod nad vam vas nas jeho jej aby bude budu bolo bola boli ktory ktore ktoru vlada vlady minister ministerstvo zahranicnych veci vyslanectvo telegram sprava spravy prosim oznamujem ziadam slovensko slovenska bratislava zaslat poslat dnes zajtra dna opakovat jedna dva tri styri pat sest sedem osem devat nula'.split()
def score(t):return sum(t.count(w)*len(w)**2 for w in words)
def decrypt(c,key):
 n=len(key); q,r=divmod(len(c),n); cols=['']*n; off=0
 for j in key:
  sz=q+(j<r); cols[j]=c[off:off+sz]; off+=sz
 return ''.join(cols[j][i] for i in range(q+1) for j in range(n) if i<len(cols[j]))
counts=Counter(s)
print('Length',len(s),'frequencies',counts)
print('IC',sum(v*(v-1) for v in counts.values())/(len(s)*(len(s)-1)))
best=[]
def keep(kind,t):
 item=(score(t),kind,t)
 if len(best)<25:heapq.heappush(best,item)
 elif item>best[0]:heapq.heapreplace(best,item)
# Exhaustive single irregular columnar widths2..8, readout both directions.
for n in range(2,9):
 for key in permutations(range(n)):
  t=decrypt(s,key)
  keep(str(key),t); keep(str(key)+' reversed',t[::-1])
# Simple rectangular route reversals, including putative indicator removal at each position.
for removed in [-1]+list(range(len(s)//5)):
 c=s if removed<0 else s[:removed*5]+s[removed*5+5:]
 for n in range(2,41):
  for key in [list(range(n)),list(range(n))[::-1]]:
   t=decrypt(c,key)
   keep('route width%d remove%d'%(n,removed),t)
   keep('route reversed width%d remove%d'%(n,removed),t[::-1])
print('Best heuristic results: not authenticated solutions')
for x in sorted(best,reverse=True):print(x)

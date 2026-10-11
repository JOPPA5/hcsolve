from pathlib import Path
from itertools import permutations
import heapq
p=Path(__file__).parent
s=''.join(c for c in (p/'transcription.txt').read_text() if c.isalpha())
# Transparent heuristic only: short common Slovak sequences, not a trained model.
words='som sme ste nie pri pre pro ako pod nad vam vas nas jeho jej aby bude budu bolo bola boli ktory ktore ktoru vlada vlady minister ministerstvo zahranicnych veci vyslanectvo telegram sprava spravy prosim oznamujem ziadam slovensko slovenska rumunsko rumunska nemecko nemecka bratislava zaslat poslat dnes zajtra dna'.split()
weights={w:len(w)**2 for w in words}
def score(t): return sum(t.count(w)*v for w,v in weights.items())
for width in [5,7]:
 h=len(s)//width
 cols=[s[i*h:(i+1)*h] for i in range(width)]
 best=[]
 for key in permutations(range(width)):
  for reverse in [False,True]:
   t=''.join(cols[j][i] for i in range(h) for j in key)
   if reverse:t=t[::-1]
   item=(score(t),key,reverse,t)
   if len(best)<10:heapq.heappush(best,item)
   elif item>best[0]:heapq.heapreplace(best,item)
 print('WIDTH',width)
 for item in sorted(best,reverse=True): print(item)

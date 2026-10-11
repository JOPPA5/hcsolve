from pathlib import Path
from collections import Counter
p=Path(__file__).parent;groups=p.joinpath('transcription.txt').read_text().split();s=''.join(groups)
phrases=['effektivne lei','efektivne lei','effektivnych lei','effektivne lei posielame kurierom','effektivne lei vam posielame kurierom','effektivne lei vam posleme kurierom','effektivne lei vam budu poslane kurierom','effektivne lei vam bude mat kurier','effektivne lei vam posleme','kurierom','diplomatickym kurierom','najblizsim kurierom','terajsim kurierom']
print('length',len(s),'inventory',dict(sorted(Counter(s).items())))
for omit in [-1]+list(range(len(groups))):
 c=s if omit<0 else ''.join(g for i,g in enumerate(groups) if i!=omit)
 print('\nOMIT',omit+1,'NONE' if omit<0 else groups[omit], 'length',len(c))
 for phrase in phrases:
  pc=Counter(phrase.replace(' ',''));missing=pc-Counter(c)
  if not missing:print('POSSIBLE INVENTORY ONLY:',phrase,'residual',''.join(sorted((Counter(c)-pc).elements())))
  elif omit==-1:print('IMPOSSIBLE unchanged:',phrase,'missing',dict(missing))

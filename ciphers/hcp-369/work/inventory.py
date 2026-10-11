from pathlib import Path
from collections import Counter
p=Path(__file__).parent;s=p.joinpath('cipher.txt').read_text();c=Counter(s)
print('length',len(s),'IC',sum(v*(v-1) for v in c.values())/(len(s)*(len(s)-1)),'counts',dict(sorted(c.items())))
for phrase in ['telegram','osemnulajednapatpat','opakujeme','opakovanie','vasu spravu','ministerstvo']:
 missing=Counter(phrase.replace(' ',''))-c
 print(phrase,'missing',dict(missing),'compatible_inventory_only',not missing)

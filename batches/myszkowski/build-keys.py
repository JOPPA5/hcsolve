from pathlib import Path
import json
p=Path(__file__).parent;keys=set();count=0
for line in Path('batches/scoring-sol61/frequency/words.tsv').read_text().splitlines():
    w=line.split('\t')[0]
    if not 2<=len(w)<=22:continue
    count+=1;letters=sorted(set(w)); keys.add(''.join(chr(97+letters.index(c)) for c in w))
(p/'keyword-patterns.txt').write_text('\n'.join(sorted(keys,key=lambda k:(len(k),k)))+'\n')
(p/'keyword-provenance.json').write_text(json.dumps(dict(source='Frozen Slovak morphological dictionary/frequencies, batches/scoring-sol61/frequency/words.tsv; no target words added',words=count,distinct_weak_order_patterns=len(keys),widths=[2,22]),indent=2))
print(count,len(keys))

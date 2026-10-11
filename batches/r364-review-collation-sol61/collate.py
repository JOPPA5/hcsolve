from pathlib import Path
from collections import Counter
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[1];original=(R/'ciphers/hcp-364/work/transcription.txt').read_text().lower().split();assert len(original)==14
base=original[:];base[7]='tsnnd';base[9]='eloen';base[11]='excuu'
reply=['nelustitelne','neudalsicislopredtextom','vidbodtripokynov','uvedcislo'];quote=''.join(reply);template='x'.join(reply)+'x';assert len(quote)==60 and len(template)==64
variants=[];inventory=[]
for ending in ['uu','uv','vu','vv']:
 groups=base[:];groups[11]='exc'+ending;body=''.join(groups);name='EXC'+ending.upper();(B/f'{name}-full70.txt').write_text(body+'\n');omitted=''.join(g for i,g in enumerate(groups)if i!=2);(B/f'{name}-omit3-65.txt').write_text(omitted+'\n');diff=[dict(group=i+1,position=j+1,original=x,preferred=y)for i,(a,b)in enumerate(zip(original,groups))for j,(x,y)in enumerate(zip(a,b))if x!=y];variants.append(dict(name=name,groups=groups,body=body,omit3=omitted,changes=diff,group12_ending='both trailing glyphs U/V ambiguous; no inventory-selected reading'))
 for omit in range(14):
  c=''.join(g for i,g in enumerate(groups)if i!=omit);expected=Counter(quote)+Counter({'x':5});missing=expected-Counter(c);excess=Counter(c)-expected;inventory.append(dict(reading=name,omitted_group=omit+1,extra=dict(excess),missing=dict(missing),exact=not excess and not missing,minimum_inventory_errors=max(sum(excess.values()),sum(missing.values()))))
(B/'variants.json').write_text(json.dumps(dict(original_groups=original,preferred_core_changes=[dict(group=8,from_reading='TSMND',to_reading='TSNND'),dict(group=10,from_reading='CLOEN',to_reading='ELOEN'),dict(group=12,from_reading='ERC',to_reading='EXC')],variants=variants,reply_sentence_templates=reply,reply60=quote,four_sentence_X_template64=template,fifth_X='insert at any of65 boundaries;60 distinct65letter strings (template already contains natural X in textom plus four sentence X)' ,inventory=inventory,source_reading_and_quote_relation='scan corrections supported; reply plaintext hypothesis remains conditional, no key recovered'),indent=2));print('exact',[(x['reading'],x['omitted_group'])for x in inventory if x['exact']]);print('omit3',[(x['reading'],x['extra'],x['missing'])for x in inventory if x['omitted_group']==3])

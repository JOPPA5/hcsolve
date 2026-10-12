from pathlib import Path
from collections import Counter
from itertools import product
import json,unicodedata,hashlib
b=Path(__file__).resolve().parent;groups=(b/'cipher-groups.txt').read_text().split();unc=json.loads((b/'cipher-reading-uncertainties.json').read_text());alph='abcdefghijklmnopqrstuvwxyz'
head='koncom juna zaciatkom jula zajali sme dvadsatsedem {zivy} americkych letcov osmi sa zabili x vlada zachovava {presne} predpisy zenevskej konvencie a vydala ihned podriadenym uradom obeznik ze treba ludsky zachadzat a chranit pred pripadnym nasil im zvedavostou a ze odplata je zakazana {xzak} aby sa nestaly pripady ako juzneho suseda x nas cerveny kriz sa usilovne stara x zajatci v listoch rodinam vychvaluju zaobchadzanie x '
tail='burzio prejavil napadny zaujem o zajatcov x ukazal som mu listy a vcera {correction} dvojhodinovu navstevu tabora x mal najlepsi dojem lebo zajatci mu priamo prejavili uplne uspokojenie s nasim postupom x iste poda zpravu vatikanu spomente aj vy prilezitostne dobre zaobchadzanie'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower())if c in alph)
variants=[]
for corrected,presne,xzak,zivy in product([False,True],[False,True],[False,True],['zivyeh','zivych']):
 correction='zaviedol na'if corrected else '';h=head.format(zivy=zivy,presne='presne'if presne else '',xzak='x'if xzak else '');t=tail.format(correction=correction);v=dict(name=f"{'adopted'if corrected else 'surviving'}-presne{int(presne)}-xzak{int(xzak)}-{zivy}",text=h+t,normalized=norm(h+t),head=norm(h),tail=norm(t),adopt_interlinear_zaviedolna=corrected,keep_presne=presne,uncertain_x_after_zakazana=xzak,first_word_variant=zivy);variants.append(v)
(b/'normalized-plaintext-variants.json').write_text(json.dumps(variants,indent=2,ensure_ascii=False)+'\n')
# Exact lengths/inventories only; no transposition or key solver.
ctcases=[]
for omitted in [0]+list(range(1,len(groups)+1)):
 gs=[g for i,g in enumerate(groups,1)if i!=omitted];ct=''.join(gs);counter=Counter(ct);low=Counter();high=Counter()
 for i,g in enumerate(groups,1):
  if i==omitted:continue
  options=unc['alternatives'].get(str(i),[g]);counters=[Counter(o)for o in options]
  for ch in alph:low[ch]+=min(z[ch]for z in counters);high[ch]+=max(z[ch]for z in counters)
 ctcases.append(dict(omitted_group=omitted,omitted_text=groups[omitted-1]if omitted else None,length=len(ct),counter=counter,low=low,high=high))
rows=[];seen={}
for v in variants:
 s=v['normalized']
 for case in ctcases:
  L=case['length'];best=None;boundbest=None;exact=[]
  samples=[(i,s[i:i+L],'contiguous',0)for i in range(len(s)-L+1)]
  for pad in range(1,5):samples.extend([(0,s[:L-pad]+'x'*pad,'prefix_minimal_X_padding',pad),(len(s)-(L-pad),s[-(L-pad):]+'x'*pad,'suffix_minimal_X_padding',pad)])
  for at,p,kind,pad in samples:
   C=Counter(p);distance=sum(abs(case['counter'][ch]-C[ch])for ch in alph)//2;outside=max(sum(max(0,case['low'][ch]-C[ch])for ch in alph),sum(max(0,C[ch]-case['high'][ch])for ch in alph));z=dict(start=at,end=at+L-pad,kind=kind,padding_x=pad,inventory_substitution_distance=distance,source_variant_box_lower_bound=outside,plaintext=p,ct_excess=dict(case['counter']-C),pt_excess=dict(C-case['counter']))
   if best is None or distance<best['inventory_substitution_distance']:best=z
   if boundbest is None or outside<boundbest['source_variant_box_lower_bound']:boundbest=z
   if distance==0:exact.append(z)
  rows.append(dict(variant=v['name'],whole_plaintext_length=len(s),omitted_group=case['omitted_group'],omitted_text=case['omitted_text'],length=L,best_preferred_ct_window=best,best_loose_source_box_window=boundbest,exact_preferred_ct_matches=exact))
summary=dict(cipher_letters=280,cipher_groups=56,plaintext_variant_lengths=sorted(set(len(v['normalized'])for v in variants)),head_lengths=sorted(set(len(v['head'])for v in variants)),tail_lengths=sorted(set(len(v['tail'])for v in variants)),preferred_exact_windows=sum(len(z['exact_preferred_ct_matches'])for z in rows),best_preferred_ct=sorted(rows,key=lambda z:z['best_preferred_ct_window']['inventory_substitution_distance'])[:8],best_source_box=sorted(rows,key=lambda z:z['best_loose_source_box_window']['source_variant_box_lower_bound'])[:8],source_box_limit='loose per-letter bounds over documented pixel variants ignore within-group covariance; positive possibility is not an exact match; no claim beyond those alternatives',normalization='ASCII letter concatenation, all securely visible X retained; no J/I merge, spelling repairs, guessed struck words or digits introduced',cipher_groups_sha256=hashlib.sha256((b/'cipher-groups.txt').read_bytes()).hexdigest())
(b/'inventory-all-omissions.json').write_text(json.dumps(rows,indent=2)+'\n');(b/'inventory-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('PT lengths',summary['plaintext_variant_lengths'],'head',summary['head_lengths'],'tail',summary['tail_lengths']);print('Exact preferred',summary['preferred_exact_windows']);print('Best preferred',[(z['omitted_group'],z['variant'],z['best_preferred_ct_window']['start'],z['best_preferred_ct_window']['inventory_substitution_distance'])for z in summary['best_preferred_ct']]);print('Best loose source box',[(z['omitted_group'],z['best_loose_source_box_window']['source_variant_box_lower_bound'])for z in summary['best_source_box']])

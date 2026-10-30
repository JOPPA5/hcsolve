#!/usr/bin/env python3
"""Rebuild the v2 record after review 1: four sign-level corrections + G family extension.
v1 files are preserved unchanged in work/v1/. Run once; writes work/*.json|txt|csv."""
from pathlib import Path
from collections import Counter
import csv,io,json,re,hashlib
W=Path(__file__).resolve().parent
fixes={'R08':('cf6gh3f6','cf6Gh3f6'),'R09':('df5 b3qf6m4','dh4 b3qf6m4'),
       'R10':('yc5n f5s5h','ycn5 f5s5h'),'R11':('g385{U1}4','g385G1')}
key=json.loads((W/'v1/key.json').read_text());key['G']='g'
rec=json.loads((W/'v1/transcription.json').read_text())
rec['method']+=' v2 (2026-10-29, Claude Opus 5.5): review-1 corrections R08 G, R09 dh4=TRI, R10 ycn5=JSME, R11 G1=GY; G is the family k-shaped sign (hcp-1541/1553/1554).'
rec['corrections_v2']={r:{'v1':a,'v2':b} for r,(a,b) in fixes.items()}
u=rec.pop('unknowns');rec['resolved_v1_unknowns']={'U1':dict(u['U1'],resolution='k-shaped G; same sign as R08 SVAGROVA and family cards hcp-1541/1553/1554; following sign 1/Y')}
rec['notes_v2']={'R04_DLOUHYM':'1/Y overwritten on another stroke (writer correction)','R10_STRAVILI':'8/L darker, apparently retraced (writer correction)'}
pos=[];cnt=Counter();idx=ch=letters=0;lit=[]
for row in rec['rows']:
    if row['row'] in fixes:
        a,b=fixes[row['row']];assert row['cipher'].count(a)==1;row['cipher']=row['cipher'].replace(a,b)
    n=0
    for wi,word in enumerate(row['cipher'].split(),1):
        for c in word:
            if c in key:
                idx+=1;n+=1;cnt[c]+=1;ch+=c=='H';letters+=len(key[c])
                pos.append([idx,row['row'],n,wi,c,key[c],'mapped',','.join(map(str,row['box_oriented_xyxy'])),','.join(map(str,row['box_original_xyxy']))])
            else: assert c in ',.!?',c
    row['literal']=''.join(key.get(c,c) for c in row['cipher']);row['source_units']=row['mapped_units']=n;lit.append(row['literal'])
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=1)+'\n')
(W/'transcription.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text('\n'.join(r['cipher'] for r in rec['rows'])+'\n')
(W/'literal-cz.txt').write_text('\n'.join(lit)+'\n')
s=io.StringIO();w=csv.writer(s,lineterminator='\n');w.writerow(['index','row','row_ordinal','word_ordinal','label','literal_unit','status','row_box_oriented_xyxy','row_box_original_xyxy']);w.writerows(pos)
(W/'positions.csv').write_text(s.getvalue())
inv={'version':2,'source_units':idx,'mapped_units':idx,'unknown_single_glyphs':0,'unknown_length_runs':0,'known_base_letters':letters,'CH_units':ch,
     'row_counts':{r['row']:r['source_units'] for r in rec['rows']},'class_counts':dict(sorted(cnt.items()))}
(W/'inventory.json').write_text(json.dumps(inv,indent=2)+'\n')
print(inv)

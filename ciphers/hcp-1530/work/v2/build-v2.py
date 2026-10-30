#!/usr/bin/env python3
"""Build transcription-v2.json from the v1 partial record (round-1 review fixes).
Changes: T01 th6r5 -> th6r1 (DRAHY, review finding 2); U1..U4 replaced by transcribed
signs with per-sign certainty (clear / faint / restored), review findings 1 and 4."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
key=json.loads((W/'key.json').read_text())
rec=json.loads((W/'transcription.json').read_text())
def parts(seq):
    out=[]
    for c,cert in seq:
        out.append({'cipher':c,'plain':key[c],'certainty':cert})
    return out
FILL={
 'U1':parts([('8','probable'),('4','restored'),('c','restored'),('d','clear'),('5','clear'),('g','clear')]),
 'U2':parts([(c,'clear') for c in 'm1m5yc4']),
 'U3':parts([('t','faint'),('4','faint'),('m','clear'),('5','clear')]),
 'U4':parts([('t','faint'),('5','faint')]),
}
NOTES={
 'U1':'Dark paint after DRAHY. 8 (L) probable; one or two signs lost in the paint, restored as 4 c (I S) from context and width; d 5 g (TEK) visible before the closing bracket. Word LISTEK = L[IS]TEK.',
 'U2':'m 1 m 5 y c 4 (NYNEJSI) fully legible through the shadow (review/work/U2x5.png).',
 'U3':'Middle of JE....MU: t 4 m 5 (DINE) discernible, t and 4 faint. Word JEDINEMU.',
 'U4':'End of URA..: t 5 (DE) visible but faint, shapes correct. Word URADE.',
}
new={'method':rec['method']+' v2 (2026-10-29, after review 1): dark spans transcribed sign by sign; only I,S in U1 restored from context.',
     'coordinate_systems':rec['coordinate_systems'],'spans':{},'rows':[],'ordinary':rec.get('ordinary'),'marks':rec.get('marks')}
for u,v in rec['unknowns'].items():
    d={k:v[k] for k in v if k.startswith('box')}; d['note']=NOTES[u]; new['spans'][u]=d
for row in rec['rows']:
    ps=[]
    for p in row['parts']:
        if 'unknown' in p:
            for q in FILL[p['unknown']]: q=dict(q); q['span']=p['unknown']; ps.append(q)
        else:
            q=dict(p)
            if 'cipher' in q: q.setdefault('certainty','clear')
            ps.append(q)
    if row['id']=='T01':
        # last sign of th6r? : 5 -> 1  (DRAHE -> DRAHY)
        i=max(k for k,q in enumerate(ps) if q.get('cipher')=='5' and 'span' not in q)
        assert [q.get('cipher') for q in ps[i-4:i+1]]==['t','h','6','r','5']
        ps[i]={'cipher':'1','plain':'Y','certainty':'clear','note':'corrected from 5 after review 1 (foot stroke as in fh581)'}
    cipher=''.join(q.get('cipher',q.get('ordinary',q.get('literal'))) for q in ps)
    new['rows'].append({'id':row['id'],'coordinate_system':row['coordinate_system'],'row_box_xyxy':row['row_box_xyxy'],'cipher':cipher,'parts':ps})
(W/'v2'/'transcription-v2.json').write_text(json.dumps(new,ensure_ascii=False,indent=1)+'\n')
print('written')

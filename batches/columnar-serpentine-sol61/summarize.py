from pathlib import Path
import json
p=Path(__file__).resolve().parent;rows=json.loads((p/'targets.json').read_text());report={}
for num in [363,393,345,396,369]:
 subset=[r for r in rows if r['cipher']==num];top=[]
 for r in subset:
  c=r['candidates'][0];top.append(dict(score=c['score'],plaintext=c['plaintext'],width=r['width'],model=r['model'],whole_reverse=r['whole_reverse'],start_up=r['start_up'],readout_columns=c['readout_columns'],readout_directions=c['readout_directions']))
 top.sort(key=lambda c:c['score'],reverse=True);report[num]=dict(cases=len(subset),length=subset[0]['length']if subset else None,erasures=subset[0]['erasures']if subset else None,top=top[:5])
(p/'summary.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))

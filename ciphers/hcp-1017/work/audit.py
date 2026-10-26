"""Artifact consistency audit; does not replace visual review."""
from pathlib import Path
from datetime import date,timedelta
import hashlib,json,subprocess,sys
p=Path(__file__).resolve().parent
body=json.loads((p/'body-shapes.json').read_text());margin=json.loads((p/'margin-shapes.json').read_text()); orient=json.loads((p/'margin-orientations.json').read_text())
source={name:hashlib.sha256((p.parent/'source'/name).read_bytes()).hexdigest()==value for name,value in body['source_sha256'].items()}
rows=body['rows']+margin['rows'];tokens=[t for row in rows for t in row['tokens'].replace('/','').split()]
plain=subprocess.check_output([sys.executable,str(p/'decode.py')],text=True)
control=(p/'control-result.txt').read_text().splitlines()[-1]==(p/'control-plain.txt').read_text().strip()
d=date(1905,6,14)
a={'source_hashes_match':source,'body_positions':sum(len(r['tokens'].replace('/','').split()) for r in body['rows']),'margin_positions':sum(len(r['tokens'].replace('/','').split()) for r in margin['rows']),'whole_positions':len(tokens),'single_letter_positions':sum(len(body['key'][t])==1 for t in tokens),'inferred_M_positions':tokens.count('blottedM'),'crossed_positions':tokens.count('crossed'),'cipher_region_scope':'both identified picture-side regions; ordinary address writing is not ciphertext','orientation_cases':len(orient['outputs']),'heldout_margin_reading':'TAUSEND / TAUSEND / GLUEHENDE / BUESSE','heldout_margin_appears_under_unchanged_body_key':any(x['rotation']==180 and not x['mirror'] and x['reversed_order'] and x['reading']=='TAUSEND / TAUSEND / GLUEHENDE / BUESSE' for x in orient['outputs']),'source_date_weekday':d.strftime('%A'),'following_day_weekday':(d+timedelta(days=1)).strftime('%A'),'discovery_screen_control_exact200':control,'manual_not_OCR':True,'review_status':'Claude Opus 5.5 REVISE addressed; this script checks consistency, not handwriting truth'}
assert all(source.values()) and len(tokens)==214
assert a['single_letter_positions']==212 and a['inferred_M_positions']==1 and a['crossed_positions']==1
assert a['heldout_margin_appears_under_unchanged_body_key'] and control
assert d.weekday()==2 and (d+timedelta(days=1)).weekday()==3
print(json.dumps(a,indent=2))

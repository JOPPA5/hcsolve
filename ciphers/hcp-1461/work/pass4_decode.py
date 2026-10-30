import json, sys, pathlib
p = pathlib.Path(__file__).with_name('pass4-readings.json')
d = json.loads(p.read_text())
for g in d['groups']:
    print(f"{''.join(chr(91-n) for n in g['codes']):12s} {'-'.join(map(str,g['codes'])):32s} [{g['status'].split(':')[0].split(' (')[0].split(';')[0]}] {g['where']}")

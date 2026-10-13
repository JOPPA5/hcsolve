from pathlib import Path
import json,base64,html,hashlib
root=Path(__file__).resolve().parents[3]
for n in (1243,1301):
 w=root/f'ciphers/hcp-{n}/work';e=json.loads((w/'manual-edition.json').read_text());k=json.loads((w/'graphic-key.json').read_text())
 img=(w/e['source']).read_bytes()
 assert hashlib.sha256(img).hexdigest()==e['sha256']
 rows=[]
 for row in e['rows']:
  txt=''.join(t[8:] if t.startswith('literal:') else k[t] for t in row['graphic_tokens'])
  rows.append(f'<tr><td>{row["row"]}</td><td>{html.escape(txt)}</td></tr>')
 stamp=w/'stamp-upright.png' if n==1301 else w/'stamp-detail.png'
 s=f'''<!doctype html><meta charset="utf-8"><title>HCP{n} — source comparison</title><style>body{{font:17px system-ui;margin:24px;color:#202b35}}.grid{{display:grid;grid-template-columns:minmax(600px,2fr) minmax(360px,1fr);gap:24px}}img{{width:100%;height:auto}}td{{padding:7px;border-bottom:1px solid #ddd}}td:first-child{{color:#666}}.note{{max-width:1000px;color:#625246}}h1{{font-size:26px}}</style><h1>HCP{n}: manual edition / immutable scan</h1><p class="note">Solver's source comparison, not an independent review. Spaces, accents and spelling normalization belong to SOLUTION.md. Here the diplomatic rows and explicit uncertainty flags are retained. Named graphic tokens were serialized from the manual reading; a successful round trip alone is not proof.</p><div class="grid"><div><img src="data:image/jpeg;base64,{base64.b64encode(img).decode()}"><h2>Removed-stamp area</h2><img style="max-width:650px" src="data:image/png;base64,{base64.b64encode(stamp.read_bytes()).decode()}"></div><table>{''.join(rows)}</table></div><p>Source SHA-256: {e['sha256']}</p>'''
 (w/'source-comparison.html').write_text(s)

from pathlib import Path
import json
root=Path(__file__).resolve().parents[2];p=Path(__file__).parent
control=json.loads((root/'ciphers/hcp-363/work/controls.json').read_text())['control-22'];ct=(root/'ciphers/hcp-363/work/control-22.txt').read_text().strip();k=control['keys'][0];N=len(ct);out=['']*N;at=0
for col in k:
 for pos in range(col,N,len(k)):out[pos]=ct[at];at+=1
assert ''.join(out)==control['plaintext']
d=dict(line.split(' ',1) for line in (p/'control22-seed610111.txt').read_text().splitlines());q={a:float(b) for line in (root/'ciphers/hcp-393/work/quadgrams.tsv').read_text().splitlines() for a,b in [line.split()]}
report={'control':'363 width22,395 letters','known_key_inverse_exact':True,'short_column_index':21,'true_short_chunk_position_zero_based':k.index(21),'search_seed':610111,'length_patterns':22,'restarts_per_pattern':10,'steps_per_restart':20000,'evaluations':int(d['evaluations']),'true_score':sum(q.get(control['plaintext'][i:i+4],-4) for i in range(N-3)),'found_score':float(d['score']),'plaintext_exact':d['plaintext']==control['plaintext'],'position_matches':sum(a==b for a,b in zip(d['plaintext'],control['plaintext'])),'key_exact':[int(a) for a in d['key'].split(',') if a]==k,'target_search_run':False}
(p/'twolevel-control-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

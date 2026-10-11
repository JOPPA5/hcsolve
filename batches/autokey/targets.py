from controls import P, parse, encrypt
from pathlib import Path
import subprocess,json
controls=json.loads((P/'controls.json').read_text());assert all(c['exact_at_true_length'] for c in controls if c['mode']<3)
rows=json.loads((P/'targets.json').read_text()) if (P/'targets.json').exists() else [];done={(r['cipher'],r['variant'],r['reverse']) for r in rows}
for num in [369,345,396,374,393,371]:
 gs=Path(f'ciphers/hcp-{num}/work/transcription.txt').read_text().lower().split();header=None
 if gs[0].isdigit():header=gs.pop(0)
 ct=''.join(gs);assert ct.isalpha() and ct.isascii()
 variants=[('literal',ct)]
 if num==396:
  alt=gs[:];alt[6]='o'+alt[6][1:];variants.append(('O-reading',''.join(alt)))
 for tag,s in variants:
  for rev in [False,True]:
   if (num,tag,rev) in done:continue
   inp=s[::-1] if rev else s;f=P/f'{num}-{tag}-{rev}.txt';f.write_text(inp+'\n')
   out=subprocess.check_output([str(P/'solver'),'batches/scoring-sol61/frequency',str(f),'12','12'],text=True)
   (P/f'{num}-{tag}-{rev}-results.txt').write_text(out);candidates=parse(out)
   for c in candidates:assert encrypt(c['plaintext'],[ord(x)-97 for x in c['primer']],c['mode'])==inp
   row=dict(cipher=num,variant=tag,reverse=rev,excluded_numeric_header=header,ciphertext=inp,candidates=candidates,all_candidates_reencrypt_exact=True)
   rows.append(row);(P/'targets.json').write_text(json.dumps(rows,indent=2));print(num,tag,rev,max(candidates,key=lambda c:c['score']),flush=True)

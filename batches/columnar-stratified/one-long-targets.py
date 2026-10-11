from controls import P,encrypt
from pathlib import Path
import subprocess,json
controls=json.loads((P/'one-long-controls.json').read_text());assert sum(c['exact_best'] for c in controls)>=3
rows=json.loads((P/'one-long-targets.json').read_text()) if (P/'one-long-targets.json').exists() else [];done={(r['cipher'],r['variant'],r['reverse'],r['width']) for r in rows}
for num in [369,396,345,393,367,374,371,399,395,363]:
 path=Path(f'ciphers/hcp-{num}/work/transcription.txt') if num!=363 else Path('ciphers/hcp-363/work/transcription-raw.txt')
 gs=path.read_text().lower().split();header=gs.pop(0) if gs[0].isdigit() else None
 gs=[''.join(c if 'a'<=c<='z' else '.' for c in g) for g in gs]
 variants=[('literal-body',''.join(gs))]
 if num in [369,396,345,393,367,374]:variants += [(f'omit-{i+1}',''.join(g for j,g in enumerate(gs) if j!=i)) for i in range(len(gs))]
 if num==396:
  alt=gs[:];alt[6]='o'+alt[6][1:];variants += [('O-body',''.join(alt))]+[(f'O-omit-{i+1}',''.join(g for j,g in enumerate(alt) if j!=i)) for i in range(len(alt))]
 for tag,ct in variants:
  for reverse in [False,True]:
   s=ct[::-1] if reverse else ct
   for width in range(5,27):
    if len(s)%width != 1 or len(s)//width<2 or (num,tag,reverse,width) in done:continue
    f=P/f'one-long-target-{num}-{tag}-{reverse}.txt';f.write_text(s+'\n');out=subprocess.check_output([str(P/'one-long'),str(P),str(f),str(width),'10000'],text=True);result=P/f'one-long-target-{num}-{tag}-{reverse}-{width}.txt';result.write_text(out);candidates=[]
    for line in out.splitlines():
     sc,k,pt=line.split();seq=[int(x) for x in k.rstrip(',').split(',')];read=[seq.index(i) for i in range(width)];assert encrypt(pt,read)==s;candidates.append(dict(score=float(sc),chunk_order=seq,readout_columns=read,plaintext=pt))
    row=dict(cipher=num,variant=tag,reverse=reverse,width=width,length=len(s),ciphertext=s,excluded_numeric_header=header,candidates=candidates,all_retained_reencrypt_exact=True);rows.append(row);(P/'one-long-targets.json').write_text(json.dumps(rows,indent=2))
 print('completed cipher',num,'cases',len(rows),flush=True)

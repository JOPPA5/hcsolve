from pathlib import Path
import json,subprocess
p=Path(__file__).parent
controls=json.loads((p/'controls.json').read_text());assert len(controls)==2 and all(x['exact_best'] for x in controls)
rows=json.loads((p/'target-summary.json').read_text()) if (p/'target-summary.json').exists() else []
done={(x['cipher'],x['variant'],x['order']) for x in rows}
for n in [396,345,393,367,374,369,371,399,395,363]:
    source=Path(f'ciphers/hcp-{n}/work/transcription.txt') if n!=363 else Path('ciphers/hcp-363/work/transcription-raw.txt')
    groups=source.read_text().lower().split()
    raw=''.join(''.join(c if 'a'<=c<='z' else '.' for c in g if 'a'<=c<='z' or c=='?') for g in groups)
    variants=[('full',raw)]
    if n==363:
        raw=''.join(c if 'a'<=c<='z' else '.' for g in groups for c in g)
        variants=[('literal-erasures',raw),('assumed-AB-X',Path('ciphers/hcp-363/work/cipher-x.txt').read_text().strip()),('assumed-AB-A',Path('ciphers/hcp-363/work/cipher-a.txt').read_text().strip())]
    cleaned=[''.join(c if 'a'<=c<='z' else '.' for c in g if 'a'<=c<='z' or c=='?') for g in groups]
    if n in [396,345,367,374,393]:
        variants += [(f'drop-{i+1:02d}',''.join(g for j,g in enumerate(cleaned) if j!=i)) for i in range(len(cleaned))]
    if n==396:
        alt=cleaned[:];alt[6]='o'+alt[6][1:]
        variants.append(('full-O',''.join(alt)))
        variants += [(f'drop-{i+1:02d}-O',''.join(g for j,g in enumerate(alt) if j!=i)) for i in range(len(alt))]
    for tag,ct in variants:
        for order in ['forward','reverse']:
            if (n,tag,order) in done:continue
            s=ct if order=='forward' else ct[::-1];stem=f'{n}-{tag}-{order}';f=p/f'{stem}-input.txt';f.write_text(s+'\n')
            out=subprocess.check_output([str(p/'solver'),'batches/scoring-sol61/frequency',str(f),'8',str(p/'keyword-patterns.txt')],text=True)
            (p/f'{stem}-result.txt').write_text(out)
            candidates=[]
            for line in out.splitlines()[1:]:
                sc,key,plain=line.split();candidates.append(dict(score=float(sc),key=[ord(c)-97 for c in key],plaintext=plain))
            row=dict(cipher=n,variant=tag,order=order,input=s,tested=out.splitlines()[0],best=candidates[0],top100_file=f'{stem}-result.txt',conditional_omission=(tag!='full'))
            rows.append(row);(p/'target-summary.json').write_text(json.dumps(rows,indent=2));print(n,tag,order,row['tested'],row['best'],flush=True)

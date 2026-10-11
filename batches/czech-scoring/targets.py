from pathlib import Path
import json, subprocess
p=Path(__file__).parent
controls=json.loads((p/'controls.json').read_text())
assert len(controls)==4
assert all(r['exact_folded'] for r in controls if r['length']==115)
rows=[]
for N in (26,28):
    for number in (369,367,334,332):
        raw=Path(f'ciphers/hcp-{number}/work/transcription.txt').read_text().lower()
        ct=''.join(c if 'a'<=c<='z' else '.' for c in raw if 'a'<=c<='z' or c=='?')
        for order in ('forward','reverse'):
            s=ct if order=='forward' else ct[::-1]
            stem=f'target-{N}-{number}-{order}'; f=p/f'{stem}.txt'; f.write_text(s+'\n')
            r=subprocess.run([str(p/f'mono{N}'),str(p),str(f),'40'],text=True,capture_output=True,check=True)
            (p/f'{stem}-result.txt').write_text(r.stdout+'\n'+r.stderr)
            v=r.stdout.split(); key=v[1]; found=v[2]
            row=dict(N=N,cipher=number,order=order,input=s,score=float(v[0]),alphabet_key=key,folded_plaintext=found,raw_plaintext=v[3][4:].replace('{','č').replace('|','š'),calibration_scope='115-letter controls passed; 85-letter erased controls FAILED, so especially shorter targets are exploratory',source_unchanged=True)
            rows.append(row);(p/'target-summary.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
            print(N,number,order,row['score'],row['raw_plaintext'],flush=True)

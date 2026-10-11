from pathlib import Path
import random,subprocess,json
p=Path(__file__).parent;plain=Path('batches/scoring-sol61/german/heldout200-plain.txt').read_text().strip()[:150];report=[]
for family in ('subtract','reverse-subtract','add'):
 for lag in (9,15):
  a=-1 if family=='reverse-subtract' else 1;b=-1 if family=='subtract' else 1;ct=[]
  for i,c in enumerate(plain):
   v=ord(c)-97;k=(7*i+3)%26 if i<lag else ord(plain[i-lag])-97
   cipher=(v-b*k)*a%26;ct.append(chr(97+cipher))
  ct=''.join(ct);ct=ct[:70]+'?'+ct[71:94]+'?'+ct[95:];src=p/f'german-plain-feedback-control-{family}-{lag}.txt';src.write_text(ct+'\n')
  args=[str(p/'plain-feedback'),str(Path('batches/scoring-sol61/german/quadgrams.tsv')),str(src),family,str(lag),str(lag),'60','30000']
  out=subprocess.check_output(args,text=True);(p/f'german-plain-feedback-control-{family}-{lag}-results.txt').write_text(out);found=out.split()[-1];row={'family':family,'lag':lag,'exact_all150':found==plain,'positions_correct':sum(a==b for a,b in zip(found,plain))};report.append(row);print(row,flush=True)
(p/'german-plain-feedback-controls.json').write_text(json.dumps(report,indent=2)+'\n')
if not all(r['exact_all150'] for r in report):raise SystemExit('Control gate failed; no targets run.')
for family in ('subtract','reverse-subtract','add'):
 for off in range(5):
  args=[str(p/'plain-feedback'),str(Path('batches/scoring-sol61/german/quadgrams.tsv')),str(p/f'target-phase-{off}.txt'),family,'1','24','30','20000']
  out=subprocess.check_output(args,text=True);(p/f'german-plain-feedback-{family}-phase-{off}-results.txt').write_text(out);print('completed',family,off,flush=True)

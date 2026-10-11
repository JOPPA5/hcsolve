from pathlib import Path
import subprocess,random,json
p=Path(__file__).parent
plains=[Path('ciphers/hcp-334/work/control-vig-plain.txt').read_text().strip()[:115], 'bucurestziadaopakovattelegramtelegrambolzaslanyzbucurestiaprisieldoodboruodkialmiboldodanyazneskorvysvetleniemadat osobny tajomnik pana ministra polyak'.replace(' ','')[:115]]
assert all(len(s)==115 for s in plains)
reports=[]
for index,plain in enumerate(plains):
 rng=random.Random(36961+index);enc=list('abcdefghijklmnopqrstuvwxyz');rng.shuffle(enc);cipher=''.join(enc[ord(c)-97] for c in plain);src=p/f'multigram-masc-control{index}.txt';src.write_text(cipher+'\n')
 out=subprocess.check_output([str(p/'mono-multigram'),'batches/scoring-sol61/frequency',str(src),'40'],text=True,stderr=(p/f'multigram-masc-control{index}-progress.txt').open('w'))
 (p/f'multigram-masc-control{index}-result.txt').write_text(out);recovered=out.split()[-1];row={'control':index,'plain':plain,'cipher':cipher,'encrypt_key':''.join(enc),'exact_plaintext':recovered==plain,'correct_positions':sum(a==b for a,b in zip(recovered,plain))};reports.append(row);print(row,flush=True)
(p/'multigram-masc-controls.json').write_text(json.dumps(reports,indent=2)+'\n')
if not all(x['exact_plaintext'] for x in reports):raise SystemExit('Control gate failed; target not attempted')
cipher=''.join((p/'transcription.txt').read_text().split()).lower()
for reverse in (False,True):
 src=p/f'multigram-masc-target-reverse{reverse}.txt';src.write_text((cipher[::-1] if reverse else cipher)+'\n')
 out=subprocess.check_output([str(p/'mono-multigram'),'batches/scoring-sol61/frequency',str(src),'40'],text=True,stderr=(p/f'multigram-masc-target-reverse{reverse}-progress.txt').open('w'));(p/f'multigram-masc-target-reverse{reverse}-result.txt').write_text(out);print('target',reverse,out.strip(),flush=True)

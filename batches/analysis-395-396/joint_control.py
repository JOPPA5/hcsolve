from pathlib import Path
import unicodedata, subprocess,json
root=Path(__file__).resolve().parents[2];p=Path(__file__).parent
src=root/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
lines=[l[9:] for l in src.read_text().splitlines() if l.startswith('# text = ')]
s=''.join(c for c in unicodedata.normalize('NFD',''.join(lines).lower()) if 'a'<=c<='z')
(p/'planted-plain395.txt').write_text(s[:280]+'\n');(p/'planted-plain396.txt').write_text(s[280:330]+'\n')
subprocess.run(['c++','-O3','-std=c++17',str(p/'joint_r.cpp'),'-o',str(p/'joint_r')],check=True)
report=[]
for widths in ['16','16,17,18']:
 label=widths.replace(',','-')
 args=[str(p/'joint_r'),str(root/'ciphers/hcp-393/work/quadgrams.tsv'),widths]
 gen=subprocess.check_output(args+['generate',str(p/'planted-plain395.txt'),str(p/'planted-plain396.txt')],text=True)
 (p/f'planted-{label}-generation.txt').write_text(gen)
 data=dict(l.split(' ',1) for l in gen.splitlines())
 a=p/f'planted-{label}-cipher395.txt';b=p/f'planted-{label}-cipher396.txt';a.write_text(data['cipher395']+'\n');b.write_text(data['cipher396']+'\n')
 out=subprocess.check_output(args+['attack',str(a),str(b),'12','30000'],text=True)
 (p/f'planted-{label}-attack.txt').write_text(out);z=dict(l.split(' ',1) for l in out.splitlines())
 result={'widths':widths,'same_plaintext395':z['plaintext395']==s[:280],'same_plaintext396':z['plaintext396']==s[280:330], 'character_matches395':sum(a==b for a,b in zip(z['plaintext395'],s[:280])),'character_matches396':sum(a==b for a,b in zip(z['plaintext396'],s[280:330])),'true_score':data['true_score'],'best_score':z['best_score'],'mutation_evaluations':int(z['evaluations'])}
 report.append(result);print(json.dumps(result),flush=True)
(p/'joint-control-results.json').write_text(json.dumps(report,indent=2)+'\n')

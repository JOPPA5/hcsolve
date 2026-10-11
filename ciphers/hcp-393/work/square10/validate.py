from pathlib import Path
import json,re,hashlib
w=Path(__file__).resolve().parent
records=json.loads((w/'controls.json').read_text()); report={'controls':[],'targets':[]}
def parse(line):
 m=re.search(r'cols=([0-9,]+) rows=([0-9,]+) ([a-z]+)$',line)
 return [int(x) for x in m[1].strip(',').split(',')],[int(x) for x in m[2].strip(',').split(',')],m[3]
def verify(ct,line):
 cols,rows,p=parse(line)
 assert sorted(cols)==sorted(rows)==list(range(10)) and len(p)==len(ct)==100
 rebuilt=['?']*100
 for i,r in enumerate(rows):
  for j,c in enumerate(cols):rebuilt[r*10+c]=p[i*10+j]
 assert ''.join(rebuilt)==ct
 return cols,rows,p
for rec in records:
 ct=(w/(rec['label']+'.txt')).read_text().strip()
 for suffix in ['results','phrase-results']:
  f=w/(rec['label']+'.'+suffix+'.txt');lines=f.read_text().splitlines()
  for line in lines:verify(ct,line)
  cols,rows,p=parse(lines[0]);ranks=[i for i,l in enumerate(lines) if parse(l)[2]==rec['plaintext']]
  report['controls'].append(dict(label=rec['label'],model=suffix,top_columns_exact=cols==rec['column_order'],top_rows_exact=rows==rec['row_order'],top_plaintext_exact=p==rec['plaintext'],truth_rank_in_top100=ranks,all100_reencrypt=True))
ct=w.parent.joinpath('cipher.txt').read_text().strip()
for suffix in ['results','phrase-results']:
 lines=w.joinpath('target.'+suffix+'.txt').read_text().splitlines()
 for line in lines:verify(ct,line)
 report['targets'].append(dict(model=suffix,all100_reencrypt=True,top_plaintext=parse(lines[0])[2],coherent=False))
for label,inputfile in [('target','cipher.txt'),('target-transposed','target-transposed.txt')]:
 ct=(w.parent/inputfile if label=='target' else w/inputfile).read_text().strip()
 lines=w.joinpath(label+'.wide-results.txt').read_text().splitlines()
 for line in lines:verify(ct,line)
 report['targets'].append(dict(model=label+'-wide',all100_reencrypt=True,top_plaintext=parse(lines[0])[2],coherent=False))
triple=json.loads(w.joinpath('triple-control.json').read_text())
lines=w.joinpath('triple-control.wide-results.txt').read_text().splitlines()
ct=w.joinpath('triple-control-transposed.txt').read_text().strip()
for line in lines:verify(ct,line)
cols,rows,p=parse(lines[0]);assert p==triple['plaintext'] and cols==triple['column_order'] and rows==triple['row_order']
s=p
for key in triple['keys']:s=''.join(s[r*10+c] for c in key for r in range(10))
assert s==w.joinpath('triple-control.txt').read_text().strip()
report['triple_control']=dict(top_plaintext_exact=True,both_reduced_keys_exact=True,three_original_keys_reencrypt_exactly=True)
files=[w.parent.parent/'source/cryptogram.jpg',w.parent.parent/'source/metadata.md',w/'sk_snk-ud-test.conllu',w.parent/'sk_snk-ud-train.conllu']
report['sha256']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
report['heldout_row_gram_rank']=(w/'heldout-row-rank.txt').read_text().strip()
report['heldout_row_lex_wide_rank']=int(re.search(r'truth lexical rank=(\d+)',(w/'heldout-0.wide-progress.txt').read_text())[1])
w.joinpath('validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report['controls'],indent=2))

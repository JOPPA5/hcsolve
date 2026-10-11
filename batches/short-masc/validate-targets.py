from pathlib import Path
import re,json
w=Path(__file__).resolve().parent;rows=[];a='abcdefghijklmnopqrstuvwxyz{|'
for f in sorted(w.glob('target-*.result.txt'))+sorted(w.glob('target-*.lex-result.txt')):
 label=f.name.split('.')[0];base=label.removesuffix('-v3');inp,lang,N=base.rsplit('-',2);ct=(w/(inp+'.txt')).read_text().strip();cand=[]
 for line in f.read_text().splitlines():
  m=re.fullmatch(r'(\d+) score=([\d.-]+) key=([a-z{|]+) plain=([a-z]+) raw=([a-z{|]+)',line)
  if not m:continue
  rank=int(m[1]);score=float(m[2]);key=m[3];pt=m[4];raw=m[5]
  assert len(raw)==len(ct) and len(key)==int(N) and set(key)==set(a[:int(N)])
  assert ''.join(key[a.index(c)] for c in ct)==raw
  enc={c:a[i] for i,c in enumerate(key)};assert ''.join(enc[c] for c in raw)==ct
  cand.append({'rank':rank,'score':score,'decryption_key':key,'plaintext_folded':pt,'plaintext_raw':raw,'full_raw_reencryption':'PASS'})
 rows.append({'file':f.name,'input':inp+'.txt','lang':lang,'N':int(N),'stage':'lex' if '.lex-result' in f.name else 'gram','version':3 if label.endswith('-v3') else 1,'length':len(ct),'exploratory_control_limits':True,'candidates':cand})
assert len(rows)==120
(w/'target-summary.json').write_text(json.dumps(rows,indent=2)+'\n')
print(len(rows),'stage outputs,',sum(len(r['candidates']) for r in rows),'full raw candidate reencryptions PASS')
review=[]
for row in rows:
 if row['stage']!='lex':continue
 selected=[]
 for c in row['candidates']:
  p=c['plaintext_folded']
  if any(sum(a!=b for a,b in zip(p,q))<4 for q in selected):continue
  selected.append(p)
  if len(selected)==8:break
 review.append({'file':row['file'],'diverse_whole_texts':selected,'interpretation':'Incoherent; no word fragment claimed as deciphered'})
(w/'whole-text-inspection.json').write_text(json.dumps(review,indent=2)+'\n')
for r in review:
 if '-v3.' in r['file']:print(r['file'],'\n'+'\n'.join(r['diverse_whole_texts'][:4]))

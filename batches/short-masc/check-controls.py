from pathlib import Path
import json,re,sys
lexical='lex' in sys.argv
tag='-v3' if 'v3' in sys.argv else '-v2' if 'v2' in sys.argv else ''
suffix='.lex-result.txt' if lexical else '.result.txt'
w=Path(__file__).resolve().parent;alpha='abcdefghijklmnopqrstuvwxyz{|';out=[]
for c in json.loads((w/'controls.json').read_text()):
 found=[]
 for s in (w/(c['label']+tag+suffix)).read_text().splitlines():
  m=re.fullmatch(r'(\d+) score=([\d.-]+) key=([a-z{|]+) plain=([a-z]+) raw=([a-z{|]+)',s)
  if m:
   rank=int(m[1]);score=float(m[2]);key=m[3];p=m[4];raw=m[5]
   assert len(key)==c['N'] and set(key)==set(alpha[:c['N']]);assert ''.join(key[alpha.index(z)] for z in c['ciphertext'])==raw
   neighbors=[]
   for a in range(c['N']):
    for b in range(a,c['N']):
     k=list(key);k[a],k[b]=k[b],k[a];pp=''.join(k[alpha.index(z)] for z in c['ciphertext']).replace('{','c').replace('|','s')
     if pp==c['plaintext_folded']:neighbors.append([a,b])
   found.append({'rank':rank,'score':score,'plain':p,'raw':raw,'folded_exact':p==c['plaintext_folded'],'raw_exact':raw==c['plaintext_raw'],'positions_correct':sum(a==b for a,b in zip(p,c['plaintext_folded'])),'neighbor_truth':neighbors})
 out.append({'label':c['label']+tag,'top':found[0],'retained_exact_folded_ranks':[r['rank'] for r in found if r['folded_exact']],'retained_exact_raw_ranks':[r['rank'] for r in found if r['raw_exact']],'retained_truth_one_swap_ranks':[r['rank'] for r in found if r['neighbor_truth']],'survivor_count':len(found)})
(w/('control'+tag+('-lex' if lexical else '')+'-checks.json')).write_text(json.dumps(out,indent=2)+'\n')
print([(r['label'],r['top']['positions_correct'],r['retained_exact_folded_ranks'],r['retained_truth_one_swap_ranks']) for r in out])

from pathlib import Path
import json,re,hashlib,subprocess
w=Path(__file__).resolve().parent
records=json.loads((w/'controls.json').read_text());report={'reference_core':json.loads((w/'reference-validation.json').read_text())['all_pass'],'controls':[]}
def key(s):return list(map(int,s.strip(',').split(',')))
def dec(s,k):
 out=['']*len(s);at=0
 for c in k:
  for j in range(c,len(s),len(k)):out[j]=s[at];at+=1
 assert at==len(s);return ''.join(out)
def enc(s,k):return ''.join(s[c::len(k)] for c in k)
def refinedcheck(line,ct,p):
 m=re.search(r'key1=([0-9,]+) key2=([0-9,]+) ([a-z]+)',line);k1,k2=key(m[1]),key(m[2]);plain=m[3]
 assert sorted(k1)==list(range(len(k1))) and sorted(k2)==list(range(len(k2)))
 assert plain==dec(dec(ct,k2),k1) and enc(enc(plain,k1),k2)==ct
 return dict(matches=sum(a==b for a,b in zip(p,plain)),full_plaintext_exact=p==plain,key1=k1,key2=k2)
for c in records:
 name=c['label'];ct=(w/(name+'.txt')).read_text().strip();p=c['plaintext'];middle=dec(ct,c['keys'][1]);assert dec(middle,c['keys'][0])==p and enc(enc(p,c['keys'][0]),c['keys'][1])==ct
 line=(w/(name+'.true-middle.single-results.txt')).read_text().splitlines()[0];m=re.search('key=([0-9,]+) ([a-z]+)',line);assert key(m[1])==c['keys'][0] and m[2]==p
 results=[]
 for l in (w/(name+'.physical-results.txt')).read_text().splitlines():
  m=re.search(r'idp=([-0-9.]+) outer=([0-9,]+) ([a-z]+)',l);k2=key(m[2]);assert dec(ct,k2)==m[3] and enc(m[3],k2)==ct;results.append(dict(idp=float(m[1]),outer_exact=k2==c['keys'][1],outer_matches=sum(a==b for a,b in zip(k2,c['keys'][1]))))
 truth=float(subprocess.check_output([str(w/'idp'),'ciphers/hcp-363/work/segmented/bigrams.tsv',str(w/(name+'.true-middle.txt')),'20','17','score'],text=True))
 item=dict(label=name,known_key_roundtrip=True,true_outer_supplied_first_key_exact=True,true_outer_idp=truth,outer_candidates=results,pipeline=[])
 for f in sorted(w.glob(name+'.pipeline-*.refined.txt')):item['pipeline'].append(refinedcheck(f.read_text(),ct,p))
 for suffix in ['trigram','multigram','multigram-v2']:
  f=w/(name+'.'+suffix+'-results.txt')
  if f.exists():item[suffix]=[refinedcheck(l,ct,p) for l in f.read_text().splitlines()]
 report['controls'].append(item)
report['w16']={}
for c in json.loads((w/'controls-w16.json').read_text()):
 ct=(w/(c['label']+'.txt')).read_text().strip();ls=(w/(c['label']+'.physical-results.txt')).read_text().splitlines();anyexact=False
 for l in ls:
  m=re.search('outer=([0-9,]+) ([a-z]+)',l);k2=key(m[1]);assert dec(ct,k2)==m[2];anyexact|=k2==c['keys'][1]
 report['w16'][c['label']]={'outer_found':anyexact}
files=[w.parent.parent/'source/75391655400592-large.jpg',w.parent.parent/'source/metadata.md',w/'lasry-methodology.pdf',w/'IDPAnalyser.cs',w/'TranspositionTransformations.cs',Path('batches/scoring-sol61/model3.tsv'),Path('batches/scoring-sol61/model4.tsv'),Path('batches/scoring-sol61/model5.tsv'),Path('ciphers/hcp-363/work/segmented/bigrams.tsv')]
report['sha256']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files};report['target_attack_performed']=False;report['solved']=False
w.joinpath('validation.json').write_text(json.dumps(report,indent=2));print('PASS core reference, all four known-key/stage1 exact controls, all saved inverse/reencryption checks; outer discovery FAIL')
for c in report['controls']:print(c['label'],'best pipeline matches',max(x['matches'] for x in c['pipeline']),'/',len(next(r['plaintext'] for r in records if r['label']==c['label'])))

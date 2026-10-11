from pathlib import Path
import json,random,subprocess,re
P=Path(__file__).parent
alphabet='abcdefghijklmnopqrstuvwxyz'
def fit(ct,phrase,at):
 a={};b={}
 for c,v in zip(ct[at:at+len(phrase)],phrase):
  if (c in a and a[c]!=v) or (v in b and b[v]!=c):return None
  a[c]=v;b[v]=c
 return a
def solve(ct,mapping,label):
 rng=random.Random(396110);seeds=[]
 for i in range(32):
  free=[c for c in alphabet if c not in mapping];vals=[c for c in alphabet if c not in mapping.values()];rng.shuffle(vals);k=dict(mapping);k.update(zip(free,vals));seeds.append(''.join(k[c] for c in alphabet)+' '+''.join('1' if c in mapping else '0' for c in alphabet))
 (P/(label+'.seeds.txt')).write_text('\n'.join(seeds)+'\n');(P/(label+'.input.txt')).write_text(ct+'\n')
 out=subprocess.check_output([str(P/'locked'),'batches/scoring-sol61',str(P/(label+'.input.txt')),str(P/(label+'.seeds.txt')),'26'],text=True,stderr=subprocess.DEVNULL);(P/(label+'.result.txt')).write_text(out);rows=[]
 for line in out.splitlines():
  m=re.fullmatch(r'(\d+) score=([^ ]+) key=([a-z]+) plain=([a-z]+) raw=([a-z]+)',line);assert m;rank,score,key,plain,raw=m.groups();assert len(set(key))==26;assert ''.join(key[ord(c)-97] for c in ct)==plain;inv={v:alphabet[i] for i,v in enumerate(key)};assert ''.join(inv[c] for c in plain)==ct;assert all(key[ord(c)-97]==v for c,v in mapping.items());rows.append(dict(score=float(score),key=key,plaintext=plain))
 return rows
if __name__=='__main__':
 controls=[c for c in json.loads(Path('batches/short-masc/controls.json').read_text()) if c['lang']=='sk' and c['N']==26];rows=[]
 for c in controls:
  # Explicit known-plaintext calibration: only one supplied fifteen-letter crib;
  # no other plaintext or planted substitution table enters the optimizer.
  phrase=c['plaintext_raw'][5:20];mapping=fit(c['ciphertext'],phrase,5);candidates=solve(c['ciphertext'],mapping,c['label']);row=dict(control=c,known_crib=phrase,offset=5,candidates=candidates,truth_ranks=[i for i,r in enumerate(candidates) if r['plaintext']==c['plaintext_raw']],all_retained_reencrypt_exact=True);rows.append(row);(P/'controls.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False));print(c['label'],row['truth_ranks'],flush=True)

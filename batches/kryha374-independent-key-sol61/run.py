from pathlib import Path
import json,hashlib,unicodedata
B=Path(__file__).resolve().parent;r=json.loads(Path('batches/kryha373-tail-sliding-sol61/SAT-(2, 462, 23).json').read_text());raw=Path('ciphers/hcp-374/work/transcription.txt').read_text();ct=''.join(raw.split());assert len(ct)==85 and ct[:5]=='kidah';body=ct[5:];P,O,K=r['P'],r['O'],r['K'];free=set('fgjmqwx');known={v:chr(97+i)for i,v in enumerate(P)if chr(97+i)not in free};ip={v:chr(97+i)for i,v in enumerate(P)}
published=Path('batches/kryha373-collation-sol61/plaintext-typed.txt').read_text();segment=published[published.index('a upozorňuje'):].replace('-\n','');expected=''.join(ch for ch in unicodedata.normalize('NFD',segment.lower())if'a'<=ch<='z').replace('j','i');assert len(expected)<=80
rows=[]
for phase in range(23):
 for shift in range(26):
  coords=[(O[ord(c)-97]-K[(i+phase)%23]-179*((i+phase)//23)-shift)%26 for i,c in enumerate(body)];decoded=''.join(known.get(x,'?')for x in coords);literal=''.join(ip[x]for x in coords);score=sum(a==b for a,b in zip(decoded,expected));rows.append(dict(phase=phase,shift=shift,coordinates=coords,known_decode=decoded,arbitrary_completion_decode=literal,known_matches=score,comparison_length=len(expected),unknown_positions=[i+1 for i,x in enumerate(coords)if x not in known]))
rows.sort(key=lambda x:x['known_matches'],reverse=True);best=rows[0]
# Independent physical encoder/displacement, using frozen recovered23-hole mask.
physical=json.loads(Path('batches/kryha373-physical-tail-sol61/summary.json').read_text());holes=[26,29,31,34,37,40,42,44,45,47,48,49,51,2,4,5,8,11,13,17,20,21,24];edges=physical['geometry'];phase=best['phase'];shift=best['shift'];disp=K[phase]+shift;h=holes[phase];out=[];inverseO={v:chr(97+i)for i,v in enumerate(O)}
for i,x in enumerate(best['coordinates']):
 out.append(inverseO[(x+disp)%26]);end=holes[(phase+i+1)%23]
 while h!=end:disp+=edges[h];h=(h+1)%52
assert ''.join(out)==body
best['independent_full80_physical_coordinate_reencryption']=True;best['first_five_literal']='kidah';best['prefix_semantics_unestablished']=True;best['expected_published_suffix']=expected;best['differences']=[dict(body_onebased=i+1,source_onebased=i+6,decoded=a,expected=b,coordinate=best['coordinates'][i])for i,(a,b)in enumerate(zip(best['known_decode'],expected))if a!=b]
(B/'results.json').write_text(json.dumps(dict(best=best,next_candidates=rows[1:6],all_phase_shift_cases=598,unused_P_letters=sorted(free),hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path('ciphers/hcp-374/work/transcription.txt'),Path('batches/kryha373-tail-sliding-sol61/SAT-(2, 462, 23).json')]}),indent=2)+'\n');print(json.dumps(best,indent=2))

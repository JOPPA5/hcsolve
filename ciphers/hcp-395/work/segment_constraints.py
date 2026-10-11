from pathlib import Path
import json, random, collections, math
p=Path(__file__).resolve().parent
groups=(p/'transcription.txt').read_text().split(); assert len(groups)==57 and all(len(g)==5 for g in groups)
def digitcode(n):return ''.join(str((n+j)%10) for j in range(5)) if n<10 else str(n)+'0'+str(n+1)
def feasible(g,n):
 d=digitcode(n);m={}
 for c,x in zip(g,d):
  if c in m and m[c]!=x:return False
  m[c]=x
 return all(list(m.values()).count(x)<=3 for x in set(m.values()))
indicators=[dict(group=i+1,text=g,alignment=[n for n in range(1,23) if feasible(g,n)]) for i,g in enumerate(groups)]
# Boundaries assume one five-letter indicator in each segment and published50minimum payload.
bounds=[i for i in range(1,57) if 50<=5*i-5<=250 and 50<=5*(57-i)-5<=250]
# Actual standard triple-columnar mathematics admits285-letter messages; test exact known-key controls.
def enc(s,k):return ''.join(s[c::len(k)] for c in k)
def dec(s,k):
 n=len(s);w=len(k);h,e=divmod(n,w);o=['']*n;at=0
 for c in k:
  for r in range(h+(c<e)):o[r*w+c]=s[at];at+=1
 return ''.join(o)
rng=random.Random(395);keys=[]
for width in (16,18,20):
 k=list(range(width));rng.shuffle(k);keys.append(k)
def triple_enc(s):
 for k in keys:s=enc(s,k)
 return s
def triple_dec(s):
 for k in keys[::-1]:s=dec(s,k)
 return s
base='ministerstvozahranicnychvecioznamujezespravaboladorucenadnesranoaprosimzasliteodpovedconajskorabysmemohlipripravitpotrebnedokumenty'
controls=[]
for n in (50,75,200,250,280,285):
 plain=(base*4)[:n];cipher=triple_enc(plain);ok=triple_dec(cipher)==plain;assert ok
 controls.append(dict(length=n,known_key_exact=ok))
# Insert/remove indicators in a two-segment285-letter control (205+80 ciphertext).
segment_plain=[(base*4)[:200],(base*4)[23:98]];cipher_segments=[]
for j,s in enumerate(segment_plain):
 ct=triple_enc(s);gs=[ct[i:i+5] for i in range(0,len(ct),5)];gs.insert(4,'defgh' if j==0 else 'jabcd');cipher_segments.append(''.join(gs))
joined=''.join(cipher_segments);assert len(joined)==285
for start,stop,plain in [(0,205,segment_plain[0]),(205,285,segment_plain[1])]:
 block=joined[start:stop];payload=block[:20]+block[25:];assert triple_dec(payload)==plain
out=dict(body_letters=285,body_groups=57,printed_line_groups=[8,8,8,8,8,8,8,1],physical_boundary_evidence=False,R_two_segment_boundary_groups=bounds,R_two_segment_boundary_letters=[5*i for i in bounds],XQ_two_segment_boundary_groups=[i for i in bounds if 5*i-5<=200 and 5*(57-i)-5<=200],indicators=indicators,known_key_controls=controls,two_segment_control=dict(cipher_lengths=[205,80],payload_lengths=[200,75],indicator_group_position=5,exact=True))
(p/'segment-constraints.json').write_text(json.dumps(out,indent=2));(p/'segment-control.json').write_text(json.dumps(dict(keys=keys,plain=segment_plain,cipher_segments=cipher_segments),indent=2));print('R allowed boundaries',out['R_two_segment_boundary_groups']);print('XQ allowed boundaries',out['XQ_two_segment_boundary_groups']);print('Controls exact:',all(x['known_key_exact'] for x in controls),'two-segment285 exact')

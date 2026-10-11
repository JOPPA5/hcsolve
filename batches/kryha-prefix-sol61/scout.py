from pathlib import Path
import json,itertools,random
b=Path(__file__).resolve().parent;r=b.parents[1]
def jumps(k):
 d=k['adjacent_distances'];h=k['holes'];a=[]
 for x,y in zip(h,h[1:]+h[:1]):
  v=0
  while True:
   v+=d[x];x=(x+1)%52
   if x==y:break
  a.append(v)
 assert sum(a)==179;return a
def decode(ct,k,phase,offset,presses):
 a=jumps(k);P,O=k['P'],k['O'];pt='';states=[]
 for i,c in enumerate(ct):
  states.append((phase,offset));pt+=chr(97+P[(O[ord(c)-97]-offset)%26])
  for _ in range(presses[i]):offset=(offset+a[phase])%26;phase=(phase+1)%len(a)
 return pt,(phase,offset),states
def encode(pt,k,phase,offset,presses):
 # Independent physical coordinate sign/advance, no jumps helper.
 h=k['holes'];d=k['adjacent_distances'];ip={v:i for i,v in enumerate(k['P'])};io={v:i for i,v in enumerate(k['O'])};ct=''
 for i,c in enumerate(pt):
  ct+=chr(97+io[(ip[ord(c)-97]+offset)%26])
  for _ in range(presses[i]):
   x=h[phase];y=h[(phase+1)%len(h)]
   while True:
    offset=(offset+d[x])%26;x=(x+1)%52
    if x==y:break
   phase=(phase+1)%len(h)
 return ct,(phase,offset)
def connected(ct,k,end,choices):
 n=len(ct);a=jumps(k);out=[]
 for presses in itertools.product(choices,repeat=n):
  phase=(end[0]-sum(presses))%len(a);off=(end[1]-sum(a[(phase+i)%len(a)] for i in range(sum(presses))))%26
  pt,got,states=decode(ct,k,phase,off,presses);assert got==end;assert encode(pt,k,phase,off,presses)==(ct,end)
  out.append(dict(plaintext=pt,start_phase=phase,start_displacement=off,presses=presses,full_prefix_reencryption_exact=True,J_selective_extra=all(p==1+(c=='j') for p,c in zip(presses,pt))))
 return out
def independent(ct,k):
 out=[]
 for phase in range(len(k['holes'])):
  for off in range(26):
   pt,end,_=decode(ct,k,phase,off,[1]*len(ct));assert encode(pt,k,phase,off,[1]*len(ct))==(ct,end);out.append(dict(plaintext=pt,start_phase=phase,start_displacement=off,presses=[1]*len(ct),prefix_reencryption_exact=True))
 return out
def run_actual():
 actual=[]
 for n in (350,351):
  d=r/f'ciphers/hcp-{n}/work/kryha-decipherment';k=json.load(open(d/'key.json'));ct=(d/'ciphertext.txt').read_text().strip();pt,end,states=decode(ct[:5],k,0,k['initial_displacement'],[1]*5);assert pt==k['plaintext'][:5]
  reset=independent(ct[:5],k);stat=[]
  for off in range(26):
   txt,_,_=decode(ct[:5],k,0,off,[0]*5);stat.append(dict(plaintext=txt,relative_displacement=off))
  row=dict(number=n,literal_cipher_prefix=ct[:5],continuation_state_at_five=end,ordinary_continuation=pt,carry_optional_extra=connected(ct[:5],k,end,[1,2]),carry_optional_hold_or_extra=connected(ct[:5],k,end,[0,1,2]),independent_reset=reset,known_rings_static_indicator=stat,body_key_unchanged=True,source_letters_unchanged=True)
  actual.append(row)
 A,B=[{x['plaintext'] for x in rr['independent_reset']} for rr in actual];summary=dict(shared_same_plaintext_independent_reset=sorted(A&B),shared_independent_reset_count=len(A&B),unrestricted_shared_MASC_indicator_assignments=26*25*24,unrestricted_indicator_pattern='ABABC',not_uniquely_identified=True,rows=[])
 for row in actual:
  summary['rows'].append(dict(number=row['number'],ordinary_carry=row['ordinary_continuation'],carry_extra_unique=len({x['plaintext'] for x in row['carry_optional_extra']}),carry_hold_extra_unique=len({x['plaintext'] for x in row['carry_optional_hold_or_extra']}),J_extra_candidates=[x for x in row['carry_optional_extra'] if x['J_selective_extra']],independent_reset_unique=len({x['plaintext'] for x in row['independent_reset']}),static_indicator=row['known_rings_static_indicator']))
 summary['same_clear_prefix_carry_intersections']={branch:sorted({x['plaintext'] for x in actual[0][branch]}&{x['plaintext'] for x in actual[1][branch]}) for branch in ('carry_optional_extra','carry_optional_hold_or_extra')}
 (b/'actual-candidates.json').write_text(json.dumps(actual,indent=2)+'\n');(b/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('Shared independent prefix choices:',summary['shared_independent_reset_count'],'; J-only carry gives only original literal prefix per copy')

if __name__=="__main__":run_actual()

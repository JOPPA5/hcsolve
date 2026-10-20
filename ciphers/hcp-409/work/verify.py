"""Independent absolute-coordinate verification; imports neither solver nor decoder."""
import json,hashlib,random
from pathlib import Path
w=Path(__file__).resolve().parent;k=json.loads((w/'key.json').read_text());edges=k['adjacent_distances'];coord=[0]
for e in edges:coord.append(coord[-1]+e)
assert len(coord)==53 and coord[-1]==179
h=k['holes_zero_based'];assert len(h)==23 and len(set(h))==23
unwrapped=[h[0]]
for x in h[1:]:unwrapped.append(x+(52 if x<h[0]else 0))
D=[coord[x%52]+179*(x//52)-coord[h[0]]for x in unwrapped]
P=k['input_positions'];O=k['output_positions'];assert sorted(P)==sorted(O)==list(range(26))
pinv={x:i for i,x in enumerate(P)};oinv={x:i for i,x in enumerate(O)}
ct=''.join((w/'transcription.txt').read_text().split());plain=[];reen=[]
for i,c in enumerate(ct):
 d=(k['first_displacement']+D[i%23]+179*(i//23))%26
 x=pinv[(O[ord(c)-97]-d)%26];plain.append(chr(97+x));reen.append(chr(97+oinv[(P[x]+d)%26]))
assert ''.join(reen)==ct
print('Independent coordinate decode:', ''.join(plain).upper());print('PASS',len(ct),'/',len(ct),'roundtrip; arc sum179; physical stop start',h[0],'; d0',k['first_displacement'])
# Every phase and starting displacement must invert a fresh deterministic control.
rng=random.Random(409);control=[rng.randrange(26)for _ in range(347)]
for phase in range(23):
 for start in range(26):
  for i,x in enumerate(control):
   j=phase+i; d=(start+D[j%23]+179*(j//23)-D[phase])%26
   c=oinv[(P[x]+d)%26];assert pinv[(O[c]-d)%26]==x
print('PASS598 phase/displacement control roundtrips,347 letters each; this verifies mechanics, not language or source glyphs')

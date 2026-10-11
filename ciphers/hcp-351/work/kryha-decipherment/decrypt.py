from pathlib import Path
import argparse,json,hashlib
here=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--variant',choices=['reviewed','collated','strong','moderate','collated-moderate'],default='reviewed');parser.add_argument('--json',action='store_true');args=parser.parse_args()
key=json.loads((here/'key.json').read_text())
for entry in key['source_images']:
 image=here.parents[1]/entry['path']
 assert hashlib.sha256(image.read_bytes()).hexdigest()==entry['sha256'],'Source image changed'
filename={'reviewed':'ciphertext.txt','collated':'ciphertext-before-review1.txt','strong':'ciphertext-strong.txt','moderate':'ciphertext-moderate.txt','collated-moderate':'ciphertext-collated-moderate.txt'}[args.variant]
raw=(here/filename).read_bytes()
assert hashlib.sha256(raw).hexdigest()==json.loads((here/'transcription-hashes.json').read_text())[filename],'Working transcription changed'
ct=raw.decode().strip()
assert len(ct)==385 and all('a'<=c<='z' for c in ct)
P,O,holes,dist=key['P'],key['O'],key['holes'],key['adjacent_distances']
assert sorted(P)==sorted(O)==list(range(26)) and len(set(holes))==23 and sum(dist)==179
jumps=[]
for a,b in zip(holes,holes[1:]+holes[:1]):
 total=0
 while True:
  total+=dist[a];a=(a+1)%52
  if a==b:break
 jumps.append(total)
assert sum(jumps)==179
pt=[];d=key['initial_displacement'];schedule=[]
for i,c in enumerate(ct):
 schedule.append(d);pt.append(chr(97+P[(O[ord(c)-97]-d)%26]));d=(d+jumps[i%23])%26
pt=''.join(pt);ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)}
assert ''.join(chr(97+io[(ip[ord(c)-97]+d)%26])for c,d in zip(pt,schedule))==ct
if args.json:print(json.dumps(dict(prepared_plaintext=pt,unknown_prefix=pt[:5],variant=args.variant,reencryption_exact=True,input_labels_not_unique=True)))
else:print(pt.upper())

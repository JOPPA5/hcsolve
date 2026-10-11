from pathlib import Path
import json,hashlib,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[1];out=[]
for n in [350,351]:
 d=ROOT/f'ciphers/hcp-{n}/work/kryha-decipherment';saved=P/str(n);saved.mkdir(exist_ok=True)
 for f in ['key.json','ciphertext.txt','prepared-plaintext.txt']:shutil.copyfile(d/f,saved/f)
 key=json.loads((saved/'key.json').read_text());ct=(saved/'ciphertext.txt').read_text().strip().lower();expected=(saved/'prepared-plaintext.txt').read_text().strip().lower();A=key['P'];B=key['O'];holes=key['holes'];dist=key['adjacent_distances'];assert sorted(A)==sorted(B)==list(range(26))
 # Independently construct absolute52-stop coordinate and successivehole travel.
 coord=[0]
 for step in dist:coord.append(coord[-1]+step)
 assert len(coord)==53 and coord[-1]==179
 moves=[(coord[b]-coord[a])%179 for a,b in zip(holes,holes[1:]+holes[:1])];assert sum(moves)==179
 ds=[];shift=key['initial_displacement']
 for i in range(len(ct)):ds.append(shift);shift=(shift+moves[i%23])%26
 pt=''.join(chr(97+A[(B[ord(c)-97]-ds[i])%26]) for i,c in enumerate(ct));ia={v:i for i,v in enumerate(A)};ib={v:i for i,v in enumerate(B)};back=''.join(chr(97+ib[(ia[ord(c)-97]+ds[i])%26]) for i,c in enumerate(pt));assert pt==expected and back==ct
 checks=dict(cipher=n,length=len(ct),inverse_exact=True,reencryption_exact=True,ciphertext_hash=hashlib.sha256(ct.encode()).hexdigest(),key_hash=hashlib.sha256((saved/'key.json').read_bytes()).hexdigest(),source_hashes={v['path']:hashlib.sha256((ROOT/f'ciphers/hcp-{n}'/v['path']).read_bytes()).hexdigest() for v in key['source_images']},prefix_ciphertext=ct[:5],prefix_plaintext=pt[:5]);out.append(checks)
 if n==351:
  strong=list(ct);strong[239]='j';strongplain=''.join(chr(97+A[(B[ord(c)-97]-ds[i])%26]) for i,c in enumerate(strong));(saved/'strong240J-only-plaintext.txt').write_text(strongplain.upper()+'\n');(saved/'strong240J-only-ciphertext.txt').write_text(''.join(strong)+'\n');assert strongplain[230]=='i' and strongplain[239]=='e';corrected=strong.copy();corrected[230]='i';new=''.join(chr(97+A[(B[ord(c)-97]-ds[i])%26]) for i,c in enumerate(corrected));(saved/'pixel-preferred-alternative-plaintext.txt').write_text(new.upper()+'\n');(saved/'pixel-preferred-alternative-ciphertext.txt').write_text(''.join(corrected)+'\n');assert new[230]=='s' and new[239]=='e'
(P/'verification.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

"""Read-only held-out context check; not a new decipherment of Solved373."""
from pathlib import Path
import json,hashlib,sys,argparse
sys.dont_write_bytecode=True
from decrypt import load,displacements
root=Path(__file__).resolve().parents[3];key,_=load()
ctfile=root/'batches/kryha373-collation-sol61/ciphertext650.txt';ct=ctfile.read_text().strip();assert len(ct)==650 and ct[:5]=='kidah'
P=key['input_positions'];O=key['output_positions'];inverse={slot:chr(97+i) for i,slot in enumerate(P)}
body=''.join(inverse[(O[ord(c)-97]-d)%26] for c,d in zip(ct[5:],displacements(key,645)))
assert body.startswith('roesnermadridoznamil') and body.endswith('ciencelulozyxx')
assert 'spanielskeprotidodavky' in body and 'xasociacion' in body and 'xvysetri' in body
assert ct[:5]=='kidah'
result=dict(source=str(ctfile.relative_to(root)),sha256=hashlib.sha256(ctfile.read_bytes()).hexdigest(),retained_source_prefix=ct[:5],prefix_not_deciphered=True,context_body_letters=645,tail_fit_letters=186,body_letters_outside_fit=459,literal_context_body_with_canonical_unused_labels=body,terminal_x_count=len(body)-len(body.rstrip('x')),sentence_x_windows=[body[max(0,i-18):i+25] for i,c in enumerate(body) if c=='x'],statement='Running Slovak outside the fitted tail supports the key; source collation/glyph errors and unbound rare labels remain. Published373content is attributed, not a new plaintext discovery.')
ap=argparse.ArgumentParser();ap.add_argument('--save',action='store_true');args=ap.parse_args()
if args.save:(Path(__file__).parent/'heldout373.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

"""Hash this card's current source/reference/manual artifacts; writes only work/sha256.json."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
references=[R/'ciphers/hcp-1520/work/key.json',R/'batches/easy-2026-10-28/published-anna-ticha-key.txt',R/'batches/easy-2026-10-28/public-reference-199/picture.jpg',R/'batches/easy-2026-10-28/public-reference-199/provenance.json']
manifest={'sources':{str(p.relative_to(R)):sha(p) for p in sorted((C/'source').iterdir()) if p.is_file()},'references':{str(p.relative_to(R)):sha(p) for p in references},'records':{str(p.relative_to(R)):sha(p) for p in sorted(W.iterdir()) if p.is_file() and p.name!='sha256.json'}}
(W/'sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
print({k:len(v) for k,v in manifest.items()});print('manifest_sha256',sha(W/'sha256.json'))

"""Authoring helper: hashes only; writes this work/manifest.json only."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
refs=[R/'ciphers/hcp-1520/work/key.json',R/'batches/easy-2026-10-28/published-anna-ticha-key.txt']
base=R/'batches/easy-2026-10-28/public-reference-199'
refs += [base/name for name in ('picture.jpg','provenance.json','upright.png','f-comparison.json','f-comparison.png')]
paths=[C/'SOLUTION.md',C/'NOTES.md']+[p for p in W.iterdir() if p.is_file() and p.name!='manifest.json']
def entries(items):return {str(p.relative_to(R)):sha(p) for p in sorted(items)}
manifest={'method':'SHA256 file integrity, not proof of manual glyph readings. Own3 source entries only; fixed9 guard never extended. Manifest excludes itself.','sources':entries(p for p in (C/'source').iterdir() if p.is_file()),'references':entries(refs),'records':entries(paths)}
(W/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen',len(manifest['sources']),'sources,',len(refs),'references,',len(paths),'records')

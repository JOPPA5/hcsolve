from pathlib import Path
import json
from exact_cover import solve
P=Path(__file__).parent;rows=[json.loads(x) for x in (P/'equal17-22-n11.jsonl').read_text().splitlines()];src=next(x for x in rows if x['widths']==[17]*3 and x['mode']=='independent_aligned_triple_control');out=solve(src['plaintext'],src['ciphertext'],src['widths'],60000,0,src['alignments'],backend='eager',anchors=True);out.update(mode='matched_unique_anchor_eager_control',planted_keys=src['planted_keys'],keys_equal_planted=out.get('keys')==src['planted_keys'],plaintext=src['plaintext'],ciphertext=src['ciphertext']);(P/'anchors-eager-control17.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

from pathlib import Path
import json, random
from solve import solve, encode

P = Path(__file__).parent
rng = random.Random(36462501)
rows = []
for text, widths, rank, timeout in [
    ('abcabdc', [2,3,4], 1, 10),
    ('nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcisloxr', [21,19,20], 5, 60),
    ('nezavislykontrolnytelegramoverujepresnosttrojitehoprehadzovaniapismenx'[:65], [21,19,20], 7, 60),
]:
    keys=[]
    for w in widths:
        key=list(range(1,w));rng.shuffle(key);key.insert(rank-1,0);keys.append(key)
    ct=text
    for key in keys:ct=encode(ct,key)
    result=solve(text,ct,widths,[rank]*3,timeout)
    result.update(plaintext=text,ciphertext=ct,planted_keys=keys,stage='fresh-blind-coordinate-control')
    rows.append(result)
    (P/'controls.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(result['status'],result['seconds'],flush=True)

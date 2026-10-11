import json, random, subprocess
from pathlib import Path

p = Path(__file__).parent
authored = json.loads((p / 'quagmire-controls.json').read_text())[2]
found = (p / 'quag2-exact-control-3-result.txt').read_text().splitlines()[0].split()[1]
assert found == authored['plaintext']
truth = json.loads((p / 'quag1-heldout-controls.json').read_text())[0]['plaintext']
rng = random.Random(334523)
K = list(range(26)); rng.shuffle(K)
R = [rng.randrange(26) for _ in range(3)]
inv = [K.index(x) for x in range(26)]
ct = ''.join('?' if c == '?' else chr(97 + inv[(ord(c)-97+R[i%3])%26]) for i,c in enumerate(truth))
f = p / 'quag2-heldout-3.txt'; f.write_text(ct+'\n')
out = subprocess.check_output([str(p/'quag2_exact'), str(p/'quadgrams.tsv'), str(f), '3'], text=True)
(p/'quag2-heldout-3-result.txt').write_text(out)
lines = out.splitlines(); found = lines[0].split()[1]
key = [int(v) for v in lines[1].split(',') if v]
offset = [int(v) for v in lines[2].split(',') if v]
coverage = []
for a in range(26):
    for b in range(a,26):
        k = key[:]; k[a],k[b] = k[b],k[a]
        s = ''.join('?' if c=='?' else chr(97+(k[ord(c)-97]-offset[i%3])%26) for i,c in enumerate(ct))
        if s == truth: coverage.append([a,b])
control = dict(source='Slovak UD TEST sentence in quag1-heldout-controls.json; excluded from TRAIN', plaintext=truth, K=K, R=R, found=found, exact=found==truth, matched_known=sum(a==b for a,b in zip(found,truth) if b!='?'), blind_swap_neighborhood_contains_truth=bool(coverage), diagnostic_matching_swaps=coverage)
(p/'quag2-heldout-control.json').write_text(json.dumps(control,indent=2))
print('CONTROL',control['exact'],control['matched_known'],bool(coverage),flush=True)
assert coverage, 'No target inference from failed calibration'
rows=[]
for gap in range(5):
    f=p/f'target-phase-{gap}.txt'; ct=f.read_text().strip()
    for T in range(1,4):
        out=subprocess.check_output([str(p/'quag2_exact'),str(p/'quadgrams.tsv'),str(f),str(T)],text=True)
        stem=f'quag2-target-{gap}-{T}'
        (p/f'{stem}-result.txt').write_text(out)
        lines=out.splitlines(); key=[int(v) for v in lines[1].split(',') if v]; offset=[int(v) for v in lines[2].split(',') if v]
        neighbors=[]
        for a in range(26):
            for b in range(a,26):
                k=key[:]; k[a],k[b]=k[b],k[a]
                s=''.join('?' if c=='?' else chr(97+(k[ord(c)-97]-offset[i%T])%26) for i,c in enumerate(ct))
                neighbors.append(dict(swap=[a,b],alphabet_key=k,plaintext=s))
        (p/f'{stem}-neighbors.json').write_text(json.dumps(neighbors,indent=2))
        row=dict(second_gap_position=90+gap,T=T,score=float(lines[0].split()[0]),plaintext=lines[0].split()[1],alphabet_key=key,phase_offsets=offset,enumeration=lines[3])
        rows.append(row); (p/'quag2-target-summary.json').write_text(json.dumps(rows,indent=2))
        print(gap,T,row['score'],row['plaintext'],flush=True)

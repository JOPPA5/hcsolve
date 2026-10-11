"""Independent check against manually read intermediate grids, not a target solution."""
from pathlib import Path
import json
p=Path(__file__).parent
plain='stahovanievyslanectvanutnexposlitesemihnedsluzobnyvozxx'
labels=[
    [7,10,21,3,18,6,20,1,19,15,9,13,5,16,2,17,4,12,8,11,14],
    [7,15,8,6,18,3,10,9,17,14,2,13,1,19,11,5,12,4,16],
    [7,20,3,12,6,19,8,16,2,17,1,18,11,5,9,4,10,15,14,13],
]
scan_grids=[
    'noyaehnzeisexvxbsnstnviztulvechytxadelolsnmoeoisvapnatu',
    'xypscvhtonebatainntoyvszlonuexxasduehaiesonlsleviezmvtn',
]
def enc(s,k):
    return ''.join(s[c::len(k)] for c in sorted(range(len(k)),key=lambda c:k[c]))
def dec(s,k):
    out=['']*len(s); at=0
    for c in sorted(range(len(k)),key=lambda c:k[c]):
        for j in range(c,len(s),len(k)):out[j]=s[at];at+=1
    return ''.join(out)
assert len(plain)==55
s=plain; stages=[]
for i,k in enumerate(labels):
    assert sorted(k)==list(range(1,len(k)+1))
    prev=s;s=enc(s,k);assert dec(s,k)==prev
    if i<2:assert s==scan_grids[i]
    stages.append(dict(width=len(k),physical_column_labels=k,output=s,intermediate_grid_matches_scan=(s==scan_grids[i]) if i<2 else None))
report=dict(source='Antal/Zajac/Grosek, HistoCrypt2020 Fig.5 p.28; immutable PDF batches/analysis-395-396/context-paper.pdf',model='Standard irregular row-write, ascending-column-label read',published_plaintext=plain,stages=stages,verified='Both intermediate grids and independent inverse match. Different widths21/19/20. Ciphertext grouping/inserted indicator not independently verified from the handwritten bottom.',alignment='Rotate physical column labels to start with n; do not confuse this with cyclic rotation of column-read-order indices.',target_solution=False)
(p/'r-example-verification.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

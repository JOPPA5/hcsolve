# hcp-1005 partial decode: number substitution A=1 ... I=9, K=10 ... Z=25 (no J).
# Transcription is the solver's reading of work/hires/..._adr.jpg (rotated 90 deg CCW); '?' = unread token.
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {'source/address-large.jpg':'6f2a99ca106d74095674d79f2de557c7bea5e0d5419d610e57c162ba3e9a1e02',
     'work/hires/cpc_1916-09-19_DE_Pollwitz_DE_Pollwitz__adr.jpg':'c5ad56c0945903e00ba27abd45b9dcd14a877f1f582fb349dbc8e9459819a4b7'}
for p,h in H.items():
    ok = hashlib.sha256((D/p).read_bytes()).hexdigest()==h
    print(('OK  ' if ok else 'BAD ')+p)
ROWS = ["11 9 5 2 5 . 5 11 18 1 .",
        "18 17 9 2 9 2 5 . 1 . 12 18 14 13=",
        "19 1 7 . 18 1 8 2 20 13 1",
        "2 5 18 14 5 13 . 7 17 20 18",
        "18 5 20 11 12 1 2 ?"]
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
for r in ROWS:
    out=[]
    for t in r.split():
        if t=='.': out.append('.'); continue
        if t=='?': out.append('?'); continue
        nn = t.endswith('='); t=t.rstrip('=')
        out.append(A[int(t)-1]+('[bar]' if nn else ''))
    print(r.ljust(40), ' '.join(out))

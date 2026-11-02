"""HCP1238: check scan hashes and print the partial literal reading. From repo root:
   python3 -I ciphers/hcp-1238/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/address-large.jpg': '10860b4b591123c1e3d3e2cc85b07683304af8dcc2deda19b74a036e5a46f7f2',
     'source/picture-large.jpg': '1dc0c72901470ea03051de34a24bfea3a9ad2880c9ca4a22675b890e706f3e1e'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
for l in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        print(l.split('#')[0].rstrip())

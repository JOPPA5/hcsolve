"""HCP1212: decode the manual shape-token ledger with the Jolanka-family key.
Run from the repo root:  python3 -I ciphers/hcp-1212/work/decode.py
Checks the SHA-256 of both source scans first. No OCR: tokens were entered by hand from the scan.
"""
import hashlib, sys, unicodedata
from pathlib import Path
D = Path(__file__).resolve().parents[1]
HASHES = {
    'source/address.jpg': '1eb57dcfe494a694a0de4e9b44ea1289e2edc7031052b0f25f6d7e6b88ab0a0d',
    'source/picture.jpg': '0c95ace98b42e67e140e2cfa819b71fdc94443d3f46c1becb49f0da9e5ddb85c',
}
for f, h in HASHES.items():
    got = hashlib.sha256((D / f).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f'hash mismatch for {f}: {got}')
KEY = {'A':'a','6':'b','(':'c','D':'d','E':'e','+':'f','G':'g','H':'h','I':'i','J':'j','K':'k',
       'L':'l','M':'m','N':'n','O':'o','P':'p','F':'r',')':'s','T':'t','X':'u','V':'v','Y':'y','Z':'z',
       ',':',','.':'.','T?':'{t?}','S?':'{s?}','R?':'{r?}'}
ACC = {'acute':'́','diaeresis':'̈','double-acute':'̋'}
for line in (D / 'work/as-seen-pass6.txt').read_text(encoding='utf-8').splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    row, *toks = line.split()
    out = []
    for t in toks:
        base, _, acc = t.partition(':') if t not in ('T?','S?','R?') else (t, '', '')
        ch = KEY[base]
        if acc:
            ch = unicodedata.normalize('NFC', ch + ACC[acc])
        out.append(ch)
    print(f'{row}: ' + ''.join(out))

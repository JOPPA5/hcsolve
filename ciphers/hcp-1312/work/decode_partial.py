import hashlib,pathlib,re
d=pathlib.Path('ciphers/hcp-1312')
for f,h in (('source/picture-large.jpg','dd64d57e9cad75d9c542fa0982c2351a844f704e7823a64ec90730e2b923db5c'),
            ('source/address-large.jpg','ff0aa5f61da71f1a043a027d98a9383980339dec1274607fdc2db94eea778903')):
    print(f,'OK' if hashlib.sha256((d/f).read_bytes()).hexdigest()==h else 'HASH MISMATCH')
for l in (d/'work/ledger-partial.txt').read_text().splitlines():
    if not l.startswith('#'):
        n,*t=l.split(); print(n,''.join(x for x in t))

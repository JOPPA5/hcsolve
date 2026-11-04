#!/usr/bin/env python3
"""hcp-1133: decode the Morse passages. Run from repo root:
   python3 -I ciphers/hcp-1133/work/decode.py
Checks the SHA-256 of the source scans, then decodes work/morse_transcription.txt."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': 'f0bf46850f8d085a0efc7ba17ca5a1b5703c464f306726625a13281450397672',
 'source/address-large.jpg': '9181d3adeae975759ad6dd9e226614c3cfd01f5beecb829d8d58ba030edcc7d3',
 'work/hires/cpc_1902-12-18_HU__HU_Helyben__pic.jpg': '7df89b9708fbfaf9fe35620caf82a7172da6e2185a8f97a4fe2131fd9df97b18',
 'work/hires/cpc_1902-12-18_HU__HU_Helyben__adr.jpg': 'a80132f1b2958cbd8be817c5ac71267bf68dbea19a81432a4213ba392b8ebcc0',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p); ok &= got == h
if not ok: sys.exit('hash mismatch')
# International Morse; plus the writer's own A-acute (.-.-- , not the standard .--.-)
# and standard Hungarian E-acute ..-..
M = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',
     '.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
     '..-..':'É','.-.--':'Á'}
out = {}
cur = None
for line in open(os.path.join(D, 'work/morse_transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('['): cur = line[1:3]; out[cur] = []; continue
    groups = [g for g in line.replace(' ', '').split('/') if g]
    out[cur].append(''.join(M.get(g, '?') for g in groups))
for k, v in out.items():
    print(f'{k}: ' + ' | '.join(v))
    print(f'{k} joined: ' + ''.join(v))

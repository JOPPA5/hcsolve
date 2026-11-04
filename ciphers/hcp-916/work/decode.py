#!/usr/bin/env python3
"""hcp-916: decode the Morse text on the picture side. Run from repo root:
   python3 -I ciphers/hcp-916/work/decode.py
Checks the SHA-256 of the source scans, then decodes work/morse_transcription.txt."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': 'cdab62a7678ed8b511c85a67bc967a8d9aa1fd06248ee3f669c2f278665a9ac8',
 'source/address-large.jpg': '83d145f05c51e4ef1ddef96d4cfe0a48705dcda5615623f1acaaf8ecb0a4a247',
 'work/hires/cpc_1904-04-01_HU_Temesvar_RO_Temesvar-Jozsefvaros__pic.jpg': '91e360513b3d8ba1d5370ec200a19866a893cb56c2d741b2a3b399197e4d5631',
 'work/hires/cpc_1904-04-01_HU_Temesvar_RO_Temesvar-Jozsefvaros__adr.jpg': '1606daecb623e738f15b8d157e9e648442c5e8c12850ebe8ba21536d21315ce2',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p); ok &= got == h
if not ok: sys.exit('hash mismatch')
# International Morse + Hungarian E-acute ..-.. + the writer's own A-acute .-.-- (same as on hcp-1133).
# '.-.-' (standard: A-umlaut) stands for C in CSOK on this card (word sense; see SOLUTION.md).
# 'HOOK' = non-Morse hooked mark with a dot, read as I-acute by word sense (IRJON).
M = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',
     '.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
     '..-..':'É','.-.--':'Á','.-.-':'C','HOOK':'Í','?':'?'}
out = {}
cur = None
for line in open(os.path.join(D, 'work/morse_transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('['): cur = line[1]; out[cur] = []; continue
    groups = [g for g in line.replace(' ', '').split('/') if g]
    out[cur].append(''.join(M.get(g, '<' + g + '>') for g in groups))
for k, v in out.items():
    print(f'{k}: ' + ' | '.join(v))
    print(f'{k} joined: ' + ''.join(v))

#!/usr/bin/env python3
"""Partial manual reading: verify immutable sources and reverse selected rows.
No OCR or automatic validation of the transcription against the image.
"""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parents[1]
checks={
 'address.jpg':'80c1cd93d4ce3d041c83f9494778544a52aef8d934a1d3e0025f6240ddbd9c42',
 'picture.jpg':'1d862b81164caf04a465b39d37ec30a3ab2b716fea017e40b333a43a02ada0b7',
 'metadata.md':'4d062211111ea8929e5124dbb019fafed015c10ebce26af7a2d397fc41836972',
 'schrodel-2021.pdf':'3e2ff353d1fa438d59f08fd4a984923b1e04e966bc9db09651108378f63a9580',
}
for name, expected in checks.items():
 actual=hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()
 assert actual==expected,(name,actual)
print('All four source SHA256 checks passed.')
print('Plain header, manual reading: Dear [initial] / Just a card / thanking you / for letter')
rows=[
 ('B1',None,'[unread] [unread] very [unread; resembles please/pleased]'),
 ('B2',None,'[unread] and would'),
 ('B3','emit dah fi etirw',None),
 ('B4','htiw ruoy',None),
 ('B5','evol lla',None),
 ('B6','kcaJ',None),
]
for label, raw, provisional in rows:
 print(label+': '+(raw[::-1] if raw else provisional))
print('Separate closing cross: X. No interpretation as an encrypted letter.')
print('PARTIAL: first two body rows unresolved; no complete message claimed.')

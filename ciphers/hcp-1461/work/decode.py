#!/usr/bin/env python3
"""Reverse alphabet over selected, manually read numeric passages only."""
from pathlib import Path
import hashlib,json
p = Path(__file__).resolve().parents[1]
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
count = 0
for item in json.loads((p/'work/excerpts.json').read_text()):
    words = []
    for nums in item['words']:
        assert all(1 <= n <= 26 for n in nums)
        word = ''.join(chr(91-n) for n in nums)
        assert [91-ord(c) for c in word] == nums
        count += len(nums)
        words.append(word)
    print(item['label']+': '+ ' '.join(words))
print(f'{count} numeric excerpt positions; remainder untranscribed.')
print('Source hashes and excerpt roundtrips passed, not OCR/full-message proof.')

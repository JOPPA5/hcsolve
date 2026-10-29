"""Acquire only observed public image URLs; never overwrite a source file."""
from pathlib import Path
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'work/source-sha256-2026-10-23-gloss.json').read_text())
for name, expected in manifest.items():
    assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest() == expected, name
jobs = json.loads((ROOT/'work/key1236-followup-downloads.json').read_text())
for job in jobs:
    dest = ROOT/'source'/job['source_file']
    if not dest.exists():
        req = urllib.request.Request(job['url'], headers={'User-Agent': 'HCP494 historical research'})
        with urllib.request.urlopen(req, timeout=30) as response:
            body = response.read()
        assert body[:2] == b'\xff\xd8', job['url']
        with dest.open('xb') as handle:
            handle.write(body)
    print(job['source_file'], dest.stat().st_size, hashlib.sha256(dest.read_bytes()).hexdigest(), flush=True)

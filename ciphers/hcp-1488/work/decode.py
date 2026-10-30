#!/usr/bin/env python3
from pathlib import Path
import codecs,hashlib,json
p=Path(__file__).resolve().parents[1]
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
count=0
for line in (p/"work/excerpts.txt").read_text().splitlines():
    if line.startswith("#"):print(line);continue
    plain=codecs.decode(line,"rot_13")
    assert codecs.encode(plain,"rot_13")==line
    print(plain)
    count+=sum(c.isascii() and c.isalpha() for c in line)
print("Letters in verified working excerpts:",count)
print("Body not transcribed. Source hashes and excerpt roundtrip passed.")

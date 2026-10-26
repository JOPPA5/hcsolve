#!/usr/bin/env python3
"""Reproduce the image transform; print a separately disclosed manual reading."""
from pathlib import Path
import hashlib,json,subprocess,tempfile,sys
p=Path(__file__).resolve().parents[1]
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path("/tmp/hcp-1491-decoded.png")
with tempfile.TemporaryDirectory(prefix="hcp1491-") as d:
    stage=Path(d)/"rotated.png"
    subprocess.run(["sips","-s","format","png","-r","270",
                    str(p/"source/address-large.jpg"),"--out",str(stage)],
                   check=True,capture_output=True)
    subprocess.run(["sips","-f","horizontal",str(stage),"--out",str(out)],
                   check=True,capture_output=True)
print("Decoded image:",out)
print("Manual reading below; NOT OCR:")
text=(p/"work/plaintext.txt").read_text()
print(text,end="")
print("Letters in manual reading:",sum(c.isascii() and c.isalpha() for c in text))
print("Source hashes passed.")

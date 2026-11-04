"""hcp-1036: number substitution, A=1 ... Z=25 over the 25-letter alphabet without J.
Run from the repo root: python3 -I ciphers/hcp-1036/work/decode.py"""
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
 "source/picture-large.jpg": "5718bec8bcd5a4bc87474ba34949bd0ec2e1f55a12894d70a52a2e1981c68051",
 "source/address-large.jpg": "4b9d4a8eea8e9c14922f8fb39d94608c8896a6927be69250dda9be321c97647f",
 "work/hires/cpc_1906-08-13_DE_Stolp_DE_Koslin__pic.jpg": "721786a873a71f2c000f007bede72bad100affb25429005da67f39f61c509ef1",
 "work/hires/cpc_1906-08-13_DE_Stolp_DE_Koslin__adr.jpg": "ce89dda4970fb0355f53f18f4653751fade980efde32b631fb5e2d411fce8a34",
}
for p, h in HASHES.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch {p}")
ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # no J
KEY = {i + 1: c for i, c in enumerate(ALPHA)}
for line in (D / "work/transcription.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    words = [w for w in line.split("  ") if w]
    print(" ".join("".join(KEY[int(n)] for n in w.split(".")) for w in words))
print("hashes OK", file=sys.stderr)

"""HCP 1355: check source hashes, then decode the Caesar -1 lines. Run: python3 -I ciphers/hcp-1355/work/solve.py"""
import hashlib, json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
for rel, want in json.load(open(os.path.join(here, "source-sha256.json"))).items():
    if hashlib.sha256(open(os.path.join(root, rel), "rb").read()).hexdigest() != want:
        sys.exit("HASH MISMATCH: " + rel)
print("source hashes OK")
def dec(s):
    return "".join(chr((ord(c.upper()) - 65 - 1) % 26 + 65) if c.isalpha() else c for c in s)
t = json.load(open(os.path.join(here, "transcription.json")))
print("clear   ", t["clear_heading"])
n = 0
for line in t["cipher_lines"]:
    n += sum(c.isalpha() for c in line)
    print(f"{line:24} {dec(line)}")
print(n, "enciphered letters decoded")

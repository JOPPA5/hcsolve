"""hcp-1475: verify source hashes, read transcription, apply the proposed expansion.
Run from repo root:  python3 -I ciphers/hcp-1475/work/decode.py

Note: for an initialism the words cannot be derived mechanically. KEY below is
the proposed expansion (an interpretation); the script only verifies that its
initials equal the transcribed letters, position by position, and prints it.
"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HASHES = {
    "source/address-large.jpg": "b04992ed502a68b2c65cdf9e1471ad6ca1cb470baed4a7e365e51ac01967a56f",
    "source/picture-large.jpg": "2cb6687ffa7c0a71b6e78ea3af1f02dcaf60ff996aaa9e688ee8069abb82d3df",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {p}: {got}")
    print(f"ok   {p}")
ct = [l.strip() for l in open(os.path.join(D, "work/transcription.txt")) if l.strip() and not l.startswith("#")]
ct = "".join(ct).rstrip(".")
# Proposed expansion: one word per capital (hard-coded, not derived).
KEY = ["I", "love", "my", "wife", "and", "my", "wife", "loves", "me"]
assert len(KEY) == len(ct), (len(KEY), len(ct))
for c, w in zip(ct, KEY):
    assert w[0].upper() == c, (c, w)
words = {}
for c, w in zip(ct, KEY):
    words.setdefault(c, set()).add(w)
print("ciphertext:", ct)
print("initials check: all", len(ct), "initials match the transcription")
print("initial -> word(s) used:", {c: sorted(s) for c, s in words.items()})
print("plaintext :", " ".join(KEY) + ".")

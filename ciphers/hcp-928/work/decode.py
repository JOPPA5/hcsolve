#!/usr/bin/env python3
"""hcp-928: verify source hashes and decode work/transcription.txt with the symbol key.
Run from the repo root:  python3 -I ciphers/hcp-928/work/decode.py
"""
import hashlib, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HASHES = {
    "source/address-large.jpg": "4685a4483ffc070b91c0b6853a9048f21c97668c59142ac72392d6d2b6a3855f",
    "source/picture-large.jpg": "1f8721943bbc99290bcaf5e01e43b235179064892d82bfedb62501a3f3737ade",
    "work/hires/cpc_1908-09-08_USA_Vance,-Alabama_USA_Birmingham,-Alabama__adr.jpg":
        "985493b1f83bb27ff21c1fe6d6d7aa86344f85fe7767ead442373720a63e585a",
    "work/hires/cpc_1908-09-08_USA_Vance,-Alabama_USA_Birmingham,-Alabama__pic.jpg":
        "e7be8b2d76a0aeb7cc50c747bf5aefd4993425ead961ff3f4c817baf0aa54737",
}
KEY = {  # cipher sign -> plaintext letter
    "X": "a", "q": "b", "6": "c", "D": "d", "8": "e", "o": "f", "2": "g", "3": "h",
    "P": "i", "J": "j", "9": "k", "d": "l", "7": "m", "/": "n", "5": "o", "n": "p",
    "a": "r", ")": "s", "C": "t", "(": "u", ":": "v", "W": "w", "Y": "y",
    "#": "[m]",  # blotted sign, restored
    "K": "[K]",  # signature sign, unresolved
}
PASS = set(" .,?'")

def check():
    ok = True
    for rel, h in HASHES.items():
        got = hashlib.sha256(open(os.path.join(BASE, rel), "rb").read()).hexdigest()
        if got != h:
            print("HASH MISMATCH", rel, file=sys.stderr); ok = False
    return ok

def decode_line(s):
    out, cap = [], False
    i = 0
    while i < len(s):
        c = s[i]
        if c == "^":
            cap = True; i += 1; continue
        if c in PASS:
            out.append(c); i += 1; continue
        if c not in KEY:
            raise SystemExit("unknown sign %r in %r" % (c, s))
        p = KEY[c]
        if cap:
            p = p.upper() if not p.startswith("[") else p; cap = False
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if nxt == '"':
            p = p + p; i += 1
        elif nxt == "~":
            p = p + "'"; i += 1
        out.append(p); i += 1
    return "".join(out)

def main():
    if not check():
        sys.exit(1)
    print("source hashes OK")
    for line in open(os.path.join(BASE, "work/transcription.txt"), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        if line.startswith("["):
            print(line); continue
        print(decode_line(line))

if __name__ == "__main__":
    main()

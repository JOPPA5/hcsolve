#!/usr/bin/env python3
"""hcp-993: decode the digit/symbol substitution from work/transcription.txt.

Run from the repo root:  python3 -I ciphers/hcp-993/work/decode.py
Checks the SHA-256 of the source scans first, then prints the full plaintext
(cipher lines decoded, plain Kurrent lines passed through).
"""
import hashlib, re, sys
from pathlib import Path

D = Path(__file__).resolve().parent.parent
HASHES = {
    "source/picture-large.jpg": "f272181545546c86bce47feb5ecb693d73028b64dde0d0699065734d6d53db2d",
    "source/address-large.jpg": "e345a539768bd39327efc25d3a1a75998594773a05ced7b74b74a2fe8d0c6ed6",
    "work/hires/cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01_pic.jpg": "7d0bd283ed9946dae93e46d1008187b40d8ea9aa8ef36e5bbf89de5688c9c705",
    "work/hires/cpc_1903-02-04_DE_Munchen_DE_Eschersheim_kellermann-01_adr.jpg": "73fd2df6ae6aa07e5078b9db24503be911c7b17c8e1f3cf0ed9456b6ffdb8806",
}
KEY = {
    "0": "o", "1": "l", "2": "n", "3": "m", "4": "e", "5": "s", "6": "b", "7": "t", "8": "h", "9": "g",
    "arc": "i", "hook": "r", "revc": "c", "Ibar": "z", "U": "u", "V": "d", "phi": "a",
    "plus": "f", "neq": "k", "w2o": "w", "vbar": "v", "Uuml": "ü", "ouml": "ö",
}

def check():
    ok = True
    for rel, h in HASHES.items():
        got = hashlib.sha256((D / rel).read_bytes()).hexdigest()
        if got != h:
            print(f"HASH MISMATCH {rel}: {got}", file=sys.stderr); ok = False
    if not ok:
        sys.exit(1)
    print("source hashes OK", file=sys.stderr)

def tok(t):
    m = re.fullmatch(r"\((.+)\)", t)          # restored sign
    if m: return KEY[m.group(1)]
    m = re.fullmatch(r"<(.+)>", t)            # omitted by writer, supplied
    if m: return KEY[m.group(1)]
    m = re.fullmatch(r"\{(.+)=(.+)\}", t)     # written as X, read as Y
    if m: return KEY[m.group(2)]
    m = re.fullmatch(r"([^.,!=\-]+)([.,!=\-]*)", t)
    if m and m.group(1) in KEY:
        return KEY[m.group(1)] + m.group(2)
    if re.fullmatch(r"\[\d+\]", t): return t[1:-1]
    if re.fullmatch(r"[.,!=\-]+", t): return t
    raise SystemExit(f"unknown sign {t!r}")

def decode_part(s):
    words = []
    for w in s.split(" / "):
        words.append("".join(tok(t) for t in w.split()))
    return " ".join(words)

def main():
    check()
    for line in (D / "work/transcription.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        label, body = line.split(":", 1)
        out = []
        for part in re.split(r"(\[plain Kurrent German: [^\]]*\])", body.strip()):
            if not part.strip():
                continue
            if part.startswith("[plain"):
                out.append(part[len("[plain Kurrent German: "):-1])
            elif part.strip().startswith("[two rows"):
                out.append("(.... ....)")
            else:
                out.append(decode_part(part.strip()))
        print(f"{label:4s} {' '.join(out)}")

if __name__ == "__main__":
    main()

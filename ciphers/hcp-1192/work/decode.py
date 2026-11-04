#!/usr/bin/env python3
"""hcp-1192: decode work/transcription.txt with the key below and check source hashes.
Run from the repo root:  python3 -I ciphers/hcp-1192/work/decode.py
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CARD = os.path.dirname(HERE)

HASHES = {
    "source/picture-large.jpg": "c44cb2d1edb5f884f70b4606ec89982ca757129df164b4dd9cd81183c29e845e",
    "source/address-large.jpg": "069deb121cb5058649967eb5684959455304d0f17acae4c521532a9d05871579",
    "work/hires/cpc_1906-11-06_USA_Cobleskill.-NY_USA___pic.jpg": "da145158e90d8d3e7a2e2f04d06b2f94650ba6f45f328ff27a2f796613751a26",
    "work/hires/cpc_1906-11-06_USA_Cobleskill.-NY_USA___adr.jpg": "e0c28447a640d01522fc547f30165ed56814e049060a906db5dd05fdfc38832d",
}

KEY = {
    "BAR1V": "a", "DASH": "b", "BAR1D": "d", "BAR2V": "e", "BAR2B": "g",
    "BAR2D": "h", "PLUS": "i", "STAR": "l", "TEE": "m", "IBEAM": "n",
    "OBAR": "o", "LADDR": "r", "LADDS": "s", "LOLLI": "t", "OCROSS": "u",
    "OX": "v", "WHEEL": "w", "HOOK": "y",
}
LITERAL = {"?", ".", ",", "'"}


def main():
    ok = True
    for rel, h in HASHES.items():
        p = os.path.join(CARD, rel)
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if got != h:
            ok = False
            print(f"HASH MISMATCH {rel}", file=sys.stderr)
    if not ok:
        sys.exit(1)
    print("source hashes OK")
    used = set()
    out = []
    for line in open(os.path.join(HERE, "transcription.txt"), encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        place, toks = line.split(":", 1)
        words = []
        for w in toks.split(" / "):
            s = ""
            for t in w.split():
                if t in KEY:
                    s += KEY[t]; used.add(t)
                elif t in LITERAL:
                    s += t
                elif t.startswith("#") and t[1:].isdigit():
                    s += t[1:]
                else:
                    raise SystemExit(f"unknown token {t!r} in {place}")
            words.append(s)
        text = " ".join(words)
        out.append(text)
        print(f"{place.strip():<70} {text}")
    unused = sorted(set(KEY) - used)
    print("unused key entries:", unused or "none")
    print()
    print("Plaintext:", " ".join(out))


if __name__ == "__main__":
    main()

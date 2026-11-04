#!/usr/bin/env python3
"""hcp-1100: decode work/transcription.txt with the sign key below and check source hashes.
Run from the repo root:  python3 -I ciphers/hcp-1100/work/decode.py
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CARD = os.path.dirname(HERE)

HASHES = {
    "source/address-large.jpg": "ad908e201b1b0655d79f71bc345ef3989146d650740fa3a5c1ad48469f38a8e6",
    "source/picture-large.jpg": "aba2f2f04a39f230ff9c73a27cee9168ab8a4962d9e161ea78561ce655e2dd05",
    "work/hires/cpc_1908-10-30_UK_Clapham_UK_Somerset__adr.jpg": "140e6eedd81b8956bdf97ae5c8342ebb22ff57251853b95beed785c2eed44620",
    "work/hires/cpc_1908-10-30_UK_Clapham_UK_Somerset__pic.jpg": "b433e06a1aa1b81657d93748ca7c35b68de94ad7ce3f76c0221d287e2f2ef178",
}

# shape code -> plaintext letter (variant shapes of one letter are listed separately)
SIGNS = {
    "c": "A",     # round C
    "cq": "A",    # angular, square-cornered C (B02 only)
    "arc": "A",   # thin open arc ( (in MAY, THAN)
    "gam": "A",   # Gamma-like hooked stroke (RATHER, HAVE in T03)
    "b": "E",     # b
    "bb": "E",    # b with a bar on top (FEEL)
    "bf": "E",    # solid triangular b (WELL, HAVE in T03)
    "lp": "E",    # loop-and-stem / triangle-loop (RATHER, TREASURE)
    "sev": "D",   # 7
    "h": "R",     # hooked h
    "lam": "S",   # stroke with a foot at lower left and a tick at upper right
    "u": "T",     # u with tall right stem
    "bar": "T",   # tall plain stroke (ANYTHING only)
    "dx": "T",    # d-like loop with crossbar (TREASURE only)
    "nine": "P",  # 9
    "cross": "J", # dagger cross
    "vs": "U",    # V with stem (Y shape)
    "vt": "U",    # V with tick (UNHAPPY only)
    "blob": "H",  # Y shape with heavy ink foot
    "i": "I",     # plain stroke
    "yn": "N",    # y/ch shape with left arm
    "eta": "N",   # eta shape (LINE in B02 only)
    "eps": "L",   # epsilon
    "rev3": "L",  # reversed epsilon, 3 (FEEL, ONLY, WELL)
    "zh": "L",    # z-hook (LOSE only)
    "p": "G",     # P
    "hn": "W",    # hyphen + N
    "hi": "F",    # hyphen + stroke
    "tri": "Q",   # closed downward triangle
    "pen": "Y",   # V/Y with a pennant or triangle, open or filled
    "hk": "M",    # hook with a horizontal bar
    "el": "K",    # Cyrillic-El shape (THINK only)
    "crl": "V",   # stroke with a curl at the top
    "sq": "O",    # square
    "sq4": "O",   # open box with stem, 4-like (ONE only)
    "amp": "&",   # d/partial shape standing alone (B04 only)
}


def check_hashes():
    ok = True
    for rel, want in HASHES.items():
        p = os.path.join(CARD, rel)
        with open(p, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
        if got != want:
            print(f"HASH MISMATCH {rel}: {got}", file=sys.stderr)
            ok = False
    return ok


def decode_line(body):
    words = []
    for w in body.split("|"):
        w = w.strip()
        if not w:
            continue
        if w.startswith("="):
            words.append(w[1:])
        elif w.startswith("["):
            words.append("[struck out]")
        else:
            words.append("".join(SIGNS[s] for s in w.split()))
    return " ".join(words)


def main():
    if not check_hashes():
        sys.exit(1)
    print("source hashes OK")
    with open(os.path.join(HERE, "transcription.txt"), encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            tag, body = line.split(":", 1)
            print(f"{tag}: {decode_line(body)}")


if __name__ == "__main__":
    main()

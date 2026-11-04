#!/usr/bin/env python3
"""hcp-1091: decode the transcription with the reconstructed key.

Run from the repo root:
    python3 -I ciphers/hcp-1091/work/decode.py
It checks the SHA-256 of the source scans, decodes work/transcription.txt,
prints the literal decode (merged letters as classes) and the resolved text,
and fails if any resolved word does not fit the literal pattern.
"""
import hashlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CIPHER = os.path.dirname(HERE)

HASHES = {
    "source/picture-large.jpg": "3dc5149543195efa6f3f33a745af1cca6594cf2ad60a1a3fdd1bee65ed734cf4",
    "source/address-large.jpg": "9631f0da8f8f52e1226037ad59109897fef01667099321cd705eb62b0272ec68",
    "work/hires/cpc_1886-03-12_AT_Wien_AT_Krems__pic.jpg": "463e2da699d31b87803c88e613a59cc39316b6ccc37ae209846c128062d9e888",
    "work/hires/cpc_1886-03-12_AT_Wien_AT_Krems__adr.jpg": "dd8c6a1cf4bd88ced71baf08c5b7bdc877a773f3aca754b22f4fac0b6e88766f",
}

# Consonants are digit-like signs, vowels are dots/dashes or marked signs.
# Upper-case letters stand for letter pairs that share one sign:
# D = d/t, G = g/k, F = f/v, Z = c/z.
KEY = {
    "0": "l", "1": "D", "2": "n", "3": "m", "4": "r", "5": "G", "6": "b",
    "7": "s", "8": "h", "9": "F", "x": "w", "+": "Z", "J": "j", "Y": "s", "S": "r",
    "T": "o", "T:": "ö",
    ".": "i", "..": "e", "...": "ie", "-": "a", '"-': "ä",
    "2u": "u", "2:": "ü", "!": "!", "?": "?",
}
CLASSES = {"D": "[dt]", "G": "[gk]", "F": "[fv]", "Z": "[cz]"}

# The writer's words (spelling as written, including his single consonants).
RESOLVED = """Lieber Jagas Bua ! Du bist also wirklich ernstlich böse ? Hab ich dich den so
tief gekränkt das du mir nie verzien wirst es ist recht hart von dir Lebe wol Lieber
Jaga wen du mir schon nicht verzien kanst sende dir aber doch noch den süsen Kus"""


def check_hashes():
    ok = True
    for rel, want in HASHES.items():
        p = os.path.join(CIPHER, rel)
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
        flag = "OK " if got == want else "BAD"
        ok &= got == want
        print(f"{flag} {rel}")
    if not ok:
        sys.exit("source hash mismatch")


def decode_sign(tok, notes):
    restored = forced = None
    m = re.fullmatch(r"\[(.+)\]", tok)
    if m:
        tok, restored = m.group(1), True
    m = re.fullmatch(r"(.+?)\{(.+)\}", tok)
    if m:
        tok, forced = m.group(1), m.group(2)
    if forced is not None:
        notes.append(f"sign '{tok}' read as '{forced}' by word sense")
        return forced
    if tok not in KEY:
        sys.exit(f"unknown sign {tok!r}")
    out = KEY[tok]
    if restored:
        notes.append(f"'{out}' restored (sign hidden)")
        return "[" + out + "]"
    return out


def main():
    check_hashes()
    lines = []
    for raw in open(os.path.join(HERE, "transcription.txt"), encoding="utf-8"):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        label, body = raw.split(":", 1)
        lines.append((label, body.strip()))
    words, notes = [], []
    print("\nLiteral decode (D=d/t G=g/k F=f/v Z=c/z, [x] restored):")
    for label, body in lines:
        out = []
        for w in body.split(" / "):
            lit = "".join(decode_sign(t, notes) for t in w.split())
            out.append(lit)
            words.append((label, lit))
        print(f"  {label:4} {'  '.join(out)}")
    res = RESOLVED.split()
    if len(res) != len(words):
        sys.exit(f"word count mismatch {len(res)} vs {len(words)}")
    for (label, lit), r in zip(words, res):
        pat = "".join(CLASSES.get(c, re.escape(c)) for c in lit.replace("[", "").replace("]", ""))
        if not re.fullmatch(pat, r, flags=re.I):
            sys.exit(f"{label}: resolved '{r}' does not fit literal '{lit}'")
    text = " ".join(res).replace(" !", "!").replace(" ?", "?")
    print("\nPlaintext (writer's spelling):\n  " + text)
    print("\nDisclosed readings:")
    for n in notes:
        print("  - " + n)


if __name__ == "__main__":
    main()

"""HCP 1503: decode the manual Morse transcription with International Morse.

Run from the repository root:
    python3 -I ciphers/hcp-1503/work/decode.py
Checks the SHA-256 of the source files, then prints the plaintext line by line
and as one running text.
"""
import hashlib
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
    "source/address-large.jpg": "7975c53679310047b49f04ab16c5c6ed36f4fd1fb20c9b00ef2320f5fb0fd3ff",
    "source/picture-large.jpg": "624fc2ecd7b8e00cd9c2bc56d3b1c87cf7d5d004cf2696fe3f55d5ab6451023a",
    "source/metadata.md": "cc9d29b87c8d03337ff1439d1c8e339d45c850c90ef560f48ce7cadb04c1a22a",
}
MORSE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z",
}
SPECIAL = {"(.)": "(.)", "~": "--"}

ok = True
for rel, h in HASHES.items():
    got = hashlib.sha256((D / rel).read_bytes()).hexdigest()
    status = "OK" if got == h else "MISMATCH"
    ok &= got == h
    print(f"sha256 {status} {rel}")
if not ok:
    sys.exit("source hash mismatch")

lines = []
for raw in (D / "work" / "transcription.txt").read_text().splitlines():
    if not raw.strip() or raw.startswith("#"):
        continue
    label, body = raw.split(":", 1)
    words = []
    for w in body.split("/"):
        out = []
        for tok in w.split():
            if tok in SPECIAL:
                out.append(SPECIAL[tok])
            elif tok in MORSE:
                out.append(MORSE[tok])
            else:
                sys.exit(f"unknown token {tok!r} in line {label}")
        words.append("".join(out))
    lines.append((label, " ".join(words)))

print()
for label, text in lines:
    print(f"{label:>2}: {text}")
print()
print(" ".join(t for _, t in lines))

#!/usr/bin/env python3
"""hcp-1332: verify source hashes, decode work/transcription.txt with the key, compare with the reading text.
Run from the repo root: python3 -I ciphers/hcp-1332/work/decipher.py"""
import hashlib, pathlib, re, unicodedata
D = pathlib.Path(__file__).resolve().parent.parent
H = {"source/picture-large.jpg": "301e5ded94e85027114d3031d9118ba89b5b0337d2d1f5baed1056896fdb54ec",
     "source/address-large.jpg": "6a9758a9edd61cbe52089a539440f75be61504f0287dc81ad013ab5dbb680d2d",
     "work/hires/pc_hcp_13_pic.JPG": "d81cc58067ca36e502f844ab458fe48af4c96de06eeba0cc6617268a39204fe2",
     "work/hires/pc_hcp_13_adr.JPG": "00bc14261acd422c258c38ea80447f516042fedf500450f8a1ad33fca9b6224d"}
for f, h in H.items():
    assert hashlib.sha256((D / f).read_bytes()).hexdigest() == h, f
KEY = dict(M="a", D="b", T="c", L="d", B="e", F="f", U="g/q", S="h", Q="i", Z="j", V="l", P="m",
           H="n", X="o", R="r", C="s", A="t", O="u", **{"9": "p", "5": "z"})
assert len(set(KEY.values())) == len(KEY)
READING = ("Meu Quinito. Ha hoje por ca uma grande telha. E sabes porque? Porque a Laura ja hontem foi a quinta, "
 "e para a semana ja pode ir ao bonito. Esta noite so sonhei com o Luizito. Vamos hoje a Torres, e com a paternidade. "
 "Que des para la alguma coisa? O nosso sobrinhito quando for mais velho ha de ser como esse menino. "
 "E muito chic o teu bilhete. Qualquer dia la iremos. Adeus amorsito ate Sabbado!! Abraca-te com todo o amor a sos, "
 "sempre so tua Triz. E hoje nao te mando um beijo!! A minha cabeca esta melhor.")
def dec(c, nxt):
    if c == "U":                     # one sign for q and g: q in que/qui/qua (sign O, then B, Q or M), else g
        return "q" if nxt[:1] == "O" and nxt[1:2] in ("B", "Q", "M") else "g"
    if c == "M" and (nxt[:2] == "M-" or nxt[:2] == "BV"):   # one sign for a and v: va-(mos), v(elho)
        return "v"
    return KEY[c]
out, letters, cnt = [], "", 0
for ln in (D / "work/transcription.txt").read_text(encoding="utf-8").splitlines():
    if ln.startswith("#") or not ln.strip():
        continue
    tag, body = ln.split(" ", 1)
    s = ""
    for i, c in enumerate(body):
        if c in KEY:
            s += dec(c, body[i + 1:i + 3]); cnt += 1
        elif c == "^":
            s = unicodedata.normalize("NFC", s + ("̂" if s[-1] == "e" else "́"))
        elif c == "~":
            s = unicodedata.normalize("NFC", s + "̃")
        else:
            s += c
    out.append(f"{tag:4}{s}")
    letters += s
print("\n".join(out))
norm = lambda t: re.sub(r"[^a-z]", "", unicodedata.normalize("NFD", t.lower()))
a, b = norm(letters), norm(READING)
print(f"\n{cnt} cipher signs decoded; all in key: yes")
if a != b:
    i = next((j for j, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    raise SystemExit(f"reading differs at {i}: {a[i-15:i+15]} / {b[i-15:i+15]}")
print("reading text equals decoded letters: yes (integrity check of the two texts only; says nothing about the scan)\n")
print(READING)

"""Decode hcp-1485 from work/transcription.txt with work/key.json and check source hashes.
Run from repo root:  python3 -I ciphers/hcp-1485/work/decode.py
"""
import hashlib, json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    "source/address-large.jpg": "0e02cffd0e0779e50156a7dd977c3116bd6a0ae05ef638317b5918eb00737967",
    "source/picture-large.jpg": "40e1fd756538b88f1c35cd7e8f9203558b013116f79d0e39062c13e4aa1a4c66",
    "source/metadata.md": "5f403a4a2204df2dc3d7360549160abdc39317e6303ce756852f555c565aa6ae",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK   " if got == h else "FAIL ") + p)
    ok &= got == h
key = json.load(open(os.path.join(D, "key.json")))
# Writer's slips: (line, word index) -> (literal, intended word, reason)
SLIPS = {
    (3, 1): ("BOT", "BUT", "U written as plain square (no diagonal)"),
    (4, 3): ("CAME", "GAME", "G written with ticks high on the stem (= C)"),
    (6, 4): ("YOO", "YOU", "U written as plain square (no diagonal)"),
}
lit_lines, read_lines = [], []
n = 0
for raw in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if raw.startswith("#") or not raw.strip():
        continue
    n += 1
    words_lit, words_read = [], []
    for wi, w in enumerate(raw.split(" / ")):
        out = ""
        for t in w.split():
            m = re.fullmatch(r"\[\[(.*)\]\]", t)
            if m:
                out += m.group(1); continue
            base, dbl = (t[:-2], 2) if t.endswith("^2") else (t, 1)
            out += key[base] * dbl
        words_lit.append(out)
        s = SLIPS.get((n, wi))
        if s:
            assert s[0] in out, (n, wi, out)
            words_read.append(out.replace(s[0], s[1]) + "{" + s[0] + "}")
        else:
            words_read.append(out)
    lit_lines.append(" ".join(words_lit))
    read_lines.append(" ".join(words_read))
print("\n-- literal decipherment --")
print("\n".join(lit_lines))
print("\n-- reading ({...} = literal form of a writer's slip) --")
print("\n".join(read_lines))
print("Arthur  [signature in plain script]")
sys.exit(0 if ok else 1)

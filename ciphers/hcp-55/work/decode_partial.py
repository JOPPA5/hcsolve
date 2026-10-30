"""HCP 55 partial decoder (Claude Opus 5.5, 2026-10-30).
Run from repo root:  python3 -I ciphers/hcp-55/work/decode_partial.py
Checks source hashes, then applies the (homophonic) key to the manual
transcription. Unknown signs print as [LABEL]; this is NOT OCR."""
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {"source/postcard-large.jpg": "26afc3bf9352ff27a9b1328b3982bfed09056102433cdc5ad80a9cd77af3ab26",
     "source/metadata.md": "f4377477c67640e740ef66019a72c14d69f467713a8ac749d23f51a81414660a"}
for f, h in H.items():
    got = hashlib.sha256((D / f).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {f}")
print("source hashes OK")
KEY = {  # sign -> letter; several letters have more than one sign
 "BAR": "a", "BARR": "i", "BARL": "g", "VEE": "g?", "OLINE": "l", "CROSSO": "m",
 "OIN": "v", "CAP": "n", "DIV": "n", "CAPBAR": "e", "H2": "e", "CUP": "o", "H1": "o",
 "CUPBAR": "f", "BOX": "r", "PBOX": "r", "BOXMID": "r", "BOXX": "t", "XARC": "w",
 "H3": "y", "BOXDOT": "y", "HX": "u", "OSLASH": "u", "NEQ": "h", "CIRC": "p",
 "ZIG": "s", "DOTUP": "d?", "XLOOP": "o?",
}
for line in (D / "work/transcription.txt").read_text().splitlines():
    if not line.startswith("R"):
        continue
    tag, body = line.split(":", 1)
    out = []
    for t in body.split():
        if t in ",.":
            out.append(t + " ")
        elif t == "P.M.":
            out.append("P.M. ")
        elif t == "[HIDDEN]":
            out.append("[...hidden...]")
        else:
            out.append(KEY.get(t, f"[{t}]"))
    print(f"{tag}: {''.join(out).strip()}")

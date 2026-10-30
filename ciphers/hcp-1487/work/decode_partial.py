"""HCP 1487 partial decoder (Claude Opus 5.5, 2026-10-30).

Run from repo root:  python3 -I ciphers/hcp-1487/work/decode_partial.py
Checks source hashes, then applies the PARTIAL key to the manual
transcription. Unknown signs print as [LABEL]. This is not a full solution.
"""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
HASHES = {
    "ciphers/hcp-1487/source/address-large.jpg": "b0cc75a8ccfd39ce6b4e8cdf59178dffbb7111bb028d9a98e41283334c84cb64",
    "ciphers/hcp-1487/source/picture-large.jpg": "0eec91628cf346e8cebd631d108986f54b8ee7b76c84ac46cfc1bc6da975e2ff",
    "ciphers/hcp-1487/source/metadata.md": "6ef11638f99da0d72ab54053411e62998fc3b7bb9d4dfdb8680874f548f5b33d",
    # clean photo of the same physical card, used read-only for reading
    "ciphers/hcp-55/source/postcard-large.jpg": "26afc3bf9352ff27a9b1328b3982bfed09056102433cdc5ad80a9cd77af3ab26",
}

# good / medium confidence values only (see work/glyphs.md)
KEY = {
    "BAR": "a", "BARL": "g", "BARR": "i", "CAP": "n", "CAPBAR": "e",
    "CUP": "o", "CUPBAR": "f", "OLINE": "l", "CROSSO": "m", "OIN": "v",
    "BOX": "r", "BOXX": "t", "XARC": "w",
}


def main():
    for rel, h in HASHES.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        print(("OK  " if got == h else "BAD ") + rel)
        if got != h:
            raise SystemExit("source hash mismatch")
    lines = (ROOT / "ciphers/hcp-1487/work/transcription.txt").read_text().splitlines()
    for line in lines:
        if not line.strip() or line.startswith("#"):
            continue
        row, toks = line.split(":", 1)
        out = []
        for t in toks.split():
            if t in (",", ".", "P.M."):
                out.append(t if t == "P.M." else t + " ")
            elif t == "[HIDDEN]":
                out.append("[...hidden by postmark...]")
            else:
                out.append(KEY.get(t, "[" + t + "]"))
        print(row + ": " + "".join(x if x.endswith(" ") or x == "P.M." else x for x in out))


if __name__ == "__main__":
    main()

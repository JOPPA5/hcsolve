"""hcp-1030 PARTIAL decoder: checks source hashes, decodes work/transcription-partial.txt with work/key.json."""
import hashlib, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {"source/picture-large.jpg": "6e3fa646935c6325922a1495609a1b15ac52c16f4b3bcd6f0c2885ed8d73429f",
     "source/address-large.jpg": "4df3a5f4c3f89c7439e9b1b9453957fba99a91ec807f3df324072a9a0371b385",
     "work/hires/cpc_1903-03-26_DE_Neunkirchen_DE_Neunkirchen__pic.jpg": "b7fc65647288dd49f6f11e0a809d1f0dc5ba5db8ff470d7045d8a36f508052e6",
     "work/hires/cpc_1903-03-26_DE_Neunkirchen_DE_Neunkirchen__adr.jpg": "8b62a95298748622e5f62e325e0adacfeeca0b35a4fa9ddfe5d6d7fe09fe3a34"}
ok = True
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    if got != h: ok = False; print("HASH MISMATCH", p)
print("hashes OK" if ok else "hashes FAILED")
key = json.load(open(os.path.join(D, "key.json")))
for line in open(os.path.join(D, "transcription-partial.txt"), encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    lab, body = line.split("#")[0].split(":", 1)
    words = []
    for w in body.split("|"):
        out = ""
        for t in w.split():
            t = t.rstrip("~")
            out += key.get(t, "?").lower()
        words.append(out)
    print(lab + ": " + " ".join(words))
print("NOTE: partial transcription (block B lines 1-4 only).")

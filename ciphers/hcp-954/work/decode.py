"""hcp-954: number substitution A=1 ... Z=25 on a 25-letter alphabet without J.
Run from the repo root:  python3 -I ciphers/hcp-954/work/decode.py"""
import hashlib, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HASHES = {
 "source/picture-large.jpg": "0455510af92881f0aac86b15b76da4068fff0ca01d82e04ae642a51c2b82e7cf",
 "source/address-large.jpg": "ae69d5856442f8fa9e9c85b64547e7c5f65c22e1cd4b9900421b888a93e0ecf5",
 "work/hires/cpc_1902-07-06_DE_Heide_DE_Jever_martha-03_pic.jpg": "deaf2455823d15c7cb016b060ecdeccfa081cf02e9a61368a5c83cd42eb53c1d",
 "work/hires/cpc_1902-07-06_DE_Heide_DE_Jever_martha-03_adr.jpg": "c436c807558e7679f783f00d7653717c7747bc7dcd3f9948a244df2fbd6378c9",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    print(("OK   " if got == h else "FAIL ") + p)
    assert got == h
ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"          # no J
KEY = {str(i + 1): c for i, c in enumerate(ALPHA)}
UML = {"A": "Ä", "O": "Ö", "U": "Ü"}
lines, words = [], []
for raw in open(os.path.join(D, "work/transcription.txt"), encoding="utf-8"):
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    out = ""
    for t in raw.split():
        if t == "/":
            out += " / "
        elif t in ".?":
            out += t
        elif t.endswith("u"):
            out += UML[KEY[t[:-1]]]
        else:
            out += KEY[t]
    lines.append(out)
print("\nKey:", " ".join(f"{c}={i+1}" for i, c in enumerate(ALPHA)))
print("\nLine-by-line decipherment:")
for l in lines:
    print("  " + l)
stream = "".join(c for c in "".join(lines) if c.isalpha())
print("\nLetter stream:", stream)
SEG = ("BESTEN DANK FÜR DEINE LIEBEN KARTEN WIE SEHNE ICH MICH ZU DIR MEINE GUTE M "
       "ICH LIEBE DICH DOCH SO SEHR MEINEN BRIEF HAST DU DOCH ERHALTEN "
       "FREUNDLICHE GRÜSZE EWIG DEIN CARL")
assert SEG.replace(" ", "") == stream, "segmentation does not match the decoded stream"
print("Word division checked against the stream (OK).")
print("\nPlaintext: Besten Dank für deine lieben Karten. Wie sehne ich mich zu dir, meine gute M.! "
      "Ich liebe dich doch so sehr. Meinen Brief hast du doch erhalten? "
      "Freundliche Grüße (Grüsze), ewig dein Carl.")

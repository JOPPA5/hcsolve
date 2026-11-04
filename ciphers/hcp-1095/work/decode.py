"""hcp-1095: decode the American (railroad) Morse transcription and check source hashes.
Run from repo root:  python3 -I ciphers/hcp-1095/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HASHES = {
 "source/picture-large.jpg": "4fb0ac97a18517aa40eba0c81a8cf7f99497580deb8dbf4d92462656c740152f",
 "source/address-large.jpg": "25be54b83e2bad19f952562703fd930a07e69acead1445ecf307753e2de85999",
 "work/hires/cpc_1905-06-23_USA_Fultonville,-NY_USA_Fultonville,-NY__pic.jpg": "172ef432c1ff18a01eeb8ff64a98762fdcd5273b619ffdaf2660fb237bf000c1",
 "work/hires/cpc_1905-06-23_USA_Fultonville,-NY_USA_Fultonville,-NY__adr.jpg": "341091aaed5118d9edca649c330627aa6b79dc308c5d9c2d1abcdad70e1bf67f",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    if got != h:
        sys.exit("HASH MISMATCH " + p)
print("source hashes OK")
# American Morse (1844 / railroad) alphabet, letters only as used here
AM = {".-":"A","-...":"B",".. .":"C","-..":"D",".":"E",".-.":"F","--.":"G","....":"H",
      "..":"I","-.-.":"J","-.-":"K","_":"L","--":"M","-.":"N",". .":"O",".....":"P",
      "..-.":"Q",". ..":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W",".-..":"X",
      ".. ..":"Y","... .":"Z","?":"?"}
out = []
for line in open(os.path.join(D, "work/transcription.txt"), encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    tag, body = line.split("]", 1)
    words = []
    for w in body.split("/"):
        letters = [s.strip() for s in w.split(",") if s.strip()]
        if not letters:
            continue
        words.append("".join(AM[s] for s in letters))
    # a line ending with ',' continues the word on the next line
    cont = body.rstrip().endswith(",")
    out.append((tag + "]", " ".join(words), cont))
for tag, txt, cont in out:
    print(tag, txt + ("-" if cont else ""))
full = ""
for tag, txt, cont in out:
    full += txt + ("" if cont else " ")
print("\nPLAINTEXT:", " ".join(full.split()))

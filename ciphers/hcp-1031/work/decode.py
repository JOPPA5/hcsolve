"""hcp-1031: verify source hashes, decipher work/transcription.txt with work/key.json.
Run from repo root:  python3 -I ciphers/hcp-1031/work/decode.py"""
import hashlib, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
HASHES = {
 "source/picture-large.jpg": "97743089331dd716395137882b2e86d2bce777bdc3453417a88ceea7cf5165d5",
 "source/address-large.jpg": "c58a7d19007d787ac890000ea81ef9bf3444e12a8d66c182f72df13b8a36ef3b",
 "work/hires/cpc_1904-03-22_AT_Wien_AT_Wien__pic.jpg": "31c4ec3c98c1fab9260e4543cdda5cd1f6648432ee2a07b23f5da90fd42dbd20",
 "work/hires/cpc_1904-03-22_AT_Wien_AT_Wien__adr.jpg": "039051842a4e08408c42686f8dc053e4448db59b3c005c3ba1f458976062aa14"}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(R, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p); assert got == h
key = {k: v for k, v in json.load(open(os.path.join(D, "key.json"))).items() if not k.startswith("_")}
UML = {"a": "ä", "o": "ö", "u": "ü"}
LITERAL = set("VI4.,-")
raw = []
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    tag, ct = line.rstrip("\n").split("\t")
    out = []
    for ch in ct:
        if ch == '"': out[-1] = UML[out[-1]]
        elif ch in key: out.append(key[ch])
        elif ch in LITERAL: out.append(ch)
        else: sys.exit("unknown sign %r in %s" % (ch, tag))
    s = "".join(out); raw.append(s); print("%-4s %s" % (tag, s))
# word division and capitals added by the solver; letters must match the raw decipherment exactly
READ = ("Liebstes Annerl. Sei so gut, gib mir bekannt wo wir uns Freitag treffen, um unsere zukün-"
        "ftige Lage besprechen zu können. Sollest du den Wortlaut des Abschiedsbriefes ha-"
        "ben, so nim ihn mit. Näheres mündlich, sei so gut mit besten Gruss "
        "Joh. Wolf. VI. Engelgasse 4. Bäckerei 4ekninger.")
norm = lambda t: "".join(c for c in t.lower() if c.isalnum() or c in ".,-")
assert norm(READ) == norm("".join(raw)), (norm(READ), norm("".join(raw)))
print("\nReading (word division added):\n" + READ.replace("-", ""))

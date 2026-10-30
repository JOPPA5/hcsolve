import datetime, hashlib, json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hashes = {
 "source/picture-large.jpg": "b9153dd7669c262f30cb9f31cc4ba8fbb13705c997a9655fea9bf13b146d4040",
 "source/address-large.jpg": "a9a08b8427916c620aa4db54b22294941766318b4ed8446a4023e864a2380489",
 "work/hires/pc_hcp_51_pic.JPG": "8dd431f762be359a3dc420a476b2ddfd9c5a3a9963bc725c0b35eb3cf824e594",
 "work/hires/pc_hcp_51_adr.JPG": "fd2e3b9a284f0b9cddfc092f1082f58405a87de96308ced3814b864a63875127",
}
for p, h in hashes.items():
    got = hashlib.sha256(open(os.path.join(root, p), "rb").read()).hexdigest()
    if got != h:
        sys.exit("HASH MISMATCH " + p)
print("source hashes OK")
def shift(s, k):
    o = ""
    for c in s:
        if c.isascii() and c.isalpha():
            a = 65 if c.isupper() else 97
            o += chr((ord(c) - a + k) % 26 + a)
        else:
            o += c
    return o
t = json.load(open(os.path.join(root, "work/transcription.json")))
n = 0
for line in t["lines"]:
    ct, pt = [], []
    for kind, tok in line:
        ct.append(tok)
        if kind == "cipher":
            d = shift(tok, -1)
            assert shift(d, 1) == tok
            n += sum(c.isalpha() for c in tok)
            pt.append(d.upper())
        else:
            pt.append("[" + tok + "]")
    print(" ".join(ct).ljust(30), "|", " ".join(pt))
print("enciphered letters decoded:", n)
print("30 Sep 1907 =", datetime.date(1907, 9, 30).strftime("%A"), "; 30 Jul 1907 =", datetime.date(1907, 7, 30).strftime("%A"))

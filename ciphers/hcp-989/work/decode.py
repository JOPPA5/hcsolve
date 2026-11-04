"""hcp-989: check source hashes, decode the cipher signs, print the full message."""
import hashlib, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {"source/picture-large.jpg": "68a71a9207fb6721bc53ed17a653db9df71a3160d405f9630131770c53236853",
     "source/address-large.jpg": "1497978a31ccdd7ddfc479cdc87484108a8dc279d173dbfded2c4ea29a7fd446",
     "work/hires/cpc_1901-10-19_AT_Wien_AT_Wien__pic.jpg": "51a84ac2179287b3285b7433df6d4feb4567e5e1e7a35c08062f47ddda3d41b1",
     "work/hires/cpc_1901-10-19_AT_Wien_AT_Wien__adr.jpg": "88e8d2dd212e1a73534e21f98fb869af1c9221f63dd5cf02eb7a5a7c1acec851"}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)
    if got != h: sys.exit(1)
key = json.load(open(os.path.join(D, "key.json")))
codes = [l.split() for l in open(os.path.join(D, "transcription.txt")) if l.strip() and not l.startswith("#")]
raw = " ".join("".join(key[s] if s != "sep" else ". " for s in line) for line in codes).strip()
# Word-sense resolutions (review 1, findings 1-2): the card writes P and B with one B-shaped sign, and F and W
# with one two-twig fehu sign. Literal sister-key output is ABFELFEIN. STUBE.; APFELWEIN needs P (1st b) and W (2nd f2).
plain = raw.replace("P/B", "P", 1).replace("P/B", "B")
plain = plain.replace("F/W", "F", 1).replace("F/W", "W", 1)
print("cipher signs ->", raw)
print("decoded      ->", plain)
print()
print("Full message (plain German parts in Latin/Kurrent script, decoded part in capitals):")
print("  Lieber Hugo   3/4 7 - 7 Uhr")
print("  Ich erwarte Dich zwischen [blacked out by the writer] Uhr")
print("  in der " + plain)
print("  [one word struck out by the writer] ([8 cipher signs, overwritten, not read]) am Samstag 19/10   Toni (or Joni)")

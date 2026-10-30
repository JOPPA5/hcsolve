#!/usr/bin/env python3
"""HCP 1361: word-list test of the third-row name, with the fourth letter left open as well.
Lists 5-letter words for each pattern and shows the ciphertext each would need (shift +1)."""
import re
W = sorted({w.strip().lower() for w in open("/usr/share/dict/words") if re.fullmatch(r"[A-Za-z]{5}", w.strip())})
enc = lambda w: "".join(chr((ord(c) - 97 + 1) % 26 + 97) for c in w)
for pat in ("ga.n.", "ga..t", "g.unt", "ga.nt", "..unt"):
    hits = [w for w in W if re.fullmatch(pat, w)]
    print(pat, len(hits), " ".join(f"{w}({enc(w)})" for w in hits))

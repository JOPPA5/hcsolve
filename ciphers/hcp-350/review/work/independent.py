# Reviewer's independent decoder for hcp-350 / hcp-351. Written from the prose description in
# SOLUTION.md and the numbers in key.json; does not import or read the solver's decrypt.py.
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[4]

def load(num, variant="ciphertext.txt"):
    d = root / f"ciphers/hcp-{num}/work/kryha-decipherment"
    key = json.loads((d / "key.json").read_text())
    ct = re.sub(r"[^A-Z]", "", (d / variant).read_text().upper())
    return key, ct

def displacements(key, n):
    holes, dist = key["holes"], key["adjacent_distances"]
    arcs = []
    for a, b in zip(holes, holes[1:] + holes[:1]):
        s, h = 0, a
        while h != b:
            s += dist[h]; h = (h + 1) % len(dist)
        arcs.append(s)
    D, out = key["initial_displacement"], []
    for i in range(n):
        out.append(D % 26); D += arcs[i % len(arcs)]
    return out, arcs

def decode(key, ct):
    P, O = key["P"], key["O"]            # P: coordinate -> letter index; O: letter index -> coordinate
    D, arcs = displacements(key, len(ct))
    return "".join(chr(65 + P[(O[ord(c) - 65] - d) % 26]) for c, d in zip(ct, D)), arcs

def encode(key, pt):
    P, O = key["P"], key["O"]
    Pinv = {v: k for k, v in enumerate(P)}; Oinv = {v: k for k, v in enumerate(O)}
    D, _ = displacements(key, len(pt))
    return "".join(chr(65 + Oinv[(Pinv[ord(c) - 65] + d) % 26]) for c, d in zip(pt, D))

if __name__ == "__main__":
    for num in ("350", "351"):
        key, ct = load(num)
        pt, arcs = decode(key, ct)
        claimed = key["plaintext"].upper()
        print(f"hcp-{num}: {len(ct)} letters; arcs sum={sum(arcs)} over {len(arcs)} stops; "
              f"P is a permutation={sorted(key['P'])==list(range(26))}; O is a permutation={sorted(key['O'])==list(range(26))}")
        print("  matches plaintext stored in key.json:", pt == claimed)
        print("  re-encrypts to the same ciphertext:  ", encode(key, pt) == ct)
        print("  " + pt)

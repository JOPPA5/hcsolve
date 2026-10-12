# Reviewer's independent check for hcp-374. Written from SOLUTION.md's prose and the numbers in
# key.json; does not read the solver's decrypt.py or verify.py.
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parents[4]
key = json.loads((root / "ciphers/hcp-374/work/key.json").read_text())
P = dict(zip(key["alphabet"], key["input_positions"]))     # plain letter  -> coordinate
O = dict(zip(key["alphabet"], key["output_positions"]))    # cipher letter -> coordinate
Pinv = {v: k for k, v in P.items()}
holes, dist = key["holes_zero_based"], key["adjacent_distances"]

def arcs_from(start_index):
    out = []
    for j in range(len(holes)):
        a, b = holes[(start_index + j) % len(holes)], holes[(start_index + j + 1) % len(holes)]
        s, h = 0, a
        while h != b:
            s += dist[h]; h = (h + 1) % len(dist)
        out.append(s)
    return out

def decode(ct, phase=0, d0=None):
    d = key["first_displacement"] if d0 is None else d0
    arcs, out = arcs_from(phase), []
    for i, c in enumerate(ct):
        out.append(Pinv[(O[c] - d) % 26]); d += arcs[i % len(arcs)]     # O(cipher) = P(plain) + d
    return "".join(out)

letters = lambda s: re.sub(r"[^a-z]", "", s.lower())

if __name__ == "__main__":
    solver = letters((root / "ciphers/hcp-374/work/transcription-collated.txt").read_text())
    old    = letters((root / "ciphers/hcp-374/work/transcription.txt").read_text())
    blind  = letters("kidah crtgs bvbpt iloiq spqhq nzyhi qlxun aipot kbcey hvuiu qoqpm tlijv abave kzaxi mlemp qxmjc jslwf")
    print("permutations:", sorted(P.values()) == list(range(26)), sorted(O.values()) == list(range(26)),
          "| arcs sum:", sum(arcs_from(0)), "over", len(holes), "stops")
    for name, t in (("solver, collated reading", solver), ("solver, original reading", old), ("reviewer's second reader, blind", blind)):
        print(f"{name:32} differs from collated at {[i+1 for i,(a,b) in enumerate(zip(t,solver)) if a!=b]}")
        print(" " * 33 + decode(t[5:]).upper())

    # How special is the claimed setting? Try every phase and starting displacement on the 80-letter body.
    target = "aupozornuiespanielskeprotidodavkyuzpevnekupenenazakladepovodnychciencelulozy"   # end of 373's published draft
    scores = sorted(((sum(a == b for a, b in zip(decode(blind[5:], ph, d), target)), ph, d)
                     for ph in range(len(holes)) for d in range(26)), reverse=True)
    print("all 598 phase/displacement settings, letters agreeing with the published sentence (of 76):")
    print("  best three:", scores[:3], "| median:", scores[len(scores)//2][0])

    # Does the same key read 373, the telegram it was recovered from?
    c373 = letters((root / "batches/kryha373-collation-sol61/ciphertext650.txt").read_text())
    best = max(((decode(c373[off:], ph, d), off, ph, d) for off in range(0, 6) for ph in range(len(holes)) for d in range(26)),
               key=lambda r: sum(r[0].count(w) for w in ("celulozy", "madrid", "zaklade", "povodnych", "kupene")))
    pt, off, ph, d = best
    print(f"373 ({len(c373)} letters) with the same rings and stops, best start offset={off} phase={ph} displacement={d}:")
    print("  ..." + pt[-200:].upper())

# Reviewer control: can the solver's searches recover a planted Slovak plaintext
# of the same length (80 letters), and how does genuine text score under its model?
import random, subprocess, pathlib
here = pathlib.Path(__file__).parent
repro = here / "repro"
q = {a: float(b) for a, b in (l.split() for l in (repro / "quadgrams.tsv").read_text().splitlines())}
score = lambda t: sum(q.get(t[i:i+4], -4) for i in range(len(t) - 3))

texts = [
    "ministerstvozahranicnychvecioznamujezevyznamenaniabuduodovzdanevyslancovidnadvadsiatehomarca",
    "ziadametelegrafickuodpovedcivladasuhlasisnavrhomnaodovzdanieradovclenomdelegacievsofii",
    "vyslanectvodostaloinstrukciuabyvyznamenaniaodovzdaloosobnepriprilezitostistatnehosviatku",
]
texts = [t[:80] for t in texts]

def enc(pt, key):               # inverse of the solver's dec(): read columns in key order
    w = len(key)
    return "".join(pt[c::w] for c in key)

def run(prog, ct, tag):
    d = here / f"ctl-{tag}"; d.mkdir(exist_ok=True)
    (d / "quadgrams.tsv").write_text((repro / "quadgrams.tsv").read_text())
    (d / "cipher.txt").write_text(ct + "\n")
    args = [str(repro / prog), str(d)] + (["cipher.txt"] if prog == "multistage" else [])
    return subprocess.run(args, capture_output=True, text=True).stdout

rnd = random.Random(2026)
for n, pt in enumerate(texts, 1):
    print(f"\n== plaintext {n}: {pt}\n   true-plaintext score under solver's model: {score(pt):.1f}")
    # (a) single columnar, width 11
    k = list(range(11)); rnd.shuffle(k)
    out = run("attack", enc(pt, k), f"{n}a")
    best = max(out.splitlines(), key=lambda l: float(l.split()[1]))
    print(f"   single w=11 : recovered={pt in out}  best line score={best.split()[1]}")
    # (b) double and (c) triple columnar, width 18 each
    for stages in (2, 3):
        ct = pt
        for _ in range(stages):
            k = list(range(18)); rnd.shuffle(k); ct = enc(ct, k)
        out = run("multistage", ct, f"{n}{'bc'[stages-2]}")
        lines = out.splitlines()
        sc = lambda l: float(l.split("score=")[1].split()[0])
        best = max(lines, key=sc)
        print(f"   {stages}-stage w=18: recovered={pt in out}  best score={sc(best):.1f}  best text={best.split('text=')[1].split()[0]}")

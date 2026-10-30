"""hcp-1456: decode the null-interleaved English postcard.

Rule (one rule for every cipher word): drop the first two letters, then keep
every second letter starting with the third (Python: word[2::2]).

Run from the repo root:  python3 -I ciphers/hcp-1456/work/decode.py
"""
import hashlib, pathlib, sys

D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
    "source/address-large.jpg": "0db6566b769caf54332ff45bde04248ef35eb7267fdbafbca2b4cfd672f62bf4",
    "source/picture-large.jpg": "a728a14fd07f1c209e7e684ed99da1453cb3c81e2991a5c3f9ebfb6122f014f6",
    "source/metadata.md": "a1a0f45b0ae35da702d0eeb25869c0e72791ebd3190d2f557cba131cd60076ee",
}
for rel, h in HASHES.items():
    got = hashlib.sha256((D / rel).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch for {rel}: {got}")
print("source hashes OK")

lines = [l.rstrip("\n") for l in (D / "work/transcription.txt").read_text().splitlines()
         if l.strip() and not l.startswith("#")]
text = " ".join(lines)
text = text.replace("= ", "").replace("- ", "").replace("+", "")
tokens = text.split()

raw = []
for t in tokens:
    if t in ".?":
        raw.append(t)
    else:
        raw.append(t[2::2].lower())
raw_s = " ".join(raw)
print("cipher words :", " ".join(tokens))
print("decoded      :", raw_s)

EXPECTED = ("thanks for your what do you mean . no stamt iam too late for the mail "
            "tonight got home from work at nine bclock . plenty of work about here . "
            "wonder why harry dont write to me . have been at ford manor this week ? "
            "kind regards to all mabel . beat . annie")
# normalise: compare letters and punctuation only
norm = lambda s: "".join(c for c in s if c.isalpha() or c in ".?")
assert norm(raw_s) == norm(EXPECTED), "decode differs from expected"

PLAIN = ("Thanks for your [...]. What do you mean. No stamt [stamp?]; I am too late for "
         "the mail tonight. Got home from work at nine o'clock [decoded 'bclock']. Plenty of "
         "work about here. [I] wonder why Harry don't write to me. Have [you] been at Ford "
         "Manor this week? Kind regards to all. Mabel. Beat. Annie. [unenciphered flourish 'Ewtt']")
print()
print(PLAIN)

# Independent reviewer decoder: reviewer's own transcription, written order per row;
# plaintext = reverse word order, reverse letters in each word.
rows = ["esaelp ysub yrev ma", "dluow dna esucxe", "emit dah fi etirw",
        "htiw ruoy", "evol lla", "kcaJ"]
out = [" ".join(w[::-1] for w in r.split()[::-1]) for r in rows]
for r,o in zip(rows,out): print(f"{r:<22} -> {o}")
print(" ".join(out))

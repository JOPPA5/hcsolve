# Independent reviewer decode of hcp-914 from my own reading of the hires picture side
# (crops row1a/row1b/row2/ort1/ort2/ue in this folder). Not derived from work/transcription.json.
name = [("A","8 12"),("E","6"),("I","4"),("K","7"),("L","1 9"),("O","2"),
        ("S","5"),("SCH","11"),("U","3 10")]
ort = [("I","2"),("L","1"),("N","3"),("Z","4")]
# printed example in the Erklaerung column, read from the card
example = [("C","1"),("A","2"),("R","3"),("L","4"),("M","5"),("E","6 8"),("I","7"),("R","9")]
def dec(cells):
    p = {int(n): l for l, ns in cells for n in ns.split()}
    assert sorted(p) == list(range(1, len(p)+1)), sorted(p)
    return "".join(p[i] for i in sorted(p))
for k, c in (("example", example), ("name", name), ("ort", ort)):
    print(k, dec(c))

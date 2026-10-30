# Independent decode (reviewer). Transcription made by reviewer from sheet0-2.png
# (card rotated 180 deg, reading order). Cells named by walls present: t,b,l,r; '*' = dot inside.
# Standard Pigpen: grid1 A..I by cell position; cell position determined by which walls are present.
pos = {frozenset('rb'):0, frozenset('lrb'):1, frozenset('lb'):2,
       frozenset('trb'):3, frozenset('tlrb'):4, frozenset('tlb'):5,
       frozenset('tr'):6, frozenset('tlr'):7, frozenset('tl'):8}
xs = {'V':'S','>':'T','<':'U','^':'V'}
def dec(tok):
    if tok in xs: return xs[tok]
    if tok == 'X': return '[x]'
    dot = tok.endswith('*'); w = frozenset(tok.rstrip('*'))
    return chr((74 if dot else 65) + pos[w])
line = "tl* rb trb X tlb rb tl* tlrb tlrb* | V tlb* lb* lb* | lb* tlrb lrb tlrb tlrb* | rb lb* lb* | tlr tlrb tl lb* | tr tl* < V |"
print(" ".join("".join(dec(t) for t in g.split()) for g in line.split("|") if g.strip()))

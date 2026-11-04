"""Reviewer's independent decode of hcp-1095 (my own reading of the pixels, written in
a different notation: letters separated by spaces, words by ' | ', 'o' = dot, 's' = short dash,
'L' = long dash, '_' = internal (American spaced-letter) gap, 'Q' = curl+dot question mark)."""
AMERICAN = {  # American (railroad) Morse, typed from a reference independently of work/decode.py
 "os":"A","sooo":"B","oo_o":"C","soo":"D","o":"E","oso":"F","sso":"G","oooo":"H","oo":"I",
 "soso":"J","sos":"K","L":"L","ss":"M","so":"N","o_o":"O","ooooo":"P","ooso":"Q","o_oo":"R",
 "ooo":"S","s":"T","oos":"U","ooos":"V","oss":"W","osoo":"X","oo_oo":"Y","ooo_o":"Z","Q":"?"}
MINE = """
soo o os o_oo | o_oo os oo_oo ss o_o so soo
ss oo_oo | os so ooo oss o o_oo | oss oooo os s
ooo oooo os L L | oo s | sooo o Q | ooo oooo os
L L | oo | os sso o_oo o o | oss oo s
oooo | s oooo o o Q | s oooo o so | L o s
oo s | sooo o | oo_oo o ooo
oo_o os o_oo o_o L oo_oo so so
oss oooo os L
"""
out=[]
for line in MINE.strip().splitlines():
    out.append(" ".join("".join(AMERICAN[s] for s in w.split()) for w in line.split("|")))
for i,l in enumerate(out,1): print(f"[{i}] {l}")

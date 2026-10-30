# Independent reviewer decoder for hcp-1401 (Caesar -1), own transcription from review crops.
import sys
own = ["gspn", "Zpvs", "Pxo", "Hjsm"]   # enciphered groups, read by reviewer from msg_rot90.png
literal = "E. L."                       # abbreviation, same as hcp-1386 / 1404
def dec(w, k):
    return "".join(chr((ord(c.upper()) - 65 - k) % 26 + 65) for c in w)
for k in range(26):
    out = " ".join(dec(w, k) for w in own)
    mark = "  <==" if k == 1 else ""
    if k in (1,) or "-v" in sys.argv:
        print(k, out, mark)
print("Message:", " ".join(dec(w,1) for w in own[:3]), literal, dec(own[3],1))
print("Letters:", sum(len(w) for w in own))

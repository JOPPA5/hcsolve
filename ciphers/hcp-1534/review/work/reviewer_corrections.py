# Applies the reviewer's pixel-checked corrections to a COPY of the solver transcription and decodes it.
import json, sys
t = json.load(open(sys.argv[1]))
fix = {"S13": ("t3c6rm2", "t3s484n"),      # DOSAHNU -> DOCILIM
       "L02": ("284pm1H", "2bh4nm1H"),     # ULIBNYCH -> UPRIMNYCH
       "L03": ("f5hm5", "f5sm5"),          # VERNE -> VECNE
       "L04": ("q6p6f2", "qbh6f2")}        # ZABAVU -> ZPRAVU
for r in t["rows"]:
    if r["id"] in fix:
        a, b = fix[r["id"]]; assert r["cipher"].count(a) == 1; r["cipher"] = r["cipher"].replace(a, b)
json.dump(t, open(sys.argv[2], "w"), indent=1)

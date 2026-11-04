"""Reviewer's independent decode of hcp-904: own transcription (read from review/work crops) with own key."""
import sys
T = """[Λ]. Μ. Κονντε λειδερ Δειν λιεβεν Βριεφ
νιχτ μεʽρ βεαντυορτεν. φιερ Ϝοχεν σινδ
αβε[ρ] λανγ, καννστ Δυ μιρ κεινε ανδε[ρ]
Αδρ. ανγεβεν? σονστ μυστ Δυ Διχ σχον σο λανγε γε-
δυλδιγεν. ʽαβε μιχ σεʽρ υβερ Δεινεν Βριεφ γεφρευτ.
ʽερζλιχεν Γρυσσ υ Κυσσ Δεινε τρ. Ιε??ι."""
G = "αβγδεζικλμνοπρστυφχ"; L = ["a","b","g","d","e","z","i","k","l","m","n","o","p","r","s","t","u","f","ch"]
K = dict(zip(G, L)); K.update({c.upper(): v.upper() if len(v)==1 else v.capitalize() for c, v in K.items()})
K.update({"ʽ": "h", "Ϝ": "W", "Ι": "J"})
used=set(); out=[]
for ch in T:
    if ch in K: used.add(ch); out.append(K[ch])
    else:
        if ch.isalpha() and ch not in "?": print("UNMAPPED", ch, file=sys.stderr)
        out.append(ch)
print("".join(out))
print("signs used:", "".join(sorted(used)), file=sys.stderr)

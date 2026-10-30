# Independent reviewer decoder for hcp-1456. Own token list typed by the reviewer
# from crops review/work/*.png (split words already joined); rule: drop 2 leading
# nulls, then take every other letter.
import sys
words = """Nitchuavnikes nifaoyr tiyhoauir nawkhiart nadio riyaoru temderaen . ranao
prsrtiarmkt ariratm nothono hiliarthe rafiour natrhoe nimuanial rathornaihgrhat nagiort
pahaormae raforoorm nawhoarak hiart zinaianhe hablcalaorcak . gnpalaehnatay raouf hawaohrak
niarbioaurt rahaerrae . rawhornadaekr nawrhiy zahiazririy nodiornat ziwhraiatae zitioa yamae .
nahiarvae nabseaetn hearts nifaohrad thmiaznioar thtohaias niwaeaeok ? nikhirnrd
yaraehgiakrades kitao hiatlil nimraibreal . rebaeiart . niahninaiae""".split()
def dec(w):
    out=[]; i=2
    while i < len(w):
        out.append(w[i].lower()); i+=2
    return "".join(out)
print(" ".join(w if w in ".?" else dec(w) for w in words))
print(len([w for w in words if w not in ".?"]), "cipher words")

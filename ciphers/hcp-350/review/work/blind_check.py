# Decode transcriptions that were made WITHOUT knowledge of the plaintext, using the solver's key,
# and count how far they are from the solver's final ciphertext and plaintext.
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from independent import load, decode, root

blind351 = """SOSOL HUJRZ PMQKK EWRTH EJPLG OFMFS ULULL LPPVV
STRFV EKMJZ XXQQH HAUEN PXNDQ NAUMR XUUMC HLLNE GVPZH PFPFN VXGIU
WGGDR ABZQJ LUUNK UUPNS DUOFY ZSBBR OKRWU GFYJR UDAVT NSKXH
UPKJD EWWPY HPJZO AYGLZ YDRAU PJUBP VIGBJ HXZPW ELIQY BADDZ EQYYP
KDJHK ZYYYQ JJPGT XEBQD BLTTE UOTWN IVBMF IIHUJ UBXCB RFJOS
EVZGE ZKFGS UDEUY UBYQV QKOAQ HRCMV EYJHQ UBHQO YWWCS IILZM OYTHO
HDOAT IHXBQ ZOACA EXUVC BXSQE WQPIS CMVTN JYFHL OOUGY UDQIE
EYRMI FWXUA USXIT STFFJ TGKDH HWUTS"""   # second Claude reader, blind, before any plaintext existed

def letters(s): return re.sub(r"[^A-Z]", "", s.upper())
def diff(a, b): return [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]

for num, sources in (("350", {"solver, before recovery (350-source-preferred.txt)": letters((root/"batches/source-variants-350-351/350-source-preferred.txt").read_text()),
                              "solver, first working text (work/cipher.txt)": letters((root/"ciphers/hcp-350/work/cipher.txt").read_text())}),
                     ("351", {"solver, before recovery (351-source-preferred.txt)": letters((root/"batches/source-variants-350-351/351-source-preferred.txt").read_text()),
                              "solver, first working text (work/cipher.txt)": letters((root/"ciphers/hcp-351/work/cipher.txt").read_text()),
                              "second reader, blind": letters(blind351)})):
    key, final = load(num)
    pt_final, _ = decode(key, final)
    print(f"\nhcp-{num}: final ciphertext.txt has {len(final)} letters")
    for name, ct in sources.items():
        d = diff(ct, final)
        pt, _ = decode(key, ct)
        print(f"  {name}: {len(ct)} letters, differs from final ciphertext at {len(d)} positions")
        print(f"     plaintext positions that change: {len(diff(pt, pt_final))}  -> {d}")
        if name.startswith("second"):
            print("     decoded blind reading:\n     " + pt)

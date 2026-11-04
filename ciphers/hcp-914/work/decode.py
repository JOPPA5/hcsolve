"""hcp-914: decode the printed name-grid card. Run from repo root:
python3 -I ciphers/hcp-914/work/decode.py"""
import hashlib, json, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HASHES = {
    "source/picture-large.jpg": "5e2a2235b16c838b9a5c5a86a3bfbdcad8fdf715ad95aa26759b5018e6716d55",
    "source/address-large.jpg": "ed7b7731ee1d09d0e7608f2c014a6c54ce7dbacc68f6fa79a76931254e6e178c",
    "work/hires/cpc_1900-06-25_AT_Linz_AT_Kremsmunster__pic.jpg": "2e27e2eeb30e20d2f68fbe4d2f4ef13129ee630811712b5ef56abf257f7fc0e4",
    "work/hires/cpc_1900-06-25_AT_Linz_AT_Kremsmunster__adr.jpg": "88231bd2a2e976ddb41527be9486aab35f851e9b3524d388b29d1c63f1de65c2",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch: {p}")
print("source hashes OK")
t = json.load(open(os.path.join(D, "work/transcription.json")))
# reading choice for the shared I/J cell, fixed by word sense (Louise / Linz)
IJ = {"name_des_absenders": "I", "ort": "I"}
for field in ("name_des_absenders", "ort"):
    pos = {}
    for letter, nums in t[field].items():
        for n in nums:
            if n in pos:
                sys.exit(f"duplicate position {n} in {field}")
            pos[n] = IJ[field] if letter == "I/J" else letter
    assert sorted(pos) == list(range(1, len(pos) + 1)), f"gap in {field}"
    print(f"{field}: " + "".join(pos[n] for n in sorted(pos)))

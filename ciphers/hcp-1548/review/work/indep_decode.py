import json, sys
key = json.load(open(sys.argv[1]))  # family key from hcp-1545
ct = open(sys.argv[2], encoding='utf-8').read()
ct = ct.replace('{U1}', '52')  # reviewer test of the claimed restoration E,U
out = []; unk = set(); n = 0
for ch in ct:
    if ch in key: out.append(key[ch]); n += 1
    elif ch in ' .-?\n': out.append(ch)
    else: out.append('['+ch+']'); unk.add(ch)
print(''.join(out)); print('units', n, 'unmapped', unk)

#!/usr/bin/env python3
"""HCP1541 final decoder (response to review 1). Read-only.

Inputs : work/transcription-final.txt  (manual transcription, final state)
         work/key-final.json           (family key; '7' = J, 'k' = k-shaped G)
Checks : source/reference hashes of work/audit-sha256.json; that the final
         transcription differs from the audited round-0 record
         (work/transcription.txt) only by the documented relabels
         (y->7, [U01]->k, [U02]->(5), [U03]->(d)5<s>4); key is one-to-one
         and every key sign is used.
Markup : (x)  sign hidden under the painted patch, restored from context;
              printed as (letter).
         <x>  visible sign of uncertain identity, best match x;
              printed as <letter>.
Prints : the full literal plaintext, line by line.
"""
import hashlib, json, re
from pathlib import Path

W = Path(__file__).resolve().parent
R = W.parent.parent.parent


def main():
    for path, digest in json.loads((W / 'audit-sha256.json').read_text()).items():
        assert hashlib.sha256((R / path).read_bytes()).hexdigest() == digest, path
    key = json.loads((W / 'key-final.json').read_text())
    assert len(set(key.values())) == len(key)
    final = (W / 'transcription-final.txt').read_text()
    old = (W / 'transcription.txt').read_text()
    back = (final.replace('(d)5<s>4', '[U03]').replace('(5)', '[U02]')
            .replace('k', '[U01]').replace('7', 'y'))
    assert back == old, 'final transcription deviates from audited record'
    used = set(); n_vis = n_rest = n_unc = 0; out = []
    for line in final.splitlines():
        res = []
        for tok in re.findall(r'\(.\)|<.>|.', line):
            if tok[0] in '(<':
                c = tok[1]; assert c in key
                res.append(tok[0] + key[c] + tok[2]); used.add(c)
                if tok[0] == '(':
                    n_rest += 1
                else:
                    n_unc += 1; n_vis += 1
            elif tok in key:
                res.append(key[tok]); used.add(tok); n_vis += 1
            else:
                assert tok in ' .,?-', 'unknown sign ' + repr(tok)
                res.append(tok)
        out.append(''.join(res))
    assert used == set(key), 'unused key signs: %s' % (set(key) - used)
    print(f'{len(final.splitlines())} rows; {n_vis} visible cipher signs decoded '
          f'({n_unc} of uncertain shape, marked <>); {n_rest} hidden signs restored '
          f'from context, marked (); all {len(key)} key signs used.\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Reviewer's independent Morse decoder for hcp-1133 (tree walk, own table)."""
import re, sys
# ITU letters as dichotomic tree string (level order): index 1=root
TREE = " ETIANMSURWDKGOHVF_L_PJBXCYZQ"
def walk(code):
    i = 1
    for s in code:
        i = 2*i + (1 if s == '-' else 0)
    return TREE[i-1] if i-1 < len(TREE) and TREE[i-1] not in ' _' else None
EXTRA = {'..-..': 'É', '.-.--': 'Á?'}   # Á: writer's own sign, as hypothesised by solver
path = sys.argv[1]
blocks = {}; cur = None; unknown = []
for ln in open(path, encoding='utf-8'):
    ln = ln.strip()
    if not ln or ln.startswith('#'): continue
    if ln.startswith('['): cur = ln[1:3]; blocks[cur] = ''; continue
    for g in filter(None, ln.replace(' ', '').split('/')):
        ch = EXTRA.get(g) or walk(g)
        if ch is None: unknown.append(g); ch = '<' + g + '>'
        blocks[cur] += ch
for k, v in blocks.items(): print(k, v)
print('unknown groups:', unknown)

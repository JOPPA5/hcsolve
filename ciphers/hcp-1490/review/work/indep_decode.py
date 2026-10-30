# Independent reviewer decoder for HCP 1490: my own token list from my crops.
grid = ['BR','B','BL','R','C','L','TR','T','TL']  # A..I cell order of standard tic-tac-toe grid
def letter(tok, swapTU=False):
    shape, dots = tok[:-1], int(tok[-1])
    i = dots*9 + grid.index(shape)
    ch = chr(65+i) if i < 26 else '#'
    if swapTU and ch in 'TU': ch = 'U' if ch=='T' else 'T'
    return ch
mine = {
 'greeting': ['C?','L1','C1','C0','TR2'],
 'body': ['BR2','B2','C1','R0','BR0','TR2','|','C1','TL2','TR0','T0','BL2'],
 'signature': ['R0','B1'],
}
for swap in (False, True):
    print('swapTU' if swap else 'standard')
    for k,v in mine.items():
        print(' ', k, ''.join(' ' if t=='|' else '?' if t.endswith('?') else letter(t,swap) for t in v))

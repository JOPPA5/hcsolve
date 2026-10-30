# Segment each cipher line of work/upright.jpg into glyph boxes by column gaps,
# and write numbered contact sheets for manual reading.
import sys
from PIL import Image, ImageOps, ImageDraw
base = sys.argv[1]
im = Image.open(base + '/work/upright.jpg').convert('L')
LINES = [('p1',48,69),('p2',70,86),('l01',88,113),('l02',128,151),('l03',163,189),('l04',198,222),
 ('l05',229,260),('l06',266,292),('l07',298,326),('l08',328,354),('l09',355,387),('l10',392,420),
 ('l11',423,447),('l12',463,484),('l13',494,521),('l14',531,553),('l15',557,582),('l16',586,604),('l17',607,625)]
X0, X1 = 578, 995
TH = 110
out = []
for name, a, b in LINES:
    cols = []
    for x in range(X0, X1):
        d = sum(1 for y in range(a+3, b-2) if im.getpixel((x, y)) < TH)
        cols.append(d)
    segs = []; inside = False
    for i, d in enumerate(cols):
        if d > 0 and not inside: s = i; inside = True
        if d == 0 and inside: segs.append((X0+s, X0+i)); inside = False
    if inside: segs.append((X0+s, X1))
    # merge tiny gaps (<2px) 
    m = []
    for s in segs:
        if m and s[0]-m[-1][1] < 2: m[-1] = (m[-1][0], s[1])
        else: m.append(s)
    segs = [s for s in m if s[1]-s[0] >= 2]
    out.append((name, a, b, segs))
    S = 8
    cell_w = 22*S; cell_h = (b-a+10)*S + 30
    per = 10
    rows = (len(segs)+per-1)//per
    sheet = Image.new('L', (per*cell_w, rows*cell_h), 255)
    dr = ImageDraw.Draw(sheet)
    for k, (s, e) in enumerate(segs):
        cx = (s+e)//2
        c = im.crop((cx-11, a-5, cx+11, b+5))
        c = ImageOps.autocontrast(c, cutoff=1).resize((22*S, (b-a+10)*S), Image.LANCZOS)
        r, q = divmod(k, per)
        sheet.paste(c, (q*cell_w, r*cell_h+30))
        dr.text((q*cell_w+5, r*cell_h+5), f'{k}  w{e-s}', fill=0)
        dr.rectangle((q*cell_w, r*cell_h, (q+1)*cell_w-1, (r+1)*cell_h-1), outline=0)
    sheet.save(f'{base}/work/seg/{name}.png')
for name, a, b, segs in out:
    print(name, len(segs), [e-s for s, e in segs])

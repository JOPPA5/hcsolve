"""Figures for the report (Claude Opus 5.5, 2026-10-30). Run from repo root with the PIL python, -I."""
import pathlib
from PIL import Image, ImageOps, ImageDraw
D = pathlib.Path(__file__).resolve().parent
pic = Image.open(D.parent/"source"/"picture.jpg").convert("L")
# top strip rotated 180 deg, 2x
strip = pic.crop((60, 5, 870, 60)).rotate(180)
strip = ImageOps.autocontrast(strip).resize((strip.width*2, strip.height*2), Image.LANCZOS)
strip.save(D/"report-line-rotated.png")
boxes = {28: (814,17,832,44), 24: (704,16,725,44), 11: (337,15,359,43), 4:(148,16,169,44), 27:(789,17,810,44), 26:(751,14,786,49)}
tiles = []
for gid in (28, 24, 11, 27, 4, 26):
    x0,y0,x1,y1 = boxes[gid]
    t = pic.crop((x0-3,y0-6,x1+3,y1+6)).rotate(180)
    t = ImageOps.autocontrast(t)
    t = t.resize((t.width*6, t.height*6), Image.LANCZOS)
    tiles.append((gid, t))
H = max(t.height for _,t in tiles) + 30
W = sum(t.width for _,t in tiles) + 20*(len(tiles)+1)
sheet = Image.new("L", (W, H), 255)
dr = ImageDraw.Draw(sheet); x = 20
for gid, t in tiles:
    sheet.paste(t, (x, 25)); dr.text((x, 5), f"glyph {gid}", fill=0); x += t.width + 20
sheet.save(D/"report-glyphs.png")
print("ok")

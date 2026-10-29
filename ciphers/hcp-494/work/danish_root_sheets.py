"""Triage-only contact sheets of observed Danish archive images 76--150.

Copies are resized for overview. Full-resolution originals must be used for
individual code readings. No source pixels are cleaned or reconstructed.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).parent / 'danish-witness-2026-10-28'
OUT = ROOT / 'root-sheets'
OUT.mkdir(exist_ok=True)
for start in range(76,151,9):
    pages = list(range(start,min(start+9,151)))
    if not all((ROOT/'keys'/f'{p:03d}.jpg').exists() for p in pages):
        continue
    canvas=Image.new('RGB',(1500,2190),'white')
    draw=ImageDraw.Draw(canvas)
    for i,p in enumerate(pages):
        src=Image.open(ROOT/'keys'/f'{p:03d}.jpg').convert('RGB')
        thumb=ImageOps.contain(src,(490,690))
        x,y=(i%3)*500,(i//3)*730
        draw.text((x+10,y+6),f'Archive image {p:03d}',fill='black')
        canvas.paste(thumb,(x+(500-thumb.width)//2,y+30))
    canvas.save(OUT/f'{start:03d}-{pages[-1]:03d}.png')
for page in (83,97,98):
    Image.open(ROOT/'keys'/f'{page:03d}.jpg').transpose(
        Image.Transpose.ROTATE_90).save(OUT/f'{page:03d}-rotated.png')

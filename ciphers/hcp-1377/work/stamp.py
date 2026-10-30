#!/usr/bin/env python3
"""Upright, contrast-stretched 3x crop of the postmark from the hires address side. Run from repo root."""
from PIL import Image, ImageOps
D='ciphers/hcp-1377/work/'
c=Image.open(D+'hires/pc_hcp_58_adr.JPG').convert('L').crop((1360,120,1660,430)).rotate(-90,expand=True)
c=ImageOps.autocontrast(c); c.resize((c.size[0]*3,c.size[1]*3),Image.LANCZOS).save(D+'stamp_up.png')

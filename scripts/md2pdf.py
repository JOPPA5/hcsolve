"""Render a cipher report.md (a small Markdown subset) to report.pdf.

Usage: <python with reportlab+PIL> scripts/md2pdf.py ciphers/<slug>/report/report.md

Supported: # / ## / ### headings, paragraphs, - bullets, ``` fences,
| tables |, **bold**, `code`, and ![caption](relative/image.jpg) on its own line.
Image paths are resolved relative to the report.md file.
"""
import html, re, sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, Paragraph, Preformatted, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

FONTS = Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/'
             'libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name, file in [('DV', 'DejaVuSans.ttf'), ('DVB', 'DejaVuSans-Bold.ttf'), ('DVM', 'DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS / file)))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DVB', italic='DV', boldItalic='DVB')

ss = getSampleStyleSheet()
body = ParagraphStyle('B', parent=ss['Normal'], fontName='DV', fontSize=9.5, leading=13.5, spaceAfter=7)
bullet = ParagraphStyle('L', parent=body, leftIndent=14, bulletIndent=4, spaceAfter=3)
cell = ParagraphStyle('C', parent=body, fontSize=8.5, leading=11, spaceAfter=0)
heads = {1: ParagraphStyle('H1', parent=body, fontName='DVB', fontSize=18, leading=23, spaceAfter=10, keepWithNext=True),
         2: ParagraphStyle('H2', parent=body, fontName='DVB', fontSize=12, leading=16, spaceBefore=10, spaceAfter=5, keepWithNext=True),
         3: ParagraphStyle('H3', parent=body, fontName='DVB', fontSize=10, leading=14, spaceBefore=6, spaceAfter=4, keepWithNext=True)}
mono = ParagraphStyle('M', fontName='DVM', fontSize=8, leading=10.5, spaceAfter=8, leftIndent=6,
                      backColor=colors.HexColor('#f3f5f8'), borderPadding=4)


def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<font name="DVM">\1</font>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    return t


def build(md_path):
    md_path = Path(md_path).resolve()
    base = md_path.parent
    lines = md_path.read_text(encoding='utf-8').splitlines()
    story, para, i = [], [], 0
    title = 'Report'

    def flush():
        if para:
            story.append(Paragraph(inline(' '.join(para)), body))
            para.clear()

    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            flush(); i += 1; buf = []
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i]); i += 1
            story.append(Preformatted('\n'.join(buf), mono))
        elif m := re.match(r'^(#{1,3}) (.*)', ln):
            flush(); lvl = len(m.group(1))
            if lvl == 1: title = m.group(2)
            story.append(Paragraph(inline(m.group(2)), heads[lvl]))
        elif m := re.match(r'^!\[(.*)\]\((.*)\)\s*$', ln):
            flush()
            from PIL import Image as PI
            p = (base / m.group(2)).resolve()
            w, h = PI.open(p).size
            maxw, maxh = A4[0] - 100, 520
            s = min(maxw / w, maxh / h)
            story.append(Image(str(p), w * s, h * s))
            if m.group(1):
                story.append(Paragraph('<i>' + inline(m.group(1)) + '</i>', cell))
            story.append(Spacer(1, 8))
        elif ln.startswith('|'):
            flush(); rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append([Paragraph(inline(c), cell) for c in cells])
                i += 1
            t = Table(rows, repeatRows=1, hAlign='LEFT')
            t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), .3, colors.HexColor('#cbd4df')),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#edf2f7')),
                                   ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
            story += [t, Spacer(1, 8)]
            continue
        elif m := re.match(r'^\s*(\d+[.)])\s+(.*)', ln):
            flush()
            label, parts = m.group(1), [m.group(2)]
            i += 1
            while (i < len(lines) and lines[i].strip() and
                   lines[i][:1].isspace() and
                   not re.match(r'^\s*(?:\d+[.)]|[-*])\s+', lines[i])):
                parts.append(lines[i].strip()); i += 1
            story.append(Paragraph(inline(' '.join(parts)), bullet, bulletText=label))
            continue
        elif re.match(r'^\s*[-*] ', ln):
            flush()
            parts = [re.sub(r'^\s*[-*] ', '', ln)]
            i += 1
            while (i < len(lines) and lines[i].strip() and
                   lines[i][:1].isspace() and
                   not re.match(r'^\s*(?:\d+[.)]|[-*])\s+', lines[i])):
                parts.append(lines[i].strip()); i += 1
            story.append(Paragraph(inline(' '.join(parts)), bullet, bulletText='•'))
            continue
        elif ln.startswith('>'):
            para.append(ln.lstrip('> ').rstrip())
        elif not ln.strip():
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()

    def footer(c, doc):
        c.setFont('DV', 7); c.setFillColor(colors.HexColor('#536174'))
        c.drawString(50, 25, title[:110]); c.drawRightString(A4[0] - 50, 25, str(doc.page))

    out = md_path.with_suffix('.pdf')
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50,
                      bottomMargin=45, title=title).build(story, onFirstPage=footer, onLaterPages=footer)
    print(out)


if __name__ == '__main__':
    build(sys.argv[1])
